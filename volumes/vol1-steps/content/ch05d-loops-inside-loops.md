<!-- part: Unit 5 — Repetition -->
## Lesson 5.4 — Loops inside loops

A loop's block can hold any lines you like: an `if`, as in lesson 5.3, or even another loop. In this lesson you put one loop inside another, and choose names that keep the two apart.

### Warm-up

1. Predict what this prints, then press Check.

```python
for letter in "hey":
    print(letter * 2)
```

2. Predict what this prints, then press Check.

```python
count = 0
for letter in "level":
    if letter == "e" or letter == "l":
        count += 1
print(count)
```

### A loop inside a loop

Here are the 1, 2 and 3 times tables, up to 3 times each:

```python
for table in range(1, 4):
    for times in range(1, 4):
        print(f"{table} x {times} = {table * times}")
```

Output:

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

The inner loop runs all the way through on every pass of the outer loop. On the outer loop's first pass, `table` is 1, and the inner loop makes its three passes, with `times` at 1, 2 and 3. Then the outer loop moves `table` on to 2, and the inner loop starts again from 1. Three outer passes, each with three inner passes, make nine lines. A loop inside a loop is called a **nested loop**, like the nested `if` in lesson 4.3.

The inner loop's block is indented twice. A line indented once belongs to the outer loop only, so it runs once per outer pass:

```python
for row in range(1, 3):
    print(f"Row {row}:")
    for seat in range(1, 4):
        print(f"seat {seat}")
```

Output:

```
Row 1:
seat 1
seat 2
seat 3
Row 2:
seat 1
seat 2
seat 3
```

### Practice

3. Predict what this prints, then press Check.

```python
for outer in range(2):
    print("Outer", outer)
    for inner in range(3):
        print(inner)
```

4. How many lines does this print?

```python
for first in range(4):
    for second in range(5):
        print(first + second)
```

### When the inner loop depends on the outer

The inner loop can use the outer loop's variable. Here, each row has as many seats as its number:

```python
for row in range(1, 4):
    for seat in range(1, row + 1):
        print(f"Row {row}, seat {seat}")
```

Output:

```
Row 1, seat 1
Row 2, seat 1
Row 2, seat 2
Row 3, seat 1
Row 3, seat 2
Row 3, seat 3
```

The inner `range()` is different on each pass: `range(1, 2)` for row 1, `range(1, 4)` for row 3. Its stop is `row + 1`, because `range()` leaves its stop out.

### Practice

5. Predict what this prints, then press Check.

```python
for size in range(1, 4):
    for step in range(size):
        print(size)
```

### Names for loop variables

You choose the name after `for`. Many programs use `i` for a counting loop, and that is fine for a short one. With two loops, though, `i` and `j` say nothing about which is which. `table` and `times`, or `row` and `seat`, tell the reader what each one holds.

A loop variable is still there after the loop, holding its last value:

```python
for number in range(1, 4):
    print(number)
print(f"After the loop, number is {number}")
```

Output:

```
1
2
3
After the loop, number is 3
```

That is rarely what you meant to use. A value you want after the loop, like lesson 5.3's count, belongs in a variable of its own.

### Practice

6. This prints a grid of squares, like a chessboard. Which names make it easiest to read?

```python
for i in range(8):
    for j in range(8):
        print(i, j)
```

7. Predict what this prints, then press Check.

```python
for letter in "dog":
    print(letter)
print(letter)
```

### Try It

8. Two dice each show a number from 1 to 6. Ask for a total, then print every pair of dice that makes it, one pair per line, like `3 + 4`, with the first die first.

> Say it: a total goes in; every pair of dice that adds up to it comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the total, as a whole number; loop over the first die, 1 to 6; inside that, loop over the second die, 1 to 6; if the two add up to the total, print the pair.
> Name it: there are two loop variables, one for each die. What would you call them?
> Check it: try 7, which has six pairs. Then the awkward ones: 2 and 12, which have one pair each, and 13, which has none.

### What you can do now

- Put a loop inside another loop, and say how many times its block runs.
- Make the inner loop depend on the outer loop's variable.
- Name loop variables for what they hold.

Key words: **nested loop**, **outer loop**, **inner loop**.
