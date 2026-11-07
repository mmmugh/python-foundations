/* The step-by-step lessons in a real browser. Every page loads without a
 * script error, fits a 390-pixel phone screen without sideways scrolling,
 * and its links (hints to the reference page, the unit quiz) resolve. One
 * checked exercise goes through Python in the page. Run it with BASE=/name/
 * too, the way GitHub Pages serves the site. */
import { launch, loadChromium, startSite } from "./browser_harness.mjs";

const PORT = 8744;
const PAGES = ["ch01z-welcome-back", "ch02a-naming-a-value", "ch02b-names-and-kinds",
               "ch02c-asking-the-user", "ch02d-putting-it-together", "99-how-to-start-a-problem"];

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const browser = await launch(chromium, stop);
let bad = 0;
const expect = (label, ok) => { if (!ok) bad++; console.log(`  ${ok ? "ok  " : "FAIL"}  ${label}`); };
try {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  for (const slug of PAGES) {
    const url = `${baseUrl}vol1-steps/${slug}.html`;
    const response = await page.goto(url, { waitUntil: "load" });
    expect(`${slug} loads`, response && response.ok());
    expect(`${slug} fits a phone screen`, await page.evaluate(
      () => document.documentElement.scrollWidth <= window.innerWidth));
    for (const href of await page.$$eval("a[href]", (as) => as.map((a) => a.href))) {
      if (!href.startsWith(baseUrl)) continue;
      const linked = await page.request.get(href);
      if (!linked.ok()) expect(`${slug} links to ${href}`, false);
    }
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
