/* Walk every checked exercise in vol1-steps through a real browser: type the
 * wrong answer (must fail), then the right one (must pass). The answers come
 * from the course's own data (tests/steps_answers.py), not typed in by hand,
 * so a check that silently stopped working cannot hide behind a stale
 * fixture here the way it could behind one.
 *
 *     node steps_walk.mjs                 every unit
 *     node steps_walk.mjs 03              only unit 3's lessons
 */
import { execFileSync } from "node:child_process";
import { join } from "node:path";
import { launch, loadChromium, ROOT, startSite } from "./browser_harness.mjs";

const PORT = 8750;
const unit = process.argv[2];
const args = [join(ROOT, "tests", "steps_answers.py")];
if (unit) args.push(unit);
const items = JSON.parse(execFileSync("python3", args, { encoding: "utf8" }));

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const browser = await launch(chromium, stop);
let bad = 0, current = "";
const page = await browser.newPage({ viewport: { width: 390, height: 844 } });

async function attempt(it, answer) {
  const id = `vol1-steps/${it.slug}#${it.n}`;
  const box = page.locator(`[data-box="${id}"]`);
  if (it.kind === "choice") await box.locator(`input[value="${answer}"]`).check();
  else if (it.kind === "predict") await box.locator("textarea.prediction").fill(answer);
  else if (it.kind === "trace") {
    const cells = box.locator("input.cell");
    for (const [i, v] of answer.entries()) await cells.nth(i).fill(v);
  } else await box.locator("textarea:not(.prediction)").fill(answer);
  // The box keeps last run's verdict on screen until Check runs again; clear
  // it first so a stale "passed" from a previous attempt cannot be mistaken
  // for this one.
  await box.evaluate((b) => { const r = b.querySelector(".result"); r.className = "result"; r.hidden = true; });
  await box.locator(".check").click();
  await page.waitForFunction((id) => /passed|failed/.test(
    document.querySelector(`[data-box="${id}"] .result`).className), id, { timeout: 90000 });
  return (await box.locator(".result").getAttribute("class")).includes("passed");
}

try {
  for (const it of items) {
    if (it.slug !== current) {
      await page.goto(`${baseUrl}vol1-steps/${it.slug}.html`, { waitUntil: "load" });
      current = it.slug;
    }
    const wrong = await attempt(it, it.wrong);
    const right = await attempt(it, it.right);
    if (wrong || !right) {
      bad++;
      console.log(`  FAIL  ${it.slug}#${it.n} ${it.kind}: wrong ${wrong ? "PASSED" : "refused"}, `
                  + `right ${right ? "passed" : "REFUSED"}`);
    }
  }
} finally {
  await browser.close();
  stop();
}
console.log(`\n${items.length} exercises; `
            + `${bad ? bad + " wrong" : "every one refuses a wrong answer and takes a right one, in the page"}`);
process.exit(bad ? 1 : 0);
