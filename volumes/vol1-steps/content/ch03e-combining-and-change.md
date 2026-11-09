<!-- part: Unit 3 — Expressions and operators -->
## Lesson 3.5 — Combining conditions, and the change machine

In this lesson you ask two questions at once, and meet a shorter way to change a value. Then you build a program that works out change in coins, using what this unit has taught you.

### Warm-up

1. Predict what this prints, then press Check.

```python
apples = 12
print(apples >= 10)
print(apples == 10)
```

2. Which one stores 0 in `lives`?

### Two questions at once

Sometimes one question is not enough. A teenager is at least 13 years old and at most 19. `and` joins two questions:

```python
age = 15
print(age >= 13 and age <= 19)
```

Output:

```
True
```

`and` gives `True` only when both sides are `True`. Two more words work the same way. `or` gives `True` when at least one side is `True`, and `not` flips `True` to `False` and `False` to `True`:

```python
has_ticket = False
is_member = True
print(has_ticket or is_member)
print(not has_ticket)
```

Output:

```
True
True
```

Python also lets you write "between" the way you would on paper:

```python
age = 15
print(13 <= age <= 19)
```

Output:

```
True
```

### Practice

3. A ride lets you on if you are at least 120 cm tall and at least 8 years old. Which line asks that?
4. `raining` is `True` and `snowing` is `False`. What does `print(raining or snowing)` print?

### A shorter way to change a value

Lesson 2.1 changed a value using its old one, as in `count = count + 1`. Programs do that so often that Python has a shorter way to write it:

```python
score = 0
score += 10
score += 25
print(score)
```

Output:

```
35
```

`score += 10` means `score = score + 10`. Here is the trace table:

| After line | score |
| --- | --- |
| 1 | 0 |
| 2 | 10 |
| 3 | 35 |
| 4 | 35 |

Each arithmetic operator has one:

| Shorthand | Means |
| --- | --- |
| `x += 3` | `x = x + 3` |
| `x -= 3` | `x = x - 3` |
| `x *= 3` | `x = x * 3` |
| `x /= 3` | `x = x / 3` |

```python
score = 35
score *= 2
score -= 5
print(score)
```

Output:

```
65
```

### Practice

5. Fill in the table, then press Check.

```python
coins = 5
coins += 3
coins -= 2
coins *= 2
```

### The change machine

Here is the problem: "Ask for an amount in cents. Print how to pay it with the fewest coins: quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent)."

Everything it needs, you have met in this unit. You will build it a step at a time, running after each step.

### Practice

6. Step 1: ask for an amount in cents, and print it in dollars with two decimal places. 87 cents is `$0.87`.

```python
# Say it: ask for an amount in cents, and show how to pay it
# with the fewest quarters, dimes, nickels and pennies.
```

7. Step 2: print how many quarters fit in the amount, and how many cents are left over after them. Copy your step 1 into this box first.

### Try It

8. Finish the machine. After the quarters, print how many dimes, nickels and pennies to give, in that order, then the total number of coins. Copy your program so far into this box first.

> Say it: in your own words, what does the machine do with the cents left after the quarters? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: take the biggest coin first. You already take as many quarters as fit, and keep what is left. From what is left, take as many dimes as fit, and keep what is left after them. Then the same for nickels. Whatever is left at the end is pennies. Each coin is how many whole, how many left again.
> Name it: a name for each kind of coin, one for the cents still to pay, and one for the total.
> Check it: 87 cents is 3 quarters, 1 dime, 0 nickels and 2 pennies: 6 coins. Then try 41, and 0.

### What you can do now

- Join questions with `and` and `or`, and flip one with `not`.
- Change a value from its old one with `+=`, `-=`, `*=` and `/=`.
- Build a program a step at a time from how many whole, how many left.

Key words: **`and`**, **`or`**, **`not`**, **`+=`**.

That is the end of unit 3. Its quiz is below: fill it in, then show or print it.
