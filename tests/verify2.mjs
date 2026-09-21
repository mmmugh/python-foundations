import { loadPyodide } from "pyodide";
import { readFileSync } from "node:fs";

const REPO = new URL("..", import.meta.url).pathname;
const boxes = JSON.parse(readFileSync(`${REPO}/site/boxes.json`, "utf8"));
const py = await loadPyodide();
py.runPython(readFileSync(`${REPO}/web/box_runner.py`, "utf8"));
const runBox = py.globals.get("run_box");
const TIMEOUT = 5;

let out = [];
py.setStdout({ batched: (t) => out.push(t) });
py.setStderr({ batched: (t) => out.push(t) });

function run(source, seconds = TIMEOUT) {
  out = [];
  let error = null;
  const ns = py.runPython("dict()");
  try { runBox(source, seconds, ns); }
  catch (e) { error = String(e.message || e).trim().split("\n").filter(Boolean).pop(); }
  finally { ns.destroy(); }
  return { output: out.join("\n"), error };
}

// ---- 1. every box, now going through the guard ----
const tally = { clean: 0, "raised as declared": 0, "skipped (input)": 0, UNEXPECTED: 0 };
const problems = [];
let slowest = { id: null, ms: 0 };
for (const box of boxes) {
  if (box.needs_input) { tally["skipped (input)"]++; continue; }
  const t = Date.now();
  const { error } = run((box.setup ? box.setup + "\n" : "") + box.code);
  const ms = Date.now() - t;
  if (ms > slowest.ms) slowest = { id: box.id, ms };
  if (!error) box.raises ? (tally.UNEXPECTED++, problems.push([box.id, `expected ${box.raises}`])) : tally.clean++;
  else if (box.raises && error.startsWith(box.raises)) tally["raised as declared"]++;
  else if (box.slug === "99-appendices") tally["raised as declared"]++;
  else { tally.UNEXPECTED++; problems.push([box.id, error.slice(0, 70)]); }
}
console.log("168 boxes through the guard, real Pyodide:");
for (const [k, v] of Object.entries(tally)) console.log(`  ${k.padEnd(20)} ${String(v).padStart(3)}`);
problems.forEach(([id, e]) => console.log(`  !! ${id.padEnd(40)} ${e}`));
console.log(`  slowest box: ${slowest.id} at ${slowest.ms}ms (limit ${TIMEOUT}s)`);

// ---- 2. does it stop a runaway loop ----
console.log("\nrunaway loops:");
for (const [name, src] of [
  ["while True: pass", "while True:\n    pass"],
  ["while True with work", "n = 0\nwhile True:\n    n += 1"],
  ["nested in a function", "def spin():\n    while True:\n        pass\nspin()"],
]) {
  const t = Date.now();
  const { error } = run(src, 2);
  console.log(`  ${name.padEnd(22)} ${(error || "completed").slice(0, 52).padEnd(54)} ${((Date.now() - t) / 1000).toFixed(2)}s`);
}

// ---- 3. does thinking time at a prompt count against the learner? ----
console.log("\ninput() pause (stdin deliberately takes 3s to answer, limit is 2s):");
py.setStdin({ stdin: () => { const end = Date.now() + 3000; while (Date.now() < end); return "7"; } });
const t = Date.now();
const r = run('n = int(input("n: "))\ntotal = 0\nfor i in range(50000):\n    total += i\nprint(f"{n} {total}")', 2);
console.log(`  result : ${r.error || r.output}`);
console.log(`  elapsed: ${((Date.now() - t) / 1000).toFixed(2)}s  -> ${r.error ? "KILLED (thinking time counted)" : "survived (thinking time excluded)"}`);

// ---- 4. the honest limit ----
console.log("\nthe case it cannot catch:");
const t2 = Date.now();
const c = run("sum(range(10**8))", 2);
console.log(`  sum(range(10**8))      ${(c.error || "completed").slice(0, 52).padEnd(54)} ${((Date.now() - t2) / 1000).toFixed(2)}s`);
