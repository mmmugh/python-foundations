<!-- part: Unit 5 — Repetition -->
## Lesson 5.2 — For, and range()

In lesson 5.1, counting with `while` took three parts: a variable, a condition, and a line to move the variable. Counting comes up so often that Python has a shorter way. In this lesson you count with a `for` loop and `range()`.

### Warm-up

1. Predict what this prints, then press Check.

```python
count = 3
while count <= 9:
    print(count)
    count += 3
```

2. A `while` loop is missing the line that moves its variable. What happens when it runs?

### Counting with for

Here is a `for` loop:

```python
for number in range(5):
    print(number)
```

Output:

```
0
1
2
3
4
```

`range(5)` gives five numbers: 0, 1, 2, 3 and 4. It starts at 0, and it stops just before 5. The `for` loop takes them one at a time. On each pass, `number` holds the next one, and the block runs. The `for` line does all three of `while`'s parts at once: it sets up `number`, knows when to stop, and moves `number` on.

The line has a shape of its own: `for`, a name of your choice, `in`, then `range()`, and a colon. The block is indented, as with `if` and `while`.

`range(n)` always gives exactly `n` numbers, so the block runs `n` times. Sometimes that is all you want, and the block never uses the number:

```python
for number in range(3):
    print("Hip hip hooray!")
```

Output:

```
Hip hip hooray!
Hip hip hooray!
Hip hip hooray!
```

### Practice

3. Predict what this prints, then press Check.

```python
for number in range(4):
    print(number * 10)
```

4. How many times does this print `Hi`?

```python
for number in range(4):
    print("Hi")
```

### Choosing where to start and stop

Give `range()` two numbers, and it starts at the first instead of 0:

```python
for number in range(2, 6):
    print(number)
```

Output:

```
2
3
4
5
```

The stop is still left out: `range(2, 6)` ends at 5. So to count from 1 to 10, you write `range(1, 11)`.

A third number is the step: how much to add each time. Without it, the step is 1.

```python
for number in range(0, 20, 5):
    print(number)
```

Output:

```
0
5
10
15
```

20 is the stop, so it is left out, even though the step would land on it.

A step below 0 counts down. Here is lesson 5.1's countdown, in three lines:

```python
for number in range(5, 0, -1):
    print(number)
print("Liftoff!")
```

Output:

```
5
4
3
2
1
Liftoff!
```

Counting down, the stop is still left out: the last number is 1, not 0. All four forms, side by side:

| Call | Gives |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 6)` | 2, 3, 4, 5 |
| `range(0, 20, 5)` | 0, 5, 10, 15 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

### Practice

5. Predict what this prints, then press Check.

```python
for number in range(3, 7):
    print(number)
```

6. Predict what this prints, then press Check.

```python
for number in range(1, 12, 4):
    print(number)
```

7. Predict what this prints, then press Check.

```python
for number in range(10, 0, -3):
    print(number)
```

8. Ask for a whole number, then print its times table from 1 to 12, one line each, like `7 x 1 = 7` up to `7 x 12 = 84`.

### Try It

9. Print the first 10 square numbers, one per line: 1, 4, 9, and so on, up to 100.

> Say it: the square of 1, the square of 2, and so on up to the square of 10, each on its own line. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: loop over the numbers 1 to 10; in the block, print the number times itself.
> Name it: what does the loop's variable hold on each pass?
> Check it: is the first line 1, and not 0? Is the last line 100?

### What you can do now

- Repeat a block a set number of times with `for` and `range()`.
- Choose where `range()` starts and stops, and the step between.
- Count down with a step below 0.

Key words: **for**, **range()**, **step**.
