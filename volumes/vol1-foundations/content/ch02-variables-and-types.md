<!-- part: Part I — Foundations -->
## Chapter 2 — Variables and Types

A **variable** is a name that refers to a value. You create one by writing a name, an equals sign, and the value you want it to hold.

```python
score = 42
player = "Ada"
print(player, "scored", score)
```

Output:

```
Ada scored 42
```

The `=` sign here does not mean *equals* in the algebra sense. It is an instruction: **work out the value on the right, then attach the name on the left to it**. Read `score = 42` as "let score be 42," not as a statement of fact. This matters because a line that would be nonsense in algebra is perfectly ordinary in Python:

```python
count = 5
count = count + 1
print(count)
```

Output:

```
6
```

Python works out the right side first (`5 + 1`, which is `6`), then points the name `count` at the new value. The old value is simply forgotten. This pattern — a variable updating itself — is the engine of nearly every loop you will write in Chapter 5.

### The four basic types

Every value in Python has a **type**, which determines what you can do with it. Four types cover almost everything in this course.

| Type | Name | Examples | Holds |
| --- | --- | --- | --- |
| `int` | integer | `7`, `0`, `-250` | Whole numbers, no decimal point |
| `float` | floating point | `3.14`, `-0.5`, `98.6` | Numbers with a decimal point |
| `str` | string | `"hello"`, `'A'`, `"42"` | Text, always in quotes |
| `bool` | boolean | `True`, `False` | One of exactly two values |

The built-in `type()` function reports the type of any value:

```python
print(type(7))
print(type(7.0))
print(type("7"))
print(type(True))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Note that `7`, `7.0`, and `"7"` are three different values of three different types. They look similar on screen and behave completely differently:

```python
print(7 + 7)
print("7" + "7")
```

Output:

```
14
77
```

Adding integers adds. Adding strings glues them end to end, which is called **concatenation**. Neither is wrong; they are different operations that happen to share a symbol.

`True` and `False` are capitalized and are not strings — no quotes. They come up constantly from Chapter 4 onward, because every decision a program makes comes down to a boolean.

### Naming variables

Python enforces a few rules, and programmers follow a few more conventions.

**Rules (Python will reject violations):**

- Names contain letters, digits, and underscores only
- Names cannot start with a digit
- Names cannot be one of Python's reserved words (`if`, `for`, `class`, `True`, and about thirty others)

**Conventions (Python allows violations; readers will not):**

- Use `snake_case`: lowercase words joined by underscores, as in `final_score` or `days_remaining`
- Say what the thing is. `x` is fine for a coordinate and terrible for a student's grade
- Do not shadow built-in names. Calling a variable `print`, `list`, or `sum` works right up until you need the original

```python
# Clear
days_until_exam = 14
average_rainfall_mm = 82.4

# Legal, but you will regret it
d = 14
x1 = 82.4
```

Code is read far more often than it is written, usually by someone who has forgotten the context. Naming is not decoration.

### Getting input

The `input()` function pauses the program, waits for the user to type a line and press Enter, and hands back what they typed:

```python
name = input("What is your name? ")
print("Nice to meet you,", name)
```

A sample run:

```
What is your name? Ada
Nice to meet you, Ada
```

The text inside `input()` is the **prompt**. Ending it with a space keeps the user's typing from running into your question.

Here is the single most important fact about `input()`: **it always returns a string.** Always, even when the user types a number. This trips up everyone exactly once:

```python
age = input("How old are you? ")
print(age + 1)
```

If the user types `14`, this crashes:

```
TypeError: can only concatenate str (not "int") to str
```

Python is being reasonable. `age` holds the string `"14"`, and there is no sensible way to glue the number `1` onto the end of a piece of text.

### Converting between types

Three functions convert values from one type to another:

| Function | Converts to | Example | Result |
| --- | --- | --- | --- |
| `int()` | integer | `int("14")` | `14` |
| `float()` | float | `float("3.5")` | `3.5` |
| `str()` | string | `str(14)` | `"14"` |

The fix for the program above is to convert the input before doing arithmetic:

```python
age = int(input("How old are you? "))
print("Next year you will be", age + 1)
```

A sample run:

```
How old are you? 14
Next year you will be 15
```

Read `int(input("..."))` from the inside out: `input()` runs first and produces a string, then `int()` converts that string to an integer. This nesting is a standard idiom and worth recognizing on sight.

Conversion can fail. `int("hello")` raises a `ValueError`, because there is no integer that text describes. `int("3.7")` also fails, because `"3.7"` is not the way an integer is written — you need `float("3.7")`. Converting a float to an int truncates toward zero rather than rounding: `int(3.9)` gives `3`.

### Worked example: unit conversion

```python
# Converts a temperature from Fahrenheit to Celsius.

fahrenheit = float(input("Temperature in degrees F: "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "degrees F is", celsius, "degrees C")
```

A sample run:

```
Temperature in degrees F: 100
100.0 degrees F is 37.77777777777778 degrees C
```

The answer is right and the display is unhelpful — nobody wants fourteen decimal places on a weather report. Chapter 3 shows how to round a number for display, and also why decimal arithmetic sometimes arrives with a tiny error attached.

Note the use of `float()` rather than `int()`. Temperatures come with decimal points, and `int()` would have rejected `98.6`. Choosing the right conversion is part of choosing the right type.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| `42 = score` | `SyntaxError` — the name goes on the left, always |
| `print(name)` before `name = ...` | `NameError` — you cannot use a variable before creating it |
| `int(input("Age: "))` then user types `fourteen` | `ValueError` — Chapter 4 shows how to handle this |
| `Score` vs `score` | Two different variables — Python is case-sensitive |
| `total = total + 1` with no earlier `total` | `NameError` — a counter must be started before it can grow |

### Try It

1. Create variables for a book's title, author, and page count, then print a sentence using all three.
2. Ask the user for two numbers and print their sum, difference, and product.
3. Ask for a number of seconds and print it as minutes and seconds. (Chapter 3 introduces the operators that make this clean; try it with division first.)
4. What does this print, and why?

```python
a = 10
b = a
a = 99
print(a, b)
```

5. Fix this broken program:

```python
height = input("Height in inches: ")
print("That is", height / 12, "feet")
```

### Chapter project: the receipt, improved

Rewrite Chapter 1's receipt so every price appears exactly once, stored in a well-named variable, and the customer's name is asked for at the start.

A solution:

```python
# Prints a personalized receipt. Each price is stored once, in a variable.

customer = input("Customer name: ")

notebook_price = 3.50
pens_price = 2.25
stickers_price = 1.75

total = notebook_price + pens_price + stickers_price

print()
print("===== CORNER STORE =====")
print("Customer:", customer)
print()
print("Notebook          ", notebook_price)
print("Pens (pack of 4)  ", pens_price)
print("Stickers          ", stickers_price)
print("------------------------")
print("Total             ", total)
```

A sample run:

```
Customer name: Ada

===== CORNER STORE =====
Customer: Ada

Notebook           3.5
Pens (pack of 4)   2.25
Stickers           1.75
------------------------
Total              7.5
```

This version cannot lie about its own total: change `notebook_price` and both the line item and the total move together, because both read the same variable. That property — one fact stored in one place — is worth more than it looks, and every later chapter leans on it.
