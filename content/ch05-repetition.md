<!-- part: Part I — Foundations -->
## Chapter 5 — Repetition

Computers are useful mainly because they will do a boring thing ten million times without complaint. A **loop** repeats a block of code. Python has two kinds, and choosing between them is easy once you know the rule:

- Use a **`for` loop** when you know how many times to repeat, or have a collection to go through
- Use a **`while` loop** when you repeat until something becomes true, and cannot say in advance how long that takes

### The `while` loop

A `while` loop repeats as long as its condition stays true.

```python
count = 1

while count <= 5:
    print(f"Count is {count}")
    count += 1

print("Done.")
```

Output:

```
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
Done.
```

Python checks the condition, runs the block if it is true, then goes back and checks again. When `count` reaches 6, the condition is false and the loop ends.

Every `while` loop needs three things, and leaving out any one of them breaks it:

1. A variable set up **before** the loop (`count = 1`)
2. A condition that can eventually become false (`count <= 5`)
3. Something **inside** the loop that moves toward that (`count += 1`)

Delete line 3 and `count` stays at 1 forever. The condition never goes false, and the program prints `Count is 1` until you stop it. This is an **infinite loop**, and every programmer writes one. In Replit, press the Stop button.

`while` loops shine when the number of repetitions depends on the user:

```python
# Keeps asking until the answer is a valid number.

answer = input("Enter a number: ")

while not answer.isdigit():
    print("That is not a whole number.")
    answer = input("Enter a number: ")

print(f"Thank you. You entered {int(answer)}.")
```

A sample run:

```
Enter a number: seven
That is not a whole number.
Enter a number: 7
Thank you. You entered 7.
```

This is the standard shape of an input-validation loop, and it is a real improvement on Chapter 4's version, which gave up after one bad answer.

### The `for` loop and `range()`

A `for` loop walks through a sequence of values, running its block once for each.

```python
for i in range(5):
    print(f"i is {i}")
```

Output:

```
i is 0
i is 1
i is 2
i is 3
i is 4
```

Notice that `range(5)` produces **five numbers starting at zero**: 0, 1, 2, 3, 4. It stops *before* 5. This looks arbitrary and is not; it fits the way Python numbers positions in lists, which Chapter 7 introduces, and it means `range(n)` always gives exactly `n` values.

`range()` takes up to three arguments:

| Call | Produces |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 6)` | 2, 3, 4, 5 |
| `range(0, 20, 5)` | 0, 5, 10, 15 |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2 |

The pattern is `range(start, stop, step)`, and the stop value is never included. A negative step counts down.

```python
print("Countdown:")
for i in range(5, 0, -1):
    print(i)
print("Liftoff.")
```

Output:

```
Countdown:
5
4
3
2
1
Liftoff.
```

The loop variable is an ordinary variable, and `i` is only a convention. Name it for what it holds when that helps:

```python
for table in range(1, 4):
    for multiplier in range(1, 4):
        print(f"{table} x {multiplier} = {table * multiplier}")
    print()
```

Output:

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

```

That is a **nested loop**: the inner loop runs completely for every single pass of the outer one. Three outer passes times three inner passes is nine lines of output. Nested loops are how you handle grids, tables, and anything two-dimensional.

### Looping over a string

`for` works on anything Python can step through, including strings, where it hands you one character at a time:

```python
for letter in "Python":
    print(letter)
```

Output:

```
P
y
t
h
o
n
```

This generalizes: in Chapter 7 the same syntax walks through lists, and in Chapter 9 through dictionaries. `for thing in collection:` is one of the most-used lines in the language.

### The accumulator pattern

Most useful loops build up an answer as they go. The shape is always the same: set up a variable before the loop, update it inside.

**Summing:**

```python
total = 0

for number in range(1, 101):
    total += number

print(f"The numbers 1 to 100 add up to {total}.")
```

Output:

```
The numbers 1 to 100 add up to 5050.
```

**Counting things that match a test:**

```python
evens = 0

for number in range(1, 51):
    if number % 2 == 0:
        evens += 1

print(f"There are {evens} even numbers from 1 to 50.")
```

Output:

```
There are 25 even numbers from 1 to 50.
```

**Tracking the largest so far:**

```python
largest = 0

for i in range(5):
    value = int(input("Enter a number: "))
    if value > largest:
        largest = value

print(f"The largest was {largest}.")
```

