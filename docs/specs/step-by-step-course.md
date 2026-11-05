# Spec: Python Foundations, step by step

Status: **draft, 2026-11-05, for Justin's review.** Decisions marked **(decided)** were made by Justin in the
design conversation of 2026-11-04 and 2026-11-05.

## Objective

Rebuild Python Foundations so that a capable beginner with no programming background can work through it
without burning out, and wants to keep going.

The first real learner, a 13-year-old who is strong at math, worked through chapters 1 to 4 and the first
three exercises of chapter 5 with a lot of effort (detailed notes, rereading every chapter several times)
and reached the point of wanting to stop. A survey of that learner, and an audit of all twelve chapters,
agree on why:

- The pace climbs from chapter 2 and is "way too fast" by chapters 4 and 5; the learner places the start of
  the trouble around chapter 3, the densest chapter in the course (about twenty operators in eight sections).
- What would help, in the learner's own choices: more worked examples before trying, a tiny practice right
  after each new idea, and a quick review of the last chapter at the start. In their words: "slower".
- What the course never teaches, though its exercises require it from chapter 1: a way to approach a problem
  (restate it, break it into steps, turn each step into code), naming as a practiced habit, tracing code by
  hand, reading error messages, and testing with awkward inputs. Chapter projects are handed over solved;
  syntax is sometimes used before it is explained; a reference solution uses `ord`/`chr`, never taught;
  automatic checks sit on the hardest exercises rather than the confidence-building ones.

The full audit is kept privately (`~/python_foundations-notes/course-audit-2026-11-04/`), as are the
learner's survey answers.

### Success

- **Per lesson:** the learner rates the pace "about right", reads it at most twice, and wants the next lesson.
- **Per unit:** at the unit's end the learner wants the next unit, and no muddiest point has repeated across
  lessons without the course being changed to address it.
- **Stop rule:** if two lessons in a row miss the per-lesson bar, building stops and the format is rethought
  before more lessons are written.

## Decisions

1. **Keep every topic; spread it out (decided).** Nothing the current course teaches is cut. Chapters become
   units of three to five short lessons; the course grows from twelve chapters to roughly thirty to thirty-five
   lessons.
2. **Lessons of 20 to 30 minutes (decided)**, one or two new ideas each, so a 40-to-60-minute sitting finishes
   a lesson with time to spare.
3. **A new volume beside the current course (decided).** The rebuilt course is `volumes/vol1-steps/`. The
   current `vol1-foundations` stays live and unchanged until the new one covers what it does and has proven
   itself, then the new one replaces it.
4. **Quizzes stay at unit boundaries (decided)**, one per unit, where today's chapter quizzes are, so most
   lessons end without a written assignment. Unit quizzes are adapted from the existing chapter quizzes.
5. **Feedback lives in a private page, never on the public course (decided).** After each lesson the learner
   taps three answers (pace, could they explain it, how many reads) and writes one "muddiest point": the
   thing still least clear, or "nothing". After each unit, beside the quiz, a short unit check-in: pace
   across the unit, the hardest lesson and why, and whether they want the next unit. The public course
   collects nothing from its learners, many of whom will be under 13.
6. **Prototype first (decided).** Five lessons (below) are built and tried, if and when the learner wants to,
   before anything else is rebuilt.

## The lesson format

Every lesson follows the same five steps:

1. **Warm-up (about three minutes):** two or three quick predict-the-output, fill-the-blank or
   multiple-choice items on the previous lesson, each with a check. Not graded; the answers can be shown.
2. **One new idea, at most two:** a plain explanation, then two or three worked examples, each runnable on the
   page, each adding at most one new thing.
3. **A tiny practice after each idea:** one to three very small exercises, each a one-step change from an
   example just shown, each with a check.
4. **One "try it"**, a small step beyond the examples, with hints revealed one at a time (see the routine
   below), ending in a full worked solution that shows the reasoning as well as the code.
5. **Wrap-up:** three lines on what the learner can now do, and the key words.

Rules for every lesson:

- No syntax, built-in function or method is used before a lesson has taught it, in examples, exercises,
  hints or reference solutions alike. Enforced by the vocabulary gate (below).
- Every exercise gets an automatic check wherever one can be written. A check must never fail a correct
  answer written in a different style: checks test what a program does, not how it is written. Where several
  answers are genuinely fine, the exercise says so and has no check or a lenient one.
