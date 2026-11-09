<!-- part: Unit 4 — Making decisions -->
## Lesson 4.2 — Elif, and turning a rule into code

`if` and `else` choose between two things. In this lesson a program chooses between as many as you like. Then you turn a rule written as a sentence, with a "but" and an "unless" in it, into code.

### Warm-up

1. Predict what this prints, then press Check.

```python
coins = 7
if coins >= 10:
    print("You can buy it.")
else:
    print("Save up a bit more.")
```

2. What comes straight after the word `else`?

### More than two choices

A grade has five possibilities, not two. `elif`, short for "else if", adds as many tests as you need:

```python
score = 85
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

Output:

```
Score 85 earns a B.
```

Python checks the conditions in order, from the top, and **stops at the first one that is `True`**. Only that block runs. The `else` at the end catches every case that no test caught.

A score of 85 fails `score >= 90`, passes `score >= 80`, and Python never looks at the rest. That is why `elif score >= 80` doesn't also need to check that the score is below 90: a score of 90 or more never gets that far.

### Practice

3. In the grade program, `score` is 72. Which line runs?
4. Predict what this prints, then press Check.

```python
temperature = 15
if temperature >= 25:
    print("Hot")
elif temperature >= 10:
    print("Mild")
elif temperature >= 0:
    print("Cold")
else:
    print("Freezing")
```

5. Ask for a whole number. Print `positive`, `negative` or `zero`.
6. Ask for two whole numbers. Print the larger one after `Larger:`, exactly like `Larger: 8`. If they are equal, print `Same`.

### Order matters

Because Python stops at the first `True`, the order of the tests matters. Here is the grade program with its tests turned upside down:

```python
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

95 is 60 or more, so the first test is `True`. Python stores `"D"` and stops. It never reaches `score >= 90`. When tests overlap, put the narrowest one first: the one that the fewest values pass.

### Practice

7. A program sorts ages: under 13 is a child, under 20 is a teen, and anything else is an adult. Which order of tests works?

### Turning a rule into code

Here is a rule written as a sentence:

"In a raffle, a ticket wins if its number is a multiple of 5. But multiples of 10 do not win, unless they are also multiples of 50."

It has a main part, a "but", and an "unless". A number is a multiple of 5 when 5 goes into it with nothing left over, so `ticket % 5 == 0` asks it, the way you tested for even numbers in lesson 3.5.

**Split it** one clause at a time, a comment line each: a multiple of 5 wins; but a multiple of 10 does not; unless it is a multiple of 50, which wins.

Now look at which clause is narrowest. Every multiple of 50 is a multiple of 10, and every multiple of 10 is a multiple of 5. In the sentence's order, `ticket % 5 == 0` would come first, and 20 would win: the trap from the last section. So turn the list around, and start with the narrowest clause, the "unless":

```python
# Say it: decide whether a raffle ticket wins.
# Split it, narrowest clause first:
# 1. a multiple of 50 wins
# 2. any other multiple of 10 does not
# 3. any other multiple of 5 wins
# 4. every other number does not
ticket = 20
if ticket % 50 == 0:
    print("Wins")
elif ticket % 10 == 0:
    print("No prize")
elif ticket % 5 == 0:
    print("Wins")
else:
    print("No prize")
```

Output:

```
No prize
```

**Check it** with one number for each clause:

| ticket | First test that is `True` | Prints |
| --- | --- | --- |
| 150 | `ticket % 50 == 0` | Wins |
| 20 | `ticket % 10 == 0` | No prize |
| 35 | `ticket % 5 == 0` | Wins |
| 7 | none, so the `else` | No prize |

### Practice

8. Change the raffle program's `ticket` to 100. What does it print?

### Try It

9. Ask for a year, and print `leap year` or `ordinary year`. The rule: a year is a leap year if it is a multiple of 4. But multiples of 100 are not leap years, unless they are also multiples of 400.

> Say it: a year goes in; which of two answers comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: one comment per clause: a multiple of 4 is a leap year; but a multiple of 100 is not; unless it is also a multiple of 400. Then put the narrowest clause first, as in the raffle.
> Name it: what would you call the year?
> Check it: try an ordinary leap year, 2024, then 2023. Then the awkward ones, where the "but" and the "unless" matter: 1900, and 2000.

### What you can do now

- Choose between many cases with `if`, `elif` and `else`.
- Put overlapping tests in the right order, narrowest first.
- Turn a rule with a "but" and an "unless" into code, one clause at a time.

Key words: **elif**.
