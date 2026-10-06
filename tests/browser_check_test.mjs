/* The Check button, end to end, across the JavaScript-to-Python boundary.
 *
 * A check's test cases travel from the page to box_runner.py as JSON. They
 * used to be converted by pyodide.toPy(), which loses two things: JSON's 61.0
 * arrives as a Python int, so an answer correctly printing "61.0" was marked
 * wrong; and JSON's null arrives as a JavaScript null that is not None, so a
 * case expecting None could never match. Both were invisible from CPython and
 * from node. The fix hands the JSON text to Python (from_json in
 * box_runner.py, called from web/app.js). This proves it from a real page,
 * and fails if that fix is reverted.
 *
 * It first lived in a session scratchpad and was lost with it.
 */

import { launch, loadChromium, startSite } from "./browser_harness.mjs";

const PORT = 8742;

const FIND_FOLDER = [
  "def find_folder(folder, name):",
  "    if folder['name'] == name:",
  "        return folder",
  "    for inner in folder['folders']:",
  "        found = find_folder(inner, name)",
  "        if found:",
  "            return found",
  "    return None",
].join("\n");

// Each trial names a practice step by its data-box id. The first two each need
// one half of the fix; the last proves Check is not simply saying yes.
const TRIALS = [
  { box: "vol1-foundations/ch12-recursion-and-problem-solving-practice#6",
    why: "a case expecting None", code: FIND_FOLDER, pass: true },
  { box: "vol1-foundations/ch11-searching-and-sorting-practice#8",
    why: "formatting 61.0, which a JavaScript number turns into 61", pass: true,
    code: [
      "def ranked(results):",
      "    return sorted(results, key=lambda result: result[1])",
      "",
      "def leaderboard_lines(results):",
      "    return [f'{i}. {r[0]} {r[1]}' for i, r in enumerate(ranked(results), 1)]",
    ].join("\n") },
  { box: "vol1-foundations/ch12-recursion-and-problem-solving-practice#6",
    why: "a wrong answer", pass: false,
    code: "def find_folder(folder, name):\n    return folder" },
];

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const browser = await launch(chromium, stop);
const page = await browser.newPage();

const problems = [];
const check = (ok, what) => { console.log(`  ${ok ? "ok  " : "FAIL"}  ${what}`);
                              if (!ok) problems.push(what); };

try {
  for (const t of TRIALS) {
    await page.goto(`${baseUrl}${t.box.split("#")[0]}.html`, { waitUntil: "load" });
    const box = page.locator(`.box[data-box="${t.box}"]`);
    await box.locator("textarea").fill(t.code);
    await box.locator("button.check").click();
    const result = box.locator(".result").first();
    await page.waitForFunction(
      el => { const s = el.textContent.trim(); return s.length > 0 && !/checking/i.test(s); },
      await result.elementHandle(), { timeout: 240000 });
    const text = (await result.textContent()).trim();
    const passed = /passed all/i.test(text);
    check(passed === t.pass,
          `${t.box.split("/")[1]}: ${t.why} ${t.pass ? "passes" : "is rejected"} (${text.split("\n")[0]})`);
  }
} catch (e) {
  check(false, `the check never finished: ${e.message.split("\n")[0]}`);
} finally {
  await browser.close();
  stop();
}

console.log(problems.length
  ? `\n${problems.length} problem(s) with Check`
  : "\nCheck gets the right answer across the boundary, and still rejects a wrong one");
process.exit(problems.length ? 1 : 0);
