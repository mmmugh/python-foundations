import { loadPyodide } from "pyodide";
import { readFileSync } from "node:fs";
const REPO = new URL("..", import.meta.url).pathname;
const py = await loadPyodide();
py.runPython(readFileSync(`${REPO}/web/box_runner.py`, "utf8"));
const replRun = py.globals.get("repl_run");
let out = [];
py.setStdout({ batched: (t) => out.push(t) });

const ns = py.runPython("dict()");
const session = [
  'type("5")', '"5" * 3', 'int("5") * 3',
  'x = [1, 2, 3]', 'x.append(4)', 'x', 'len(x)',
  'for i in range(3):', '    print(i * i)', '',
  'def double(n):', '    return n * 2', '',
  'double(21)', '_ + 1',
  'undefined_name', 'while True:\n    pass',
];
let pending = [];
for (const line of session) {
  pending.push(line);
  const source = pending.join("\n");
  out = [];
  let value = "", incomplete = false, err = null;
  try {
    const r = replRun(source, 2, ns);
    value = r.get(0); incomplete = r.get(1); r.destroy();
  } catch (e) { err = String(e.message || e).trim().split("\n").filter(Boolean).pop(); }
  const prompt = pending.length > 1 ? "... " : ">>> ";
  if (incomplete) { console.log(`${prompt}${line}`); continue; }
  console.log(`${prompt}${line}`);
  if (out.length) console.log(out.join("\n"));
  if (err) console.log(`    ${err}`);
  else if (value) console.log(value);
  pending = [];
}
