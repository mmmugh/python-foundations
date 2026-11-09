<!-- part: Unit 3 — Expressions and operators -->
## Lesson 3.1 — More arithmetic

You already know `+`, `-`, `*` and `/`. In this lesson you meet three more arithmetic operators. Two of them work as a pair, and together they answer a question that comes up all the time.

### Warm-up

1. Predict what this prints, then press Check.

```python
print(7 / 2)
```

2. Fill in the table, then press Check.

```python
minutes = 90
hours = minutes / 60
```

### How many whole, how many left

Seventeen cookies are shared between 5 friends. `17 / 5` is 3.4, but nobody wants 0.4 of a cookie. What you really want to know is how many whole cookies each friend gets, and how many are left over.

`//` divides and keeps only the whole part:

```python
print(17 // 5)
```

Output:

```
3
```

5 goes into 17 three whole times, so each friend gets 3 cookies.

`%` gives what is left over, which is called the **remainder**:

```python
print(17 % 5)
```

Output:

```
2
```

Three 5s make 15, and 17 is 2 more than that, so 2 cookies are left.

The two work best as a pair, on the same two numbers. Here 50 eggs go into boxes of 12:

```python
eggs = 50
boxes = eggs // 12
left = eggs % 12
print(boxes, "boxes and", left, "eggs left over")
```

Output:

```
4 boxes and 2 eggs left over
```

`//` says how many whole boxes, and `%` says how many eggs are left. This pattern has a name in this course: **how many whole, how many left**. You will use it for time, money and anything else that comes in big pieces and small ones.

Here is its trace table. It has a column for each of the three variables:

| After line | eggs | boxes | left |
| --- | --- | --- | --- |
| 1 | 50 |  |  |
| 2 | 50 | 4 |  |
| 3 | 50 | 4 | 2 |
| 4 | 50 | 4 | 2 |

### Practice

3. Fill in the table, then press Check.

```python
marbles = 23
bags = marbles // 4
spare = marbles % 4
```

4. Print how many whole hours and how many minutes are left in 135 minutes. Use how many whole, how many left.

```python
minutes = 135
```

### Powers

`**` raises a number to a power. `2 ** 3` means three 2s multiplied together, 2 × 2 × 2:

```python
print(2 ** 3)
```

Output:

```
8
```

The number after `**` says how many times the first one is multiplied in:

```python
print(5 ** 2)
print(10 ** 3)
```

Output:

```
25
1000
```

### Practice

5. A square has sides of 9 cm. Store 9 in a variable, then use `**` to print the square's area.

### Check it: awkward numbers

Check it says to try an awkward value as well as an ordinary one. With `//`, two awkward values are worth knowing about.

A negative number:

```python
print(-17 // 5)
```

Output:

```
-4
```

`-17 / 5` is -3.4. `//` always rounds down, and for a negative number down means away from zero, so the answer is -4, not -3.

### Practice

6. Predict what this prints, then press Check. Work out the `/` answer first, then round it down.

```python
print(-7 // 2)
```

### Dividing by zero

The second awkward value is zero:

```python
print(17 // 0)
```

Python responds with something like:

```
ZeroDivisionError: division by zero
```

No number of 0s adds up to 17, so there is no answer, and Python stops. The same happens with `/` and `%`.

### Practice

7. A program works out `cookies // friends`. Which value of `friends` is the awkward one worth trying?

### Try It

8. Ask how many seconds something took, and print it as minutes and seconds. For example, 125 seconds is 2 minutes and 5 seconds.

> Say it: seconds go in; what comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the seconds as a whole number, work out the whole minutes, work out the seconds left, print both. It is how many whole, how many left again.
> Name it: what would you call the seconds typed in, the minutes, and the seconds left over?
> Check it: try 125, then 59, then 0. Does each answer make sense?

### What you can do now

- Work out how many whole with `//`, and how many left with `%`.
- Raise a number to a power with `**`.
- Check arithmetic with awkward numbers, like 0 and negatives.

Key words: **`//`**, **`%`**, **remainder**, **`**`**, **how many whole, how many left**.
