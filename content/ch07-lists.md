<!-- part: Part II — Structuring Data -->
## Chapter 7 — Lists

Every variable so far has held one value. A program that tracks four test scores needs four variables, which is tolerable. A program that tracks a class of thirty needs a different idea.

A **list** holds many values in one variable, in order.

```python
scores = [88, 92, 79, 95]
names = ["Ada", "Grace", "Alan"]
mixed = [1, "two", 3.0, True]
empty = []

print(scores)
print(len(scores))
```

Output:

```
[88, 92, 79, 95]
4
```

Square brackets create a list, commas separate the items, and `len()` reports how many there are. A list can hold any type, including a mix, though in practice a list whose items are all the same kind of thing is far more useful.

### Indexing

Each item has a position, called its **index**. Python counts from **zero**.

```python
names = ["Ada", "Grace", "Alan", "Katherine"]

print(names[0])
print(names[2])
print(names[-1])
print(names[-2])
```

Output:

```
Ada
Alan
Katherine
Alan
```

Counting from zero surprises everyone at first. It is worth making peace with it early, because it is consistent across the whole language — recall that `range(5)` also starts at 0.

| Item | `Ada` | `Grace` | `Alan` | `Katherine` |
| --- | --- | --- | --- | --- |
| Index | 0 | 1 | 2 | 3 |
| Negative index | -4 | -3 | -2 | -1 |

Negative indexes count backward from the end, so `names[-1]` is the last item regardless of how long the list is. That is much better than `names[len(names) - 1]`, which does the same thing awkwardly.

Asking for an index that does not exist raises an error:

```python
names = ["Ada", "Grace"]
print(names[5])
```

```
IndexError: list index out of range
```

The last valid index is always `len(list) - 1`. An `IndexError` almost always means a loop ran one step too far.

### Lists are mutable

Unlike strings and numbers, lists can be changed after they are made:

```python
scores = [88, 92, 79, 95]
scores[2] = 85
print(scores)
```

Output:

```
[88, 92, 85, 95]
```

This property is called **mutability**, and it is the main practical difference between a list and the other containers in this course.

### Slicing

A **slice** takes a section of a list, using `list[start:stop]`. As with `range()`, the stop position is not included.

```python
letters = ["a", "b", "c", "d", "e", "f"]

print(letters[1:4])
print(letters[:3])
print(letters[3:])
print(letters[-2:])
print(letters[::2])
```

Output:

```
['b', 'c', 'd']
['a', 'b', 'c']
['d', 'e', 'f']
['e', 'f']
['a', 'c', 'e']
```

Leaving out the start means "from the beginning"; leaving out the stop means "to the end." A third number is a step, so `[::2]` takes every second item. A slice always produces a **new list**; the original is untouched.

### List methods

A **method** is a function attached to a value, called with a dot. Lists have many; these are the ones worth knowing now.

| Method | Does | Example |
| --- | --- | --- |
| `.append(x)` | Adds `x` to the end | `scores.append(100)` |
| `.insert(i, x)` | Inserts `x` at index `i` | `names.insert(0, "Ada")` |
| `.remove(x)` | Removes the first `x` | `names.remove("Alan")` |
| `.pop()` | Removes and returns the last item | `last = scores.pop()` |
| `.pop(i)` | Removes and returns item at `i` | `first = scores.pop(0)` |
| `.sort()` | Sorts the list in place | `scores.sort()` |
| `.reverse()` | Reverses the list in place | `names.reverse()` |
| `.count(x)` | How many times `x` appears | `votes.count("yes")` |
| `.index(x)` | Index of the first `x` | `names.index("Alan")` |

```python
scores = [88, 92, 79]

scores.append(95)
print(scores)

scores.sort()
print(scores)

highest = scores.pop()
print(highest, scores)
```

Output:

```
[88, 92, 79, 95]
[79, 88, 92, 95]
95 [79, 88, 92]
```

A critical distinction: **`.sort()` changes the list and returns nothing**, while the built-in `sorted()` leaves the original alone and returns a new sorted list.

```python
scores = [88, 92, 79]

result = scores.sort()
print(result)

scores = [88, 92, 79]
ordered = sorted(scores)
print(ordered, scores)
```

Output:

```
None
[79, 88, 92] [88, 92, 79]
```

`scores = scores.sort()` is a classic bug: it throws away your list and replaces it with `None`. Use `.sort()` on its own line, or use `sorted()` when you need both versions.

### Useful built-ins

```python
scores = [88, 92, 79, 95]

print(len(scores))
print(sum(scores))
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))
print(92 in scores)
print(100 in scores)
```

Output:

```
4
354
95
79
88.5
True
False
```

The `in` operator tests membership and produces a boolean, which makes it useful directly in conditions: `if name in guest_list:`.

Notice that `max()` solves Chapter 5's "largest so far" problem in one word, and correctly handles negative numbers. Reach for the built-in when one exists — but Chapter 11 has you write these by hand anyway, because knowing how they work is the point of the exercise.

### Looping over lists

The direct way hands you each item:

```python
scores = [88, 92, 79, 95]

for score in scores:
    print(f"Score: {score}")
```

When you need the position as well as the value, `enumerate()` supplies both:

