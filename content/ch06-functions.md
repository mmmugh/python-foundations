<!-- part: Part I — Foundations -->
## Chapter 6 — Functions

A **function** is a named block of code you can run whenever you want. You have been using functions since page one: `print()`, `input()`, `int()`, and `range()` are all functions someone else wrote. This chapter is about writing your own.

```python
def greet():
    print("Hello!")
    print("Welcome to the program.")

greet()
greet()
```

Output:

```
Hello!
Welcome to the program.
Hello!
Welcome to the program.
```

`def` **defines** the function — it stores the instructions under a name and runs nothing. `greet()` **calls** it, which is what actually runs the block. Defining and calling are separate acts, and confusing them is the most common early error: a program with only the `def` produces no output at all, and looks broken.

### Parameters

A function becomes far more useful when you can hand it information. Names listed in the parentheses of the `def` line are **parameters**; the values you pass when calling are **arguments**.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ada")
greet("Grace")
```

Output:

```
Hello, Ada!
Hello, Grace!
```

Multiple parameters are separated by commas, and the order matters — arguments are matched to parameters by position:

```python
def describe_rectangle(width, height):
    print(f"A {width} by {height} rectangle has area {width * height}.")

describe_rectangle(7, 4)
describe_rectangle(4, 7)
```

Output:

```
A 7 by 4 rectangle has area 28.
A 4 by 7 rectangle has area 28.
```

Parameters can have **default values**, used when the caller leaves the argument out:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ada")
greet("Ada", "Good morning")
```

Output:

```
Hello, Ada!
Good morning, Ada!
```

Parameters with defaults must come after those without.

### Return values

So far these functions print. Far more often you want a function that **produces a value** for the rest of the program to use. That is what `return` does.

```python
def area(width, height):
    return width * height

room = area(12, 10)
print(f"The room is {room} square feet.")
print(f"Two rooms would be {area(12, 10) * 2} square feet.")
```

Output:

```
The room is 120 square feet.
Two rooms would be 240 square feet.
```

The difference between printing and returning is the most important idea in this chapter.

|  | Printing | Returning |
| --- | --- | --- |
| Who receives it | A human, on screen | The rest of the program |
| Can it be stored? | No | Yes |
| Can it be used in a calculation? | No | Yes |

Compare these two:

```python
def double_print(n):
    print(n * 2)

def double_return(n):
    return n * 2

a = double_print(5)
b = double_return(5)

print("a is", a)
print("b is", b)
```

Output:

```
10
a is None
b is 10
```

`double_print` displays `10` and hands back nothing, so `a` holds `None` — Python's word for "no value at all." `double_return` displays nothing but hands back `10`, which `b` captures. A function without a `return` returns `None` automatically.

The rule of thumb: **functions that calculate should return; only functions whose job is display should print.** A function that calculates *and* prints is hard to reuse, because you cannot get at the answer.

`return` also ends the function immediately, which is useful for handling special cases up front:

```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

Output:

```
5.0
None
```

A function can return more than one value by separating them with commas, which arrive as a group the caller can unpack:

```python
def split_time(total_seconds):
    return total_seconds // 60, total_seconds % 60

minutes, seconds = split_time(500)
print(f"{minutes} minutes and {seconds} seconds")
```

Output:

```
8 minutes and 20 seconds
```

(What actually comes back is a tuple, which Chapter 10 covers.)

### Scope

Variables created inside a function exist only inside it. This is called **local scope**, and it is a feature: it means you can name a variable `total` inside a function without worrying about whether some other part of the program already uses that name.

```python
def calculate():
    result = 42
    return result

print(calculate())
print(result)
```

The last line raises:

```
NameError: name 'result' is not defined
```

`result` was created inside `calculate` and disappeared when the function returned. Values get out of a function by being returned, and only by being returned.

A function can *read* variables defined outside it, but relying on that makes functions harder to reuse and harder to reason about. Pass what the function needs as parameters instead:

```python
# Fragile — depends on an outside variable
tax_rate = 0.08
def total_with_tax(price):
    return price * (1 + tax_rate)

# Better — everything it needs is declared
def total_with_tax(price, tax_rate):
    return price * (1 + tax_rate)
