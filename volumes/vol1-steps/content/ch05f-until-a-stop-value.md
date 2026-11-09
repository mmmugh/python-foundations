<!-- part: Unit 5 — Repetition -->
## Lesson 5.6 — Until a stop value, and break

Every loop so far knew how many passes it would make. Sometimes nobody knows in advance: a teacher types in scores until there are no more. In this lesson a loop runs until a particular value is typed, and you meet a second way out of a loop, `break`.

### Warm-up

1. Predict what this prints, then press Check.

```python
total = 0
for number in range(2, 7, 2):
    total += number
print(total)
```

2. A loop keeps the largest number so far. Where should the largest so far start?

### Until a stop value

Lesson 5.5's game asked for exactly 4 rounds. When you don't know how many values are coming, agree on one value that means "that's all". It is called a **stop value**. Here the stop value is the word `stop`:

```python
word = input("Word (or stop): ")
while word != "stop":
    print(f"You typed {word}.")
    word = input("Word (or stop): ")
print("Goodbye.")
```

A sample run:

```
Word (or stop): cat
You typed cat.
Word (or stop): dog
You typed dog.
Word (or stop): stop
Goodbye.
```

`input()` appears twice, and both are needed. The first, before the loop, gives the condition something to test the first time. The second, at the end of the block, reads the next word before the condition asks again. Read, loop, read again. The stop value itself never reaches the `print()`: the condition sees it first, and the loop ends. If `stop` is the first thing typed, the block never runs at all.

A `for` loop needs to know how many passes it will make. When you can't know, use `while`.

Here is the shape with a total, worked through with the routine:

```python
# Say it: add up scores until the user types done.
# Split it:
# 1. start the total at 0
# 2. read the first entry
# 3. while it is not done: add it to the total, then read the next
# 4. after the loop, print the total
total = 0
entry = input("Score (or done): ")
while entry != "done":
    total += int(entry)
    entry = input("Score (or done): ")
print(f"Total: {total}")
```

A sample run:

```
Score (or done): 8
Score (or done): 5
Score (or done): 9
Score (or done): done
Total: 22
```

`int()` is used inside the block, not on the `input()` lines, because `int("done")` would stop the program with a `ValueError`. Inside the block, the condition has already let only scores through. Check it with the awkward case: type `done` first, and the total is 0, which is right.

### Practice

3. In the words program, what happens if you leave out the `input()` at the end of the block, and type `cat`?
4. In the scores program, why is `int()` inside the block, and not on the `input()` lines?
5. Keep asking for names until `stop` is typed, and greet each one like `Hello, Ada!`. Don't greet `stop`.

### Asking until it is right

The same shape can keep asking until an answer is good:

```python
age = int(input("Age: "))
while age < 0 or age > 120:
    print("Please enter a realistic age.")
    age = int(input("Age: "))
print(f"Next year you will be {age + 1}.")
```

A sample run:

```
Age: 150
Please enter a realistic age.
Age: -3
Please enter a realistic age.
Age: 14
Next year you will be 15.
```

In lesson 4.4, a bad age got one refusal, and the program ended. Now it asks again, as many times as it takes.

### Practice

6. Ask for a month from 1 to 12. Until it is one, print `Please type a month from 1 to 12.` and ask again. Then print the month, like `Month: 5`.
7. A loop should keep asking while the answer is neither `y` nor `n`. Which condition does that?

### Leaving a loop with break

The words program wrote `input()` twice. `break` lets you write it once:

```python
while True:
    word = input("Word (or stop): ")
    if word == "stop":
        break
    print(f"You typed {word}.")
print("Goodbye.")
```

`while True` asks a question whose answer is always `True`, so on its own it would loop forever. `break` leaves the loop at once: the rest of the block is skipped, and Python goes on to the line after the loop. Both shapes do the same job; use whichever reads better to you.

`break` works in a `for` loop too, and ends it early:

```python
for number in range(50, 100):
    if number % 7 == 0:
        print(f"The first multiple of 7 from 50 is {number}.")
        break
```

Output:

```
The first multiple of 7 from 50 is 56.
```

The loop could make 50 passes, but `break` ends it at the first match.

### Practice

8. Predict what this prints, then press Check.

```python
for number in range(1, 10):
    if number * number > 20:
        break
    print(number)
print("Stopped.")
```

### Try It

9. Ask for whole numbers until 0 is typed. Then print their total, and how many numbers there were, not counting the 0, like `Total: 18` and `Count: 3`.

> Say it: numbers go in until a 0; their total and how many there were come out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: start a total and a count at 0; read the first number; while it is not 0: add it to the total, add 1 to the count, and read the next number; after the loop, print the total, then the count. (Or loop with `while True`, and `break` when the number is 0.)
> Name it: two accumulators again. What does each one hold?
> Check it: try 5, 10, 3, then 0. Then the awkward ones: 0 as the very first number, and numbers below 0, like 7, -2, then 0.

### What you can do now

- Read values until a stop value: read, loop, read again.
- Keep asking until an answer is good.
- Leave a loop early with `break`.

Key words: **stop value**, **break**.
