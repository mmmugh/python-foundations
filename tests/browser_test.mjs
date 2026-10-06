/* The only test that starts where a student starts: a real browser, a real
 * page, a real click.
 *
 * Everything else here drives box_runner.py under Pyodide in node, which skips
 * the entire interface -- the module graph, the served content types, and
 * whether Python is fetched from this site or from someone else's CDN. Those
 * are the parts that break when the build is reorganized, and node cannot see
 * any of them.
 *
 * It runs against site/ at the root, one level down (BASE, the way GitHub
 * Pages serves a project site), or a deployed site (SITE_URL); see
 * browser_harness.mjs. Optional locally, because a headless browser is
 * ~140 MB and the rest of this project needs nothing:
 *
 *     npm ci && npx playwright-core install chromium
 *     node browser_test.mjs
 */

import { launch, loadChromium, skip, startSite } from "./browser_harness.mjs";

const PORT = 8741;

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const origin = new URL(baseUrl).origin;
const basePath = new URL(baseUrl).pathname;

// Read the first chapter out of the site under test rather than naming one,
// so this keeps working when a volume is added, renamed or reordered.
let boxes;
try {
  boxes = await (await fetch(`${baseUrl}boxes.json`)).json();
} catch (e) {
  stop();
  console.log(`FAIL  could not read ${baseUrl}boxes.json: ${e.message}`);
  process.exit(1);
}
const first = boxes.find(b => /\/ch\d\d-/.test(b.id));
if (!first) { stop(); skip("no chapter pages in the site -- build first."); }
const PAGE = `${first.volume}/${first.slug}.html`;

const browser = await launch(chromium, stop);
const page = await browser.newPage();

const external = [], escaped = [], failed = [], errored = [], errors = [], fetched = [];
const types = {};
page.on("request", r => {
  const u = new URL(r.url());
  if (u.origin !== origin) external.push(r.url());
  else if (!u.pathname.startsWith(basePath)) escaped.push(u.pathname);
  if (u.pathname.includes("/pyodide/")) fetched.push(u.pathname);
});
page.on("response", r => {
  const u = new URL(r.url());
  if (r.status() >= 400) errored.push(`${r.status()} ${u.pathname}`);
  const name = u.pathname.split("/").pop();
  if (name === "pyodide.mjs" || name.endsWith(".wasm")) types[name] = r.headers()["content-type"] || "";
});
page.on("requestfailed", r => failed.push(`${r.url()} :: ${r.failure()?.errorText}`));
page.on("pageerror", e => errors.push(String(e)));

const problems = [];
const check = (ok, what) => { console.log(`  ${ok ? "ok  " : "FAIL"}  ${what}`);
                              if (!ok) problems.push(what); };

try {
  await page.goto(`${baseUrl}${PAGE}`, { waitUntil: "load" });

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
} catch (e) {
  check(false, `the page never got there: ${e.message.split("\n")[0]}`);
}

// What the network saw is checked whether or not the page got there. When the
// runtime never loads, an escaped path or a 404 is usually the reason, and
// these lines are what say so; left inside the try above, a timeout skipped
// them and the only report was "the page never got there".
try {
  check(external.length === 0,
        `no request leaves this origin${external.length ? ": " + external.join(", ") : ""}`);
  check(escaped.length === 0,
        `every request stays under ${basePath}${escaped.length ? ": " + escaped.join(", ") : ""}`);
  check(errored.length === 0,
        `no response is an error${errored.length ? ": " + errored.join(", ") : ""}`);
  const mjs = types["pyodide.mjs"] || "";
  const wasm = Object.entries(types).find(([name]) => name.endsWith(".wasm"))?.[1] || "";
  check(/javascript/.test(mjs), `pyodide.mjs is served as JavaScript (${mjs || "not seen"})`);
  check(wasm.startsWith("application/wasm"),
        `the runtime .wasm is served as application/wasm (${wasm || "not seen"})`);
  check(failed.length === 0, `no failed request${failed.length ? ": " + failed.join(", ") : ""}`);
  check(errors.length === 0, `no page error${errors.length ? ": " + errors.join(", ") : ""}`);
} finally {
  await browser.close();
  stop();
}

console.log(problems.length
  ? `\n${problems.length} problem(s) in the browser`
  : "\nthe page works from a real browser, and talks to nobody else");
process.exit(problems.length ? 1 : 0);
