<!-- part: Unit 3 — Expressions and operators -->
## Lesson 3.3 — Formatting output

In this lesson you choose exactly how your output looks: values placed right inside a sentence, and numbers shown with exactly the decimal places you want, like money.

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

3. Predict what this prints, then press Check.

```python
side = 3
print(f"A square with side {side} has area {side ** 2}.")
```

4. `name` holds `"Sam"`. Which line prints `Hi, Sam`?
5. This program prints a space before the `!`. Rewrite the `print()` as an f-string, so that it doesn't.

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

6. Predict what this prints, then press Check.

```python
height = 1.4567
print(f"{height:.1f}")
print(f"{height:.3f}")
print(height)
```

7. Change the `print()` so it shows the price in dollars with two decimal places, like this: `$4.50`.

```python
price = 4.5
print(price)
```

### Try It

8. Ask for the price of one item and how many are being bought. Print the total cost with two decimal places, like `Total: $6.75`.

> Say it: a price and a number of items go in; what comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the price as a decimal number, ask how many as a whole number, multiply them, print the total with `:.2f`.
> Name it: what would you call the price, how many, and the total?
> Check it: try 2.25 and 3. Then 0.50 and 4: does it show 2.00, not 2.0? Then try 0 items.

### What you can do now

- Put values, and whole expressions, inside text with an f-string.
- Spot a missing `f` from the braces it prints.
- Show a number with exactly the decimal places you want, like `:.2f`, without changing the value.

Key words: **f-string**, **format specifier**.
