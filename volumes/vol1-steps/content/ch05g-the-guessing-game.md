<!-- part: Unit 5 — Repetition -->
## Lesson 5.7 — Skipping, and a guessing game

In this lesson you build a guessing game yourself, a step at a time, with the loops you already know. On the way you meet two small new things: `continue`, which skips the rest of a pass, and a flag, which remembers how a loop ended.

### Warm-up

1. Predict what this prints, then press Check.

```python
for letter in "planet":
    if letter == "n":
        break
    print(letter)
```

2. A program reads names until someone types `stop`. Which loop fits?

### The problem

The computer thinks of a secret number from 1 to 10. The player guesses until they get it. After each wrong guess, the program says whether the guess was too high or too low.

While you build and check it, the secret is always 7, in a variable: `secret = 7`. That way you know what to type. At the end of the lesson, you will see how to make it random.

### Practice

3. Step 1: keep asking for a guess, as a whole number, until it is the secret. Then print how many guesses it took, like `Correct! Guesses: 3`.

```python
secret = 7
```

> Split it: start a count of guesses at 0; loop with `while True`: ask for a guess, add 1 to the count, and if the guess is the secret, `break`; after the loop, print the line.
> Check it: try 3, 9, then 7, which is 3 guesses. Then the awkward one: 7 first, which is 1.

4. Step 2: after each wrong guess, print `Too high.` or `Too low.` Copy your step 1 into this box first.

> Check it: try 9, then 7: one `Too high.` Then 2, then 7: one `Too low.` Then 7 first: neither.

### Skipping the rest of a pass

Type a word into your game, and `int()` stops it with a `ValueError`. With `try` and `except`, from lesson 4.4, the game can say so instead. But a typing slip should not cost the player a guess. For that, there is `continue`. It skips the rest of the pass, and the loop goes straight on with its next pass. (`break`, by contrast, ends the loop.)

```python
for number in range(1, 11):
    if number % 3 != 0:
        continue
    print(number)
```

Output:

```
3
6
9
```

Each number that is not a multiple of 3 reaches `continue`, so the `print()` is skipped on that pass. Here it is after an `except`:

```python
total = 0
for turn in range(3):
    try:
        points = int(input("Points: "))
    except ValueError:
        print("Not a whole number: skipped.")
        continue
    total += points
print(f"Total: {total}")
```

A sample run:

```
Points: 4
Points: ten
Not a whole number: skipped.
Points: 5
Total: 9
```

When `int()` fails, `points` has no new value. `continue` makes sure the line that adds it is skipped, so only real numbers reach it.

### Practice

5. Predict what this prints, then press Check.

```python
total = 0
for number in range(1, 6):
    if number == 3:
        continue
    total += number
print(total)
```

6. Step 3: if a guess is not a whole number, print `Please type a whole number.`, and don't count it as a guess. Copy your step 2 into this box first.

> Check it: try 9, seven, then 7: that is 2 guesses, not 3.

### Remembering how a loop ended

A game with a limit, say 5 guesses, can end in two ways: the player guesses it, or the guesses run out. After the loop, the program has to know which. A `True` or `False` variable can remember it. It is set before the loop, changed inside it when something happens, and read after it. This is called a **flag**:

```python
word = "rhythm"
found = False
for letter in word:
    if letter == "y":
        found = True
        break
if found:
    print(f"{word} has a y.")
else:
    print(f"{word} has no y.")
```

Output:

```
rhythm has a y.
```

### Practice

7. Predict what this prints, then press Check.

```python
found = False
for number in range(1, 20, 4):
    if number % 6 == 0:
        found = True
print(found)
```

### Making it random

A real game needs a secret that nobody knows. When your game works, replace `secret = 7` with these two lines:

```python
import random
secret = random.randint(1, 10)
print(secret)
```

Run it a few times: the number changes. `import random` brings in Python's tools for random numbers, and `random.randint(1, 10)` picks a whole number from 1 to 10. Unlike `range()`, it can give the 10 too. (The `print()` is only here to show you; leave it out of the game.)

### Practice

8. Which numbers can `random.randint(1, 10)` give?

### Try It

9. Step 4: give the player at most 5 guesses. A word still does not count as a guess. If they get it, print `Correct! Guesses: 3` as before. If the 5 guesses run out, print `Out of guesses. It was 7.` Copy your step 3 into this box first, and keep `secret = 7` while you check it.

> Say it: the same game, but it ends after 5 wrong guesses, and says which way it ended. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: before the loop, set a flag to `False`; loop while fewer than 5 guesses have been counted; when a guess is right, set the flag to `True` and `break`; after the loop, if the flag is `True`, print the Correct line, otherwise print the out-of-guesses line.
> Name it: the flag says whether the player won. What would you call it?
> Check it: try 3, 9, then 7, which wins in 3. Then the awkward ones: five wrong guesses; the right one on exactly the fifth guess; and a word among the guesses, which must not use one up.

### What you can do now

- Skip the rest of a pass with `continue`.
- Remember how a loop ended with a flag.
- Build a game one step at a time, checking each step.

Key words: **continue**, **flag**, **random**.

That is the end of unit 5. Its quiz is below: fill it in, then show or print it.
