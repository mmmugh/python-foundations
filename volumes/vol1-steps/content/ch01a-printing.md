<!-- part: Unit 1 — Your first programs -->
## Lesson 1.1 — Printing

A **program** is a list of instructions that a computer follows, in order. The computer is fast and very literal: it does exactly what you wrote, even the parts you did not mean.

In this lesson you write your first programs. They all do one thing: show text on the screen. Every grey box on this page runs. Press Run to see what it does, and change anything you like.

### Printing a line

`print()` shows something on the screen.

```python
print("Hello, world!")
```

Output:

```
Hello, world!
```

Text inside quotes is called a **string**. A string means "these exact characters". Python does not try to understand it. It just shows it.

Single quotes work too, as long as the two ends match:

```python
print('Single quotes are fine.')
```

Output:

```
Single quotes are fine.
```

If the text has an apostrophe in it, put double quotes around it. Then Python does not mistake the apostrophe for the end of the string:

```python
print("It's easier with double quotes.")
```

Output:

```
It's easier with double quotes.
```

### Practice

1. Which line prints `Good night` without an error?
2. Print this sentence, exactly: `I'm learning Python.` It has an apostrophe, so choose your quotes with care.

### One line at a time

Each `print()` shows its text on a line of its own. Python runs the lines in the order they are written, from top to bottom:

```python
print("First line")
print("Second line")
print("Third line")
```

Output:

```
First line
Second line
Third line
```

Swap two of those lines, and the output swaps too. Python never looks ahead, and never changes the order.

That is already enough to draw a picture, one row at a time. Each `print()` here is one row of the shape:

```python
print("*")
print("**")
print("***")
print("****")
```

Output:

```
*
**
***
****
```

An empty `print()` prints a blank line. It is an easy way to space things out:

```python
print("Section 1")
print()
print("Section 2")
```

Output:

```
Section 1

Section 2
```

### Practice

3. Predict what this prints, then press Check. Follow it one line at a time, from the top.

```python
print("Ready")
print("Go!")
print()
print("Set")
```

4. Make the shape six rows tall. The last row has six stars.

```python
print("*")
print("**")
print("***")
print("****")
```

### Several things on one line

One `print()` can show several things, if you put commas between them. Python puts one space between each:

```python
print("Hydrogen", "Helium", "Lithium")
```

Output:

```
Hydrogen Helium Lithium
```

That space comes from the comma, not from the strings. Compare these two lines:

```python
print("Name:", "Ada")
print("Name:Ada")
```

Output:

```
Name: Ada
Name:Ada
```

### Practice

5. What does `print("A", "B")` print?
6. Print the words `cats`, `dogs` and `fish` on one line, using one `print()`.

### Try It

7. Print three lines about yourself. The first starts with `Name:`, the second with `School:`, and the third with `Favorite subject:`. Put your own answer after each one.

> You need one `print()` for each line, so three in all.
> The label and your answer can be one string, like `print("Name: Ada")`, or two strings with a comma between them, like `print("Name:", "Ada")`.

### What you can do now

- Print text with `print()`, in single or double quotes.
- Print lines in the order you want, with blank lines between them.
- Print several things on one line, with commas.

Key words: **program**, **print()**, **string**.
