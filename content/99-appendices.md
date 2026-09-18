# Appendices

## Appendix A — Reading Errors and Debugging

An error message is not a rebuke. It is the most specific help you will get, and learning to read one is worth more than memorizing any amount of syntax.

### How to read a traceback

```
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    print(average(scores))
  File "main.py", line 8, in average
    return total / len(numbers)
ZeroDivisionError: division by zero
```

Read it **from the bottom**.

1. **The last line names the problem.** `ZeroDivisionError: division by zero`. That is what went wrong.
2. **The line above it is the code that failed.** `return total / len(numbers)`.
3. **Work upward for how you got there.** Line 12 called `average`, and the failure happened inside it at line 8.

The top of a traceback is where the program started; the bottom is where it broke. Beginners often read the first line and stop, which is the least useful part.

### The errors you will actually meet

| Error | Usual cause | How to fix |
| --- | --- | --- |
| `SyntaxError` | Missing colon, bracket, or quote | Check the reported line *and the one above it* |
| `IndentationError` | Inconsistent spacing | Use four spaces per level, consistently |
| `TabError` | Tabs and spaces mixed | Convert tabs to spaces |
| `NameError` | Misspelled or undefined name | Check spelling and case; define before use |
| `TypeError` | Wrong type for the operation | Usually `str` where a number was needed; convert |
| `ValueError` | Right type, impossible value | `int("abc")`; validate input first |
| `IndexError` | Position past the end | Valid indexes are `0` to `len(x) - 1` |
| `KeyError` | Dictionary key absent | Use `.get()` or test with `in` |
| `ZeroDivisionError` | Dividing by zero | Check the divisor before dividing |
| `AttributeError` | Method does not exist for that type | Check the type; check the spelling |
| `RecursionError` | Missing or unreachable base case | Make sure the input shrinks toward the base case |
| `UnboundLocalError` | Using a local variable before assigning it | Assign it first, or pass it in as a parameter |

### A note on `SyntaxError`

Syntax errors often report the line *after* the real mistake, because Python reads forward until something becomes impossible:

```python
print("hello"
print("world")
```

```
SyntaxError: '(' was never closed
```

The missing parenthesis is on line 1. When a syntax error makes no sense on the line reported, look at the line above.

### Silent bugs

The errors above are the easy ones — the program stops and tells you where. Worse is a program that runs happily and produces the wrong answer.

```python
# Intended: the average of the scores. Prints 33.0 instead of 88.0.
scores = [88, 92, 84]
average = sum(scores) / len(scores) / 2
print(average)
```

Nothing is malformed. Python has no way to know what you meant. These are found by checking output against a case you can compute yourself.

### Debugging techniques

**1. Print the variables.** Unglamorous and effective. When a program misbehaves, print everything involved right before the failure:

```python
print(f"DEBUG: total={total}, count={count}, average={total / count}")
```

Prefix them with `DEBUG:` so they are easy to find and delete later.

**2. Check the types.** A surprising share of bugs are a string where a number belongs:

```python
print(f"DEBUG: score={score!r}, type={type(score)}")
```

The `!r` shows quotes around strings, making `"5"` and `5` distinguishable on screen.

**3. Cut the problem in half.** If a 60-line program misbehaves, comment out the second half. Still broken? The bug is in the first half. This is binary search applied to your own code, and it finds a bug in a few steps rather than by reading everything.

**4. Test the pieces separately.** This is what Chapter 6's decomposition is for. Call each function with a value whose answer you know:

```python
print(letter_grade(90))
print(letter_grade(89))
print(letter_grade(0))
```

Boundaries are where bugs live. Test 89 and 90, not 85.

**5. Read the code aloud.** Describe what each line does, out loud, in plain language. The line where your description differs from the code is usually the bug. This works absurdly well and feels ridiculous, which is why people skip it.

**6. Rubber-duck it.** Explain the program, line by line, to a patient object. Articulating what you *think* it does forces you to notice where that is not what it *says*.

**7. Walk through it by hand.** For a short loop, write out the variables on paper for each pass. Slow, and it finds off-by-one errors nothing else catches.

### Before asking for help

A good question is most of an answer. Have these ready:

- What you expected to happen
- What actually happened, with the **complete** error message
- The smallest piece of code that still shows the problem
- What you have already tried

Assembling that list solves the problem outright surprisingly often.

### Habits that prevent bugs