```

The second version can be read, tested, and moved to another program on its own. The first cannot.

### Docstrings

A string on the first line of a function is a **docstring**, and it is the standard way to say what a function does:

```python
def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit.__doc__)
```

Output:

```
212.0
Convert a Celsius temperature to Fahrenheit.
```

Triple quotes let a string span lines. Write docstrings for anything non-obvious; a one-line description of what goes in and what comes out is usually enough.

### Decomposition

The real reason functions matter is not that they save typing. It is that they let you **name a piece of a problem**, and once a piece has a name you can think about it without thinking about its insides.

Here is Chapter 4's ticket kiosk, rewritten:

```python
def base_price(age):
    """Return the ticket price in dollars for a customer of the given age."""
    if age < 5:
        return 0
    elif age <= 12:
        return 8
    elif age <= 64:
        return 14
    else:
        return 10


def apply_discount(price, day):
    """Return the price after any day-of-week discount."""
    if day == "tuesday" and price > 0:
        return price - 3
    return price


def ticket_price(age, day):
    """Return the final ticket price for an age and day."""
    return apply_discount(base_price(age), day)


print(ticket_price(70, "tuesday"))
print(ticket_price(3, "tuesday"))
print(ticket_price(30, "friday"))
```

Output:

```
7
0
14
```

The deep nesting from Chapter 4 is gone. Each function does one thing, and the name says what. `ticket_price` reads almost as English: take the base price for this age, then apply the day's discount.

Better still, each piece can be tested on its own. Those three `print()` calls at the bottom check that an infant on Tuesday stays free and that a senior gets the discount — the exact edge cases that are easy to get wrong. Checking pieces separately is the difference between a program you hope works and one you know works.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| Defining a function but never calling it | Nothing happens; no error |
| `greet` instead of `greet()` | Refers to the function itself rather than calling it |
| Using `print()` where `return` was needed | The caller gets `None` |
| Calling with the wrong number of arguments | `TypeError` naming what was expected |
| Expecting a function to change an outside variable | It cannot, unless you return the new value |
| Calling a function before its `def` in the file | `NameError` — define before calling |

### Try It

1. Write `is_even(n)` that returns `True` or `False`, then use it in a loop to print the even numbers from 1 to 20.
2. Write `bmi(weight_kg, height_m)` returning the body mass index, rounded to one decimal place.
3. Write `largest_of_three(a, b, c)` without using Python's built-in `max`.
4. Write `count_vowels(word)` returning how many vowels the word contains.
5. Write `is_prime(n)` returning whether `n` is prime, then use it to print every prime under 50.
6. What does this print, and why?

```python
def add_ten(n):
    n = n + 10

x = 5
add_ten(x)
print(x)
```

### Chapter project: a grade calculator

Build a program made entirely of small functions that computes a student's average and letter grade.

```python
# Computes a student's average and letter grade from scores entered one at a time.


def get_score(prompt):
    """Ask repeatedly until the user enters a number from 0 to 100, and return it."""
    while True:
        answer = input(prompt)
        if answer.isdigit() and 0 <= int(answer) <= 100:
            return int(answer)
        print("Please enter a whole number from 0 to 100.")


def letter_grade(average):
    """Return the letter grade for a numeric average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def print_report(name, average, grade):
    """Display a formatted grade report."""
    print()
    print("=" * 32)
    print(f"Student: {name}")
    print(f"Average: {average:.1f}")
    print(f"Grade:   {grade}")
    print("=" * 32)


def main():
    """Run the grade calculator."""
    name = input("Student name: ")

    total = 0
    count = 4
    for i in range(count):
        total += get_score(f"Score {i + 1} of {count}: ")

    average = total / count
    print_report(name, average, letter_grade(average))


main()
```

A sample run:

```
Student name: Ada
Score 1 of 4: 88
Score 2 of 4: 105
Please enter a whole number from 0 to 100.
Score 2 of 4: 92
Score 3 of 4: 79
Score 4 of 4: 95

================================
Student: Ada
Average: 88.5
Grade:   B
================================
```

Notice the shape. Each function has one job, stated in its docstring, and `main()` does nothing but call the others in order. That `main()` convention — one function that runs the program, called on the last line — is near-universal in Python, and it means anyone reading the file can start at `main()` to see the shape of the whole thing.

Notice also that `get_score` combines the validation loop from Chapter 5 with the early-`return` idea from this chapter, and the whole messy business of retrying takes up one line at the call site. That is what decomposition buys you: complexity does not disappear, but it gets boxed up behind a name and stops crowding everything else.
