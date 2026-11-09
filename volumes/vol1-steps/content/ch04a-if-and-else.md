<!-- part: Unit 4 — Making decisions -->
## Lesson 4.1 — If, and else

Every program so far has done the same thing every time it ran. In this lesson your programs make a choice: they run some lines only when the answer to a question is `True`, and other lines when it is `False`.

### Warm-up

1. Predict what this prints, then press Check.

```python
temperature = 95
print(temperature > 90)
print(temperature > 100)
```

2. `points` holds 40. Which one asks whether `points` is at least 50?

### Doing something only sometimes

Here is a program that makes a choice:

```python
temperature = 95
if temperature > 90:
    print("It is hot out.")
    print("Bring water.")
print("Have a good day.")
```

Output:

```
It is hot out.
Bring water.
Have a good day.
```

Change the first line to `temperature = 70`, and two lines vanish:

```python
temperature = 70
if temperature > 90:
    print("It is hot out.")
    print("Bring water.")
print("Have a good day.")
```

Output:

```
Have a good day.
```

An `if` has three parts, and Python is strict about all of them:

1. The word `if`, then a **condition**: a question whose answer is `True` or `False`, like the comparisons in lesson 3.5.
2. A colon, `:`, at the end of the line.
3. A **block**: the lines underneath, pushed in by four spaces. Pushing a line in like this is called **indenting** it. The block runs only when the condition is `True`.

The last line is not indented, so it is not part of the block. It runs either way.

On this page, pressing Tab in a code box puts in four spaces for you. Some editors put in a tab character instead, and mixing tabs and spaces in one program makes Python stop with a `TabError`, so stick to spaces.

A trace table shows the choice too. In this program the condition is `False`, so line 4 never runs, and it gets no row:

```python
points = 40
bonus = 0
if points >= 50:
    bonus = 10
points = points + bonus
```

| After line | points | bonus |
| --- | --- | --- |
| 1 | 40 |  |
| 2 | 40 | 0 |
| 3 | 40 | 0 |
| 5 | 40 | 0 |

Line 3 asks the question and changes nothing. The answer is `False`, so Python jumps past the block to line 5.

### Practice

3. Predict what this prints, then press Check. Look carefully at which lines are indented.

```python
lives = 0
if lives > 0:
    print("Keep playing.")
    print("Good luck.")
print("Thanks for playing.")
```

4. Fill in the table, then press Check. One line is skipped, so it has no row.

```python
price = 12
age = 70
if age < 5:
    price = 0
if age >= 65:
    price = 8
```

### When the shape is wrong

Leave out the colon, and Python cannot make sense of the program at all:

```python
score = 75
if score >= 50
    print("You passed.")
```

Python responds with something like:

```
SyntaxError: expected ':'
```

Forget to indent the block, and Python cannot tell which lines belong to the `if`:

```python
score = 75
if score >= 50:
print("You passed.")
```

Python responds with something like:

```
IndentationError: expected an indented block after 'if' statement on line 2
```

A condition asks a question, so it needs `==`. One `=` stores, and Python refuses it here:

```python
score = 90
if score = 90:
    print("Top marks!")
```

Python responds with something like:

```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Python guesses well: `==` is the one you want. (`:=` is something else, which you don't need.) As in lesson 1.3, read each error from the bottom. The last line says what Python expected.

### Practice

5. Which `if` line is written correctly?
6. Python says `IndentationError: expected an indented block`. What needs fixing?

### Otherwise: else

Often you want one thing to happen when the answer is `True`, and something else when it is `False`. `else` gives the second block:

```python
age = int(input("Your age: "))
if age >= 18:
    print("You can vote.")
else:
    print(f"You can vote in {18 - age} years.")
```

A sample run:

```
Your age: 15
You can vote in 3 years.
```

`else` has no condition of its own. It means "in every other case", so the colon comes straight after the word. `else` lines up with its `if`, and its block is indented like the `if`'s block. Exactly one of the two blocks runs, every time.

### Practice

7. Predict what this prints, then press Check.

```python
temperature = 12
if temperature >= 20:
    print("T-shirt weather.")
else:
    print("Bring a jacket.")
print("Have fun.")
```

8. This program stops with an error when you type 14. Run it, type 14, and read the last line of the error. ("Instances of" is Python's way of saying "values of"; you don't need to remember it.) Then fix it.

```python
age = input("How old are you? ")
if age > 12:
    print("You are a teenager or older.")
else:
    print("You are 12 or younger.")
```

### Try It

9. Ask for a test score, as a whole number. Print `Pass` if it is 50 or more, and `Fail` if it is not.

> Say it: a score goes in, and one of two words comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the score, as a whole number; ask whether it is 50 or more; if it is, print Pass; otherwise, print Fail.
> Name it: what would you call the score?
> Check it: try 75, then 30. Then the awkward ones: exactly 50, and 0.

### What you can do now

- Run some lines only when a condition is `True`, with `if`.
- Choose between two blocks with `if` and `else`.
- Read the errors a missing colon, a missing indent or a single `=` cause.

Key words: **if**, **condition**, **block**, **indent**, **else**.
