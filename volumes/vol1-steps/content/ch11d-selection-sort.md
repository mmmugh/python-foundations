<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.4 — Selection sort

A binary search needs a sorted list. `sorted()` gives you one, but how does a computer put a list in order? In this lesson you sort a list by hand, the way you might sort a hand of cards: find the smallest, put it first, and do the same with the rest. Then you count the work it takes.

### Warm-up

1. Predict what this prints, then press Check.

```python
def halvings(size):
    count = 0
    while size > 0:
        size = size // 2
        count += 1
    return count


print(halvings(16))
print(halvings(31))
print(halvings(0))
```

2. A list doubles from 500 items to 1,000. What happens to the worst case for a linear search of it?

### Where is the smallest?

To find the smallest item from some position onward, keep the position of the smallest so far, and move it whenever a later item is smaller:

```python
numbers = [64, 25, 12, 22]
start = 1
smallest = start
for position in range(start + 1, len(numbers)):
    if numbers[position] < numbers[smallest]:
        smallest = position
print(smallest, numbers[smallest])
```

Output:

```
2 12
```

`smallest` holds a position, not a value, so you know where the smallest item is as well as what it is. It starts at `start`, and the loop looks at every position after it. Items before `start`, like the 64 here, are never looked at. Here is its trace table:

| After line | position | smallest |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  | 1 |
| 4 | 2 | 1 |
| 5 | 2 | 1 |
| 6 | 2 | 2 |
| 4 | 3 | 2 |
| 5 | 3 | 2 |
| 4 | 3 | 2 |
| 7 | 3 | 2 |

12, at position 2, is smaller than 25, at position 1, so line 6 moves `smallest` to 2. 22 is not smaller than 12, so line 6 is skipped. Line 4 gets one last row when the positions run out.

### Practice

3. Fill in the table, then press Check.

```python
numbers = [9, 4, 7, 1]
start = 0
smallest = start
for position in range(start + 1, len(numbers)):
    if numbers[position] < numbers[smallest]:
        smallest = position
```

### Swapping two items

To swap the items at two positions, unpack, as you swapped two names in lesson 10.1. The right side is worked out first, then stored into the two positions:

```python
numbers = [64, 25, 12, 22]
numbers[0], numbers[2] = numbers[2], numbers[0]
print(numbers)
```

Output:

```
[12, 25, 64, 22]
```

### Practice

4. Predict what this prints, then press Check.

```python
letters = ["c", "a", "b"]
letters[0], letters[1] = letters[1], letters[0]
print(letters)
letters[1], letters[2] = letters[2], letters[1]
print(letters)
```

### Selection sort

Put the two together. On each pass, find the smallest item from `start` onward, and swap it into position `start`. The `print()` inside shows the list after each pass:

```python
def selection_sort(items):
    result = items.copy()
    for start in range(len(result)):
        smallest = start
        for position in range(start + 1, len(result)):
            if result[position] < result[smallest]:
                smallest = position
        result[start], result[smallest] = result[smallest], result[start]
        print(result)
    return result


numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))
print(numbers)
```

Output:

```
[11, 25, 12, 22, 64]
[11, 12, 25, 22, 64]
[11, 12, 22, 25, 64]
[11, 12, 22, 25, 64]
[11, 12, 22, 25, 64]
[11, 12, 22, 25, 64]
[64, 25, 12, 22, 11]
```

After the first pass, the smallest item is first, and it never moves again. After the second, the first two are final, and so on. In the last two passes the smallest was already at `start`, so the swap swaps an item with itself, which changes nothing. Each pass selects the smallest of what is left, so this is called **selection sort**. `copy()` (lesson 9.7) gives the function a list of its own, so the caller's list is left as it was: the last line shows it.

How much work is it? Count the comparisons, the `<` on line 6. The first pass compares the 4 items after `start` with the smallest so far: 4. The second pass compares 3, then 2, then 1, then 0. That is 4 + 3 + 2 + 1 = 10 comparisons for 5 items, whatever order they start in.

For 10 items it is 9 + 8 + ... + 1 = 45, and for 20 items, 190. Double the list, and the work is about four times as much: each pass is about twice as long, and there are twice as many passes.

### Practice

5. Predict what this prints, then press Check.

```python
def selection_sort(items):
    result = items.copy()
    for start in range(len(result)):
        smallest = start
        for position in range(start + 1, len(result)):
            if result[position] < result[smallest]:
                smallest = position
        result[start], result[smallest] = result[smallest], result[start]
        print(result)
    return result


numbers = [3, 1, 2]
print(selection_sort(numbers))
print(numbers)
```

6. Write a function `largest_first(items)` that gives back a new list of the items, biggest first, sorted by a selection sort, and leaves the caller's list as it was. Write it above these lines, then run them all.

```python
scores = [60, 95, 82, 95, 70]
print(largest_first(scores))
print(scores)
print(largest_first([]))
print(largest_first([5]))
```

> Split it: selection sort with one change: each pass finds the biggest item from `start` onward, not the smallest. Copy the list first.
> Check it: the lines print `[95, 95, 82, 70, 60]`, then the scores as they were, `[60, 95, 82, 95, 70]`. Then the awkward ones: `[]` and `[5]`.
> Did it sort by selection? While you try it, put `print(result)` (or whatever you named the copy) at the end of each pass, as the example does: the biggest of what is left joins the front, one pass at a time. Take the print out before you press Check.

7. A selection sort of 20 items makes 190 comparisons. About how many does it make for 40 items?

### Try It

8. Write a function `selection_count(items)` that gives back how many comparisons a selection sort makes when it sorts `items`. So `selection_count([64, 25, 12, 22, 11])` gives 10.

> Say it: a list goes in; the number of times a selection sort compares two items, sorting it, comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start a count at 0. 2. do the selection sort, on a copy. 3. add one to the count each time two items are compared, just before the `if`. 4. give back the count, not the list.
> Name it: the function and its parameter are named for you. What would you call the count?
> Check it: try the five numbers above, which give 10, and `[2, 1]`, which gives 1. Then the awkward ones: `[]` and `[7]`, which give 0, because there is nothing to compare.

### What you can do now

- Find the position of the smallest item from a given position onward.
- Swap two items in a list in one line, and sort a list by selection sort.
- Count a sort's comparisons, and say what doubling the list does to them.

Key words: **selection sort**.
