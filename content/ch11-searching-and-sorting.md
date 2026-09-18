<!-- part: Part III — Algorithms -->
## Chapter 11 — Searching and Sorting

An **algorithm** is a procedure for solving a problem: a finite sequence of unambiguous steps that turns an input into the right output. Every program you have written contains algorithms. This chapter is about a handful that are important enough to have names, and about the question that separates a working program from a good one — *how much work does this take?*

Python can already search and sort for you. You will write these by hand anyway, for the same reason you learn long division after getting a calculator: the methods are the point.

### Linear search

To find something in a list, look at each item until you find it.

```python
def linear_search(items, target):
    """Return the index of target in items, or -1 if it is absent."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


numbers = [17, 4, 23, 8, 42, 15, 9]

print(linear_search(numbers, 42))
print(linear_search(numbers, 99))
```

Output:

```
4
-1
```

Returning `-1` for "not found" is a widespread convention, because it cannot be mistaken for a valid index.

The important question is how many comparisons this takes. Best case, the target is first: one comparison. Worst case, it is last or absent: one comparison per item. On average, about half the list.

The headline number is the worst case, because it is what you can promise. For a list of *n* items, linear search needs **at most *n* comparisons**. Double the list and you double the work.

This is fine for a hundred items and painful for ten million.

### Binary search

If the list is **already sorted**, you can do enormously better.

Think about looking up a word in a physical dictionary. You do not start at page one. You open near the middle, see whether your word falls before or after, and throw away half the book. Then you repeat.

```python
def binary_search(items, target):
    """Return the index of target in a SORTED list, or -1 if it is absent."""
    low = 0
    high = len(items) - 1

    while low <= high:
        middle = (low + high) // 2

        if items[middle] == target:
            return middle
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


numbers = [4, 8, 9, 15, 17, 23, 42]

print(binary_search(numbers, 42))
print(binary_search(numbers, 4))
print(binary_search(numbers, 99))
```

Output:

```
6
0
-1
```

The variables `low` and `high` mark the section still under consideration. Each pass checks the middle item and discards half of what remains. When `low` passes `high`, nothing is left and the target is absent.

Watching it work makes the idea concrete:

```python
def binary_search_verbose(items, target):
    """Binary search that prints each step."""
    low = 0
    high = len(items) - 1
    step = 0

    while low <= high:
        step += 1
        middle = (low + high) // 2
        print(f"Step {step}: checking index {middle} (value {items[middle]}), "
              f"{high - low + 1} items still in range")

        if items[middle] == target:
            return middle
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


numbers = list(range(0, 100, 2))
result = binary_search_verbose(numbers, 74)
print(f"Found at index {result}")
```

Output:

```
Step 1: checking index 24 (value 48), 50 items still in range
Step 2: checking index 37 (value 74), 25 items still in range
Found at index 37
```

Two steps to find one value among fifty. Linear search would have taken 38.

### Counting the work

Binary search halves the remaining range each step, so the question "how many steps?" becomes "how many times can I halve *n* before reaching 1?" That is the base-2 logarithm.

| List size | Linear search (worst) | Binary search (worst) |
| --- | --- | --- |
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1,000 | 1,000 | 10 |
| 1,000,000 | 1,000,000 | 20 |
| 1,000,000,000 | 1,000,000,000 | 30 |

Read the bottom row again. Searching a billion sorted items takes about thirty comparisons. This is not a small optimization; it is a different category of thing, and it is why so much of computing is arranged around keeping data sorted or indexed.

The standard notation for this is **big-O**. Linear search is **O(n)** — work grows in proportion to the size. Binary search is **O(log n)** — work grows like the logarithm, which is to say barely. Big-O describes how cost *scales*, deliberately ignoring constant factors and the speed of the machine, because those change and the scaling does not.

A few common classes:

| Notation | Name | Doubling *n* means | Example |
| --- | --- | --- | --- |
| O(1) | Constant | No change | `list[5]`, dictionary lookup |
| O(log n) | Logarithmic | One more step | Binary search |
| O(n) | Linear | Twice the work | Linear search, summing a list |
| O(n²) | Quadratic | Four times the work | The sorts below |

This also explains a claim from Chapter 9. Finding a name in a list of a thousand takes up to a thousand comparisons; finding it in a dictionary takes roughly one, regardless of size. Dictionary lookup is O(1). That is the real reason to choose a dictionary, and it is why the gradebook got faster as well as safer.

Binary search has one prerequisite, and it is a real cost: **the list must be sorted.** Which raises the next question.

### Selection sort

Repeatedly find the smallest remaining item and put it in place.

```python
def selection_sort(items):
    """Return a new sorted list, using selection sort."""
    result = items.copy()

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]

    return result


print(selection_sort([64, 25, 12, 22, 11]))
```

Output:

```
[11, 12, 22, 25, 64]
```

The outer loop walks a boundary from left to right: everything to its left is sorted and final. The inner loop scans the unsorted remainder for the smallest value, and the tuple-unpacking swap from Chapter 10 puts it where it belongs.

Watching the boundary move:

```python
def selection_sort_verbose(items):
    """Selection sort that shows the list after each pass."""
    result = items.copy()

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
        sorted_part = " ".join(str(v) for v in result[:i + 1])
        rest = " ".join(str(v) for v in result[i + 1:])
        print(f"Pass {i + 1}: [{sorted_part}] {rest}")

    return result


selection_sort_verbose([64, 25, 12, 22, 11])
```

Output:

```
Pass 1: [11] 25 12 22 64
Pass 2: [11 12] 25 22 64
Pass 3: [11 12 22] 25 64
Pass 4: [11 12 22 25] 64
Pass 5: [11 12 22 25 64] 
```

