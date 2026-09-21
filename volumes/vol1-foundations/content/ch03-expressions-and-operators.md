<!-- part: Part I — Foundations -->
## Chapter 3 — Expressions and Operators

An **expression** is anything Python can work out to produce a single value. `7` is an expression. So is `3 + 4`, and `(price * quantity) * 1.08`, and `score > 90`. Python **evaluates** an expression — reduces it to one value — and then uses that value.

This chapter covers the operators you build expressions from.

### Arithmetic

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `17 + 5` | `22` |
| `-` | Subtraction | `17 - 5` | `12` |
| `*` | Multiplication | `17 * 5` | `85` |
| `/` | Division | `17 / 5` | `3.4` |
| `//` | Floor division | `17 // 5` | `3` |
| `%` | Modulo (remainder) | `17 % 5` | `2` |
| `**` | Exponent | `2 ** 10` | `1024` |

The first three behave as you expect. The next three deserve attention.

**`/` always produces a float**, even when the division comes out even. `10 / 2` is `5.0`, not `5`. If you need a whole number, convert it or use `//`.

**`//` divides and throws away the fractional part**, giving a whole number: `17 // 5` is `3`, because 5 goes into 17 three whole times. Be aware that it rounds *down*, toward negative infinity, so `-17 // 5` is `-4`, not `-3`.

**`%` gives the remainder** after that division: `17 % 5` is `2`, because 17 is 5 × 3 with 2 left over. Modulo is far more useful than it first appears, and two uses come up constantly:

```python
# Is a number even? Even numbers have remainder 0 when divided by 2.
print(24 % 2)
print(25 % 2)

# Split a total into units: 500 seconds is how many minutes and seconds?
total_seconds = 500
print(total_seconds // 60, "minutes and", total_seconds % 60, "seconds")
```

Output:

```
0
1
8 minutes and 20 seconds
```

That pairing of `//` and `%` — one for the whole units, one for what is left over — is the standard way to break a quantity into larger and smaller parts, and you will use it for time, money, and page counts.

### Order of operations

Python follows the precedence rules from algebra. From highest to lowest:

1. Parentheses `()`
2. Exponent `**`
3. `*`, `/`, `//`, `%` (left to right)
4. `+`, `-` (left to right)

```python
print(10 + 3 * 2)
print((10 + 3) * 2)
print(2 ** 3 * 4)
```

Output:

```
16
26
32
```

Parentheses override everything, and you should use them freely. An expression that is technically unambiguous but takes a reader ten seconds to parse is worse than one with two redundant parentheses.

### Why `0.1 + 0.2` is not `0.3`

Try this:

```python
print(0.1 + 0.2)
```

Output:

```
0.30000000000000004
```

This is not a bug in Python, and every other mainstream language does the same thing. Computers store floats in binary, and just as `1/3` cannot be written exactly as a decimal (0.3333... forever), `0.1` cannot be written exactly in binary. The stored value is very slightly off, and the error surfaces when you add.

Two practical consequences:

- **Round for display.** The error is far too small to matter for a temperature or a price, but it looks terrible on screen. Fix it when you print, using the tools below.
- **Do not test floats for exact equality.** `0.1 + 0.2 == 0.3` is `False`. If you need to compare floats, check that the difference is small rather than that they match.

### Rounding and formatting

The `round()` function takes a number and, optionally, how many decimal places to keep:

```python
print(round(3.14159))
print(round(3.14159, 2))
print(round(0.1 + 0.2, 2))
```

Output:

```
3
3.14
0.3
```

For controlling how a value *appears*, the better tool is an **f-string**. Put an `f` before the opening quote, and anything in curly braces inside the string gets replaced by its value:

```python
name = "Ada"
score = 91.5

print(f"{name} scored {score} points.")
print(f"{name} scored {score:.1f} points.")
print(f"Half of that is {score / 2:.2f}.")
```

Output:

```
Ada scored 91.5 points.
Ada scored 91.5 points.
Half of that is 45.75.
```

The `:.2f` after a value is a **format specifier**: it means "show this as a float with exactly 2 decimal places." This is how you get money to display properly:

```python
total = 7.5
print(f"Total: ${total:.2f}")
```

Output:

```
Total: $7.50
```

That is the fix for the receipt in Chapters 1 and 2. Note that `:.2f` changes only the display; the variable `total` still holds `7.5`.

F-strings can contain any expression, which makes them much cleaner than stringing values together with commas:

```python
width = 7
height = 4
print(f"A {width} by {height} rectangle has area {width * height}.")
```

Output:

```
A 7 by 4 rectangle has area 28.
```

Use f-strings for anything more complicated than printing a single value. The rest of this course does.

