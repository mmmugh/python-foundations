<!-- part: Unit 4 — Making decisions -->
## Lesson 4.4 — Checking input

A program can't choose what people type. In this lesson your programs check what they are given before they use it: a number that is too big or too small, and a word typed where a number belongs.

### Warm-up

1. Predict what this prints, then press Check.

```python
answer = ""
if answer:
    print("You typed something.")
else:
    print("You typed nothing.")
```

2. When does `or` give `True`?

### Checking a number before using it

The grade program from lesson 4.2 grades whatever it is given. A score of 150 earns an A, and -20 earns an F, though neither is a real score. A program should check a value before it uses it. This is called **validating** it:

```python
score = 150
if score < 0 or score > 100:
    print("A score must be from 0 to 100.")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

Output:

```
A score must be from 0 to 100.
```

The check comes first, so a bad score never reaches the grading. `score < 0 or score > 100` is `True` when the score is outside the range: below the bottom, or above the top. It is `or`, because one side being `True` is enough. The ends, 0 and 100, are real scores, so the tests are `<` and `>`, not `<=` and `>=`.

You can also ask the opposite question, whether a value is inside the range, written the way you would on paper (lesson 3.6):

```python
age = 130
if 0 <= age <= 120:
    print("Thank you.")
else:
    print("Please enter a realistic age.")
```

Output:

```
Please enter a realistic age.
```

Here the good case goes in the `if` block, and the refusal goes in the `else`.

### Practice

3. A month number must be from 1 to 12. Which test is `True` for a bad month number?
4. Change this program so that a score below 0 or above 100 prints `A score must be from 0 to 100.` instead of a grade.

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
print(f"Grade: {grade}")
```

> Check it: try 85, then the awkward ones: 150, -5, and the ends, 0 and 100.

### When the input is a word

In lesson 2.3, a word made `int()` stop the program with a `ValueError`. Then, all you could do was look for that input before somebody else did. Now your program can cope with it, using `try` and `except`:

```python
answer = "fourteen"
try:
    age = int(answer)
    print(f"Next year you will be {age + 1}.")
except ValueError:
    print("That is not a whole number.")
```

Output:

```
That is not a whole number.
```

Python runs the lines in the `try` block. If one of them stops with a `ValueError`, Python jumps straight to the `except` block, and the rest of the `try` block is skipped. `ValueError` is the name on the last line of the error from lesson 2.3.

With a good answer, nothing goes wrong, and it is the `except` block that is skipped:

```python
answer = "14"
try:
    age = int(answer)
    print(f"Next year you will be {age + 1}.")
except ValueError:
    print("That is not a whole number.")
```

Output:

```
Next year you will be 15.
```

Put the line that might fail in the `try` block, together with the lines that need its answer. With `input()`, it looks like this:

```python
try:
    tickets = int(input("How many tickets? "))
    print(f"That will be ${tickets * 12}.")
except ValueError:
    print("Please type a whole number.")
```

A sample run:

```
How many tickets? three
Please type a whole number.
```

### Practice

5. Predict what this prints, then press Check.

```python
answer = "seven"
try:
    count = int(answer)
    print("Got it.")
except ValueError:
    print("Not a number.")
print("Done.")
```

6. Predict what this prints, then press Check.

```python
answer = "7"
try:
    count = int(answer)
    print(count * 2)
except ValueError:
    print("Not a number.")
print("Done.")
```

7. This program stops with an error when someone types a word. Run it, type `ten`, and read the last line of the error. Then use `try` and `except`, so that a word prints `Please type a whole number.` instead.

```python
pets = int(input("How many pets? "))
print(f"You have {pets} pets.")
```

### Try It

8. Ask for a month as a number from 1 to 12, and print how many days it has. February has 28; April, June, September and November have 30; the rest have 31. If what was typed is a word, or a number outside 1 to 12, print `Please type a month from 1 to 12.`

> Say it: a month number goes in; a number of days comes out, or a request for a real month. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: in a `try` block, ask for the month as a whole number; if it is below 1 or above 12, print the message; otherwise February first, then the four 30-day months joined with `or`, and every other month has 31. In the `except` block, print the message too.
> Name it: what would you call the month?
> Check it: try 1, 2 and 4. Then the awkward ones: the ends, 1 and 12; just past them, 0 and 13; and a word, like June.

### What you can do now

- Validate a number before using it, and refuse one outside a range.
- Catch a word typed where a number belongs, with `try` and `except`.
- Check a range at its ends and just past them.

Key words: **validating**, **try**, **except**, **ValueError**.
