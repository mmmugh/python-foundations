<!-- part: Unit 10 — Tuples and records -->
## Lesson 10.1 — Tuples, and unpacking

A point on a grid has two parts, x and y. A list could hold them, but a list can change, and the parts of a point belong together. In this lesson you meet the tuple, a list that cannot change, and a neat way to give each of its parts a name of its own.

### Warm-up

1. Predict what this prints, then press Check.

```python
scores = {"Ada": 88, "Grace": 92}
for name, score in scores.items():
    print(name, score)
print(sorted(scores, key=scores.get, reverse=True))
```

2. A list holds a point: `point = [3, 4]`. What does `point[0] = 5` do?

### A list that cannot change

A **tuple** is an ordered collection, like a list, that cannot change once it is made. You write it with round brackets instead of square ones:

```python
point = (3, 4)
color = (255, 128, 0)
print(point)
print(point[0])
print(len(color))
print(color[1:])
print(128 in color)
for value in color:
    print(value)
```

Output:

```
(3, 4)
3
3
(128, 0)
True
255
128
0
```

Indexing, slicing, `len()`, `in` and `for` all work as they do for a list. A slice of a tuple is a tuple. The one thing you cannot do is change it:

```python
point = (3, 4)
point[0] = 5
```

It stops, and the last line of the error says `TypeError: 'tuple' object does not support item assignment`. Item assignment is Python's name for storing a value at a position with `=`; you don't need to remember it.

To move the point, make a new tuple and store it under the same name. The old tuple was never changed; the name now holds a different one:

```python
point = (3, 4)
point = (5, point[1])
print(point)
```

Output:

```
(5, 4)
```

Why have a list that cannot change? Because it tells whoever reads your code: these values belong together, and they stay as they are. A point, a color, a date: each is one thing with parts, not a collection you will add to or take from. And a function you hand a tuple to cannot change it behind your back, as a function could sort a list it was handed in lesson 7.6.

### Practice

3. Predict what this prints, then press Check.

```python
rgb = (255, 128, 0)
print(rgb[2])
print(len(rgb))
print(0 in rgb)
print(rgb[:2])
for number in rgb:
    print(number // 100)
```

4. This program should move the point 5 to the right and print `(8, 4)`, but it stops with an error. Run it and read the last line of the error. Then fix it by making a new tuple.

```python
point = (3, 4)
point[0] = point[0] + 5
print(point)
```

5. Which of these fits a tuple best?

### Unpacking

Put several names on the left of `=`, with commas between, and each one gets one of the tuple's values, in order. This is called **unpacking**:

```python
point = (3, 4)
x, y = point
print(x)
print(y)
```

Output:

```
3
4
```

You have done this already: `for name, score in scores.items():` unpacks each pair as the loop goes, and so does `for position, name in enumerate(names):` in lesson 7.7.

Anything with the right number of values unpacks: a tuple, a list, or the list `split()` gives back:

```python
full_name = "Ada Lovelace"
first, last = full_name.split()
print(last + ", " + first)
```

Output:

```
Lovelace, Ada
```

The number of names must match the number of values:

```python
day, month = "9 11 2026".split()
```

It stops, and the last line of the error says `ValueError: too many values to unpack`, then how many names it expected. There are three values and two names. Too few values is a `ValueError` too.

On the right of `=`, values with commas between make a tuple, even without brackets. So one line can give two names their values. Python works out the whole right side first, and only then unpacks it into the names on the left:

```python
width, height = 8, 5
print(width * height)
```

Output:

```
40
```

### Practice

6. Predict what this prints, then press Check.

```python
date = (9, 11, 2026)
day, month, year = date
print(month)
first, last = "Grace Hopper".split()
print(first)
low, high = 10, 25
print(high - low)
```

7. This line stops with a `ValueError`. Why?

```python
first, last = "Ada King Lovelace".split()
```

8. Write a program that asks for a full name, a first name and a last name with a space between, like `Ada Lovelace`, and prints it last name first, like `Lovelace, Ada`. Unpack the split into two names.

> Split it: ask for the name. Use `split()` on it, and unpack the two words into two names. Print the last name, a comma and a space, and the first name.
> Check it: try `Ada Lovelace`, which prints `Lovelace, Ada`. Then `Grace Hopper`.

### Try It

9. Write a program that asks for two whole numbers, one after the other, and prints them on one line with a space between, the smaller first. So 7 then 3 prints `3 7`. If the first number is bigger, swap the two names' values in one line, by unpacking, before you print.

> Say it: two numbers go in; they come out on one line, the smaller first. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. ask for the two numbers. 2. if the first is bigger than the second, swap them in one line: the two names on the left of `=`, and the same two names the other way round on the right. 3. print them both.
> Name it: what would you call the number typed first, and the number typed second?
> Check it: try 7 then 3, which prints `3 7`, and 2 then 9, which prints `2 9`. Then the awkward ones: 5 and 5, which prints `5 5`; -4 then 1, which prints `-4 1`; and 9 then 10, which prints `9 10` only if you compare them as numbers, not as text.

### What you can do now

- Make a tuple and read it like a list, knowing it cannot change.
- Unpack a tuple, a list or a split into names, one value each.
- Swap two values in one line.

Key words: **tuple**, **unpacking**.
