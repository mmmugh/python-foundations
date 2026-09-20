/* Python Foundations — the browser runtime.
 *
 * Everything that knows about Pyodide lives behind runPython() and the check
 * helpers below, so the day a Web Worker + JSPI setup is worth it, only those
 * change. Pinned to Pyodide 314.0.7 (CPython 3.14). The loader is
 * pyodide.asm.mjs as of 314.0.0 — pyodide.asm.js no longer exists on the CDN.
 */

const PYODIDE = "https://cdn.jsdelivr.net/npm/pyodide@314.0.7/";

/* web/box_runner.py, inlined by build.py */
const BOX_RUNNER = {{harness}};

const TIMEOUT_SECONDS = 5;

let pyodide = null;
let loading = null;
let python = {};          // the entry points from box_runner.py
let sink = null;          // where the currently running program's output goes

const pill = document.querySelector(".runtime");
const slug = document.body.dataset.slug;

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

    pyodide.setStdout({ batched: (text) => sink && sink(text) });
    pyodide.setStderr({ batched: (text) => sink && sink(text) });

    // Set stdin explicitly rather than relying on the default: Pyodide's JS API
    // reference and its streams page disagree about what the default is, and
    // prompt() returns null on Cancel, which Python reads as EOF and turns into
    // an EOFError in the middle of chapter 3. An empty line is kinder.
    pyodide.setStdin({
      stdin: () => {
        const typed = globalThis.prompt("Input:");
        return typed === null ? "" : typed;
      },
    });

    pyodide.runPython(BOX_RUNNER);
    for (const name of ["run_box", "check_function", "check_output",
                        "check_prediction", "check_stdin"]) {
      python[name] = pyodide.globals.get(name);
    }

    say("Python ready", true);
    setTimeout(() => (pill.hidden = true), 1600);
    return pyodide;
  })();

  return loading;
}

/** Run source in a namespace of its own. Returns {output, error}. */
async function runPython(source, onOutput) {
  await boot();
  const chunks = [];
  sink = (text) => {
    chunks.push(text);
    onOutput && onOutput(chunks.join("\n"));
  };

  let error = null;
  const namespace = pyodide.runPython("dict()");
  try {
    python.run_box(source, TIMEOUT_SECONDS, namespace);
  } catch (e) {
    error = String(e.message || e);
  } finally {
    namespace.destroy();
    sink = null;
  }
  return { output: chunks.join("\n"), error };
}

/** Check one answer. Returns {passed, notes, total}. */
async function checkAnswer(spec, source, prediction) {
  await boot();
  sink = null;
  let result;
  if (spec.kind === "function") {
    const cases = pyodide.toPy(spec.cases);
    result = python.check_function(source, spec.name, cases);
    cases.destroy();
  } else if (spec.kind === "output") {
    result = python.check_output(source, spec.expected);
  } else if (spec.kind === "stdin") {
    const runs = pyodide.toPy(spec.runs);
    result = python.check_stdin(source, runs);
    runs.destroy();
  } else {
    result = python.check_prediction(source, prediction || "");
  }
  const passed = result.get(0);
  const notes = result.get(1).toJs();
  result.destroy();
  return { passed, notes, total: (spec.cases || spec.runs || [1]).length };
}

/* ------------------------------------------------------------------ boxes */

function autosize(area) {
  area.style.height = "auto";
  area.style.height = area.scrollHeight + "px";
}

function remember(key, value, original) {
  try {
    value !== original ? localStorage.setItem(key, value) : localStorage.removeItem(key);
  } catch (e) { /* private window, blocked storage — not worth breaking over */ }
}

function restore(key, area, original) {
  try {
    const saved = localStorage.getItem(key);
    if (saved !== null && saved !== original) area.value = saved;
  } catch (e) { /* ignore */ }
}

document.querySelectorAll(".box").forEach((box) => {
  const area = box.querySelector("textarea:not(.prediction)");
  const prediction = box.querySelector(".prediction");
  const runButton = box.querySelector(".run");
  const checkButton = box.querySelector(".check");
  const resetButton = box.querySelector(".reset");
  const status = box.querySelector(".status");
  const result = box.querySelector(".result");

  const original = area.value;
  const key = `pf:${slug}:${box.dataset.box}`;
  const spec = box.dataset.check ? JSON.parse(box.dataset.check) : null;

  // Autosave is the safety net for a runaway loop: on the main thread nothing
  // can interrupt one from outside, so reloading must never cost the learner
  // their work.
  restore(key, area, original);
  if (prediction) restore(key + ":prediction", prediction, "");

  const edited = () => area.value !== original;
  resetButton.hidden = !edited();
  autosize(area);

  area.addEventListener("input", () => {
    autosize(area);
    resetButton.hidden = !edited();
    remember(key, area.value, original);
  });

  if (prediction) {
    prediction.addEventListener("input", () =>
      remember(key + ":prediction", prediction.value, ""));
  }

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
    result.className = "result";
  });

  /** Paint "working…" before Python takes the thread back. */
  async function beginWork(button, label) {
    button.disabled = true;
    status.textContent = pyodide ? label : "starting Python…";
    result.hidden = false;
    result.className = "result";
    result.textContent = "";
    await new Promise((resolve) => requestAnimationFrame(() => setTimeout(resolve, 0)));
  }

  runButton.addEventListener("click", async () => {
    await beginWork(runButton, "running…");
    const setup = box.dataset.setup ? box.dataset.setup + "\n" : "";
    const { output, error } = await runPython(setup + area.value, (text) => {
      result.textContent = text;
    });

    if (error) {
      result.className = "result error";
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

  if (checkButton) {
    checkButton.addEventListener("click", async () => {
      await beginWork(checkButton, "checking…");
      const { passed, notes, total } = await checkAnswer(
        spec, area.value, prediction ? prediction.value : "");

      if (passed) {
        result.className = "result passed";
        if (spec.kind === "function") {
          result.textContent = `Passed all ${total} test cases.`;
        } else if (spec.kind === "stdin") {
          result.textContent = total > 1
            ? `Correct — checked with ${total} different inputs.`
            : "Correct.";
        } else {
          result.textContent = "Correct.";
        }
        status.textContent = "";
      } else {
        result.className = "result failed";
        result.textContent = notes.join("\n");
        status.textContent = "not yet";
      }
      checkButton.disabled = false;
    });
  }
});
