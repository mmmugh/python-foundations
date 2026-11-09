<!-- part: Unit 3 — Expressions and operators -->
## Lesson 3.3 — Formatting output

In this lesson you choose exactly how your output looks: values placed right inside a sentence, money with two decimal places, and lines drawn from repeated characters.

### Warm-up

1. Predict what this prints, then press Check.

```python
print(round(7.456, 1))
```

2. Predict what this prints, then press Check.

```python
print(10 - 2 * 3)
```

### Values inside text

Commas in `print()` always put a space between things, even where you don't want one:

```python
name = "Ada"
print("Hello,", name, "!")
```

Output:

```
Hello, Ada !
```

An **f-string** puts a value right where you want it in the text. Put an `f` just before the opening quote, then write the name in curly braces, `{ }`, inside the string. Python replaces the braces with the value:

```python
name = "Ada"
print(f"Hello, {name}!")
```

Output:

```
Hello, Ada!
```

The braces can hold any expression, not just a name. Python evaluates it and puts in the answer:

```python
width = 7
height = 4
print(f"A {width} by {height} rectangle has area {width * height}.")
```

Output:

```
A 7 by 4 rectangle has area 28.
```

The `f` is easy to forget. Without it, the braces are just characters, and Python prints them as they are:

```python
name = "Ada"
print("Hello, {name}!")
```

Output:

```
Hello, {name}!
```

### Practice

3. This program prints a space before the `!`. Rewrite the `print()` as an f-string, so that it doesn't.

```python
pet = input("Your pet's name: ")
print("Good morning,", pet, "!")
```

### Decimal places

Unit 1's receipt printed its total as 7.5, not 7.50. An f-string can fix that:

```python
total = 7.5
print(f"Total: ${total:.2f}")
```

Output:

```
Total: $7.50
```

`:.2f` after the name, inside the braces, means "show this with exactly 2 decimal places". It is called a **format specifier**. The `$` before the brace is just a character in the text, like the colon.

Change the number to change the places:

```python
score = 91.456
print(f"{score:.1f} points")
```

Output:

```
91.5 points
```

A format specifier changes only how the value is shown. The variable keeps its value:

```python
total = 7.5
print(f"{total:.2f}")
print(total)
```

Output:

```
7.50
7.5
```

### Practice

4. Change the `print()` so it shows the price in dollars with two decimal places, like this: `$4.50`.

```python
price = 4.5
print(price)
```

### Strings with + and *

You met `+` on strings in lesson 2.2: it glues them end to end.

```python
first = "Ada"
last = "Lovelace"
print(first + " " + last)
```

Output:

```
Ada Lovelace
```

`*` with a whole number repeats a string. It is a quick way to draw a line:

```python
print("-" * 20)
print("ab" * 3)
```

Output:

```
--------------------
ababab
```

`+` needs text on both sides. `"Score: " + 42` stops with a `TypeError`, just as `age + 1` did in lesson 2.3. There are two fixes. `str()` turns a number into text, the way `int()` turns text into a number. Or use an f-string, which turns the number into text for you:

```python
score = 42
print("Score: " + str(score))
print(f"Score: {score}")
```

Output:

```
Score: 42
Score: 42
```

### Practice

5. Print a rectangle of `#` characters, 20 wide and 5 tall. Use `*`, so you never type more than one `#` at a time.

### Try It

6. Ask for the price of one item and how many are being bought. Print the total cost with two decimal places, like `Total: $6.75`.

> Say it: a price and a number of items go in; what comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the price as a decimal number, ask how many as a whole number, multiply them, print the total with `:.2f`.
> Name it: what would you call the price, how many, and the total?
> Check it: try 2.25 and 3. Then 0.50 and 4: does it show 2.00, not 2.0? Then try 0 items.

### What you can do now

- Put values inside text with an f-string.
- Show a number with exactly the decimal places you want, with `:.2f`.
- Join strings with `+`, and repeat them with `*`.

Key words: **f-string**, **format specifier**, **str()**.
