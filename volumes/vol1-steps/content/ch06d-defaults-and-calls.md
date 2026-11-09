<!-- part: Unit 6 — Functions -->
## Lesson 6.4 — Default values, and functions that use functions

In this lesson your functions get two more abilities: a parameter that has a value even when the call leaves it out, and calls to your other functions.

### Warm-up

1. Predict what this prints, then press Check.

```python
level = 1

def next_level(level):
    level = level + 1
    return level

print(next_level(level))
print(level)
```

2. Where does a docstring go?

### Default values

`round()` takes one argument or two. `round(3.14159)` gives back 3, and `round(3.14159, 2)` gives back 3.14. When the second is left out, `round()` uses 0 places. Your own functions can do the same, with a **default value**: a value a parameter takes when the call leaves it out.

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

`greeting="Hello"` in the `def` line gives `greeting` its default. The first call has no second argument, so `greeting` holds `"Hello"`. The second call has one, and it replaces the default.

A parameter with a default must come after the ones without. Otherwise Python can't tell which argument goes where, and refuses to start:

```python
def greet(greeting="Hello", name):
    print(f"{greeting}, {name}!")
```

The last line of the error says `SyntaxError: parameter without a default follows parameter with a default`. Older versions of Python say something like `non-default argument follows default argument`.

### Practice

3. Predict what this prints, then press Check.

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(2, 3))
```

4. Write a function `repeat_text(text, times=2)` that gives back the text repeated that many times. `repeat_text("ha")` gives back `"haha"`, and `repeat_text("ha", 3)` gives back `"hahaha"`.

> Split it: string `*` from lesson 3.4 repeats a string.
> Check it: try `repeat_text("ha")` and `repeat_text("ha", 3)`. Then the awkward ones: an empty string, and 0 times.

5. Which `def` line does Python accept?

### Functions that use functions

The block of a function can call another function, just as your loops call `print()`. Here, `sum_of_squares()` calls `square()` twice:

```python
def square(number):
    return number * number

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))
```

Output:

```
25
```

A call can also go straight into another call, as an argument, the way `int(input())` does in lesson 2.3. Here is lesson 6.2's `ticket_price()` with a second function for the Tuesday discount from lesson 4.5:

```python
def ticket_price(age):
    if age < 5:
        return 0
    elif age <= 12:
        return 8
    elif age <= 64:
        return 14
    else:
        return 10

def apply_discount(price, day):
    if day == "Tuesday" and price > 0:
        return price - 3
    return price

print(apply_discount(ticket_price(70), "Tuesday"))
print(apply_discount(ticket_price(3), "Tuesday"))
print(apply_discount(ticket_price(30), "Friday"))
```

Output:

```
7
0
14
```

The inner call runs first: `ticket_price(70)` gives back 10, and then `apply_discount(10, "Tuesday")` gives back 7. Each function does one job, and its name says what. Each can also be checked on its own. The three calls check the edge cases from lesson 4.5: a senior on a Tuesday, a free ticket on a Tuesday, and a day with no discount.

### Practice

6. Copy your `is_even()` from lesson 6.3 into this box. Then use it in a loop to print the even numbers from 1 to 20, one per line.

> Split it: a `for` loop over 1 to 20; inside it, an `if` that calls `is_even()` with the loop's number.

7. Predict what this prints, then press Check.

```python
def double(number):
    return number * 2

def add_one(number):
    return number + 1

print(add_one(double(5)))
print(double(add_one(5)))
```

### Try It

8. Write a function `is_vowel(letter)` that gives back `True` for a, e, i, o or u, and `False` for any other letter. Then write `count_vowels(word)`, which uses `is_vowel()` to give back how many vowels a word has.

> Say it: a word goes in; the number of vowels in it comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: `is_vowel()` first, and check it on its own with a few letters. Then `count_vowels()`: start a count at 0; for each letter of the word, if `is_vowel()` says so, add 1; after the loop, return the count.
> Name it: the functions and their parameters are named for you. What would you call the count?
> Check it: try `banana`, which has 3. Then the awkward ones: `sky`, which has none; `queue`, with four vowels in a row; and an empty string.

### What you can do now

- Give a parameter a default value, for calls that leave it out.
- Call one of your functions from inside another.
- Pass what one call gives back straight into another call.

Key words: **default value**.