Selection sort makes about n²/2 comparisons: the outer loop runs n times and the inner loop averages n/2. That is **O(n²)**, and it is a sharp contrast with what came before. Ten times the data means a hundred times the work.

### Bubble sort

Repeatedly compare neighboring items and swap them when they are out of order. Large values "bubble" toward the end.

```python
def bubble_sort(items):
    """Return a new sorted list, using bubble sort with early exit."""
    result = items.copy()
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


print(bubble_sort([64, 25, 12, 22, 11]))
print(bubble_sort([1, 2, 3, 4, 5]))
```

Output:

```
[11, 12, 22, 25, 64]
[1, 2, 3, 4, 5]
```

The `swapped` flag is the interesting part. If a full pass makes no swaps, the list is already in order and the function stops. That makes bubble sort **O(n)** on already-sorted data, which is its one genuine advantage — and a reminder that worst-case analysis does not describe every situation.

The `n - i - 1` in the inner loop skips the tail, where the largest values have already settled.

### What Python actually does

```python
numbers = [64, 25, 12, 22, 11]

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(["banana", "Apple", "cherry"], key=str.lower))
```

Output:

```
[11, 12, 22, 25, 64]
[64, 25, 22, 12, 11]
['Apple', 'banana', 'cherry']
```

Python's `sorted()` uses an algorithm called Timsort, which is **O(n log n)** — far better than the quadratic sorts here and close to the best possible for general-purpose sorting. It is also written in C, thoroughly tested, and handles edge cases you have not thought of.

**Always use `sorted()` or `.sort()` in real programs.** The hand-written sorts in this chapter are for understanding, not for production. Knowing that the built-in is O(n log n) while a naive sort is O(n²) — and knowing what that difference means for a million records — is the actual takeaway.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| Binary search on an unsorted list | Silently wrong answers, no error |
| `middle = (low + high) / 2` | `TypeError` — indexes must be integers; use `//` |
| `while low < high` instead of `<=` | Misses a one-item range |
| Forgetting `low = middle + 1` | Infinite loop |
| Sorting in place when the caller needed the original | Use `.copy()` or `sorted()` |
| Writing your own sort for real work | Slower, and probably wrong on some edge case |

### Try It

1. Modify `linear_search` to return every index where the target appears.
2. Add a step counter to both searches and compare them on a list of 1,000 items.
3. Write `binary_search` that returns where the target *would* go if absent, rather than -1.
4. Implement insertion sort: take each item and slide it back to its place.
5. Sort a list of student records by score, then by name, using `sorted()` with a `key`.
6. Write `is_sorted(items)` returning whether a list is already in order, in one pass.
7. Find the two closest values in a list. First try every pair, then try sorting first — and compare the work each does.

### Chapter project: measuring algorithms

Write a program that counts the actual operations each algorithm performs, so the big-O claims stop being theory.

```python
# Counts the comparisons each algorithm performs at several list sizes.

import random


def linear_search_counted(items, target):
    """Return (index, comparisons) for a linear search."""
    comparisons = 0
    for i in range(len(items)):
        comparisons += 1
        if items[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search_counted(items, target):
    """Return (index, comparisons) for a binary search on a sorted list."""
    low = 0
    high = len(items) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        middle = (low + high) // 2
        if items[middle] == target:
            return middle, comparisons
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1, comparisons


def selection_sort_counted(items):
    """Return (sorted list, comparisons) for a selection sort."""
    result = items.copy()
    comparisons = 0

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            comparisons += 1
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]

    return result, comparisons


def compare_searches(sizes):
    """Print worst-case comparison counts for both searches."""
    print("SEARCHING for a value that is not present (worst case)")
    print(f"{'Size':>10}{'Linear':>10}{'Binary':>10}{'Ratio':>10}")
    print("-" * 40)

    for size in sizes:
        data = list(range(size))
        missing = size + 1
        _, linear = linear_search_counted(data, missing)
        _, binary = binary_search_counted(data, missing)
        print(f"{size:>10}{linear:>10}{binary:>10}{linear / binary:>9.0f}x")


def compare_sorts(sizes):
    """Print comparison counts for selection sort at several sizes."""
    print("\nSORTING a shuffled list")
    print(f"{'Size':>10}{'Comparisons':>14}{'Size squared':>14}")
    print("-" * 38)

    for size in sizes:
        data = list(range(size))
        random.shuffle(data)
        _, comparisons = selection_sort_counted(data)
        print(f"{size:>10}{comparisons:>14}{size * size:>14}")


compare_searches([10, 100, 1000, 10000])
compare_sorts([10, 50, 100, 200])
```

Output:

```
SEARCHING for a value that is not present (worst case)
      Size    Linear    Binary     Ratio
----------------------------------------
        10        10         4        2x
       100       100         7       14x
      1000      1000        10      100x
     10000     10000        14      714x

SORTING a shuffled list
      Size   Comparisons  Size squared
--------------------------------------
        10            45           100
        50          1225          2500
       100          4950         10000
       200         19900         40000
```

The search table shows the gap widening as the data grows — 2× at ten items, 714× at ten thousand. An algorithm choice that looks irrelevant on test data can dominate everything in production, and this is what people mean when they say a program "does not scale."

The sort table shows comparisons landing at almost exactly half of n². 4,950 against 10,000; 19,900 against 40,000. The ratio holds steady as n grows, which is what O(n²) means: the constant factor (here, one half) does not change the shape, so big-O ignores it.

Note `_, linear = ...` — by convention `_` names a value you are deliberately discarding. And `random.shuffle()` reorders a list in place, returning `None`, in the same way `.sort()` does.
