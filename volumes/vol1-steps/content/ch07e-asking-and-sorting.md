<!-- part: Unit 7 — Lists -->
## Lesson 7.5 — Asking about a list, and sorting it

You can change a list. In this lesson you ask questions about one, like how many items it has and which is the largest, each with one word. Then you put a list in order.

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

### Putting a list in order

`sorted()` gives back a new list, in order, and leaves the old one as it was:

```python
scores = [88, 92, 79]
ordered = sorted(scores)
print(ordered)
print(scores)
```

Output:

```
[79, 88, 92]
[88, 92, 79]
```

Numbers go from smallest to largest. Text goes in alphabetical order, with every capital letter before every small one, as in lesson 3.5:

```python
names = ["Grace", "Ada", "Alan"]
print(sorted(names))
```

Output:

```
['Ada', 'Alan', 'Grace']
```

A list also has a method, `sort()`, which puts the list itself in order:

```python
scores = [88, 92, 79]
scores.sort()
print(scores)
```

Output:

```
[79, 88, 92]
```

So there are two ways to sort. `sorted(scores)` makes a new list and leaves `scores` alone. `scores.sort()` changes `scores`, and gives back nothing at all, which is `None` (lesson 6.2):

```python
scores = [88, 92, 79]
result = scores.sort()
print(result)
```

Output:

```
None
```

`reverse()` is a method like `sort()`. It turns the list itself around, and gives back `None` too:

```python
names = ["Ada", "Grace", "Alan"]
names.reverse()
print(names)
```

Output:

```
['Alan', 'Grace', 'Ada']
```

### Practice

5. Predict what this prints, then press Check.

```python
ages = [13, 9, 11]
in_order = sorted(ages)
print(ages)
print(in_order)
ages.sort()
ages.reverse()
print(ages)
```

6. This program should sort the scores, then print the lowest, 79. It stops with an error. Run it and read the last line of the error. (`NoneType` is Python's name for the kind of value `None` is; you don't need to remember it.) Then fix it.

```python
scores = [88, 92, 79]
scores = scores.sort()
print(scores[0])
```

7. This function should give back the scores in order, and leave the caller's list as it was. Run it: the second line shows that `marks` was sorted too, because inside the function, `scores` is a second name for the same list (lesson 7.3). Fix the function, so that the program prints `[79, 88, 92]`, then `[88, 92, 79]`.

```python
def in_order(scores):
    scores.sort()
    return scores

marks = [88, 92, 79]
print(in_order(marks))
print(marks)
```

> Split it: which way of sorting makes a new list, and leaves the old one alone?

8. Ask for four words, one at a time, and put them in a list. Then print the list in alphabetical order.

> Check it: try pear, apple, fig and kiwi. The list should start with apple and end with pear.

### Try It

9. Write a function `average(numbers)` that gives back the average of a list of numbers. For an empty list, it gives back 0.

> Say it: a list of numbers goes in; their average comes out, and an empty list gives 0. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. if the list is empty, give back 0. 2. otherwise, add up the numbers, divide by how many there are, and give that back.
> Name it: the function and its parameter are named for you. What would you call the total, if you store it first?
> Check it: try `[88, 92, 79, 95]`, which gives 88.5. Then the awkward one: `[]`. What happens if you leave out step 1?

### What you can do now

- Ask how many items a list has, and their total, largest and smallest.
- Check what happens with an empty list.
- Sort into a new list with `sorted()`, or sort the list itself with `sort()`.

Key words: **len**, **sorted**, **sort**.
