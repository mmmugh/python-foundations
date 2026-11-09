<!-- part: Unit 7 — Lists -->
## Lesson 7.6 — Looping over a list

In lesson 5.3, a `for` loop stepped through a string, one character at a time. In this lesson it steps through a list, one item at a time: to build a new list from an old one, and to know where each item is.

### Warm-up

1. Predict what this prints, then press Check.

```python
points = [4, 9, 2]
print(len(points))
print(sum(points))
print(sorted(points))
print(points)
```

2. What does `scores.sort()` give back?

### One item at a time

Put a list where the string was:

```python
scores = [88, 92, 79, 95]
for score in scores:
    print(f"Score: {score}")
```

Output:

```
Score: 88
Score: 92
Score: 79
Score: 95
```

On each pass, `score` holds the next item, starting from index 0. Four items, four passes. The list is called `scores` and one item `score`: a plural name for the list and the singular for one item reads well.

### Practice

3. Predict what this prints, then press Check.

```python
prices = [3, 5, 2]
total = 0
for price in prices:
    total += price
    print(total)
```

### Building a new list

Start with an empty list, and `append()` to it inside the loop (lesson 7.3). Here each temperature in Celsius becomes one in Fahrenheit:

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

With an `if` inside the loop, only some items go into the new list:

```python
scores = [88, 92, 45, 95, 58, 71]
passing = []
for score in scores:
    if score >= 60:
        passing.append(score)
print(passing)
print(len(passing), "of", len(scores), "passed")
```

Output:

```
[88, 92, 95, 71]
4 of 6 passed
```

In both, the old list is left as it was.

### Practice

4. Write a function `evens(numbers)` that gives back a new list of only the even numbers in `numbers`, in the same order.

> Split it: start from `passing` above. What does the `if` ask instead? (An even number divides by 2 with nothing left over.)
> Check it: try `[1, 2, 3, 4]`, which gives `[2, 4]`. Then the awkward ones: `[]`, and `[0, -2, 3]`, where 0 and -2 are both even.

5. Write a function `count_above(numbers, threshold)` that gives back how many numbers in the list are above `threshold`.

> Check it: try `[3, 8, 5, 10]` with 5, which gives 2: 5 is not above 5. Then the awkward ones: `[]`, and a threshold of 0.

### Don't change a list while you loop over it

This loop tries to take every 2 out of the list, but one gets away:

```python
numbers = [1, 2, 2, 3]
for number in numbers:
    if number == 2:
        numbers.remove(number)
print(numbers)
```

Output:

```
[1, 2, 3]
```

The loop goes through the list by position. At index 1 it finds a 2, and removes it. Every item after it moves back one place, so the second 2 moves into index 1, which the loop has just looked at. Next it looks at index 2, which now holds 3, and the second 2 is never seen.

So never add to or take out of a list while a loop is going through it. Build a new list instead:

```python
numbers = [1, 2, 2, 3]
kept = []
for number in numbers:
    if number != 2:
        kept.append(number)
print(kept)
```

Output:

```
[1, 3]
```

### Practice

6. Predict what this prints, then press Check.

```python
marks = [5, 5, 6]
for mark in marks:
    if mark == 5:
        marks.remove(mark)
print(marks)
```

### Where each item is

Sometimes you need each item's index as well. `range(len(names))` gives every index of `names`, and `names[i]` is the item there:

```python
names = ["Ada", "Grace", "Alan"]
for i in range(len(names)):
    print(i + 1, names[i])
```

Output:

```
1 Ada
2 Grace
3 Alan
```

`i + 1` turns index 0 into the 1 people expect at the top of a numbered list.

`enumerate()` does the same job more neatly. Each time round, it gives the index and then the item, and the `for` line names both, with a comma between:

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

When you only need the items, `for name in names:` is clearest. Use an index only when the loop needs it.

### Practice

7. Predict what this prints, then press Check.

```python
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, color)
print("Done")
```

8. You want to print every name in `names`, and nothing else. Which loop is clearer?

### Try It

9. Write a function `positions(items, target)` that gives back a list of every index where `target` appears in `items`. If it is not there at all, it gives back an empty list.

> Say it: a list and a value go in; a list of the indexes where that value sits comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start with an empty list of indexes. 2. loop over the items, with their indexes. 3. if an item is the target, append its index. 4. after the loop, give back the list of indexes.
> Name it: the function and its parameters are named for you. What would you call the list you build? And the two loop variables?
> Check it: try `["a", "b", "a"]` with `"a"`, which gives `[0, 2]`. Then the awkward ones: `[]`, and a target that is not in the list.

### What you can do now

- Step through a list with `for`, one item at a time.
- Build a new list from an old one, keeping all its items or only some.
- Loop with each item's index too, with `range(len())` or `enumerate()`.

Key words: **enumerate**.
