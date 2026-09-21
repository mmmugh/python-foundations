<!-- part: Part III — Algorithms -->
## Chapter 12 — Recursion and Problem Solving

A **recursive** function is one that calls itself. That sounds circular and is not, provided the function always calls itself on a *smaller* version of the problem and knows when to stop.

Start with something you can already write two ways. The factorial of 5 is 5 × 4 × 3 × 2 × 1.

```python
def factorial_loop(n):
    """Return n! using a loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial(n):
    """Return n! using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial_loop(5))
print(factorial(5))
```

Output:

```
120
120
```

The recursive version rests on a fact about factorials: **5! is just 5 × 4!**. If you can get 4!, you are done. And 4! is 4 × 3!, and so on down to 1! which is simply 1.

### The two required parts

Every recursive function needs both of these, and leaving out either one breaks it:

1. A **base case** — a version of the problem small enough to answer outright, with no further call. Here: `if n <= 1: return 1`.
2. A **recursive case** — which calls itself on a smaller input and builds the answer from the result. Here: `return n * factorial(n - 1)`.

The recursive case must move *toward* the base case. `factorial(n - 1)` shrinks `n` each time, so it must eventually reach 1. Write `factorial(n)` instead and the function calls itself forever:

```
RecursionError: maximum recursion depth exceeded
```

Python stops at about a thousand nested calls. That error nearly always means a missing or unreachable base case.

### Following the calls

Printing at each level shows what actually happens:

```python
def factorial_traced(n, depth=0):
    """Factorial that shows each call and each return."""
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")

    if n <= 1:
        print(f"{indent}base case, returning 1")
        return 1

    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{indent}returning {n} * factorial({n - 1}) = {result}")
    return result


factorial_traced(4)
```

Output:

```
factorial(4) called
  factorial(3) called
    factorial(2) called
      factorial(1) called
      base case, returning 1
    returning 2 * factorial(1) = 2
  returning 3 * factorial(2) = 6
returning 4 * factorial(3) = 24
```

Notice the shape: the calls go all the way *down* to the base case before any of them returns, and then the answers come back *up*. Each level is waiting, holding its own `n`, for the level below to finish. Nothing is actually multiplied until the bottom is reached.

That is the mental model worth keeping. Recursion is not a loop that goes around; it is a stack of unfinished work that unwinds.

### More examples

**Summing a list:**

```python
def total(numbers):
    """Return the sum of a list, recursively."""
    if not numbers:
        return 0
    return numbers[0] + total(numbers[1:])


print(total([1, 2, 3, 4, 5]))
```

Output:

```
15
```

The base case is an empty list, whose sum is 0. Otherwise: the first item plus the sum of everything else.

**Reversing a string:**

```python
def reverse(text):
    """Return the text reversed, recursively."""
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


print(reverse("recursion"))
```

Output:

```
noisrucer
```

**Counting down:**

```python
def countdown(n):
    """Print a countdown from n to 1, then Liftoff."""
    if n <= 0:
        print("Liftoff.")
        return
    print(n)
    countdown(n - 1)


countdown(3)
```

Output:

```
3
2
1
Liftoff.
```

A bare `return` with no value ends the function immediately, returning `None`.

### When recursion goes wrong: Fibonacci

The Fibonacci sequence starts 0, 1, and each later number is the sum of the two before it. The recursive definition is so natural it almost writes itself:

```python
def fib(n):
    """Return the nth Fibonacci number. Correct, but very slow."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(fib(i), end=" ")
print()
```

Output:

```
0 1 1 2 3 5 8 13 21 34 
```

This is correct and it is a disaster. `fib(30)` takes about 1.6 million calls; `fib(50)` would take longer than you will wait.

The reason is that it recomputes the same values endlessly. Calculating `fib(5)` requires `fib(4)` and `fib(3)`; but `fib(4)` also requires `fib(3)`, which gets computed from scratch a second time — and each of those recomputes `fib(2)`, and so on. The work roughly doubles with each step, which is **O(2ⁿ)**.

The fix is to remember answers already computed, a technique called **memoization**:

