<!-- part: Unit 2 — Variables and types -->
## Lesson 2.3 — Asking the user

So far, every value was written into the program. In this lesson the program asks the person using it, and you learn to check a program with an input that might break it.

### Warm-up

1. What does `print("5" + "5")` print?
2. Which name explains itself best?

### Asking a question

`input()` pauses the program, waits for the user to type something and press Enter, and gives back what they typed.

```python
name = input("What is your name? ")
print("Nice to meet you,", name)
```

A sample run:

```
What is your name? Ada
Nice to meet you, Ada
```

The text inside the brackets is the **prompt**: the question the user sees. End it with a space, so their typing doesn't run into it. On this page, pressing Run opens a box for you to type in.

### Practice

1. Ask for the user's favorite animal, and print a sentence that uses it.

### Text, not a number

Here is the most important fact about `input()`: it always gives back text, even when the user types digits.

```python
age = input("How old are you? ")
print(age + 1)
```

If the user types `14`, this crashes:

```
TypeError: can only concatenate str (not "int") to str
```

`age` holds the text `"14"`, and Python cannot add the number 1 to a piece of text. The fix is to turn the text into a number first, with `int()`:

```python
age = int(input("How old are you? "))
print("Next year you will be", age + 1)
```

A sample run:

```
How old are you? 14
Next year you will be 15
```

Read the first line from the inside out: `input()` runs first and gives back text, then `int()` turns that text into a whole number.

For a number with a decimal point, use `float()` instead:

```python
price = float(input("Price: "))
print(price * 2)
```

A sample run:

```
Price: 2.5
5.0
```

### Practice

1. This program stops with an error when you type a number. Run it, type 60, and read the last line of the error. Then fix it.

```python
height = input("Height in inches: ")
print("That is", height / 12, "feet")
```

2. Ask for two whole numbers, and print their sum.

### Check it: try an awkward input

**Check it** is the last step of the routine. Once a program works with an ordinary input, try one that might break it: 0, a negative number, a decimal, or a word. Two things are worth knowing first.

`int()` of a number with a decimal point cuts off the part after the point. It does not round:

```python
print(int("14"))
print(int(3.9))
```

Output:

```
14
3
```

And a word cannot become a number at all:

```python
number = int("fourteen")
```

Python responds with something like:

```
ValueError: invalid literal for int() with base 10: 'fourteen'
```

Later units show how a program can cope with that. For now, it is enough to know that an awkward input can stop a program, and to look for one before somebody else finds it.

### Practice

1. A program asks "Cookies: " and runs `int(input(...))` on the answer. Which input is the awkward one worth trying?

### Try It

1. Ask how many minutes a movie lasts, and print how many hours that is.

> Say it: minutes go in; what comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the minutes, turn them into a number, divide by 60, print.
> Name it: what would you call the minutes, and the hours?
> Check it: try 90, then 45. Do the answers make sense?

### What you can do now

- Ask the user for text with `input()`.
- Turn it into a number with `int()` or `float()`.
- Check a program with an awkward input.

Key words: **input()**, **prompt**, **int()**, **float()**, **Check it**.
