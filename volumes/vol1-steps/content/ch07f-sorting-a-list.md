<!-- part: Unit 7 — Lists -->
## Lesson 7.6 — Sorting a list

In this lesson you put a list in order, in two different ways: into a new list, or by changing the list itself. Telling the two apart matters, and the practices show why.

### Warm-up

1. Predict what this prints, then press Check.

```python
points = [7, 2, 9, 4]
print(len(points))
print(sum(points))
print(max(points) - min(points))
```

2. What does `max(empty)` do, when `empty` is `[]`?

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

### Practice

3. Ask for four words, one at a time, and put them in a list. Then print the list in alphabetical order.

> Check it: try pear, apple, fig and kiwi. The list should start with apple and end with pear.

### Changing the list itself

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

4. Predict what this prints, then press Check.

```python
ages = [13, 9, 11]
in_order = sorted(ages)
print(ages)
print(in_order)
ages.sort()
ages.reverse()
print(ages)
```

5. This program should sort the scores, then print the lowest, 79. It stops with an error. Run it and read the last line of the error. (`NoneType` is Python's name for the kind of value `None` is; you don't need to remember it.) Then fix it.

```python
scores = [88, 92, 79]
scores = scores.sort()
print(scores[0])
```

6. This function should give back the scores in order, and leave the caller's list as it was. Run it: the second line shows that `marks` was sorted too, because inside the function, `scores` is a second name for the same list (lesson 7.3). Fix the function, so that the program prints `[79, 88, 92]`, then `[88, 92, 79]`.

```python
def in_order(scores):
    scores.sort()
    return scores

marks = [88, 92, 79]
print(in_order(marks))
print(marks)
```

> Split it: which way of sorting makes a new list, and leaves the old one alone?

### Try It

7. Write a function `second_largest(numbers)` that gives back the second-largest number in a list, without changing the list. Count from the top of the sorted list, so in `[4, 9, 9]` it is 9. A list with fewer than two numbers has no second-largest: give back `None`.

> Say it: a list of numbers goes in; the number just below the top of it, in order, comes out, or `None` if there is no such number. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. if the list has fewer than two numbers, give back `None`. 2. make a sorted copy of the list. 3. give back its second item from the end.
> Name it: the function and its parameter are named for you. What would you call the sorted copy?
> Check it: try `[3, 9, 5]`, which gives 5. Then the awkward ones: `[]` and `[7]`, which give `None`; and numbers below 0, like `[-1, -5, -3]`, which gives -3.

### What you can do now

- Sort into a new list with `sorted()`, and keep the old one as it was.
- Sort or reverse the list itself with `sort()` and `reverse()`, which give back `None`.
- Choose the one that leaves the caller's list alone, when a function gets a list.

Key words: **sorted**, **sort**, **reverse**.
