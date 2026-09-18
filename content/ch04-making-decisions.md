<!-- part: Part I — Foundations -->
## Chapter 4 — Making Decisions

Every program so far has run straight through, doing the same thing every time. Real programs choose. The `if` statement is how they do it.

```python
temperature = 95

if temperature > 90:
    print("It is hot out.")
    print("Bring water.")

print("Have a good day.")
```

Output:

```
It is hot out.
Bring water.
Have a good day.
```

Change `temperature` to `70` and the first two lines vanish, while the last one still prints. That difference is the whole point.

### Anatomy of an `if`

The structure has three parts, and Python is strict about all of them:

1. The keyword `if`, followed by a **condition** — any expression that produces `True` or `False`
2. A **colon** at the end of the line
3. An indented **block** of statements that run only when the condition is true

The indentation is not decoration. In most languages, curly braces mark which statements belong to the `if`, and indentation is a courtesy. In Python the indentation *is* the grouping, and getting it wrong changes what the program does.

```python
score = 45

if score >= 60:
    print("You passed.")
    print("Congratulations.")
```

Nothing prints, because both indented lines belong to the `if`. Now move the second line left:

```python
score = 45

if score >= 60:
    print("You passed.")
print("Congratulations.")
```

Output:

```
Congratulations.
```

The second `print()` is no longer inside the `if`, so it always runs — and now congratulates a student who failed. Python did exactly what the indentation said.

Use four spaces per level. Replit inserts them when you press Tab after a colon. Never mix tabs and spaces in one file; Python raises `TabError` and the file looks fine on screen, which makes it a miserable bug to find.

### `else`

An `else` block runs when the condition is false. Exactly one of the two blocks runs, always.

```python
age = int(input("Your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print(f"You can vote in {18 - age} years.")
```

A sample run:

```
Your age: 15
You can vote in 3 years.
```

`else` takes no condition of its own — it means "in every other case" — so it gets a colon directly after it.

### `elif`

When there are more than two possibilities, `elif` (short for "else if") chains conditions together:

```python
score = int(input("Test score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} earns a {grade}.")
```

A sample run:

```
Test score: 85
Score 85 earns a B.
```

Python checks the conditions **in order and stops at the first true one**. That is what makes this work with such simple tests. A score of 85 fails `>= 90`, passes `>= 80`, and Python never looks at the rest — so `elif score >= 70` does not need to also check that the score is below 80.

This also means **order matters enormously**. Reverse the chain and everything breaks:

```python
# BROKEN — do not copy this
score = 95

if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 90:
    grade = "A"

print(grade)
```

Output:

```
D
```

A score of 95 satisfies `>= 60`, so Python assigns `"D"` and stops. When you chain conditions that overlap, put the most specific or most extreme case first.

### Nesting

An `if` can contain another `if`. Each level indents four more spaces.

```python
has_ticket = True
age = 15

if has_ticket:
    if age >= 13:
        print("Enjoy the show.")
    else:
        print("You need an adult with you.")
else:
    print("Please buy a ticket first.")
```

Output:

```
Enjoy the show.
```

Nesting is sometimes the clearest way to express a decision, but it gets hard to read quickly. Past two levels, consider whether `and` would say the same thing more plainly:

```python
if has_ticket and age >= 13:
    print("Enjoy the show.")
```

That version is shorter but loses the distinction between the two failure messages. Neither is automatically better; choose the one that matches what you actually need to say.

### Truthiness

Python accepts any value as a condition, not just booleans. Values that count as false are few and worth memorizing:

| Counts as `False` | Counts as `True` |
| --- | --- |
| `False` | `True` |
| `0` and `0.0` | Any other number |
| `""` (empty string) | Any non-empty string |
| `[]`, `{}` (empty containers) | Any non-empty container |
| `None` | Essentially everything else |

This lets you write natural-sounding checks:

```python
name = input("Your name (or press Enter to skip): ")

if name:
    print(f"Hello, {name}.")
else:
    print("Hello, stranger.")
```

`if name:` reads as "if a name was given," which is exactly what it means, and is preferred over `if name != "":`.

