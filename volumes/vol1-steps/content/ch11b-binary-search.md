<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.2 — Halving the search

A linear search of 1,000 names may look at all 1,000. But when the list is sorted, there is a much quicker way, and you have used it already: in lesson 5.7's guessing game, each `Too high.` or `Too low.` told you which half of the numbers to forget. In this lesson a search does the same.

### Warm-up

1. Predict what this prints, then press Check.

```python
def find_position(items, target):
    for position in range(len(items)):
        if items[position] == target:
            return position
    return -1


print(find_position([5, 9, 5], 5))
print(find_position([], 5))
print(7 // 2)
print((4 + 6) // 2)
```

2. A list holds 1,000 names. A linear search looks for a name that is not in it. How many names does it look at?

### Halving

In the guessing game, a good first guess for a number from 1 to 100 is 50, the middle. If 50 is too low, the numbers 1 to 50 are out, and half the work is done with one guess.

A sorted list works the same way. Look at the middle item. If it is the target, you have found it. If it is smaller than the target, the target can only be to its right, so the middle and everything to its left are out. If it is bigger, everything from the middle rightwards is out. Then do the same with what is left.

Two names keep track of what is left: `low` is the position of the first item still in play, and `high` the position of the last. The middle is halfway between them, worked out with `//` so that it is a whole number:

```python
numbers = [4, 8, 9, 15, 17, 23, 42]
target = 23
low = 0
high = len(numbers) - 1
where = -1
while low <= high:
    middle = (low + high) // 2
    if numbers[middle] == target:
        where = middle
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
print(where)
```

Output:

```
5
```

This is called a **binary search**: binary means "in two", and each pass cuts what is left in two. Here is its trace table:

| After line | low | high | middle |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 | 0 |  |  |
| 4 | 0 | 6 |  |
| 5 | 0 | 6 |  |
| 6 | 0 | 6 |  |
| 7 | 0 | 6 | 3 |
| 8 | 0 | 6 | 3 |
| 11 | 0 | 6 | 3 |
| 12 | 4 | 6 | 3 |
| 6 | 4 | 6 | 3 |
| 7 | 4 | 6 | 5 |
| 8 | 4 | 6 | 5 |
| 9 | 4 | 6 | 5 |
| 10 | 4 | 6 | 5 |
| 15 | 4 | 6 | 5 |

On the first pass, the middle is position 3, which holds 15. Line 8 asks whether 15 is the target, and line 11 whether it is smaller. It is, so line 12 moves `low` to 4: positions 0 to 3 are out. On the second pass, the middle of 4 to 6 is 5, which holds 23. Found, in two passes. A linear search would have looked at six items.

### Practice

3. Fill in the table, then press Check. This time the target is to the left of the middle, so the `else` runs. As in lesson 4.3, an `else:` line gets no row of its own: the next row is the line inside it.

```python
numbers = [4, 8, 9, 15, 17, 23, 42]
target = 8
low = 0
high = len(numbers) - 1
where = -1
while low <= high:
    middle = (low + high) // 2
    if numbers[middle] == target:
        where = middle
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
```

### When it is not there

Here is the same search for 10, which is not in the list, with a `print()` to show each pass:

```python
numbers = [4, 8, 9, 15, 17, 23, 42]
target = 10
low = 0
high = len(numbers) - 1
where = -1
while low <= high:
    middle = (low + high) // 2
    print(low, high, middle)
    if numbers[middle] == target:
        where = middle
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
print(where)
```

Output:

```
0 6 3
0 2 1
2 2 2
-1
```

On the third pass, `low` and `high` are both 2: one item is still in play, so it must be looked at. That is why the loop runs while `low <= high`, not `low < high`. It holds 9, which is smaller than 10, so `low` becomes 3. Now `low` has passed `high`, nothing is left in play, and the loop ends with `where` still -1.

`middle + 1` and `middle - 1` matter too: the middle item has been looked at, so it is out as well. Leave out the `+ 1`, and `low` can stop moving, so the loop never ends.

### Practice

4. Predict what this prints, then press Check.

```python
numbers = [4, 8, 9, 15, 17, 23, 42]
target = 50
low = 0
high = len(numbers) - 1
where = -1
while low <= high:
    middle = (low + high) // 2
    print(low, high, middle)
    if numbers[middle] == target:
        where = middle
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
print(where)
```

### Only on a sorted list

A binary search trusts that everything left of the middle is smaller, and everything right of it is bigger. On a list that is not sorted, that is not true:

```python
numbers = [15, 4, 42, 8, 23, 9, 17]
target = 42
low = 0
high = len(numbers) - 1
where = -1
while low <= high:
    middle = (low + high) // 2
    if numbers[middle] == target:
        where = middle
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
print(where)
```

Output:

```
-1
```

42 is at position 2. But the middle holds 8, which is smaller than 42, so the search threw away the left half, 42 included. There is no error: just a wrong answer, which is worse.

### Practice

5. What must be true of a list before a binary search of it can be trusted?

6. This search should print 4, the position of 17, but it stops with an error. Run it and read the last line of the error: indices is the plural of index, and Python's name for a position in a list; you don't need to remember it. Then fix it.

```python
numbers = [4, 8, 9, 15, 17, 23, 42]
target = 17
low = 0
high = len(numbers) - 1
where = -1
while low <= high:
    middle = (low + high) / 2
    if numbers[middle] == target:
        where = middle
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
print(where)
```

> Split it: what kind of value does `/` always give back, even for `6 / 2`? A position must be a whole number.

7. Someone writes `while low < high:` instead of `while low <= high:`. Their search looks for 7 in the list `[7]`. What does it give?

8. Someone writes `low = middle` instead of `low = middle + 1`. What happens when their search looks for 50 in `[4, 8, 9, 15, 17, 23, 42]`?

### Try It

9. Write a function `binary_search(items, target)` that gives back the position of `target` in the sorted list `items`, or -1 if it is not there. Use a binary search.

> Say it: a sorted list and a target go in; the position of the target comes out, or -1, found by halving. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. set `low` to the first position and `high` to the last. 2. while `low <= high`, work out the middle. 3. if the middle item is the target, give back the middle. 4. if it is smaller, move `low` past the middle; otherwise move `high` before it. 5. below the loop, give back -1.
> Name it: the function and its parameters are named for you, and `low`, `high` and `middle` say what they hold.
> Check it: try `[4, 8, 9, 15, 17, 23, 42]` with 23, which gives 5, and with 4 and 42, the two ends, which give 0 and 6. Then the awkward ones: 10, which is not there and gives -1; `[7]` with 7, which gives 0; and `[]`, an empty list, which gives -1.
> Did it halve? While you try it, add `print(low, high, middle)` as the first line inside the loop, as the example did. For the list of 7, you see at most 3 lines, where a linear search could look at all 7 items. Take the print out before you press Check.

### What you can do now

- Search a sorted list by halving it, with `low`, `high` and `middle`.
- Say why the loop runs while `low <= high`, and why `low` moves to `middle + 1`.
- Say why a binary search needs a sorted list.

Key words: **binary search**.
