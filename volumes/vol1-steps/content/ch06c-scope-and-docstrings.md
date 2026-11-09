<!-- part: Unit 6 — Functions -->
## Lesson 6.3 — Where names live, and describing a function

A variable made inside a function belongs to that function. In this lesson you see what that means, how a function can use names from outside it, and how to write down what a function is for.

### Warm-up

1. Predict what this prints, then press Check.

```python
def grade(score):
    if score >= 50:
        return "pass"
    return "fail"

print(grade(50))
print(grade(49))
```

2. A function has no `return`. What does a call to it give back?

### Names made inside a function

This function makes a variable, `result`, and returns its value. Then the program tries to use `result` itself:

```python
def calculate():
    result = 42
    return result

print(calculate())
print(result)
```

It prints `42`, then stops. The last line of the error says `NameError: name 'result' is not defined`.

`result` was made inside `calculate()`, so it exists only while the function runs. It is a **local** variable. When the function returns, `result` is gone. The value 42 got out, because it was returned, but the name stayed behind. To keep the value, store what the call gives back: `answer = calculate()`.

A parameter is local too. Changing it inside the function changes nothing outside:

```python
def add_ten(number):
    number = number + 10
    print("Inside:", number)

score = 5
add_ten(score)
print("Outside:", score)
```

Output:

```
Inside: 15
Outside: 5
```

The call gives `number` the value of `score`, which is 5. Then `number` changes to 15, but `score` is a different variable, and it still holds 5.

### Practice

3. Predict what this prints, then press Check. Both variables are called `points`.

```python
def double_it(points):
    points = points * 2
    print(points)

points = 4
double_it(points)
print(points)
```

4. This program should print 24: a price of 20, plus 4 for shipping. Run it, and read the last line of the error. Then fix it: make `add_shipping()` give back the total, and print what it gives back.

```python
def add_shipping(price):
    total = price + 4

add_shipping(20)
print(total)
```

> Split it: two changes. In the function, `return` the total. Below it, store what the call gives back in a variable, and print that.
> Check it: does it print 24? Would it still work for a price of 0?

### Names from outside

A variable made outside every function is a **global** variable. A function can read it:

```python
discount = 3

def sale_price(price):
    return price - discount

print(sale_price(10))
```

Output:

```
7
```

It works, but `sale_price()` now depends on a line far away from it. Change `discount`, and every answer changes, though the function's own lines did not. It is clearer to pass in everything a function needs, as a parameter. Then its brackets tell you all it uses:

```python
def sale_price(price, discount):
    return price - discount

print(sale_price(10, 3))
```

Output:

```
7
```

A function's own name is a variable too, made when its `def` line runs. Call a function above its `def`, and the name does not exist yet:

```python
greet()

def greet():
    print("Hi!")
```

The last line of the error says `NameError: name 'greet' is not defined`.

### Practice

5. Predict what this prints, then press Check.

```python
bonus = 5

def add_bonus(score):
    return score + bonus

print(add_bonus(10))
bonus = 20
print(add_bonus(10))
```

6. Change `add_bonus()` so that the bonus is a second parameter, `bonus`, instead of a global variable.

```python
bonus = 5

def add_bonus(score):
    return score + bonus
```

> Check it: `add_bonus(10, 5)` should give back 15. Then the awkward ones: `add_bonus(0, 20)`, and a bonus below 0.

7. A program calls `show_menu()` on line 1, and defines it on line 3. What happens?

### Describing a function

A function's name says a little about it. A **docstring** says more: what goes in, and what comes out. It is a string on the first line of the function's block, with three quotes on each side:

```python
def c_to_f(celsius):
    """Give back a Celsius temperature in Fahrenheit."""
    return celsius * 9 / 5 + 32

print(c_to_f(100))
print(c_to_f.__doc__)
```

Output:

```
212.0
Give back a Celsius temperature in Fahrenheit.
```

The docstring does nothing when the function runs. But Python keeps it with the function, and `c_to_f.__doc__` gives it back: two underscores, `doc`, and two underscores.

### Practice

8. Predict what this prints, then press Check.

```python
def area(width, height):
    """Give back the area of a rectangle."""
    return width * height

print(area(3, 4))
print(area.__doc__)
```

### Try It

9. Write a function `is_even(number)` that gives back `True` if the number is even, and `False` if it is not. Give it a docstring.

> Say it: a whole number goes in; `True` or `False` comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: first the docstring; then, a number is even when dividing it by 2 leaves nothing over, so test its remainder with `%` (lesson 3.1), and return `True` or `False`.
> Name it: the function and its parameter are named for you. Does your docstring say what goes in and what comes out?
> Check it: try 4 and 7. Then the awkward ones: 0, which is even, and numbers below 0, like -2 and -3.

### What you can do now

- Get a value out of a function by returning it, since its local variables stay inside.
- Pass in what a function needs, rather than reading a global variable.
- Describe a function with a docstring.

Key words: **local**, **global**, **docstring**.
