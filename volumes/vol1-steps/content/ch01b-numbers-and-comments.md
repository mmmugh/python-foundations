<!-- part: Unit 1 — Your first programs -->
## Lesson 1.2 — Numbers and comments

In this lesson Python does arithmetic for you, and you learn to leave notes in a program for the people who read it.

### Warm-up

1. Predict what this prints, then press Check.

```python
print("Hello")
print()
print("See", "you")
```

2. Which line prints `It's sunny` without an error?

### Numbers

A number does not need quotes:

```python
print(7)
```

Output:

```
7
```

Without quotes, Python works out a calculation first, then prints the answer:

```python
print(3 + 4)
```

Output:

```
7
```

Python has an operator for each kind of arithmetic. `*` multiplies and `/` divides:

```python
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 / 4)
```

Output:

```
14
6
40
2.5
```

Dividing with `/` always gives a number with a decimal point, even when it comes out exact: `8 / 2` prints `4.0`.

A calculation can use more than two numbers:

```python
print(2 * 3 * 4)
```

Output:

```
24
```

### Practice

3. Fifteen cookies are shared equally between 4 friends. Make Python work out how many cookies each friend gets.
4. There are 7 days in a week, 24 hours in a day, and 60 minutes in an hour. Make Python work out the number of minutes in a week. Use a calculation, not the answer.

### A value, or text about it

Quotes make a big difference. Look carefully at these two lines:

```python
print(3 + 4)
print("3 + 4")
```

Output:

```
7
3 + 4
```

Without quotes, `3 + 4` is a calculation. Python works it out and prints its **value**, 7. With quotes, `"3 + 4"` is a string: text that describes the calculation, printed exactly as written.

A comma lets you print both on one line, the text and then the value:

```python
print("3 + 4 =", 3 + 4)
```

Output:

```
3 + 4 = 7
```

### Practice

5. Predict what this prints, then press Check.

```python
print("6 * 7")
print(6 * 7)
```

6. Print `12 / 5 =` followed by the answer, worked out by Python, all on one line.

### Comments

A line that starts with `#` is a **comment**. Python skips it completely. A comment is a note for the people who read the code, including you, a few weeks from now.

```python
# hours in a week
print(24 * 7)
```

Output:

```
168
```

Python really does skip it. The first line here looks like code, but the `#` turns it into a comment:

```python
# print("This line never runs.")
print("This one does.")
```

Output:

```
This one does.
```

A comment can also go at the end of a line of code. Everything from the `#` onward is skipped:

```python
print(26.2 * 1.609)  # a marathon is 26.2 miles; a mile is 1.609 km
```

Output:

```
42.1558
```

A good comment says what the code alone does not: here, what 26.2 and 1.609 are. A comment that only repeats the code, like `# multiply`, adds nothing.

### Practice

7. Predict what this prints, then press Check.

```python
# print("one")
print("two")  # print("three")
```

### Try It

8. A bus has 12 rows of 4 seats. Print how many seats one bus has. Then, on the next line, print how many seats 3 of those buses have. Put a comment above each line that says what it works out.

> You need two `print()` lines, each with a calculation inside, and a comment above each one.
> One bus has 12 times 4 seats. Three buses have 3 times as many, so the second calculation multiplies three numbers.

### What you can do now

- Let Python do arithmetic with `+`, `-`, `*` and `/`.
- Tell a value, like `7`, from text that describes it, like `"3 + 4"`.
- Leave notes for readers in `#` comments.

Key words: **value**, **comment**.