```python
names = ["Ada", "Grace", "Alan"]

for position, name in enumerate(names):
    print(f"{position + 1}. {name}")
```

Output:

```
1. Ada
2. Grace
3. Alan
```

The `+ 1` turns zero-based indexes into the one-based numbering humans expect in a printed list.

Building a new list from an old one uses the accumulator pattern from Chapter 5, with `.append()` doing the accumulating:

```python
temperatures_c = [0, 25, 100, 37]
temperatures_f = []

for c in temperatures_c:
    temperatures_f.append(c * 9 / 5 + 32)

print(temperatures_f)
```

Output:

```
[32.0, 77.0, 212.0, 98.6]
```

Filtering works the same way, with an `if` deciding what gets appended:

```python
scores = [88, 92, 45, 95, 58, 71]
passing = []

for score in scores:
    if score >= 60:
        passing.append(score)

print(f"{len(passing)} of {len(scores)} passed: {passing}")
```

Output:

```
4 of 6 passed: [88, 92, 95, 71]
```

**Never add to or remove from a list while looping over it.** The loop loses track of its position and skips items. Build a new list instead, as above.

### Nested lists

A list can contain lists, which is how you represent a grid or table. Two indexes reach an item: the first picks the row, the second picks the position within it.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0])
print(grid[1][2])

for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

Output:

```
[1, 2, 3]
6
1 2 3 
4 5 6 
7 8 9 
```

The `end=" "` argument tells `print()` to finish with a space instead of a newline, which is how the values stay on one line. The bare `print()` after the inner loop then ends the row.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| `scores[4]` on a 4-item list | `IndexError` — valid indexes are 0 to 3 |
| `scores = scores.sort()` | `scores` becomes `None` |
| `scores.append(1, 2)` | `TypeError` — `.append()` takes one item; use `.extend([1, 2])` |
| Removing items while looping | Items get skipped silently |
| `list = [1, 2, 3]` | Works, but shadows the built-in `list` |
| `b = a` then changing `b` | Both names refer to the same list; use `b = a.copy()` |

That last one deserves a demonstration, because it surprises people:

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)

c = [1, 2, 3]
d = c.copy()
d.append(4)
print(c)
```

Output:

```
[1, 2, 3, 4]
[1, 2, 3]
```

`b = a` does not make a second list; it makes a second *name* for the same list. This is different from how numbers and strings behave, and it follows from lists being mutable.

### Try It

1. Make a list of ten numbers and print its total, average, largest, and smallest.
2. Ask the user for five words and print them in alphabetical order.
3. Write `count_above(numbers, threshold)` returning how many items exceed the threshold.
4. Given a list of numbers, build a new list containing only the even ones.
5. Reverse a list without using `.reverse()` or `[::-1]`.
6. Write `second_largest(numbers)` returning the second-largest value.
7. Build a 3-by-3 grid of zeros, set the center to 5, and print it row by row.

### Chapter project: a class gradebook

Build a gradebook that stores students and their scores in parallel lists and reports on the class.

```python
# A class gradebook using parallel lists.


def average(numbers):
    """Return the mean of a list of numbers, or 0.0 for an empty list."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def letter_grade(score):
    """Return the letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def print_roster(names, scores):
    """Print each student with their score and letter grade."""
    print(f"{'Student':<12}{'Score':>6}{'Grade':>7}")
    print("-" * 25)
    for i, name in enumerate(names):
        print(f"{name:<12}{scores[i]:>6}{letter_grade(scores[i]):>7}")


def print_summary(names, scores):
    """Print class statistics."""
    mean = average(scores)
    best = names[scores.index(max(scores))]
    passing = [s for s in scores if s >= 60]

    print("-" * 25)
    print(f"Class average: {mean:.1f}")
    print(f"Highest:       {max(scores)} ({best})")
    print(f"Lowest:        {min(scores)}")
    print(f"Passing:       {len(passing)} of {len(scores)}")


names = ["Ada", "Grace", "Alan", "Katherine", "Edsger"]
scores = [88, 92, 45, 95, 71]

print_roster(names, scores)
print_summary(names, scores)
```

Output:

```
Student      Score  Grade
-------------------------
Ada             88      B
Grace           92      A
Alan            45      F
Katherine       95      A
Edsger          71      C
-------------------------
Class average: 78.2
Highest:       95 (Katherine)
Lowest:        45
Passing:       4 of 5
```

Three things here are new.

**Alignment in f-strings.** `{name:<12}` pads to 12 characters, left-aligned; `{score:>6}` pads to 6, right-aligned. This is how you get columns that line up without counting spaces by hand.

**Finding the matching name.** `scores.index(max(scores))` gets the position of the highest score, and that same position in `names` gives the student. This works only because the two lists are kept in the same order — they are **parallel lists**, and every operation has to maintain that correspondence. It is fragile: sort `scores` and the gradebook starts attributing grades to the wrong students. Chapters 9 and 10 give you sturdier ways to tie a name to a score.

**List comprehension.** `[s for s in scores if s >= 60]` builds the filtered list in one line, doing exactly what the four-line filtering loop above did. Comprehensions are compact and extremely common in real Python. Write the loop version when you are learning and the comprehension when the operation is simple enough to read at a glance.
