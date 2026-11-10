/* The step-by-step lessons in a real browser. Every page loads without a
 * script error, fits a 390-pixel phone screen without sideways scrolling,
 * and its links (hints to the reference page, the unit quiz) resolve. A
 * `pre`, `.trace-wrap` or `.options` may scroll inside itself, but never
 * pushes the page wider. Practice pages are built pages too, so they are
 * walked here, and each must be offered from a lesson, labeled optional.
 * One checked exercise goes through Python in the page. Run it with
 * BASE=/name/ too, the way GitHub Pages serves the site. */
import { readdirSync } from "node:fs";
import { join } from "node:path";
import { launch, loadChromium, ROOT, startSite } from "./browser_harness.mjs";

const PORT = 8744;
// Derived from what the build actually produced, not typed in twice: a new
// lesson shows up here the day its file lands, with nothing to edit here.
// This volume has no bundle, so every page at the top level is a lesson.
const PAGES = readdirSync(join(ROOT, "site", "vol1-steps"))
  .filter((name) => name.endsWith(".html"))
  .map((name) => name.slice(0, -".html".length))
  .sort();

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const browser = await launch(chromium, stop);
let bad = 0;
const expect = (label, ok, detail) => {
  if (!ok) bad++;
  console.log(`  ${ok ? "ok  " : "FAIL"}  ${label}${!ok && detail ? "  (" + detail + ")" : ""}`);
};
try {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  const offered = new Set();
  for (const slug of PAGES) {
    const url = `${baseUrl}vol1-steps/${slug}.html`;
    const response = await page.goto(url, { waitUntil: "load" });
    expect(`${slug} loads`, response && response.ok());
    expect(`${slug} fits a phone screen`, await page.evaluate(
      () => document.documentElement.scrollWidth <= window.innerWidth));
    const overflowing = await page.$$eval("pre, .trace-wrap, .options", (els) => els
      // A closed <details> (a hint not yet revealed, a solution not yet
      // shown) keeps its last-known layout box under content-visibility,
      // so scrollWidth/clientWidth stay nonzero though nothing is on
      // screen. Only what the learner can actually see is in scope here.
      .filter((el) => el.checkVisibility({ checkVisibilityCSS: true }))
      .filter((el) => el.scrollWidth > el.clientWidth)
      .filter((el) => !["auto", "scroll"].includes(getComputedStyle(el).overflowX))
      .map((el) => el.className || el.tagName.toLowerCase()));
    expect(`${slug} containers scroll inside themselves, never the page`,
           overflowing.length === 0, JSON.stringify(overflowing));
    for (const href of await page.$$eval("a[href]", (as) => as.map((a) => a.href))) {
      if (!href.startsWith(baseUrl)) continue;
      const linked = await page.request.get(href);
      if (!linked.ok()) expect(`${slug} links to ${href}`, false);
    }
    for (const p of await page.$$eval("p.practice", (ps) => ps.map((p) => ({
      href: p.querySelector("a")?.getAttribute("href") || "", text: p.textContent })))) {
      if (/optional/i.test(p.text) && /Nothing later needs it/.test(p.text)) offered.add(p.href.replace(/\.html$/, ""));
    }
  }
  for (const slug of PAGES.filter((s) => s.endsWith("-practice"))) {
    expect(`${slug} is offered from its unit, labeled optional`, offered.has(slug));
  }
  expect("no page raised a script error", errors.length === 0);

  await page.goto(`${baseUrl}vol1-steps/ch02a-naming-a-value.html`, { waitUntil: "load" });
  const box = page.locator('[data-box="vol1-steps/ch02a-naming-a-value#3"]');
  await box.locator("textarea").fill("days = 7\nprint(days * 24)");
  await box.locator(".check").click();
  await page.waitForFunction(() => /passed|failed/.test(
    document.querySelector('[data-box="vol1-steps/ch02a-naming-a-value#3"] .result').className), null, { timeout: 60000 });
  expect("a lesson exercise is checked by Python in the page",
         (await box.locator(".result").getAttribute("class")).includes("passed"));
} finally {
  await browser.close();
  stop();
}
console.log(`\n${bad ? bad + " wrong" : "the lessons work in a real browser, on a phone, under any path"}`);
process.exit(bad ? 1 : 0);