### String operators

Two arithmetic symbols also work on strings, with different meanings:

```python
first = "Ada"
last = "Lovelace"

print(first + " " + last)
print("-" * 30)
print("ab" * 3)
```

Output:

```
Ada Lovelace
------------------------------
ababab
```

`+` joins strings, and `*` with an integer repeats one. The repetition trick is genuinely useful for drawing separator lines. Note that `+` requires both sides to be strings: `"Score: " + 42` raises a `TypeError`. Use `str(42)` or, better, an f-string.

### Comparison operators

These compare two values and produce a boolean — `True` or `False`.

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `3 >= 5` | `False` |

The distinction between `=` and `==` is the single most common beginner error. **`=` assigns a value; `==` asks a question.** `score = 90` sets the score. `score == 90` checks whether it is 90 and produces `True` or `False`.

Comparisons work on strings too, using alphabetical order — more precisely, character-code order, which puts all uppercase letters before all lowercase ones:

```python
print("apple" < "banana")
print("Zebra" < "apple")
```

Output:

```
True
True
```

### Boolean operators

Three operators combine or invert booleans:

- `and` — `True` only when both sides are true
- `or` — `True` when at least one side is true
- `not` — flips a boolean to its opposite

```python
age = 15
has_permission = True

print(age >= 13 and age <= 19)
print(age < 13 or has_permission)
print(not has_permission)
```

Output:

```
True
True
False
```

Python also allows the mathematical shorthand for a range, which reads exactly as it would on paper:

```python
age = 15
print(13 <= age <= 19)
```

Output:

```
True
```

These expressions look pointless in isolation. In Chapter 4 they become the conditions that decide what a program does.

### Shorthand assignment

Updating a variable based on its own value is so common that Python has a shorthand for it:

| Shorthand | Means |
| --- | --- |
| `x += 3` | `x = x + 3` |
| `x -= 3` | `x = x - 3` |
| `x *= 3` | `x = x * 3` |
| `x /= 3` | `x = x / 3` |

```python
score = 0
score += 10
score += 25
score *= 2
print(score)
```

Output:

```
70
```

These are conveniences, not new ideas — but `total += price` is used so heavily from Chapter 5 onward that it is worth being fluent in.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| `if score = 90:` | `SyntaxError` — comparison needs `==` |
| `"Total: " + 42` | `TypeError` — use an f-string |
| Expecting `10 / 2` to be `5` | It is `5.0`; `/` always gives a float |
| `0.1 + 0.2 == 0.3` | `False` — never test floats for exact equality |
| `print("{name}")` with no `f` | Prints the braces literally |
| `5 / 0` | `ZeroDivisionError` — check the divisor first |

### Try It

1. Ask for a number of minutes and print it as hours and minutes using `//` and `%`.
2. Write a program that asks for a price and a tax rate as a percentage, then prints the tax and the total, each to two decimal places.
3. Print a rectangle of `#` characters 20 wide and 5 tall, using string repetition and only five `print()` calls.
4. Predict the output, then check:

```python
print(7 // 2, 7 % 2, 7 / 2)
print(2 ** 3 ** 2)
print("5" * 3)
print(int("5") * 3)
```

5. Ask the user for three test scores and print their average to one decimal place.

### Chapter project: a change-making machine

Write a program that asks for an amount in cents and prints how to pay it with the fewest quarters, dimes, nickels, and pennies.

This is a genuine algorithm — a **greedy algorithm**, which at every step takes as much as it can of the largest remaining coin. For US coin values it always produces the fewest coins, though that is a property of these particular values rather than a general truth about greedy methods.

```python
# Breaks an amount of cents into the fewest US coins, largest first.

cents = int(input("Amount in cents: "))
original = cents

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
pennies = cents % 5

print(f"\n{original} cents = ${original / 100:.2f}")
print(f"Quarters: {quarters}")
print(f"Dimes:    {dimes}")
print(f"Nickels:  {nickels}")
print(f"Pennies:  {pennies}")
print(f"Total coins: {quarters + dimes + nickels + pennies}")
```

A sample run:

```
Amount in cents: 87

87 cents = $0.87
Quarters: 3
Dimes:    1
Nickels:  0
Pennies:  2
Total coins: 6
```

The same two-line pattern repeats for each coin: `//` takes as many as possible, `%` keeps what is left. Seeing a repeated pattern like that is a signal, and Chapter 5 gives you loops and Chapter 6 gives you functions — two different ways to stop writing the same thing four times.

(The `\n` at the start of that first f-string is an **escape sequence** meaning "newline." It prints a blank line before the text. `\t` similarly means "tab.")