- **Write a little, run a little.** Three lines at a time, not sixty. A bug in three new lines is trivial to locate.
- **Name things honestly.** `x` hides meaning; `remaining_attempts` reveals it.
- **One function, one job.** Small functions are testable; large ones are guesswork.
- **Test the boundaries.** Zero, one, empty, negative, the largest allowed value, and one past it.
- **Do not repeat yourself.** The same logic in two places will eventually be updated in one.
- **Comment the reasoning.** Not what the line does — why it does it.

## Appendix B — Quick Reference

Everything in this book, on one page.

### Output and input

```python
print("text")
print(a, b, c)                  # space between items
print("no newline", end="")
print(f"{name} is {age}")       # f-string
print(f"{price:.2f}")           # 2 decimal places
print(f"{name:<12}{score:>6}")  # left-pad 12, right-pad 6

name = input("Prompt: ")        # ALWAYS returns a string
age = int(input("Age: "))       # convert for arithmetic
```

### Types and conversion

```python
int, float, str, bool           # the four basic types
type(value)                     # report a value's type

int("42"), float("3.5"), str(42)
round(3.14159, 2)               # 3.14
```

### Operators

```python
+  -  *  /                      # / always gives a float
//                              # floor division: 17 // 5 is 3
%                               # remainder: 17 % 5 is 2
**                              # exponent: 2 ** 10 is 1024

==  !=  <  >  <=  >=            # comparison, gives True/False
and  or  not                    # boolean logic
in  not in                      # membership

x += 1    x -= 1    x *= 2      # shorthand assignment
```

### Conditionals

```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...

value = a if condition else b   # conditional expression
```

Falsy values: `False`, `0`, `0.0`, `""`, `[]`, `{}`, `None`. Everything else is truthy.

### Loops

```python
for i in range(5):              # 0 1 2 3 4
for i in range(2, 6):           # 2 3 4 5
for i in range(0, 20, 5):       # 0 5 10 15
for i in range(5, 0, -1):       # 5 4 3 2 1

for item in collection:
for i, item in enumerate(items):
for i, item in enumerate(items, start=1):
for key, value in d.items():

while condition:
while True:
    if done:
        break                   # exit the loop
    continue                    # skip to the next pass
```

### Functions

```python
def name(param, other=default):
    """One-line description."""
    return value                # no return means None

return a, b                     # returns a tuple
x, y = name()                   # unpack it
```

### Lists

```python
items = [1, 2, 3]
items[0]        items[-1]       # first, last
items[1:3]      items[:2]       # slices; stop is excluded
items[::-1]                     # reversed copy

items.append(x)                 # add to the end
items.insert(i, x)              # add at a position
items.remove(x)                 # remove first occurrence
items.pop()     items.pop(i)    # remove and return
items.sort()                    # sorts IN PLACE, returns None
items.reverse()                 # reverses in place
items.count(x)  items.index(x)
items.copy()                    # a real copy, not another name

len(items)  sum(items)  max(items)  min(items)
sorted(items)                   # returns a NEW sorted list
sorted(items, reverse=True)
sorted(records, key=lambda r: r["score"])
x in items

[f(x) for x in items]           # list comprehension
[x for x in items if test(x)]   # with a filter
```

### Strings

```python
text[0]   text[-1]   text[1:4]   text[::-1]
len(text)

text.upper()        text.lower()      text.title()
text.strip()        text.replace(a, b)
text.split()        text.split(",")
", ".join(list_of_strings)
text.count(x)       text.find(x)      # -1 if absent
text.startswith(x)  text.endswith(x)
text.isdigit()      text.isalpha()    text.isalnum()

\n  \t  \"  \\                  # escape sequences
```

Strings are **immutable** — every method returns a new string.

### Dictionaries

```python
d = {"key": "value"}
d["key"]                        # KeyError if absent
d.get("key")                    # None if absent
d.get("key", default)           # default if absent
d["new"] = value                # add or update
del d["key"]
"key" in d
len(d)

for key in d:
for value in d.values():
for key, value in d.items():

d.setdefault(key, []).append(x) # group into lists
d[k] = d.get(k, 0) + 1          # count occurrences
max(d, key=d.get)               # key with the largest value
```

### Sets and tuples

```python
s = {1, 2, 3}                   # set() for an empty one
set(items)                      # remove duplicates
s | t    s & t    s - t         # union, intersection, difference

t = (1, 2)                      # tuple: cannot be changed
(5,)                            # single-item tuple needs the comma
a, b = t                        # unpacking
a, b = b, a                     # swap
```

