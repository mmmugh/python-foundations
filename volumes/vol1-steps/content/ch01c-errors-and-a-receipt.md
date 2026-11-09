<!-- part: Unit 1 — Your first programs -->
## Lesson 1.3 — When things go wrong, and a receipt

In this lesson you learn to read the message Python shows when something goes wrong. Then you write a bigger program, a receipt, and meet a way to start a problem when you can't see where to begin.

### Warm-up

1. Predict what this prints, then press Check.

```python
print("10 / 4 =", 10 / 4)
```

2. Which line does Python skip completely?

### Reading an error

Every programmer's code goes wrong, all the time. When Python can't run a line, it stops and tells you why. The message is there to help you.

This line is missing its closing quote:

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

Read an error from the bottom up. The last line names the problem. A **SyntaxError** means Python could not make sense of how the line is written. The lines above it say where: line 1, with a `^` pointing near the spot where Python noticed. The mistake is usually there, or just before it.

Here is a different kind. Python can make sense of how this is written, so it starts running it, and the first line works:

```python
print("Ready")
print(Hello)
```

Python responds with something like:

```
Ready
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print(Hello)
          ^^^^^
NameError: name 'Hello' is not defined
```

Again, start at the bottom. A **NameError** means Python met a word it does not know. Without quotes, `Hello` is not text: Python looks for something called `Hello`, and finds nothing. The line above says where: line 2. With quotes around it, `print("Hello")` works.

These are the mistakes you are most likely to meet first:

| Mistake | What you see |
| --- | --- |
| `Print("hi")` | `NameError`: `print` must be all lowercase |
| `print("hi"` | `SyntaxError`: the closing bracket is missing |
| `print(Hello)` | `NameError`: without quotes, Python looks for a name |
| quotes copied from a word processor, like `“hi”` | `SyntaxError`: type the quotes in the code box itself |

### Practice

3. This program stops with an error. Run it and read the last line of the error. Then fix it so it prints both lines.

```python
print("Good morning")
Print("hi")
```

4. Which of these lines stops with a `SyntaxError`?

### A bigger problem

Every program so far has done one small thing. Here is a bigger problem. Have a go at it before you read on. It is fine to get stuck: the section after it is about exactly that.

### Practice

5. Print a receipt for the Corner Store. It shows the store's name, a line for each of three items (a notebook at 3.50, pens at 2.25 and stickers at 1.75), and a total that Python works out.

### A way to start

What makes the receipt harder is that it asks for several things at once: a name, three items and a total. When a problem feels too big to start, don't start with the code. Start with two small steps.

First, **Say it**: write what the program must do, in your own words, as a comment at the top. Then **Split it**: break it into small steps, one comment each.

```python
# Say it: print a receipt for three items, with a total Python works out.
# Split it:
# 1. print the store's name
# 2. print a line for each item
# 3. print the total
```

That program runs, and prints nothing: it is only comments. But now there are three small jobs instead of one big one. Next, **Build it**: turn the first comment into code, and run it.

```python
# Say it: print a receipt for three items, with a total Python works out.
# Split it:
# 1. print the store's name
# 2. print a line for each item
# 3. print the total
print("CORNER STORE")
print()
```

Output:

```
CORNER STORE
```

It works, so build the next step and run it again. Then build the last one:

```python
# Say it: print a receipt for three items, with a total Python works out.
# Split it:
# 1. print the store's name
# 2. print a line for each item
# 3. print the total
print("CORNER STORE")
print()
print("Notebook 3.50")
print("Pens 2.25")
print("Stickers 1.75")
print()
print("Total", 3.50 + 2.25 + 1.75)
```

Output:

```
CORNER STORE

Notebook 3.50
Pens 2.25
Stickers 1.75

Total 7.5
```

Running after each step means that when something goes wrong, you know it was the line you just wrote. The comments stay in the finished program, where they explain it.

The total prints as `7.5`, not `7.50`. Python does not know these are dollars, so it sees no reason to keep the last zero. That is fine for now.

These three steps are the start of a routine for any problem: **Say it, Split it, Build it**. It is written out on one page, [How to start a problem](99-how-to-start-a-problem.html), for whenever you are stuck.

### Try It

6. The film club's snack bar sells popcorn at 3.75, a drink at 3.00 and a pretzel at 2.50. Print a receipt for one of each, with the club's name at the top and a total that Python works out.

> Say it: in your own words, what must the receipt show? Write it as a comment at the top. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: one comment for each step: the name, a line for each item, the total.
> Build it: turn the first comment into code, and run it. Then the next, and the next.

### What you can do now

- Read an error from the bottom up: first what went wrong, then where.
- Fix a `NameError`, and spot a `SyntaxError`.
- Start a problem by saying it and splitting it into steps, then build it a step at a time.

Key words: **SyntaxError**, **NameError**, **Say it**, **Split it**, **Build it**.

That is the end of unit 1. Its quiz is below: fill it in, then show or print it.