That last one has a hidden bug: starting `largest` at 0 gives the wrong answer if every number entered is negative. The usual fixes are to start from the first value read rather than from zero, or to use a flag variable — and Chapter 7 shows a cleaner way still.

**Building a string:**

```python
bar = ""

for i in range(10):
    bar += "#"
    print(bar)
```

This prints a growing staircase of hash marks. The same accumulator idea works for text.

### `break` and `continue`

Two keywords alter a loop's flow mid-pass.

`break` exits the loop immediately:

```python
while True:
    command = input("Enter a command (or 'quit'): ")
    if command == "quit":
        break
    print(f"You said: {command}")

print("Goodbye.")
```

`while True:` is a deliberate infinite loop whose only exit is the `break`. This is a standard and readable way to write a menu, because the exit condition sits where the exit actually happens rather than being crammed into the `while` line.

`continue` skips the rest of the current pass and starts the next one:

```python
for number in range(1, 21):
    if number % 3 != 0:
        continue
    print(number)
```

Output:

```
3
6
9
12
15
18
```

Everything not divisible by 3 hits the `continue` and gets skipped. Note that this loop could just as well be written `if number % 3 == 0: print(number)`. `continue` earns its place when the skip condition is complicated or when the work after it is long.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| Forgetting `count += 1` in a `while` | Infinite loop |
| `for i in range(1, 10)` expecting 10 passes | You get 9; the stop value is excluded |
| `total = 0` inside the loop | Resets every pass; the total is always the last value |
| `for i in range(len(word))` to print letters | Works, but `for letter in word` is clearer |
| `while answer != "y" or answer != "n"` | Always true — one of them is always the case; use `and` |
| Using the loop variable after the loop | It survives, holding the last value, which is rarely what you want |

### Try It

1. Print the first 20 square numbers, one per line.
2. Ask for a number and print its multiplication table from 1 to 12.
3. Sum the numbers a user enters, stopping when they enter 0.
4. Print a right triangle of stars 6 rows tall using a nested loop.
5. Count how many vowels are in a word the user enters.
6. Write a guessing game: pick a secret number in the code, and keep asking until the user gets it, saying "too high" or "too low" each time.
7. Predict the output, then check:

```python
total = 0
for i in range(1, 6):
    if i == 3:
        continue
    total += i
print(total)
```

### Chapter project: a number-guessing game

Write a complete guessing game in which the computer picks a number and the player guesses, with a limited number of tries.

This needs one new thing: the `random` module. `import random` at the top of a file makes its functions available, and `random.randint(1, 100)` returns a random whole number from 1 to 100 inclusive. (Unlike `range()`, `randint()` *does* include its upper bound — an inconsistency worth remembering.)

```python
# A guessing game with a limited number of attempts.

import random

secret = random.randint(1, 100)
max_tries = 7
tries_used = 0
won = False

print("I am thinking of a number between 1 and 100.")
print(f"You have {max_tries} tries.\n")

while tries_used < max_tries:
    guess_text = input(f"Try {tries_used + 1}: ")

    if not guess_text.isdigit():
        print("Please enter a whole number.")
        continue

    guess = int(guess_text)
    tries_used += 1

    if guess == secret:
        won = True
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")

print()
if won:
    print(f"Correct. You got it in {tries_used} tries.")
else:
    print(f"Out of tries. The number was {secret}.")
```

A sample run:

```
I am thinking of a number between 1 and 100.
You have 7 tries.

Try 1: 50
Too low.
Try 2: 75
Too high.
Try 3: 62
Too low.
Try 4: 68

Correct. You got it in 4 tries.
```

Two design decisions are worth pointing out.

The `continue` on invalid input means a typo does not cost the player a turn, because `tries_used += 1` sits after the validation. Where you put that line is a rule of the game, not a technicality.

The variable `won` exists because the loop can end two ways — by `break` or by running out of tries — and the program needs to tell them apart afterward. A boolean used this way is called a **flag**, and it is a common tool whenever a loop's exit reason matters.

Finally: a player using the strategy in that sample run, always guessing the middle of the remaining range, can find any number from 1 to 100 in at most 7 tries. That is not a coincidence, and Chapter 11 explains why — it is an algorithm called binary search.
