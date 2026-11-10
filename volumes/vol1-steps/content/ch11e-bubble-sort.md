<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.5 — Bubble sort, and stopping early

A selection sort makes the same comparisons however the list starts, even when it is sorted already. In this lesson you meet a sort that only ever compares two items side by side, and that can tell when the list is in order and stop.

### Warm-up

1. Predict what this prints, then press Check.

```python
numbers = [5, 2, 8, 1]
smallest = 0
for position in range(1, len(numbers)):
    if numbers[position] < numbers[smallest]:
        smallest = position
numbers[0], numbers[smallest] = numbers[smallest], numbers[0]
print(numbers)
```

2. How many comparisons does a selection sort make on a list of 6 items?

### Neighbors

Two items side by side are **neighbors**. Walk along the list comparing each item with its neighbor on the right, and swap them when the left one is bigger:

```python
numbers = [5, 1, 4, 2]
for position in range(len(numbers) - 1):
    if numbers[position] > numbers[position + 1]:
        numbers[position], numbers[position + 1] = numbers[position + 1], numbers[position]
print(numbers)
```

Output:

```
[1, 4, 2, 5]
```

`range(len(numbers) - 1)` stops one short, because the last item has no neighbor on its right: `numbers[position + 1]` would be past the end. Here is the trace table. The list changes on line 4, in place:

| After line | position | numbers |
| --- | --- | --- |
| 1 |  | [5, 1, 4, 2] |
| 2 | 0 | [5, 1, 4, 2] |
| 3 | 0 | [5, 1, 4, 2] |
| 4 | 0 | [1, 5, 4, 2] |
| 2 | 1 | [1, 5, 4, 2] |
| 3 | 1 | [1, 5, 4, 2] |
| 4 | 1 | [1, 4, 5, 2] |
| 2 | 2 | [1, 4, 5, 2] |
| 3 | 2 | [1, 4, 5, 2] |
| 4 | 2 | [1, 4, 2, 5] |
| 2 | 2 | [1, 4, 2, 5] |
| 5 | 2 | [1, 4, 2, 5] |

The 5 is swapped at every step, so one pass carries it all the way to the end. The list is not sorted yet, but its biggest item is in its final place.

### Practice

3. Fill in the table, then press Check. Write each list the way Python prints it.

```python
numbers = [3, 2, 1]
for position in range(len(numbers) - 1):
    if numbers[position] > numbers[position + 1]:
        numbers[position], numbers[position + 1] = numbers[position + 1], numbers[position]
```

### Pass after pass

One pass puts the biggest item last. A second pass puts the next biggest just before it, and so on. The biggest items rise to the end like bubbles in water, so this is called **bubble sort**:

```python
def bubble_sort(items):
    result = items.copy()
    for done in range(len(result)):
        for position in range(len(result) - 1 - done):
            if result[position] > result[position + 1]:
                result[position], result[position + 1] = result[position + 1], result[position]
        print(result)
    return result


print(bubble_sort([5, 1, 4, 2]))
```

Output:

```
[1, 4, 2, 5]
[1, 2, 4, 5]
[1, 2, 4, 5]
[1, 2, 4, 5]
[1, 2, 4, 5]
```

`done` counts the passes already made. After `done` passes, the last `done` items are in their final places, so `- done` stops each pass before them: there is no need to compare them again.

### Practice

4. Predict what this prints, then press Check.

```python
def bubble_sort(items):
    result = items.copy()
    for done in range(len(result)):
        for position in range(len(result) - 1 - done):
            if result[position] > result[position + 1]:
                result[position], result[position + 1] = result[position + 1], result[position]
        print(result)
    return result


print(bubble_sort([4, 3, 2, 1]))
```

5. Why does each pass stop at `len(result) - 1 - done`, not at `len(result) - 1`?

### Stopping early

In the example, the last three passes changed nothing. A pass that swaps nothing has found every neighbor in order, so the list is sorted, and the sort can stop. A `True`/`False` name, set to `False` at the start of each pass and to `True` by any swap, tells it so:

```python
def bubble_sort(items):
    result = items.copy()
    for done in range(len(result)):
        swapped = False
        for position in range(len(result) - 1 - done):
            if result[position] > result[position + 1]:
                result[position], result[position + 1] = result[position + 1], result[position]
                swapped = True
        print(result)
        if not swapped:
            break
    return result


print(bubble_sort([5, 1, 4, 2]))
print(bubble_sort([1, 2, 3, 4]))
```

Output:

```
[1, 4, 2, 5]
[1, 2, 4, 5]
[1, 2, 4, 5]
[1, 2, 4, 5]
[1, 2, 3, 4]
[1, 2, 3, 4]
```

The first list takes three passes: the third swaps nothing, and the sort stops. The second list is sorted already, so one pass of 3 comparisons does it. A selection sort would make 6. On a sorted list of any size, this bubble sort makes one comparison per neighbor pair and stops: that is its one real strength.

### Practice

6. Predict what this prints, then press Check.

```python
def bubble_sort(items):
    result = items.copy()
    for done in range(len(result)):
        swapped = False
        for position in range(len(result) - 1 - done):
            if result[position] > result[position + 1]:
                result[position], result[position + 1] = result[position + 1], result[position]
                swapped = True
        print(result)
        if not swapped:
            break
    return result


print(bubble_sort([2, 1, 3, 4]))
print(bubble_sort([1, 2, 3]))
```

7. Write a function `bubble_swaps(items)` that gives back how many swaps a bubble sort makes when it sorts `items`. So `bubble_swaps([5, 1, 4, 2])` gives 4.

> Split it: start a count at 0. Bubble sort a copy of the list, and add one to the count each time two neighbors are swapped. Give back the count.
> Check it: try `[5, 1, 4, 2]`, which gives 4: three swaps in the first pass, one in the second. Then the awkward ones: `[]` and `[1, 2, 3]`, which give 0, and `[2, 2]`, which gives 0 too, because the left one is not bigger.

### Try It

8. Write a function `is_sorted(items)` that gives back `True` if every item in `items` is no bigger than its neighbor on the right, and `False` otherwise. So `[1, 2, 2, 5]` is sorted, and `[1, 3, 2]` is not.

> Say it: a list goes in; `True` comes out if it is in order, smallest first, and `False` if any neighbor pair is the wrong way round. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. walk along the neighbor pairs, as one pass of a bubble sort does. 2. as soon as a left item is bigger than its right neighbor, give back `False`. 3. below the loop, give back `True`.
> Name it: the function and its parameter are named for you. What would you call each position as the loop goes?
> Check it: try `[1, 2, 2, 5]`, which gives `True`, and `[1, 3, 2]`, where only the last pair is wrong, which gives `False`. Then the awkward ones: `[]` and `[7]`, which give `True`, because nothing is out of order.

### What you can do now

- Compare neighbors, and swap them when they are out of order.
- Sort a list by bubble sort, and stop it early when a pass makes no swaps.
- Check whether a list is sorted in one pass.

Key words: **neighbors**, **bubble sort**.
