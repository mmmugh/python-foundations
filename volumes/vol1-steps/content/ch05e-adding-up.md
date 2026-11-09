<!-- part: Unit 5 — Repetition -->
## Lesson 5.5 — Adding up as you go

In lesson 5.3, a counter went up by 1 each time a letter matched. The same idea can add up any amounts, build up a string, or remember the largest value so far. In this lesson your loops build up an answer as they go.

### Warm-up

1. Predict what this prints, then press Check.

```python
for row in range(1, 3):
    for seat in range(row):
        print(row)
```

2. After `for number in range(5):` has finished, what does `number` hold?

### Adding up

This adds up 1, 2 and 3:

```python
total = 0
for number in range(1, 4):
    total += number
print(total)
```

Output:

```
6
```

Here is its trace table. Line 2 gets a row each time `for` takes the next number, and one more at the end, when `range()` has none left. That is like the `while` line in lesson 5.1, which got one more row than the lines in its block.

| After line | number | total |
| --- | --- | --- |
| 1 |  | 0 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |
| 2 | 2 | 1 |
| 3 | 2 | 3 |
| 2 | 3 | 3 |
| 3 | 3 | 6 |
| 2 | 3 | 6 |
| 4 | 3 | 6 |

Change one number, and the same loop adds up 1 to 100:

```python
total = 0
for number in range(1, 101):
    total += number
print(f"1 to 100 add up to {total}.")
```

Output:

```
1 to 100 add up to 5050.
```

A variable that builds up an answer, pass by pass, is called an **accumulator**. It has three places in the program: it is set up before the loop, changed in the block, and used after the loop. Lesson 5.3's count was one.

An accumulator can build up a string too. It starts empty, as `""`:

```python
bar = ""
for step in range(4):
    bar += "#"
    print(bar)
```

Output:

```
#
##
###
####
```

### Practice

3. Fill in the table, then press Check.

```python
points = 0
for bonus in range(5, 20, 5):
    points += bonus
```

4. Predict what this prints, then press Check.

```python
line = ""
for number in range(1, 4):
    line += str(number)
print(line)
```

5. Predict what this prints, then press Check. Look at where `total` is set to 0.

```python
for number in range(1, 4):
    total = 0
    total += number
print(total)
```

### The largest so far

To find the largest of several numbers, keep the largest so far in a variable. Each pass compares the new number with it, and keeps the new one only if it is bigger:

```python
largest = 0
for turn in range(3):
    number = int(input("Number: "))
    if number > largest:
        largest = number
print(f"The largest was {largest}.")
```

A sample run:

```
Number: 4
Number: 9
Number: 2
The largest was 9.
```

It looks right. Now try it with numbers below 0:

```
Number: -5
Number: -2
Number: -8
The largest was 0.
```

Nobody typed 0. It won because it was there first, and no number below 0 can beat it. Numbers that are all below 0 are an edge case, as in lesson 4.5. The fix is to start from the first number typed. Before the loop, it is the only number so far, so it is the largest so far. The loop then reads the other two:

```python
largest = int(input("Number: "))
for turn in range(2):
    number = int(input("Number: "))
    if number > largest:
        largest = number
print(f"The largest was {largest}.")
```

A sample run:

```
Number: -5
Number: -2
Number: -8
The largest was -2.
```

### Practice

6. This program should print the coldest of three temperatures. Run it, and type 12, 8 and 15: it says the coldest was 0, which nobody typed. Fix it.

```python
coldest = 0
for day in range(3):
    temperature = int(input("Temperature: "))
    if temperature < coldest:
        coldest = temperature
print(f"The coldest was {coldest}.")
```

> Check it: try 12, 8 and 15. Then the ones below 0, like -3, -9 and -1.

### Try It

7. A game scores each round, and a round's points can be below 0. Ask for the points of 4 rounds. After the loop, print the total, then the highest round, like `Total: 20` and `Highest: 10`.

> Say it: four rounds of points go in; their total and the highest round come out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the first round's points: so far, that is both the total and the highest; loop over the other three rounds: ask for the points, add them to the total, and if they beat the highest, keep them; after the loop, print the total, then the highest.
> Name it: there are two accumulators. What would you call them?
> Check it: try 3, 5, 10 and 2. Then the awkward ones: all below 0, like -3, -8, -1 and -4; and all 0.

### What you can do now

- Add up as you go, with an accumulator set up before the loop.
- Build up a string the same way, starting from `""`.
- Keep the largest so far, starting from the first value, not from 0.

Key words: **accumulator**, **largest so far**.
