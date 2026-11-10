<!-- part: Unit 10 — Tuples and records -->
## Lesson 10.2 — Giving back two values

A function gives back one value. But some answers come in two parts: 500 seconds is 8 minutes and 20 seconds. In this lesson a function gives back both parts at once, as a tuple, and you unpack them where you call it. Then you work with points, and find the distance between two of them.

### Warm-up

1. Predict what this prints, then press Check.

```python
color = (255, 128, 0)
red, green, blue = color
print(green)
print(color[-1])
```

2. `size = (1920, 1080)` is a tuple. Which of these lines stops with an error?

3. Fill in the table, then press Check.

```python
a = 1
b = 2
a, b = b, a
```

### Two values from one function

Put two values after `return`, with a comma between:

```python
def split_time(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds


print(split_time(500))
minutes, seconds = split_time(500)
print(f"{minutes} minutes and {seconds} seconds")
```

Output:

```
(8, 20)
8 minutes and 20 seconds
```

`return minutes, seconds` still gives back one value: a tuple of two. The comma makes the tuple, as it did on the right of `=` in lesson 10.1. Where you call the function, unpack the tuple into two names.

Here is one more, with `type()` to show what comes back:

```python
def lowest_and_highest(numbers):
    return min(numbers), max(numbers)


result = lowest_and_highest([5, 2, 9, 1])
print(result)
print(type(result))
low, high = lowest_and_highest([5, 2, 9, 1])
print(f"from {low} to {high}")
```

Output:

```
(1, 9)
<class 'tuple'>
from 1 to 9
```

Since it is the comma that makes a tuple, not the brackets, a tuple of one item needs a comma too: `(5,)`. Without it, `(5)` is just the number 5 in brackets, as in arithmetic:

```python
print(type((5,)))
print(type((5)))
```

Output:

```
<class 'tuple'>
<class 'int'>
```

### Practice

4. Predict what this prints, then press Check.

```python
def halves(number):
    return number // 2, number % 2


print(halves(7))
whole, left_over = halves(10)
print(whole, left_over)
print(type((3,)))
print(type((3)))
```

5. Write a function `split_price(total_cents)` that gives back two values: the whole dollars, then the cents left over. So `split_price(1250)` gives back 12 and 50. Write it above these lines, which use it, then run them all.

```python
dollars, cents = split_price(1250)
print(dollars, cents)
print(split_price(99))
print(split_price(0))
```

> Split it: there are 100 cents in a dollar. `//` gives the whole dollars, and `%` the cents left over. Give back both, with a comma between.
> Check it: the lines print `12 50`, then `(0, 99)`, then the awkward one, `(0, 0)`.

6. Which of these is a tuple with one item in it?

### Points

A point is a natural tuple. A function can take two points and unpack each one into its x and y:

```python
def run_and_rise(start, end):
    x1, y1 = start
    x2, y2 = end
    return x2 - x1, y2 - y1


print(run_and_rise((1, 2), (4, 6)))
```

Output:

```
(3, 4)
```

To get from (1, 2) to (4, 6), you go 3 across and 4 up. The straight line between them is the long side of a right triangle whose other sides are 3 and 4. By Pythagoras, its length is the square root of 3 squared plus 4 squared. In Python, a power of 0.5 is a square root:

```python
print(25 ** 0.5)
print(2 ** 0.5)
across = 3
up = 4
print((across ** 2 + up ** 2) ** 0.5)
```

Output:

```
5.0
1.4142135623730951
5.0
```

`** 0.5` always gives back a float, even when the square root is a whole number.

### Practice

7. Predict what this prints, then press Check.

```python
def run_and_rise(start, end):
    x1, y1 = start
    x2, y2 = end
    return x2 - x1, y2 - y1


across, up = run_and_rise((2, 5), (8, 13))
print(across, up)
print((across ** 2 + up ** 2) ** 0.5)
print(16 ** 0.5)
```

8. Write a function `midpoint(start, end)` that gives back the point halfway between two points, as a tuple. Halfway between (0, 0) and (4, 6) is (2.0, 3.0). Write it above these lines, then run them all.

```python
print(midpoint((0, 0), (4, 6)))
print(midpoint((1, 1), (2, 2)))
print(midpoint((3, 5), (3, 5)))
print(midpoint((-4, 2), (4, -2)))
```

> Split it: unpack each point into its x and y, as `run_and_rise()` does. The x halfway is the two x values added and divided by 2, and the same for y. Give back both, with a comma between.
> Check it: the lines print `(2.0, 3.0)` and `(1.5, 1.5)`. Then the awkward ones: the same point twice gives that point, `(3.0, 5.0)`, and points either side of (0, 0) give `(0.0, 0.0)`.

### Try It

9. Write a function `distance(p1, p2)` that gives back the straight-line distance between two points. Write it above these lines, then run them all.

```python
print(distance((0, 0), (3, 4)))
print(distance((1, 2), (7, 10)))
print(distance((2, 3), (2, 3)))
print(distance((5, 5), (-7, 0)))
print(round(distance((0, 0), (1, 1)), 3))
```

> Say it: two points go in; the length of the straight line between them comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. unpack each point into its x and y. 2. work out how far across and how far up, as `run_and_rise()` does. 3. give back the square root of across squared plus up squared.
> Name it: the function and its parameters are named for you. What would you call the x and y of each point, and how far across and up?
> Check it: the first two lines print `5.0` and `10.0`. Then the awkward ones: the same point twice is `0.0` apart. From (5, 5) to (-7, 0), across and up are negative, -12 and -5; squaring makes them positive, so it is `13.0`. The last line prints `1.414`.

### What you can do now

- Give back two values from a function, as a tuple, and unpack them where you call it.
- Write a tuple of one item, with its comma.
- Work with points as tuples, and find a square root with `** 0.5`.

Key words: **square root**.
