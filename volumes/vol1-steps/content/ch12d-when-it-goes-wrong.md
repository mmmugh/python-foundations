<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.4 — When recursion goes wrong

Every recursive function so far has had a base case, every call has moved toward it, and every call has given back its answer. In this lesson you see what happens when one of those is missing, how to read what Python says, and how to fix it.

### Warm-up

1. Predict what this prints, then press Check.

```python
def product(numbers):
    if numbers == []:
        return 1
    else:
        return numbers[0] * product(numbers[1:])


print(product([2, 5]))
print(product([]))
```

2. What does `"c"[1:]` give?

### Calls that never stop

Leave out the base case, and nothing stops the calls:

```python
def sum_to(n):
    return n + sum_to(n - 1)


print(sum_to(3))
```

It never prints an answer. The calls go 3, 2, 1, 0, -1, -2, and on, each one waiting for the next. Python allows about 1,000 calls waiting at once, then stops the program. The last line of the error says `RecursionError: maximum recursion depth exceeded`. The recursion depth is how many calls are waiting at once; it is Python's name, and you don't need to remember it.

A base case can also be there and still be missed:

```python
def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)


print(sum_to(3))
print(sum_to(-1))
```

It prints 6, then stops with the same error. From -1 the calls go -2, -3, -4, and never land on 0. `if n <= 0:` catches every number at or below the bottom, as `count_down_by()` needed in lesson 12.1.

So a `RecursionError` nearly always means the calls never reach a base case: there isn't one, or the calls go past it. Look at the base case, and at what each call hands on.

### Practice

3. This program should print 24, then 1, but it stops with an error. Run it and read the last line of the error. Then fix it.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n)


print(factorial(4))
print(factorial(0))
```

> Split it: there is a base case. Does each call hand on something smaller?

4. A program stops with `RecursionError: maximum recursion depth exceeded`. What does that nearly always mean?

5. Which of these calls never reaches the base case?

```python
def halves(n):
    if n == 1:
        return 0
    else:
        return 1 + halves(n // 2)
```

### An answer that goes missing

The recursive case must give back what it works out. Leave out its `return`, and the call works out the answer, then drops it:

```python
def power_of_two(n):
    if n == 0:
        return 1
    else:
        2 * power_of_two(n - 1)


print(power_of_two(0))
print(power_of_two(1))
```

Output:

```
1
None
```

`power_of_two(1)` works out 2 * 1, then reaches the end of the function with no `return`, so it gives back `None` (lesson 6.2). For a bigger `n` it goes further wrong: `power_of_two(2)` waits for `power_of_two(1)`, gets `None`, and tries `2 * None`. The last line of the error says `TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'`. An operand is a value on either side of `*`, and `NoneType` is Python's name for the kind of value `None` is; you don't need to remember either.

### Practice

6. Predict what this prints, then press Check.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        n * factorial(n - 1)


print(factorial(0))
print(factorial(1))
```

7. This program should print 6, but it stops with an error. Run it and read the last line of the error. Then fix it.

```python
def sum_to(n):
    if n <= 0:
        return 0
    else:
        n + sum_to(n - 1)


print(sum_to(3))
```

> Split it: which call gave back `None`, and why? Look at the recursive case.

### Try It

8. The greatest common divisor, or GCD, of two whole numbers is the biggest number that divides both exactly: for 12 and 18 it is 6. Euclid wrote down a rule for it over 2,000 years ago. The GCD of `a` and 0 is `a`. Otherwise, the GCD of `a` and `b` is the GCD of `b` and `a % b`. Write a recursive function `gcd(a, b)` that gives it back.

> Say it: two whole numbers go in; the biggest number that divides both comes out, by Euclid's rule. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. the base case: if `b` is 0, give back `a`. 2. the recursive case: give back the GCD of `b` and `a % b`.
> Name it: the function and its parameters are named for you.
> Check it: try `gcd(12, 18)`, which gives 6, and `gcd(17, 5)`, which gives 1. Then the awkward ones: `gcd(7, 0)`, which gives 7, and `gcd(0, 5)`, which gives 5. Every call reaches the base case, because `a % b` is always smaller than `b`, so the second number shrinks until it is 0.
> Did it call itself? While you try it, add `print("called with", a, b)` as the first line inside the function: for 12 and 18 you see 12 18, 18 12, 12 6, then 6 0. Take the print out before you press Check.

### What you can do now

- Read a `RecursionError` and look for the base case the calls never reach.
- Make a base case catch every number at or below the bottom, with `<=`.
- Find a recursive case that forgets its `return`, from a `None` or a `TypeError`.

Key words: **RecursionError**.
