import { loadPyodide } from "pyodide";
import { readFileSync } from "node:fs";
import { checks, boxes, qualify } from "./volume.mjs";
const REPO = new URL("..", import.meta.url).pathname;
const SP = new URL(".", import.meta.url).pathname;

const py = await loadPyodide();
py.runPython(readFileSync(`${REPO}/web/box_runner.py`, "utf8"));   // the SHIPPED code
py.runPython(readFileSync(`${SP}/reference_solutions.py`, "utf8"));
const checkFunction = py.globals.get("check_function");
const checkOutput = py.globals.get("check_output");
const checkPrediction = py.globals.get("check_prediction");
const GOOD = py.globals.get("GOOD"), MUTANT = py.globals.get("MUTANT");
const OG = py.globals.get("OUTPUT_GOOD"), OM = py.globals.get("OUTPUT_MUTANT");

let bad = 0, n = 0;
const call = (fn, ...a) => { const r = fn(...a); const v = [r.get(0), r.get(1).toJs()]; r.destroy(); return v; };

for (const [id, spec] of Object.entries(checks)) {
  n++;
  if (spec.kind === "function") {
    const cases = py.toPy(spec.cases);
    const [g] = call(checkFunction, GOOD.get(spec.name), spec.name, cases);
    const [m, notes] = call(checkFunction, MUTANT.get(spec.name), spec.name, cases);
    cases.destroy();
    if (!(g === true && m === false)) { bad++; console.log(`  BROKEN ${id}`); }
    else if (id.endsWith("#3") && spec.name === "count_above")
      console.log(`  sample failure message: ${notes[0]}`);
  } else if (spec.kind === "output") {
    const [g] = call(checkOutput, OG.get(id), spec.expected);
    const [m] = call(checkOutput, OM.get(id), spec.expected);
    if (!(g === true && m === false)) { bad++; console.log(`  BROKEN ${id}`); }
  }
}

// predict-the-output: a right prediction passes, a wrong one is told which line
console.log("\npredict-the-output, using the book's own ch01 fence:");
const fence = `print("A")\nprint("B", "C")\nprint()\nprint(2 * 3)\nprint("2 * 3")`;
for (const [label, guess] of [
  ["exactly right", "A\nB C\n\n6\n2 * 3"],
  ["thinks 2 * 3 stays literal", "A\nB C\n\n2 * 3\n2 * 3"],
  ["forgot the blank line", "A\nB C\n6\n2 * 3"],
]) {
  const r = checkPrediction(fence, guess);
  const ok = r.get(0), notes = r.get(1).toJs(); r.destroy();
  console.log(`  ${ok ? "PASS" : "FAIL"}  ${label.padEnd(28)} ${notes[0] || ""}`);
}
console.log(`\n${n} checks exercised through the shipped box_runner.py — ${bad === 0 ? "all sound" : bad + " broken"}`);
