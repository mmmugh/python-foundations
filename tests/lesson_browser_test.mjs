/* The lesson format in a real browser: a hint revealed one at a time, then the
 * worked solution; a multiple-choice check; a trace-table check; and a unit's
 * quiz link. Builds a throwaway lesson volume, and removes it again whatever
 * happens. */
import { execFileSync } from "node:child_process";
import { launch, loadChromium, startSite, ROOT } from "./browser_harness.mjs";

const PORT = 8743;
const trial = (step) => execFileSync("python3", ["tests/lesson_trial.py", step], { cwd: ROOT, stdio: "inherit" });

const chromium = await loadChromium();
trial("up");
let bad = 0;
const expect = (label, ok) => { if (!ok) bad++; console.log(`  ${ok ? "ok  " : "FAIL"}  ${label}`); };
try {
  const { baseUrl, stop } = await startSite(PORT);
  const browser = await launch(chromium, stop);
  try {
    const page = await browser.newPage();
    await page.goto(`${baseUrl}_trial-lessons/ch02a-trial.html`, { waitUntil: "load" });

    expect("a unit's quiz link is labeled with the unit",
           (await page.locator(".quiz a").textContent()) === "Unit 2 quiz");

    const hinted = page.locator('[data-box="_trial-lessons/ch02a-trial#4"]');
    await hinted.locator(".hint-next").click();
    expect("the first hint shows", await hinted.locator(".hint").nth(0).isVisible());
    expect("the second hint waits", !(await hinted.locator(".hint").nth(1).isVisible()));
    await hinted.locator(".hint-next").click();
    expect("the solution waits until every hint is shown", !(await hinted.locator(".solution").isVisible()));
    await hinted.locator(".hint-next").click();
    expect("then the worked solution shows", await hinted.locator(".solution").isVisible());

    const choice = page.locator('[data-box="_trial-lessons/ch02a-trial#2"]');
    await choice.locator('input[value="0"]').check();
    await choice.locator(".check").click();
    expect("a wrong choice is told so", (await choice.locator(".result").textContent()).startsWith("Not that one"));
    await choice.locator('input[value="1"]').check();
    await choice.locator(".check").click();
    expect("the right choice is told why", (await choice.locator(".result").textContent()).includes("says what"));

    const trace = page.locator('[data-box="_trial-lessons/ch02a-trial#3"]');
    const cells = trace.locator("input.cell");
    for (const [i, v] of ["12", "-", "12", "3"].entries()) await cells.nth(i).fill(v);
    await trace.locator(".check").click();
    await page.waitForFunction(() => document.querySelector('[data-box="_trial-lessons/ch02a-trial#3"] .result').className.includes("passed")
      || document.querySelector('[data-box="_trial-lessons/ch02a-trial#3"] .result').className.includes("failed"), null, { timeout: 60000 });
    expect("a correct trace table passes", (await trace.locator(".result").getAttribute("class")).includes("passed"));
    await cells.nth(2).fill("13");
    await trace.locator(".check").click();
    await page.waitForFunction(() => document.querySelector('[data-box="_trial-lessons/ch02a-trial#3"] .result').className.includes("failed"), null, { timeout: 60000 });
    expect("a wrong cell is named by line and variable", (await trace.locator(".result").textContent()).includes("line 2, price"));
  } finally {
    await browser.close();
    stop();
  }
} finally {
  trial("down");
}
console.log(`\n${bad ? bad + " wrong" : "the lesson format works in a real browser"}`);
process.exit(bad ? 1 : 0);
