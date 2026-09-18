/* Python Foundations — the browser runtime.
 *
 * Everything that knows about Pyodide lives behind runPython() below, so the
 * day a Web Worker + JSPI setup is worth it, only that function changes.
 *
 * Pinned to Pyodide 314.0.7 (CPython 3.14). Note the loader is pyodide.asm.mjs
 * as of 314.0.0 — pyodide.asm.js no longer exists on the CDN.
 */

const PYODIDE = "https://cdn.jsdelivr.net/npm/pyodide@314.0.7/";

/* web/box_runner.py, inlined by build.py */
const BOX_RUNNER = {{harness}};

const pill = document.querySelector(".runtime");
const slug = document.body.dataset.slug;

const TIMEOUT_SECONDS = 5;

let pyodide = null;
let loading = null;
let runBox = null;        // the Python entry point from box_runner.py
let sink = null;          // where the currently running program's output goes

function say(message, ready = false) {
  pill.hidden = false;
  pill.classList.toggle("ready", ready);
  pill.querySelector(".msg").textContent = message;
}

async function boot() {
  if (pyodide) return pyodide;
  if (loading) return loading;

  loading = (async () => {
    say("Starting Python… (about 6 MB, once)");
    const { loadPyodide } = await import(PYODIDE + "pyodide.mjs");
    pyodide = await loadPyodide({ indexURL: PYODIDE });

    // Send every program's output to whichever box is running.
    pyodide.setStdout({ batched: (text) => sink && sink(text) });
    pyodide.setStderr({ batched: (text) => sink && sink(text) });

    // Set stdin explicitly rather than relying on the default: Pyodide's own
    // JS API reference and its streams page disagree about what the default is,
    // and prompt() returns null on Cancel, which Python reads as EOF and turns
    // into an EOFError in the middle of chapter 3. An empty line is kinder.
    pyodide.setStdin({
      stdin: () => {
        const typed = globalThis.prompt("Input:");
        return typed === null ? "" : typed;
      },
    });

    // box_runner.py is inlined here at build time by build.py.
    pyodide.runPython(BOX_RUNNER);
    runBox = pyodide.globals.get("run_box");

    say("Python ready", true);
    setTimeout(() => (pill.hidden = true), 1600);
    return pyodide;
  })();

  return loading;
}

/** Run source in a namespace of its own. Returns {output, error}. */
async function runPython(source, onOutput) {
  const py = await boot();
  const chunks = [];
  sink = (text) => {
    chunks.push(text);
    onOutput && onOutput(chunks.join("\n"));
  };

  let error = null;
  const namespace = py.runPython("dict()");
  try {
    runBox(source, TIMEOUT_SECONDS, namespace);
  } catch (e) {
    error = String(e.message || e);
  } finally {
    namespace.destroy();
    sink = null;
  }
  return { output: chunks.join("\n"), error };
}

/* ------------------------------------------------------------------ boxes */

function autosize(area) {
  area.style.height = "auto";
  area.style.height = area.scrollHeight + "px";
}

document.querySelectorAll(".box").forEach((box) => {
  const area = box.querySelector("textarea");
  const runButton = box.querySelector(".run");
  const resetButton = box.querySelector(".reset");
  const status = box.querySelector(".status");
  const result = box.querySelector(".result");

  const original = area.value;
  const key = `pf:${slug}:${box.dataset.box}`;

  // Restore an edit from a previous visit. Autosave is the whole safety net
  // for a runaway loop: on the main thread there is no way to interrupt one,
  // so reloading the tab must never cost the learner their work.
  try {
    const saved = localStorage.getItem(key);
    if (saved !== null && saved !== original) area.value = saved;
  } catch (e) { /* private window, blocked storage — not worth breaking over */ }

  const edited = () => area.value !== original;
  resetButton.hidden = !edited();
  autosize(area);

  area.addEventListener("input", () => {
    autosize(area);
    resetButton.hidden = !edited();
    try {
      edited() ? localStorage.setItem(key, area.value) : localStorage.removeItem(key);
    } catch (e) { /* ignore */ }
  });

  area.addEventListener("keydown", (event) => {
    if (event.key !== "Tab") return;
    event.preventDefault();
    const { selectionStart: start, selectionEnd: end, value } = area;
    area.value = value.slice(0, start) + "    " + value.slice(end);
    area.selectionStart = area.selectionEnd = start + 4;
    area.dispatchEvent(new Event("input"));
  });

  resetButton.addEventListener("click", () => {
    area.value = original;
    area.dispatchEvent(new Event("input"));
    result.hidden = true;
  });

  runButton.addEventListener("click", async () => {
    const setup = box.dataset.setup ? box.dataset.setup + "\n" : "";
    runButton.disabled = true;
    status.textContent = pyodide ? "running…" : "starting Python…";
    result.hidden = false;
    result.classList.remove("error");
    result.textContent = "";

    // Let the browser paint "running…" before Python takes the thread.
    await new Promise((resolve) => requestAnimationFrame(() => setTimeout(resolve, 0)));

    const { output, error } = await runPython(setup + area.value, (text) => {
      result.textContent = text;
    });

    if (error) {
      result.classList.add("error");
      result.textContent = (output ? output + "\n" : "") + error;
      status.textContent = error.includes("KeyboardInterrupt")
        ? `stopped after ${TIMEOUT_SECONDS}s`
        : "raised an error";
    } else {
      result.textContent = output || "(no output)";
      status.textContent = "done";
    }
    runButton.disabled = false;
    setTimeout(() => (status.textContent = ""), 2500);
  });
});
