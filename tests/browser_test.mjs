/* The only test that starts where a student starts: a real browser, a real
 * page, a real click.
 *
 * Everything else here drives box_runner.py under Pyodide in node, which skips
 * the entire interface -- the module graph, the served content types, and
 * whether Python is fetched from this site or from someone else's CDN. Those
 * are the parts that break when the build is reorganised, and node cannot see
 * any of them.
 *
 * Optional, because a headless browser is ~140 MB and the rest of this project
 * needs nothing:
 *
 *     npm install playwright-core && npx playwright-core install chromium
 *     node browser_test.mjs
 */

import { spawn } from "node:child_process";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const PORT = 8741;

// Read the first chapter out of the built site rather than naming one, so this
// keeps working when a volume is added, renamed or reordered.
const boxes = JSON.parse(readFileSync(join(ROOT, "site", "boxes.json"), "utf8"));
const first = boxes.find(b => /\/ch\d\d-/.test(b.id));
if (!first) { console.log("skipped: no chapter pages in site/ -- build first."); process.exit(0); }
const PAGE = `${first.volume}/${first.slug}.html`;

let chromium;
try {
  ({ chromium } = await import("playwright-core"));
} catch (e) {
  // Only "it is not installed" is a skip. A corrupted install or a broken
  // import is a failure: swallowing it would turn a real breakage into a
  // green run that says "skipped".
  if (e.code !== "ERR_MODULE_NOT_FOUND") {
    console.log(`FAIL  playwright-core is installed but will not load: ${e.message}`);
    process.exit(1);
  }
  console.log("skipped: playwright-core is not installed.");
  console.log("  npm install playwright-core && npx playwright-core install chromium");
  process.exit(0);
}

const server = spawn("python3", [join(ROOT, "scripts", "serve.py"), String(PORT)],
                     { stdio: "ignore" });
const stop = () => { try { server.kill(); } catch {} };
process.on("exit", stop);

await new Promise(r => setTimeout(r, 1500));

let browser;
try {
  browser = await chromium.launch();
} catch (e) {
  stop();
  // Same rule: a missing executable is a skip, any other launch failure is a
  // failure. A sandbox problem or a bad launch argument must not read as
  // "no browser installed".
  if (!/Executable doesn't exist|please run.*install/i.test(e.message)) {
    console.log(`FAIL  the browser is installed but would not start: ${e.message.split("\n")[0]}`);
    process.exit(1);
  }
  console.log("skipped: no browser binary installed.");
  console.log("  npx playwright-core install chromium");
  process.exit(0);
}
const page = await browser.newPage();

const external = [], failed = [], errors = [], fetched = [];
page.on("request", r => {
  const u = new URL(r.url());
  if (u.hostname !== "localhost") external.push(r.url());
  if (u.pathname.includes("/pyodide/")) fetched.push(u.pathname);
});
page.on("requestfailed", r => failed.push(`${r.url()} :: ${r.failure()?.errorText}`));
page.on("pageerror", e => errors.push(String(e)));

const problems = [];
const check = (ok, what) => { console.log(`  ${ok ? "ok  " : "FAIL"}  ${what}`);
                              if (!ok) problems.push(what); };

try {
  await page.goto(`http://localhost:${PORT}/${PAGE}`, { waitUntil: "load" });

  // Pyodide boots on the first Run, not on load: a reader who only reads must
  // not be made to download 13 MB.
  check(fetched.length === 0, "nothing from pyodide/ is fetched before a click");

  const started = Date.now();
  await page.locator("button.run").first().click();
  await page.waitForFunction(
    () => document.querySelector(".runtime .msg")?.textContent?.includes("ready"),
    null, { timeout: 180000 });
  console.log(`        (booted in ${((Date.now() - started) / 1000).toFixed(1)}s)`);

  await page.waitForFunction(
    () => { const r = document.querySelector('.box[data-box="0"] pre.result');
            return r && !r.hidden && r.textContent.trim().length; },
    null, { timeout: 60000 });
  const printed = (await page.locator('.box[data-box="0"] pre.result').textContent()).trim();
  check(printed === "Hello, world!", `Run prints "Hello, world!" (got ${JSON.stringify(printed)})`);

  // Edit then re-run: proves the box runs what the student typed, not the page's copy.
  await page.locator('.box[data-box="0"] textarea').fill('print(6 * 7)\nprint("edited")');
  await page.locator("button.run").first().click();
  await page.waitForFunction(
    () => document.querySelector('.box[data-box="0"] pre.result')?.textContent.includes("42"),
    null, { timeout: 60000 });
  const edited = (await page.locator('.box[data-box="0"] pre.result').textContent()).trim();
  check(edited === "42\nedited", `an edited box runs the edit (got ${JSON.stringify(edited)})`);

  check(fetched.length === 5, `all 5 runtime files come from this site (${fetched.length})`);
  check(external.length === 0,
        `no request leaves this origin${external.length ? ": " + external.join(", ") : ""}`);
  check(failed.length === 0, `no failed request${failed.length ? ": " + failed.join(", ") : ""}`);
  check(errors.length === 0, `no page error${errors.length ? ": " + errors.join(", ") : ""}`);
} catch (e) {
  check(false, `the page never got there: ${e.message.split("\n")[0]}`);
} finally {
  await browser.close();
  stop();
}

console.log(problems.length
  ? `\n${problems.length} problem(s) in the browser`
  : "\nthe page works from a real browser, and talks to nobody else");
process.exit(problems.length ? 1 : 0);
