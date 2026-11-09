<!-- part: Unit 7 — Lists -->
## Lesson 7.5 — Asking about a list

You can change a list. In this lesson you ask questions about a whole list, like how many items it has, their total, and which is the largest, each with one word.

### Warm-up

1. Predict what this prints, then press Check.

```python
cards = ["A", "B", "C"]
cards.insert(1, "Z")
taken = cards.pop()
print(taken)
print(cards)
```

2. Which of these gives back the item it takes out of the list?

### How many, and how much

Python has functions that answer a question about a whole list. `len()` gives how many items it has, and `sum()` adds them up:

```python
scores = [88, 92, 79, 95]
print(len(scores))
print(sum(scores))
```

Output:

```
4
354
```

`len` is short for length. `max()` gives the largest item, and `min()` the smallest. With `sum()` and `len()` together, you have an average:

```python
scores = [88, 92, 79, 95]
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))
```

Output:

```
95
79
88.5
```

`max()` does in one word what the "largest so far" loop of lesson 5.5 does.

An empty list has 0 items, and they add up to 0. But it has no largest item:

```python
empty = []
print(len(empty))
print(sum(empty))
print(max(empty))
```

This prints 0 and 0, then stops. The last line of the error starts with `ValueError` and says the argument is empty: `max()` was given nothing to choose from. `min()` does the same. And `sum(empty) / len(empty)` would divide by 0, which is a `ZeroDivisionError` (lesson 3.1). So an empty list is the awkward case to check, whenever a list goes into a program.

### Practice

3. Predict what this prints, then press Check.

```python
heights = [150, 162, 158]
print(len(heights))
print(sum(heights))
print(max(heights) - min(heights))
```

4. Write a function `spread(numbers)` that gives back the largest number minus the smallest. For an empty list, it gives back 0.

> Split it: first, if the list is empty, its `len()` is 0: give back 0. Otherwise, give back the largest minus the smallest.
> Check it: try `[3, 9, 5]`, which gives 6. Then the awkward ones: `[]`, which gives 0, and a list of one number, like `[7]`, which also gives 0.


5. Print the total, the largest and the smallest of the numbers in `rolls`, one per line.

```python
rolls = [4, 6, 1, 5, 3, 6]
```

> Check it: the total is 25, the largest 6 and the smallest 1.

### Try It

6. Write a function `average(numbers)` that gives back the average of a list of numbers. For an empty list, it gives back 0.

> Say it: a list of numbers goes in; their average comes out, and an empty list gives 0. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. if the list is empty, give back 0. 2. otherwise, add up the numbers, divide by how many there are, and give that back.
> Name it: the function and its parameter are named for you. What would you call the total, if you store it first?
> Check it: try `[88, 92, 79, 95]`, which gives 88.5. Then the awkward one: `[]`. What happens if you leave out step 1?


### What you can do now

- Ask how many items a list has with `len()`, and add them up with `sum()`.
- Find the largest and smallest with `max()` and `min()`, and work out an average.
- Check what happens with an empty list, the awkward case for any list.

Key words: **len**, **sum**, **max**, **min**.
