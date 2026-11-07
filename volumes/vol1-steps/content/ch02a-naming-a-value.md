<!-- part: Unit 2 — Variables and types -->
## Lesson 2.1 — Naming a value

In this lesson you give a value a name, change it, and follow a program line by line to see what it does.

### Warm-up

1. Predict what this prints, then press Check.

```python
print("2 + 2", 2 + 2)
```

2. What does Python do with a line that starts with `#`?

### A name for a value

A **variable** is a name for a value. You make one with `=`:

```python
price = 12
print(price)
```

Output:

```
12
```

The `=` here is not "equals" from math. It means: let the name on the left stand for the value on the right. Read `price = 12` as "let price be 12". The name always goes on the left. After that line, writing `price` gives you 12.

A program can have as many variables as it needs, and you can do arithmetic with them:

```python
price = 12
count = 3
print(price * count)
```

Output:

```
36
```

A variable can hold text, too:

```python
player = "Ada"
print("Hello,", player)
```

Output:

```
Hello, Ada
```

### Practice

3. Store `7` in a variable called `days`, then print how many hours that is: `days` times 24.
4. This program stops with an error. Run it and read the last line of the error. Then fix it so it prints 5.

```python
print(total)
total = 5
```

### Changing a value

A name can be pointed at a new value. The old value is forgotten.

```python
score = 10
score = 20
print(score)
```

Output:

```
20
```

A variable can even get its new value from its old one:

```python
count = 5
count = count + 1
print(count)
```

Output:

```
6
```

Python works out the right side first: `count` is 5, so `count + 1` is 6. Only then does it point `count` at the answer.

You can follow a program on paper with a **trace table**: one row per line, showing the value of each variable after that line. Here is the trace table for the program above.

| After line | count |
| --- | --- |
| 1 | 5 |
| 2 | 6 |
| 3 | 6 |

Line 3 only prints, so nothing changes. Tracing by hand is how you check what a program does before you run it.

One more, with two variables:

```python
a = 10
b = a
a = 99
print(a, b)
```

Output:

```
99 10
```

`b = a` gave `b` the value 10 at that moment. Changing `a` afterward does not change `b`: `b` does not follow `a` around. Its trace table has a column for each variable. After line 1, `b` has no value yet, so its cell is left empty:

| After line | a | b |
| --- | --- | --- |
| 1 | 10 |  |
| 2 | 10 | 10 |
| 3 | 99 | 10 |
| 4 | 99 | 10 |

### Practice

5. Fill in the table: the value of `lives` after each line. Then press Check.

```python
lives = 3
lives = lives - 1
lives = lives + 2
```

6. Fill in the table for two variables. As in the table for `a` and `b`, leave a cell empty (or write -) while a variable has no value yet. Then press Check.

```python
price = 12
count = 3
price = price + count
```

### Try It

7. A game gives you 5 coins. You spend 2, then find 4 more. Use one variable, and print how many coins you have at the end.

> Say it: what happens to the coins, in your own words? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: one step for each thing that happens: start with 5, spend 2, find 4, print.

### What you can do now

- Give a value a name.
- Change it, even from its own old value.
- Trace a program line by line.

Key words: **variable**, **trace table**.
