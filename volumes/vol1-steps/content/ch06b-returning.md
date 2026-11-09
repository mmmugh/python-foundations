<!-- part: Unit 6 — Functions -->
## Lesson 6.2 — Giving back a value

Your functions so far print. In this lesson they hand an answer back to the program instead, so it can store the answer, or use it in a calculation.

### Warm-up

1. Predict what this prints, then press Check.

```python
def countdown(start):
    for number in range(start, 0, -1):
        print(number)

countdown(3)
countdown(1)
```

2. In `welcome("Ada")`, what is `"Ada"`?

### Handing a value back

`int("13")` gives back the number 13, and `age = int("13")` keeps it. A function that only prints can't do that: its answer goes to the screen, and the program never gets it. `return` hands a value back from your own function:

```python
def area(width, height):
    return width * height

room = area(12, 10)
print(f"The room is {room} square meters.")
print(f"Two rooms are {area(12, 10) * 2} square meters.")
```

Output:

```
The room is 120 square meters.
Two rooms are 240 square meters.
```

`return` gives a value back to the line that called the function. That line can store it, like `room = area(12, 10)`, or use it in a calculation, like `area(12, 10) * 2`. The function itself prints nothing. The `print()` lines do that.

### Practice

3. Predict what this prints, then press Check.

```python
def triple(number):
    return number * 3

answer = triple(4)
print(answer + 1)
print(triple(10))
```

4. Write a function `average(first, second, third)` that gives back the average of three numbers, rounded to 1 decimal place.

> Split it: add the three, divide by 3, round to 1 place, and `return` the result.
> Check it: try 80, 90 and 75, which is 81.7. Then the awkward ones: 0, 0 and 0; and -2, 4 and 1, which is 1.0.

### Print or return?

These two functions look alike:

```python
def double_print(number):
    print(number * 2)

def double_return(number):
    return number * 2

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

`double_print(5)` shows 10 on the screen, but hands nothing back. A function with no `return` hands back `None`, Python's value for "nothing at all". So `a` holds `None`. `double_return(5)` shows nothing, but hands back 10, and `b` keeps it.

| | Printing | Returning |
| --- | --- | --- |
| Who gets the answer | a person, on the screen | the program |
| Can it be stored? | no | yes |
| Can it be used in a calculation? | no | yes |

A good habit: a function that works something out returns it, and the program that called it decides whether to print it.

### Practice

5. Predict what this prints, then press Check.

```python
def half(number):
    print(number / 2)

result = half(9)
print(result)
```

6. This function should give back the total price, but `cost` ends up as `None`. Change the function so that it returns its answer.

```python
def total_price(price, count):
    print(price * count)

cost = total_price(3, 4)
print(cost)
```

### Several ways back

A function can have more than one `return`. Here is the price rule from the ticket kiosk in lesson 4.5, as a function, made with the routine:

```python
# Say it: an age goes in; the ticket price comes out.
# Split it:
# 1. under 5: free
# 2. 5 to 12: $8
# 3. 13 to 64: $14
# 4. 65 and over: $10
def ticket_price(age):
    if age < 5:
        return 0
    elif age <= 12:
        return 8
    elif age <= 64:
        return 14
    else:
        return 10

print(ticket_price(3))
print(ticket_price(30))
print(ticket_price(70))
```

Output:

```
0
14
10
```

Each branch has its own `return`, and each call takes exactly one branch. `return` also ends the function at once. As soon as one runs, Python leaves the function, and nothing after it in the function runs. That makes a special case easy to deal with first:

```python
def safe_divide(top, bottom):
    if bottom == 0:
        return None
    return top / bottom

print(safe_divide(10, 4))
print(safe_divide(10, 0))
```

Output:

```
2.5
None
```

When `bottom` is 0, the first `return` ends the function, so the division never runs, and there is no `ZeroDivisionError` (lesson 3.1).

### Practice

7. Predict what this prints, then press Check.

```python
def size(number):
    if number > 10:
        return "big"
    print("checking...")
    return "small"

print(size(50))
print(size(5))
```

8. Write a function `sign(number)` that gives back `"positive"`, `"negative"` or `"zero"`.

> Check it: try 5 and -3. Then the awkward one: 0.

### Try It

9. Write a function `largest_of_three(a, b, c)` that gives back the largest of three numbers.

> Say it: three numbers go in; the biggest of them comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: if `a` is at least as big as `b`, and at least as big as `c`, return `a`; otherwise, if `b` is at least as big as `c`, return `b`; otherwise, return `c`.
> Name it: the function and its parameters are named for you. If you keep a largest so far, as in lesson 5.5, what would you call it?
> Check it: try 3, 9 and 5. Then the awkward ones: two the same, like 7, 7 and 2; all below 0, like -1, -5 and -3; and the largest last.

### What you can do now

- Hand a value back from a function with `return`, and store it or use it.
- Tell printing an answer from returning it, and spot a `None`.
- Give a function several ways back, one `return` per branch.

Key words: **return**, **None**.
