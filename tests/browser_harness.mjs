/* Shared by the browser tests: where the site is, and a browser to open it in.
 *
 * Three ways to point a test at the site:
 *
 *     node browser_test.mjs                                  site/ at the root
 *     BASE=/python-foundations/ node browser_test.mjs        site/ one level down
 *     SITE_URL=https://example.github.io/repo/ node ...      a deployed site
 *
 * BASE exists because GitHub Pages serves a project site under /<repo>/, and
 * a page that only works at the root -- an absolute "/pyodide/..." anywhere --
 * passes every local test and breaks on the day it goes live. SITE_URL exists
 * because only the real host shows the content types it actually sends.
 *
 * REQUIRE_BROWSER=1 makes every skip a failure. A skipped browser test exits
 * 0, and in CI that is a green run that tested nothing.
 */

import { spawn } from "node:child_process";
import { mkdtempSync, rmSync, symlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

export const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");

/** Exit as skipped -- or as failed, when REQUIRE_BROWSER is set. */
export function skip(reason, hint) {
  if (process.env.REQUIRE_BROWSER) {
    console.log(`FAIL  ${reason} (REQUIRE_BROWSER is set, so this cannot be skipped)`);
    process.exit(1);
  }
  console.log(`skipped: ${reason}`);
  if (hint) console.log(`  ${hint}`);
  process.exit(0);
}

/** playwright's chromium, or exit: skipped when not installed, failed when broken. */
export async function loadChromium() {
  try {
    return (await import("playwright-core")).chromium;
  } catch (e) {
    // Only "it is not installed" is a skip. A corrupted install or a broken
    // import is a failure: swallowing it would turn a real breakage into a
    // green run that says "skipped".
    if (e.code !== "ERR_MODULE_NOT_FOUND") {
      console.log(`FAIL  playwright-core is installed but will not load: ${e.message}`);
      process.exit(1);
    }
    skip("playwright-core is not installed.", "npm ci && npx playwright-core install chromium");
  }
}

/** Start the site (or locate a deployed one). Returns { baseUrl, stop }. */
export async function startSite(port) {
  if (process.env.SITE_URL) {
    const url = process.env.SITE_URL;
    return { baseUrl: url.endsWith("/") ? url : url + "/", stop: () => {} };
  }
  const base = process.env.BASE || "/";
  if (!/^\/([A-Za-z0-9._-]+\/)?$/.test(base)) {
    console.log(`FAIL  BASE must look like /name/ -- got ${JSON.stringify(base)}`);
    process.exit(1);
  }
  let dir = join(ROOT, "site");
  let scratch = null;
  if (base !== "/") {
    // site/ one level down, by symlink rather than copying 14 MB.
    scratch = mkdtempSync(join(tmpdir(), "pf-base-"));
    symlinkSync(join(ROOT, "site"), join(scratch, base.slice(1, -1)));
    dir = scratch;
  }
  const server = spawn("python3", [join(ROOT, "scripts", "serve.py"), String(port), dir],
                       { stdio: "ignore" });
  const stop = () => {
    try { server.kill(); } catch {}
    if (scratch) rmSync(scratch, { recursive: true, force: true });
  };
  process.on("exit", stop);

  // Wait for the server to actually answer rather than guessing at a delay.
  // A fixed sleep here was a race: anything that slows start-up turns into
  // "the page never got there", which reads as a broken site.
  for (let i = 0; ; i++) {
    try { await fetch(`http://localhost:${port}/`); break; }
    catch {
      if (i > 100) { stop(); console.log("  FAIL  the server never came up"); process.exit(1); }
      await new Promise(r => setTimeout(r, 200));
    }
  }
  return { baseUrl: `http://localhost:${port}${base}`, stop };
}

/** A launched browser, or exit: skipped when the binary is missing, failed otherwise. */
export async function launch(chromium, stop) {
  try {
    return await chromium.launch();
  } catch (e) {
    stop();
    // A missing executable is a skip; any other launch failure is a failure.
    // A sandbox problem or a bad launch argument must not read as "no browser
    // installed".
    if (!/Executable doesn't exist|please run.*install/i.test(e.message)) {
      console.log(`FAIL  the browser is installed but would not start: ${e.message.split("\n")[0]}`);
      process.exit(1);
    }
    skip("no browser binary installed.", "npx playwright-core install chromium");
  }
}
