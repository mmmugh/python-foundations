# Python Foundations — Code Bundle

Every code example and project from *Python Foundations: A First Course in
Programming*. All of it runs on plain Python 3 with nothing installed.

## Getting this into Replit

1. Go to **replit.com** and create a free account.
2. Click **Create Repl** and choose the **Python** template.
3. Drag this whole folder (or the `.zip`) into the file list on the left.
4. Press **Run**. `main.py` gives you a menu of every file in the book.

You can also run any file on its own from the Replit Shell:

```
python3 examples/ch07_lists.py
python3 projects/ch05_guessing_game.py
```

## What is here

```
main.py       A menu that runs any chapter's code
examples/     Every worked example, one file per chapter
projects/     The end-of-chapter projects
```

### examples/

One file per chapter, containing the worked examples in the order the book
presents them. Run a file and follow along with that chapter.

Examples that ask for typed input are wrapped in functions at the bottom of
their file, so the file runs start to finish without stopping. Uncomment the
call at the end to try one interactively.

A few lines are commented out with a note saying they raise an error on
purpose — `names[5]` on a four-item list, assigning to a character of a
string. Uncomment them when you want to see the error message the book
describes.

| File | Chapter |
| --- | --- |
| `ch01_first_programs.py` | Your First Programs |
| `ch02_variables_and_types.py` | Variables and Types |
| `ch03_expressions_and_operators.py` | Expressions and Operators |
| `ch04_making_decisions.py` | Making Decisions |
| `ch05_repetition.py` | Repetition |
| `ch06_functions.py` | Functions |
| `ch07_lists.py` | Lists |
| `ch08_strings_as_data.py` | Strings as Data |
| `ch09_dictionaries_and_sets.py` | Dictionaries and Sets |
| `ch10_tuples_and_records.py` | Tuples and Structured Records |
| `ch11_searching_and_sorting.py` | Searching and Sorting |
| `ch12_recursion.py` | Recursion and Problem Solving |

### projects/

The larger program at the end of each chapter, ready to run and to modify.
Projects 2 through 6 ask you to type something; the rest print a report and
finish on their own.

## Requirements

Python 3.6 or newer, because of f-strings. Nothing else — no `pip install`,
no libraries beyond `random` from the standard library.

## A note on the output

Every example in this bundle was run and its output checked against what the
book prints. If something behaves differently on your machine, that is worth
investigating rather than ignoring — and Appendix A of the book is about
exactly that.
