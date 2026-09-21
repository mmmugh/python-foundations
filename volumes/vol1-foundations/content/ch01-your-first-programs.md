<!-- part: Part I — Foundations -->
## Chapter 1 — Your First Programs

A program is a list of instructions written in an order a computer can follow. That is the whole idea. The computer is fast and literal: it will do exactly what you wrote, at enormous speed, including the parts you did not mean.

Python runs your instructions one line at a time, top to bottom. Understanding that single fact explains most of what beginners find confusing.

### Output with `print()`

The `print()` function displays something on the screen. It is the first tool you get and the one you will use most, because it is how a program tells you what it is doing.

```python
print("Hello, world!")
```

Output:

```
Hello, world!
```

The quotation marks matter. Text inside quotes is called a **string**, and it means *these exact characters*. Python does not try to understand a string; it just carries it around. Single and double quotes both work, as long as you match them:

```python
print('Single quotes are fine too.')
print("Use double quotes when the text has an apostrophe: it's easier.")
```

### One line at a time

Each `print()` puts its text on its own line, and Python runs them in the order written:

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

Swap the order of those three lines and the output order changes to match. Nothing in Python looks ahead or reorders your work.

You can print more than one thing at a time by separating items with commas. Python puts a single space between them:

```python
print("Hydrogen", "Helium", "Lithium")
```

Output:

```
Hydrogen Helium Lithium
```

An empty `print()` prints a blank line, which is a cheap and useful way to space out your output:

```python
print("Section 1")
print()
print("Section 2")
```

### Printing numbers

Numbers do not need quotes, and Python will do arithmetic on them:

```python
print(7)
print(3 + 4)
print("3 + 4")
```

Output:

```
7
7
3 + 4
```

Look at the last two lines carefully. `3 + 4` without quotes is a calculation, so Python works it out and prints `7`. With quotes it is a string, so Python prints the characters exactly. This distinction between *a value* and *text describing a value* runs through the whole language, and Chapter 2 makes it precise.

### Comments

A line beginning with `#` is a **comment**. Python ignores it completely. Comments are notes to human readers, including you in three weeks when you have forgotten why you wrote something.

```python
# Convert a distance from miles to kilometers
print(26.2 * 1.609)   # a marathon, in km
```

Output:

```
42.1558
```

Comments can sit on their own line or at the end of a line of code. Good comments explain *why*, not *what*: `# add 1 to count` is noise, because the code already says that. `# count starts at 0 because the first lap does not score` is worth writing.

### When things go wrong

Python will refuse to run code it cannot understand, and it tells you where it gave up. This is a feature, not a scolding.

```python
print("Missing a quote)
```

Python responds with something like:

```
  File "main.py", line 1
    print("Missing a quote)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

Read error messages from the bottom up. The last line names the problem (`SyntaxError`), and the line above it points at where Python noticed. The error is usually at or just before that spot. Appendix A collects the messages you will meet most often.

### Common mistakes

| Mistake | What you see |
| --- | --- |
| `Print("hi")` | `NameError` — Python is case-sensitive; it must be lowercase `print` |
| `print("hi"` | `SyntaxError` — the closing parenthesis is missing |
| `print(Hello)` | `NameError` — without quotes, Python looks for a variable named `Hello` |
| Using smart quotes from a word processor | `SyntaxError` — type quotes in the editor, not in Google Docs |

### Try It

1. Write a program that prints your name, your school, and your favorite subject, each on its own line.
2. Make Python calculate and print the number of minutes in a week. Use a calculation, not the answer.
3. Write a program that prints a small shape out of asterisks, like a triangle four rows tall.
4. Predict the output of the program below *before* running it, then run it and check.

```python
print("A")
print("B", "C")
print()
print(2 * 3)
print("2 * 3")
```

### Chapter project: a receipt

Write a program that prints a tidy receipt for a purchase of three items. Use `print()` for the layout, a comment at the top explaining what the program does, and a calculation (not a typed-in answer) for the total.

A solution looks like this:

```python
# Prints a receipt for three items and calculates the total.

print("===== CORNER STORE =====")
print()
print("Notebook           3.50")
print("Pens (pack of 4)   2.25")
print("Stickers           1.75")
print("------------------------")
print("Total             ", 3.50 + 2.25 + 1.75)
print("========================")
```

Output:

```
===== CORNER STORE =====

Notebook           3.50
Pens (pack of 4)   2.25
Stickers           1.75
------------------------
Total              7.5
========================
```

Notice the total prints as `7.5`, not `7.50`. Python does not know these are dollars, and it has no reason to keep a trailing zero. Chapter 3 shows how to control the way numbers are displayed.

The program also has a real weakness: the prices appear twice, once in the text and once in the calculation. Change a price in one place and forget the other, and the receipt lies. Chapter 2 fixes this.
