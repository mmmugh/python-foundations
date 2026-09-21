import { loadPyodide } from "pyodide";
import { readFileSync } from "node:fs";
const REPO = new URL("..", import.meta.url).pathname;
const SP = new URL(".", import.meta.url).pathname;

const checks = JSON.parse(readFileSync(`${REPO}/content/_checks.json`, "utf8"));
const boxes = JSON.parse(readFileSync(`${REPO}/site/boxes.json`, "utf8"));
const py = await loadPyodide();
py.runPython(readFileSync(`${REPO}/web/box_runner.py`, "utf8"));
py.runPython(readFileSync(`${SP}/project_answers.py`, "utf8"));
const checkStdin = py.globals.get("check_stdin");
const ALT = py.globals.get("ALT"), BUG = py.globals.get("BUG");

const call = (src, runs) => { const r = checkStdin(src, runs); const v=[r.get(0), r.get(1).toJs()]; r.destroy(); return v; };

console.log("project                              course's own   another style   a real bug");
console.log("-".repeat(88));
let bad = 0;
for (const [id, spec] of Object.entries(checks)) {
  if (!ALT.get(id)) continue;
  const book = boxes.find((b) => b.id === id).code;
  const runs = py.toPy(spec.runs);
  const [a, an] = call(book, runs);
  const [b] = call(ALT.get(id), runs);
  const [c, cn] = call(BUG.get(id), runs);
  runs.destroy();
  const ok = a === true && b === true && c === false;
  if (!ok) bad++;
  console.log(`${id.padEnd(38)}${String(a).padEnd(15)}${String(b).padEnd(16)}${String(c).padEnd(6)}${ok ? "ok" : "*** REJECT ***"}`);
  if (a !== true) console.log(`      the course's own solution FAILED: ${an[0]}`);
  if (b !== true) console.log(`      the other style FAILED: ${call(ALT.get(id), py.toPy(spec.runs))[1][0]}`);
  if (ok) console.log(`      bug is caught with: ${cn[0]}`);
}
console.log("-".repeat(88));
console.log(bad === 0 ? "all 4 project checks sound" : `${bad} rejected`);