One trap: the string `"False"` is a non-empty string, so it counts as `True`. So does `"0"`. Convert input to the type you actually want before testing it.

### Validating input

Until now, a user typing `banana` at a number prompt has crashed the program. Two tools handle that.

The string method `.isdigit()` reports whether a string contains only digits:

```python
answer = input("How many tickets? ")

if answer.isdigit():
    tickets = int(answer)
    print(f"That will be ${tickets * 12}.")
else:
    print("Please enter a whole number.")
```

A sample run:

```
How many tickets? three
Please enter a whole number.
```

Note the order: check first, convert second. The `int()` call sits inside the `if` block, where it only runs once the string is known to be safe.

The more general tool is `try` / `except`, which lets the risky operation run and catches the error if one occurs:

```python
answer = input("Enter a price: ")

try:
    price = float(answer)
    print(f"With tax: ${price * 1.08:.2f}")
except ValueError:
    print("That is not a number.")
```

This handles decimals and negatives, which `.isdigit()` rejects. Use `.isdigit()` for simple whole-number prompts and `try` / `except` for anything else.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| `if score = 90:` | `SyntaxError` — use `==` |
| Missing colon after the condition | `SyntaxError` |
| Inconsistent indentation | `IndentationError`, or silently wrong behavior |
| Mixing tabs and spaces | `TabError` |
| `if 0 < score < 100` when you meant `<=` | Off-by-one at the boundaries |
| Broad condition before narrow one in an `elif` chain | The narrow branch never runs |
| `if grade == "a":` when the user typed `A` | Comparison is case-sensitive; use `.lower()` |

### Try It

1. Ask for a number and print whether it is positive, negative, or zero.
2. Ask for a year and print whether it is a leap year. (A year is a leap year if divisible by 4, except years divisible by 100, unless also divisible by 400.)
3. Ask for two numbers and print the larger, handling the case where they are equal.
4. Ask for a month number, 1 to 12, and print how many days it has. Assume February has 28.
5. Trace this by hand, then run it:

```python
x = 12
if x > 10:
    if x > 20:
        print("big")
    else:
        print("medium")
else:
    print("small")
```

6. Rewrite the grade program so it rejects scores below 0 or above 100 before grading.

### Chapter project: a ticket pricing kiosk

Write a program that calculates a movie ticket price from the customer's age and the day of the week, validating its input along the way.

Rules: children under 5 are free; ages 5 to 12 pay $8; ages 13 to 64 pay $14; ages 65 and over pay $10. On Tuesdays every paying customer gets $3 off.

```python
# Calculates a movie ticket price from age and day of the week.

age_input = input("Customer age: ")

if not age_input.isdigit():
    print("Age must be a whole number.")
else:
    age = int(age_input)

    if age > 120:
        print("Please enter a realistic age.")
    else:
        day = input("Day of the week: ").strip().lower()

        if age < 5:
            price = 0
            category = "Infant"
        elif age <= 12:
            price = 8
            category = "Child"
        elif age <= 64:
            price = 14
            category = "Adult"
        else:
            price = 10
            category = "Senior"

        discount = 0
        if day == "tuesday" and price > 0:
            discount = 3
            price -= discount

        print(f"\nCategory: {category}")
        if discount > 0:
            print(f"Tuesday discount: -${discount}")
        print(f"Price: ${price}")
```

A sample run:

```
Customer age: 70
Day of the week: Tuesday

Category: Senior
Tuesday discount: -$3
Price: $7
```

Three details are worth noticing.

`.strip().lower()` cleans the day input before comparing it, so `" Tuesday "` and `"TUESDAY"` both work. Cleaning user input before testing it is a habit worth forming early; Chapter 8 covers these string methods properly.

The condition `day == "tuesday" and price > 0` prevents the discount from making a free infant ticket cost negative three dollars. Edge cases like this one rarely announce themselves, and finding them is most of what testing is for.

Finally, the nesting is getting deep — three levels before any real work happens. The program is at about the size where that starts to hurt. Chapter 6 introduces functions, which are the usual cure.