- An exercise that needs a plan comes only after a worked example has shown that kind of plan being made.
- A unit's project is built in steps across its lessons, never handed over solved.
- Each unit has one optional extra-practice page, labeled optional, never needed to continue.

## The problem-solving routine

**Say it, Split it, Name it, Build it, Check it.**

1. Say it: restate the problem in your own words, as a comment at the top.
2. Split it: break it into small steps, one comment line each.
3. Name it: choose names that say what each value means.
4. Build it: turn one comment into code, run it, then the next.
5. Check it: try an ordinary input and an awkward one.

Introduced gradually: Say it, Split it and Build it in unit 1 (the receipt is built from comment steps); Name
it in unit 2, when there are names to choose; Check it once programs take input. From then on, all five.

It runs through the course:

- Worked examples that solve a problem start from its sentence and visibly go through the steps; the comment
  steps stay in the finished code.
- A "try it"'s hints are the routine: hint 1 Say it, hint 2 Split it (the steps as comments), hint 3 Name it,
  then the worked solution.
- Naming is practiced: tiny practices ask the learner to pick the clearer of two names, or to rename variables
  so a program explains itself.
- Tracing: trace-table exercises (each variable's value after each line, then run to check), from unit 2's
  reassignment onwards.
- Reading errors: each unit has one fix-the-bug practice that starts from a real error message.
- A short reference page, "How to start a problem", states the routine; every hint links to it.

## The prototype

The learner restarts at unit 2, the first chapter they rated "a bit fast"; chapter 1 went well and is not
redone.

| Lesson | Teaches | Routine |
|---|---|---|
| 0. Welcome back | a light recap of printing and arithmetic | Say it, Split it, Build it, on a tiny receipt |
| 2.1 Naming a value | variables, reassignment | first trace table |
| 2.2 Names that explain, and kinds of value | naming, `int`, `float`, `str`, `True`/`False`, `type()` | Name it joins; `True`/`False` gets its own practice |
| 2.3 Asking the user | `input()`, `int()`, `float()` | Check it joins |
| 2.4 Putting it together | the improved receipt, built step by step | all five; no solved version handed over |

Unit 2 ends with its quiz (adapted from the chapter 2 quiz) and the unit check-in. Unit 3 is designed and
built only after the prototype has been judged against the success bar.

## How it fits the build

- **The new volume:** `volumes/vol1-steps/` with its own `volume.json`; lessons are content files grouped into
  units. The front page becomes a shelf showing both courses, the new one marked "in progress" until it
  replaces the old. Nothing in `vol1-foundations` changes.
- **New lesson blocks:** hints (an ordered list revealed one at a time, ending in a worked solution) and
  warm-ups.
- **New check kinds**, beside today's `output`, `stdin`, `function` and `predict`: `choice` (multiple choice)
  and `trace` (a trace table compared row by row). Both run entirely in the page.
- **The vocabulary gate:** each lesson declares what it teaches. A test parses every code example, exercise,
  hint and reference solution in the new volume with Python's `ast` module and fails if anything uses a
  construct, built-in function or method no earlier lesson has taught.
- **Quizzes:** the existing quiz generator renders one quiz and key per unit from the volume's `quizzes.json`.
- **The feedback page:** a private claude.ai artifact (lesson picker, three taps, a muddiest-point box, and
  the unit check-in), storing answers in its own private store. Never linked from the public site.

## Testing

- Every check in the new volume is run against its reference answer, as the current course's are.
- The new check kinds and block types are written test-first.
- The vocabulary gate is proven able to fire with a planted violation, as every guard in this repository is.
- `second_volume_test.py` keeps the two-volume shelf working; `quiz_test.py` covers the new volume's quizzes.
- CI runs everything on Python 3.9 and 3.14, as today.

## Boundaries

- **Always:** one idea per example; checks that accept any correct style; the learner chooses when to try a
  lesson.
- **Ask first:** changing anything in `vol1-foundations`; pushing the new volume to the public site; building
  past the prototype.
- **Never:** collect anything from learners on the public site; name the first learner, or quote their
  answers, in the repository.

## Open questions

None. Unit 3 and beyond are designed after the prototype is judged.
