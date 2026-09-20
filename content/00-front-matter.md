# Python Foundations: A First Course in Programming

*A workable textbook for beginners — every example runs as written.*

2026-09-20 · Justin Stewart—built with Claude Opus 5

## How to Use This Course

This course teaches you to write programs in Python. It assumes you have never written a line of code and know roughly the algebra taught in a first high-school course. By the end you will be able to read a problem, break it into steps, choose a way to store the data, and write a program that solves it.

Every example here runs exactly as shown. Nothing needs to be installed, no files need to be downloaded, and no example depends on one printed in an earlier chapter unless it says so. If you type it in and it does not run, the problem is a typo, and Appendix A will help you find it.

### The three parts

**Part I (Chapters 1-6)** builds the machinery every program uses: storing values, doing arithmetic, making choices, repeating work, and packaging steps into functions. These six ideas are enough to write real programs, and everything later is built on them.

**Part II (Chapters 7-10)** is about *structuring data*. A program that tracks one test score needs a variable. A program that tracks a whole class needs a list, and one that tracks a whole school needs something better still. These chapters cover the containers Python gives you and, more importantly, when to reach for each one.

**Part III (Chapters 11-12)** is about *algorithms*: named, reusable procedures for common problems. You will write searching and sorting algorithms by hand, measure how much work each one does, and meet recursion, where a function calls itself.

### What each chapter contains

| Section | What it is |
| --- | --- |
| Concept | The idea explained in plain language, with a worked example |
| Worked examples | Complete programs, ready to run and to change |
| Try It | Short exercises that practice one thing each, many with a Check button |
| Common mistakes | Errors that catch nearly everyone, and what they look like |
| Chapter project | A longer program combining everything in the chapter |

Do the Try It exercises as you go rather than saving them for the end. Programming is a skill like playing an instrument: reading about it and doing it are different activities, and only one of them works.

### Running the code

There is nothing to install and nothing to download. Every example sits in a box you can type in, with a **Run** button underneath. Press Run, and the output appears below the box.

Then change something and press Run again. Change a number, swap a `<` for a `>`, delete a line and see which part of the output disappears. This is the whole reason the code is in a box rather than on a page, and there is no way to break anything: the **Reset** button puts a box back to exactly how it started, and your own edits are kept if you close the page and come back.

Each box starts from nothing and runs top to bottom, the way a saved file does. A variable you create in one box does not exist in the next one. Where an example needs something set up first, the box shows you that setup above the code, marked *already defined for you*.

A few boxes fail on purpose. Those carry a note saying so before you run them, because the error message is the thing being taught.

> **A note on `input()`.** Several programs ask you to type something. A box appears asking for it; type your answer and press OK. If a program seems to be doing nothing, check whether it is waiting for you.

> **If a program never stops.** A loop with no way out is an easy mistake to make, and here it stops itself after five seconds and reports `KeyboardInterrupt`. Nothing is lost when it does.

### The scratchpad

The boxes behave like files, because a program is a file. But a lot of learning happens by simply asking Python a question — what does `"5" * 3` do? is `round(2.5)` 2 or 3? — and for that there is a **Scratchpad** button in the corner.

It works the way a Python interpreter does. It remembers what you typed, so you can build something up a line at a time, and it shows you the value of anything you type without your having to print it. Appendix D explains the difference between the two, and when each is the right one to reach for.

### Checking your answers

Every chapter ends with a handful of Try It exercises. About half have a **Check** button: it runs your answer against several test cases and, if something is wrong, tells you which case failed and what it expected. It does not care how you wrote it — a `for` loop and a comprehension that both work will both pass.

Some exercises have no Check button. Those are the ones where you choose the words the program prints, or the data it works on, so there is no single right answer to check against. The box says as much rather than pretending otherwise. Appendix A is how you check those yourself, and it is worth reading before you need it.

### On typing the examples out

Every example is already typed in for you, which is convenient and is also a trap. Reading code you did not write feels like understanding; writing it is what turns into being able to write it. Type the short examples out yourself — over the top of the box, or into the scratchpad — and run the long ones as printed, then change them until you can predict what the change will do.

### If you would rather use your own editor

Nothing here requires it, but every example and project is also supplied as a folder of `.py` files, one per chapter, if you would rather work on your own machine. You need Python 3.6 or newer and nothing else — no installs, no libraries beyond `random`.

Every deterministic example here is run, and its output compared against what the course says it prints, every time the site is rebuilt. If the two ever disagree, the build fails. So if an example behaves differently for you, something really is different, and Appendix A is about tracking that down.
