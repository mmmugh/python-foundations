<!-- part: Unit 5 — Repetition -->
## Lesson 5.1 — Repeating with while

So far, each line of a program runs once, or not at all. In this lesson your programs repeat lines: the same block, again and again, for as long as a condition stays `True`.

### Warm-up

1. Predict what this prints, then press Check.

```python
count = 1
count += 1
count += 1
print(count)
```

2. `count` holds 6. Which condition is `True`?

### Doing it again

To print 1, 2 and 3, you could write three `print()` lines. To print 1 to 100, you would need a hundred. A `while` loop runs the same lines again and again instead:

```python
count = 1
while count <= 3:
    print(count)
    count += 1
print("Done.")
```

Output:

```
1
2
3
Done.
```

`while` looks like `if`: a condition, a colon, and an indented block. The difference comes at the end of the block. After an `if` block, Python goes on to the next line. After a `while` block, Python goes back up and asks the question again. When the answer is `False`, it skips the block and goes on to the line after it.

Here, `count` starts at 1. Each time through the block, the program prints `count` and adds 1 to it. After it prints 3, `count` becomes 4. `4 <= 3` is `False`, so the loop ends and `Done.` is printed. Each time through the block is called a **pass**. This loop makes three passes.

To count higher, change one number:

```python
count = 1
while count <= 6:
    print(count)
    count += 1
print("Done.")
```

Output:

```
1
2
3
4
5
6
Done.
```

The count can move by more than 1 each pass. This one counts in twos:

```python
count = 2
while count <= 10:
    print(count)
    count += 2
```

Output:

```
2
4
6
8
10
```

A loop like these has three parts:

1. A variable set up before the loop: `count = 2`.
2. A condition that becomes `False` sooner or later: `count <= 10`.
3. A line in the block that moves the variable toward that: `count += 2`.

### Practice

3. Predict what this prints, then press Check.

```python
number = 5
while number <= 20:
    print(number)
    number += 5
print("Finished.")
```

4. Change this program so that it prints the numbers 1 to 10, one per line.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Tracing a loop

In a trace table, a line gets a row each time it runs. In a loop, the same lines run on every pass, so their line numbers come round again. This loop doubles `number` three times:

```python
count = 1
number = 1
while count <= 3:
    number *= 2
    count += 1
```

| After line | count | number |
| --- | --- | --- |
| 1 | 1 |  |
| 2 | 1 | 1 |
| 3 | 1 | 1 |
| 4 | 1 | 2 |
| 5 | 2 | 2 |
| 3 | 2 | 2 |
| 4 | 2 | 4 |
| 5 | 3 | 4 |
| 3 | 3 | 4 |
| 4 | 3 | 8 |
| 5 | 4 | 8 |
| 3 | 4 | 8 |

Lines 3, 4 and 5 come round three times, once for each pass. Line 3 gets one more row than the others: the fourth time Python asks, `4 <= 3` is `False`, and the loop ends there.

### Practice

5. Fill in the table, then press Check. The loop's lines come round, so the same line numbers appear more than once.

```python
passes = 0
coins = 10
while coins > 4:
    coins -= 2
    passes += 1
```

### When a loop never ends

Leave out the third part, the line that moves the variable, and the condition never becomes `False`. The loop runs forever. This is called an **infinite loop**, and every programmer writes one sooner or later. On this page, a program that runs for more than 5 seconds is stopped for you, with an error that ends `this looks like a loop that never ends`.

### Practice

6. This program should double `number` three times and print 8, but it never stops. Run it, and after 5 seconds read the last line of the error. (`KeyboardInterrupt` is Python's name for a program being stopped from outside; you don't need to remember it.) Then fix it.

```python
count = 1
number = 1
while count <= 3:
    number *= 2
print(number)
```

### Try It

7. Count down: print 5, 4, 3, 2 and 1, one per line, then `Liftoff!`

> Say it: numbers go down from 5 to 1, and then one word. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: before the loop, set a variable to 5; loop while it is 1 or more; in the block, print it, then take 1 away; after the loop, print Liftoff!
> Name it: what would you call the number that counts down?
> Check it: does it stop? Is the last number 1, and not 0?

### What you can do now

- Repeat a block with `while`, for as long as its condition is `True`.
- Trace a loop, with a row each time a line runs.
- Spot a loop that never ends, and fix it.

Key words: **while**, **loop**, **pass**, **infinite loop**.
