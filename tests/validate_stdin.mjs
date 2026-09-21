import { loadPyodide } from "pyodide";
import { readFileSync } from "node:fs";
import { checks, boxes, qualify } from "./volume.mjs";
const REPO = new URL("..", import.meta.url).pathname;
const SP = new URL(".", import.meta.url).pathname;
const py = await loadPyodide();
py.runPython(readFileSync(`${REPO}/web/box_runner.py`, "utf8"));
py.runPython(readFileSync(`${SP}/stdin_answers.py`, "utf8"));
const checkStdin = py.globals.get("check_stdin");
const A = py.globals.get("A");

let bad = 0, n = 0;
console.log("exercise                              style A  style B  mistake  verdict");
console.log("-".repeat(80));
for (const [id, spec] of Object.entries(checks)) {
  if (spec.kind !== "stdin") continue;
  const trio = A.get(id);
  if (!trio) continue;          // chapter projects are covered by validate_projects.mjs
  n++;
  const runs = py.toPy(spec.runs);
  const res = [0, 1, 2].map((i) => {
    const r = checkStdin(trio.get(i), runs);
    const v = [r.get(0), r.get(1).toJs()];
    r.destroy();
    return v;
  });
  runs.destroy();
  const [[a], [b], [m, why]] = res;
  const ok = a === true && b === true && m === false;
  if (!ok) bad++;
  console.log(`${id.padEnd(37)} ${String(a).padEnd(8)} ${String(b).padEnd(8)} ${String(m).padEnd(8)} ${ok ? "ok" : "*** REJECT ***"}`);
  if (!ok) {
    if (a !== true) console.log(`      style A false-failed: ${res[0][1][0]}`);
    if (b !== true) console.log(`      style B false-failed: ${res[1][1][0]}`);
    if (m !== false) console.log(`      mistake slipped through`);
  } else if (id === "ch05-repetition#2") {
    console.log(`      message a learner sees: ${why[0]}`);
  }
}
console.log("-".repeat(80));
console.log(`${n} stdin checks — ${bad === 0 ? "all sound" : bad + " rejected"}`);

/* Exit status, not just a printed table. Without this the harness prints
 * "3 broken" and still exits 0, so anything that gates on it -- npm test, a CI
 * step, `node x.mjs && node y.mjs` -- reports green while the checks are
 * broken. A test that cannot fail its caller is a report, not a test.
 */
if (n === 0) { console.log("no stdin checks were exercised -- do the fixture ids still\nmatch _checks.json?"); process.exit(1); }
process.exit(bad ? 1 : 0);