```python
def fib_fast(n, memo=None):
    """Return the nth Fibonacci number, remembering previous results."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_fast(n - 1, memo) + fib_fast(n - 2, memo)
    return memo[n]


print(fib_fast(50))
print(fib_fast(90))
```

Output:

```
12586269025
2880067194370816120
```

That returns instantly. A dictionary — the Chapter 9 structure — turns an O(2ⁿ) algorithm into an O(n) one by ensuring each value is computed exactly once. This is a genuinely important idea, and choosing the right data structure is again what made the difference.

A loop also handles Fibonacci perfectly well, in O(n) and with no recursion at all:

```python
def fib_loop(n):
    """Return the nth Fibonacci number, using a loop."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib_loop(50))
```

Output:

```
12586269025
```

### When to use recursion

Anything recursive can be written with a loop, and anything looped can be written recursively. The choice is about clarity.

**Recursion fits** when the problem is naturally self-similar: tree and folder structures, nested menus, dividing a problem in half repeatedly, or puzzles like the Towers of Hanoi whose rules are stated recursively.

**Loops fit** when you are stepping through a sequence. Summing a list recursively, as above, is a fine teaching exercise and worse code than `sum()`.

For a 9th-grade course the honest summary is: recognize recursion, be able to trace it, and know that some problems become much simpler when expressed this way. Do not force it where a loop is clearer.

### A problem that wants recursion

Binary search from Chapter 11, written recursively, is arguably clearer than the loop version — the "search this half instead" step becomes a literal call:

```python
def binary_search(items, target, low=0, high=None):
    """Return the index of target in a sorted list, or -1 if absent."""
    if high is None:
        high = len(items) - 1

    if low > high:
        return -1

    middle = (low + high) // 2

    if items[middle] == target:
        return middle
    elif items[middle] < target:
        return binary_search(items, target, middle + 1, high)
    else:
        return binary_search(items, target, low, middle - 1)


numbers = [4, 8, 9, 15, 17, 23, 42]
print(binary_search(numbers, 23))
print(binary_search(numbers, 5))
```

Output:

```
5
-1
```

The base cases are "the range is empty" and "found it." Each recursive call searches a strictly smaller range, so it always terminates.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| No base case | `RecursionError` |
| A base case that is never reached | `RecursionError` |
| Not returning the recursive call's result | Returns `None` |
| Not shrinking the input | Infinite recursion |
| Using recursion where a loop is clearer | Slower and harder to read |
| A mutable default like `memo={}` | Shared across calls; use `None` and create it inside |

### Try It

1. Write `power(base, exponent)` recursively, without `**`.
2. Write `count_down_up(n)` printing n to 1, then 1 back to n, using one recursive function.
3. Write `digit_sum(n)` returning the sum of a number's digits, recursively.
4. Write `is_palindrome(text)` recursively.
5. Write `count_item(items, target)` counting occurrences in a list, recursively.
6. Write `gcd(a, b)` using Euclid's algorithm: the GCD of a and b equals the GCD of b and a % b, and the GCD of a and 0 is a.
7. Solve the Towers of Hanoi for 3 disks, printing each move.

### Capstone project: a student records system

This brings together everything in the course: functions, loops, conditionals, lists, dictionaries, records, searching, and sorting.

