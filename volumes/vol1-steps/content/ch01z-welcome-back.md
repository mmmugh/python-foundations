<!-- part: Unit 1 — Your first programs -->
## Lesson 0 — Welcome back

Welcome back. This short lesson replays the two things from unit 1 that everything else rests on: printing, and letting Python do arithmetic. Then it shows you a way to start any problem, which the rest of the course builds on. It takes about 20 minutes, and every grey box runs: press Run to see what it does.

### Printing text and numbers

`print()` shows something on the screen.

```python
print("Hello, world!")
```

Output:

```
Hello, world!
```

You can print several things on one line by putting commas between them. Python puts one space between each.

```python
print("Hydrogen", "Helium", "Lithium")
```

Output:

```
Hydrogen Helium Lithium
```

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

Without quotes, Python works out `3 + 4` and prints the answer. With quotes, it prints the characters exactly as written. Text in quotes is called a **string**.

### Practice

1. Which line prints exactly `3 + 4`?
2. Print the words `cats` and `dogs` on one line, using one `print()`.

### Working things out

A line that starts with `#` is a **comment**. Python skips it completely. It is a note for people reading the code, including you next week.

```python
# hours in a week
print(24 * 7)
```

Output:

```
168
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

### Practice

3. Make Python work out the number of minutes in a week. Use a calculation, not the answer.
4. Predict what this prints, then press Check.

```python
print("2 * 3")
print(2 * 3)
```

### A way to start any problem

Here is a problem: "Print a receipt for 3 notebooks at 2 dollars each, with the total."

Before writing any code, **Say it**: write what the program must do, in your own words, as a comment. Then **Split it**: list the small steps, one comment each.

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the item line
# 2. print the total
```

That program runs, and prints nothing: it is only comments. Now **Build it**: turn the first comment into code, and run it.

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the item line
# 2. print the total
print("3 notebooks at 2 dollars each")
```

Output:

```
3 notebooks at 2 dollars each
```

It works, so build the next step.

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the item line
# 2. print the total
print("3 notebooks at 2 dollars each")
print("Total:", 3 * 2)
```

Output:

```
3 notebooks at 2 dollars each
Total: 6
```

The comments stay in the finished program, where they explain it. This is the start of a routine for any problem, and the next lessons add to it. The whole routine is on one page: [How to start a problem](99-how-to-start-a-problem.html).

### Try It

5. Print a receipt for 2 pencils at 1 dollar each and 1 eraser at 3 dollars, with the total worked out by Python.

> Say it: in your own words, what must the receipt show? Write it as a comment. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: three steps, one comment each: the pencils line, the eraser line, the total.

### What you can do now

- Print text and numbers.
- Let Python do arithmetic.
- Start a problem by saying it, then splitting it into steps.

Key words: **string**, **comment**, **Say it, Split it, Build it**.
