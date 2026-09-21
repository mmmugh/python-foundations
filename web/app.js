/* Python Foundations — the browser runtime.
 *
 * Everything that knows about Pyodide lives behind runPython() and the check
 * helpers below, so the day a Web Worker + JSPI setup is worth it, only those
 * change. Pinned to Pyodide 314.0.7 (CPython 3.14). The loader is
 * pyodide.asm.mjs as of 314.0.0—pyodide.asm.js no longer exists.
 */

/* Served from this site, not from a CDN: the course works with no network
 * after a clone, and nobody else decides what Python a student runs. The bytes
 * live in vendor/pyodide/ and build.py copies them here.
 *
 * Resolved against this module's own URL rather than the page's, so it stays
 * correct if the pages ever move into subdirectories.
 */
const PYODIDE = new URL("pyodide/", import.meta.url).href;

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
    say("Starting Python… (13 MB, once)");
    const { loadPyodide } = await import(PYODIDE + "pyodide.mjs");
    // packageBaseUrl as well as indexURL: left unset, Pyodide keeps a built-in
    // https://cdn.jsdelivr.net/pyodide/... fallback for loadPackage and micropip.
    // The course never calls either, so it never fires -- but pointing it at our
    // own origin makes "no external CDN" a property of the code rather than a
    // consequence of what we happen not to call.
    pyodide = await loadPyodide({ indexURL: PYODIDE, packageBaseUrl: PYODIDE });

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
                        "check_prediction", "check_stdin", "repl_run"]) {
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


/* -------------------------------------------------------------- scratchpad */

/* A place to poke at Python and see what comes back, which is how a lot of
 * people learn types and syntax. Its namespace persists while the page is
 * open, and a bare expression shows its value — the two things that make a
 * REPL a REPL, and the two things the code boxes deliberately do not do. */

const scratch = document.querySelector(".scratchpad");
const scratchTab = document.querySelector(".scratch-tab");

if (scratch) {
  const transcript = scratch.querySelector(".transcript");
  const input = scratch.querySelector(".entry textarea");
  const caret = scratch.querySelector(".caret");
  let namespace = null;
  let pending = [];
  const history = [];
  let cursor = 0;

  function write(text, className) {
    const line = document.createElement("span");
    if (className) line.className = className;
    line.textContent = text.endsWith("\n") ? text : text + "\n";
    transcript.appendChild(line);
    transcript.scrollTop = transcript.scrollHeight;
  }

  function grow() {
    input.style.height = "auto";
    input.style.height = input.scrollHeight + "px";
  }

  async function submit() {
    const line = input.value;
    write((pending.length ? "... " : ">>> ") + line, "typed");
    pending.push(line);
    input.value = "";
    grow();

    if (line.trim() !== "" || pending.length === 1) {
      const source = pending.join("\n");
      await boot();
      if (!namespace) namespace = pyodide.runPython("dict()");

      const chunks = [];
      sink = (text) => chunks.push(text);
      let value = "", incomplete = false, failed = null;
      try {
        const out = python.repl_run(source, TIMEOUT_SECONDS, namespace);
        value = out.get(0);
        incomplete = out.get(1);
        out.destroy();
      } catch (e) {
        failed = String(e.message || e).trim().split("\n").filter(Boolean).pop();
      } finally {
        sink = null;
      }

      if (incomplete) {
        caret.textContent = "...";
        return;
      }
      if (chunks.length) write(chunks.join("\n"));
      if (failed) write(failed, "oops");
      else if (value) write(value);
    }

    pending = [];
    caret.textContent = ">>>";
  }

  input.addEventListener("input", grow);

  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      if (input.value.trim() && history[history.length - 1] !== input.value) {
        history.push(input.value);
      }
      cursor = history.length;
      submit();
      return;
    }
    if (event.key === "Tab") {
      event.preventDefault();
      const { selectionStart: a, selectionEnd: b, value } = input;
      input.value = value.slice(0, a) + "    " + value.slice(b);
      input.selectionStart = input.selectionEnd = a + 4;
      grow();
      return;
    }
    // Arrow through what you typed before, the way a terminal does.
    if ((event.key === "ArrowUp" || event.key === "ArrowDown") && !input.value.includes("\n")) {
      if (event.key === "ArrowUp" && cursor > 0) cursor -= 1;
      else if (event.key === "ArrowDown" && cursor < history.length) cursor += 1;
      else return;
      event.preventDefault();
      input.value = history[cursor] || "";
      grow();
    }
  });

  function open(yes) {
    scratch.hidden = !yes;
    scratchTab.hidden = yes;
    scratchTab.setAttribute("aria-expanded", String(yes));
    if (yes) input.focus();
    try { localStorage.setItem("pf:scratchpad", yes ? "open" : "shut"); } catch (e) { /* ignore */ }
  }

  scratchTab.addEventListener("click", () => open(true));
  scratch.querySelector(".scratch-close").addEventListener("click", () => open(false));
  scratch.querySelector(".scratch-clear").addEventListener("click", () => {
    transcript.textContent = "";
    pending = [];
    caret.textContent = ">>>";
    if (namespace) { namespace.destroy(); namespace = null; }
    write("Cleared. Anything you defined is forgotten.", "typed");
  });

  try {
    if (localStorage.getItem("pf:scratchpad") === "open") open(true);
  } catch (e) { /* ignore */ }
}