```python
# A student records system: add, search, sort, and report.

students = [
    {"id": 1004, "name": "Ada Lovelace", "grade": 9, "scores": [88, 92, 85]},
    {"id": 1001, "name": "Grace Hopper", "grade": 10, "scores": [95, 91, 98]},
    {"id": 1007, "name": "Alan Turing", "grade": 9, "scores": [45, 62, 58]},
    {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]},
    {"id": 1009, "name": "Edsger Dijkstra", "grade": 10, "scores": [71, 68, 75]},
]


def average(numbers):
    """Return the mean of a list of numbers, or 0.0 if empty."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def letter_grade(score):
    """Return the letter grade for a numeric average."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def find_by_id(records, student_id):
    """Binary search a list sorted by id. Returns the record or None."""
    low = 0
    high = len(records) - 1

    while low <= high:
        middle = (low + high) // 2
        if records[middle]["id"] == student_id:
            return records[middle]
        elif records[middle]["id"] < student_id:
            low = middle + 1
        else:
            high = middle - 1

    return None


def search_by_name(records, text):
    """Return every record whose name contains the text, ignoring case."""
    return [r for r in records if text.lower() in r["name"].lower()]


def group_by_grade(records):
    """Return a dictionary mapping each grade level to its records."""
    groups = {}
    for record in records:
        groups.setdefault(record["grade"], []).append(record)
    return groups


def print_roster(records):
    """Print all records, ranked by average, highest first."""
    ranked = sorted(records, key=lambda r: average(r["scores"]), reverse=True)

    print(f"{'Rank':<6}{'ID':<7}{'Name':<20}{'Gr':<4}{'Avg':>7}{'Grade':>7}")
    print("-" * 51)
    for position, record in enumerate(ranked, start=1):
        mean = average(record["scores"])
        print(
            f"{position:<6}{record['id']:<7}{record['name']:<20}"
            f"{record['grade']:<4}{mean:>7.1f}{letter_grade(mean):>7}"
        )
    print("-" * 51)


def print_grade_summary(records):
    """Print a per-grade-level summary."""
    print("\nBy grade level")
    groups = group_by_grade(records)
    for grade in sorted(groups):
        members = groups[grade]
        means = [average(r["scores"]) for r in members]
        print(f"  Grade {grade}: {len(members)} students, average {average(means):.1f}")


def print_class_stats(records):
    """Print statistics for the whole class."""
    means = [average(r["scores"]) for r in records]
    passing = [m for m in means if m >= 60]
    best = max(records, key=lambda r: average(r["scores"]))

    print("\nClass statistics")
    print(f"  Students:      {len(records)}")
    print(f"  Class average: {average(means):.1f}")
    print(f"  Top student:   {best['name']} ({average(best['scores']):.1f})")
    print(f"  Passing:       {len(passing)} of {len(records)}")


print_roster(students)
print_grade_summary(students)
print_class_stats(students)

by_id = sorted(students, key=lambda r: r["id"])
found = find_by_id(by_id, 1007)
print(f"\nLookup 1007:   {found['name'] if found else 'not found'}")
print(f"Lookup 9999:   {find_by_id(by_id, 9999)}")

matches = search_by_name(students, "a")
print(f"Names with 'a': {len(matches)}")
```

Output:

```
Rank  ID     Name                Gr      Avg  Grade
---------------------------------------------------
1     1002   Katherine Johnson   11     96.7      A
2     1001   Grace Hopper        10     94.7      A
3     1004   Ada Lovelace        9      88.3      B
4     1009   Edsger Dijkstra     10     71.3      C
5     1007   Alan Turing         9      55.0      F
---------------------------------------------------

By grade level
  Grade 9: 2 students, average 71.7
  Grade 10: 2 students, average 83.0
  Grade 11: 1 students, average 96.7

Class statistics
  Students:      5
  Class average: 81.2
  Top student:   Katherine Johnson (96.7)
  Passing:       4 of 5

Lookup 1007:   Alan Turing
Lookup 9999:   None
Names with 'a': 5
```

Read through that program and count what it uses. Functions with docstrings and single responsibilities. Loops and conditionals. Lists, dictionaries, records, list comprehensions. `sorted()` with `key=lambda`. Binary search on a sorted list, and linear search where the data is not sorted by the field being searched. f-string alignment throughout.

That is the whole course.

A few points of craft worth extracting.

`find_by_id` requires its input sorted by id, which is why the call site sorts first. The docstring says so, because a function with a precondition that is not documented is a trap. When a caller violates it, binary search does not fail loudly — it returns a confidently wrong answer.

`enumerate(ranked, start=1)` takes a `start` argument, which is tidier than writing `position + 1` everywhere.

`max(records, key=...)` finds the top student by average, returning the whole record rather than just the number — the same `key` idea as in `sorted()`.

And "Grade 11: 1 students" is grammatically wrong. Fixing that is your first exercise: it needs a conditional expression, and noticing it at all is the skill worth having.