### Handling errors

```python
try:
    value = int(text)
except ValueError:
    print("Not a number.")
```

### The random module

```python
import random

random.randint(1, 6)            # 1 to 6, INCLUSIVE
random.choice(items)
random.shuffle(items)           # in place, returns None
```

### Cost of common operations

| Operation | Cost |
| --- | --- |
| `items[i]`, `len(x)` | O(1) |
| `d[key]`, `key in d`, `x in set` | O(1) |
| `x in list`, `sum()`, a `for` loop | O(n) |
| Binary search (sorted) | O(log n) |
| `sorted()`, `.sort()` | O(n log n) |
| Selection sort, bubble sort | O(n²) |
| Naive recursive Fibonacci | O(2ⁿ) |

### Choosing a container

| Need | Use |
| --- | --- |
| Ordered, duplicates allowed, access by position | List |
| Look up by a name or ID | Dictionary |
| Membership and uniqueness only | Set |
| A fixed group of related values | Tuple |
| A collection of multi-field records | List of dictionaries |

### Style conventions

```python
snake_case          # variables and functions
CONSTANT_CASE       # values that never change
four spaces         # one indentation level, never tabs

def main():         # the program's entry point
    ...
main()              # called on the last line
```

## Appendix C — Where to Go Next

This book covered the core of programming: values, decisions, repetition, decomposition, data structures, and algorithms. Those ideas transfer to every language you will ever use. What follows are the things deliberately left out, roughly in the order they become useful.

### Left out on purpose

**Objects and classes.** Python lets you define your own types, bundling data and the functions that work on it. A `Student` class would replace this book's student dictionaries with something that carries its own `average()` method. This is the single biggest idea still ahead, and it is normally the start of a second course. Everything in this book works without it.

**Reading and writing files.** Programs here kept data in variables, so it vanished when the program ended. `open()`, and the `csv` and `json` modules, let a program save its work and read data it did not create.

**Modules and libraries.** `import random` was the only import used. The standard library ships with modules for dates, math, files, and web requests, and the wider ecosystem adds tools for data analysis, graphics, and machine learning.

**Error handling in depth.** `try`/`except` appeared briefly. Real programs use it systematically, and can raise their own exceptions.

**Testing frameworks.** Checking work by calling functions with known inputs is testing by hand. Tools like `pytest` run hundreds of such checks automatically, every time you change something.

### A sensible order to learn them

1. **Files** — because a program that remembers things is far more interesting
2. **Modules** — the standard library is enormous and free
3. **Classes** — once your programs have several kinds of thing in them
4. **Testing** — once your programs are too big to check by hand
5. **A second language** — the concepts transfer; only the syntax is new

### Where the algorithms go

Chapter 11 covered searching and sorting because they are the classic introduction. The field continues:

- **Data structures** — stacks, queues, linked lists, trees, graphs, hash tables (which is what a dictionary actually is)
- **Better sorts** — merge sort and quicksort, both O(n log n), both naturally recursive
- **Graph algorithms** — shortest paths, network connectivity, dependency ordering
- **Dynamic programming** — the general form of the memoization trick from Chapter 12

A first algorithms course covers roughly that list, and it is where computer science starts to feel like mathematics.

### Practicing

Programming is learned by writing programs. Some ways to keep going:

- **Finish the exercises.** Every Try It in this book, including the ones you skipped.
- **Extend the projects.** Add letter-grade curves to the gradebook. Make the inventory system accept new items. Give the guessing game a high-score table.
- **Solve puzzles.** Project Euler, Advent of Code, and similar sites offer graded problems that are good practice and genuinely fun.
- **Automate something tedious.** The best beginner projects solve a problem you actually have — renaming a folder of files, tracking a habit, calculating something you currently do by hand.
- **Read other people's code.** Open-source projects are free to read. Most of it will be over your head at first, which is fine and normal.

### A closing thought

The difficulty in programming is rarely syntax. Syntax is memorization and it comes with practice. The difficulty is **decomposition** — looking at a problem and seeing the pieces it breaks into, and working out how to represent its data.

That skill is what Chapter 6 and Part II were really teaching, and it is the one that makes a good programmer. It is also the one that does not become obsolete: the languages change every decade, and knowing how to break a problem apart does not.
