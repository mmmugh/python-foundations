<!-- part: Unit 4 — Making decisions -->
## Lesson 4.3 — Nesting, and what counts as true

Some decisions take two questions, the second asked only when the first answer is yes. In this lesson you put an `if` inside another `if`. Then you find out what happens when a condition is not a comparison at all.

### Warm-up

1. Predict what this prints, then press Check.

```python
points = 55
if points >= 80:
    print("Gold")
elif points >= 50:
    print("Silver")
else:
    print("Bronze")
```

2. `sunny` is `True` and `temperature` is 18. What does `sunny and temperature > 25` give?

### An if inside an if

A cinema asks two questions: do you have a ticket, and, if you do, are you old enough to go in alone?

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

`has_ticket` already holds `True` or `False`, so it can be the condition on its own: `if has_ticket:` means "if `has_ticket` is `True`".

The inner `if` is part of the outer `if`'s block, so it is indented by four spaces, and its own block by four more. This is called **nesting**. Each `else` lines up with its own `if`. The last `else` belongs to the outer `if`: it runs when there is no ticket, whatever the age.

A trace table shows which lines run. Text goes in it with its quotes:

```python
temperature = 30
sunny = True
plan = "stay in"
if sunny:
    if temperature > 25:
        plan = "swim"
    else:
        plan = "walk"
```

| After line | temperature | sunny | plan |
| --- | --- | --- | --- |
| 1 | 30 |  |  |
| 2 | 30 | True |  |
| 3 | 30 | True | "stay in" |
| 4 | 30 | True | "stay in" |
| 5 | 30 | True | "stay in" |
| 6 | 30 | True | "swim" |

Both questions are `True`, so line 6 runs, and Python skips the inner `else` and its block.

### Practice

3. Fill in the table, then press Check. Text can go in with or without its quotes.

```python
x = 12
if x > 10:
    if x > 20:
        size = "big"
    else:
        size = "medium"
else:
    size = "small"
```

### Or use and

When you don't need two different messages, `and` can do the job of an `if` inside an `if`:

```python
has_ticket = True
age = 15
if has_ticket and age >= 13:
    print("Enjoy the show.")
else:
    print("Sorry, you can't go in.")
```

Output:

```
Enjoy the show.
```

It is shorter, but it loses something: someone without a ticket and someone too young now get the same message. Neither way is always better. Choose the one that says what you need to say.

### Practice

4. Which one `if` line does the same job as the two `if` lines that lead to `plan = "swim"`?

### What counts as true

A condition doesn't have to be a comparison. Python accepts any value as a condition, and decides whether it counts as true:

```python
name = ""
if name:
    print(f"Hello, {name}.")
else:
    print("Hello, stranger.")
```

Output:

```
Hello, stranger.
```

```python
name = "Ada"
if name:
    print(f"Hello, {name}.")
else:
    print("Hello, stranger.")
```

Output:

```
Hello, Ada.
```

`""`, with nothing between the quotes, is the **empty string**. It counts as `False`, and any other string counts as `True`. So `if name:` reads as "if a name was given". It is what `input()` gives back when someone presses Enter without typing.

Numbers work the same way. 0 counts as `False`, and every other number counts as `True`, even a negative one:

```python
coins = 0
if coins:
    print("You have coins.")
else:
    print("No coins yet.")
```

Output:

```
No coins yet.
```

| Counts as `False` | Counts as `True` |
| --- | --- |
| `False` | `True` |
| `0` and `0.0` | any other number, like `5` or `-3` |
| `""`, the empty string | any other string, like `"Ada"` |

Python's name for this is **truthiness**. There is one trap. A string with anything in it counts as `True`, even `"0"` and `"False"`:

```python
answer = "0"
if answer:
    print("It counts as true.")
answer = "False"
if answer:
    print("This counts as true too.")
```

Output:

```
It counts as true.
This counts as true too.
```

`"0"` is text with one character in it, so it is not empty. When a user types a number, turn it into a number with `int()` before you test it.

### Practice

5. Predict what this prints, then press Check.

```python
score = 0
if score:
    print("A")
else:
    print("B")
temperature = -5
if temperature:
    print("C")
else:
    print("D")
```

6. Predict what this prints, then press Check.

```python
name = ""
if name:
    print("Hi,", name)
else:
    print("No name")
word = "no"
if word:
    print("Got a word")
```

7. Which of these counts as `False`?

### Try It

8. A club lets people in when they type a name and are 13 or older. Ask for a name, then an age. If the name is empty, print `Please type your name.` Otherwise, print `Welcome, Ada!` (with their name) when they are 13 or older, and `Sorry, Bo, you must be 13.` (with their name) when they are younger.

> Say it: a name and an age go in, and one of three messages comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the name; ask for the age, as a whole number; first question: was a name typed? If not, ask for one. If it was, the second question: is the age 13 or more? Then welcome, or sorry.
> Name it: what would you call the name, and the age?
> Check it: try Ada and 14, then Bo and 9. Then the awkward ones: press Enter without typing a name, and an age of exactly 13.

### What you can do now

- Put an `if` inside another `if`, and trace which lines run.
- Use `and` instead, when one message will do.
- Say which values count as false: `False`, 0 and the empty string.

Key words: **nesting**, **empty string**, **truthiness**.
