<!-- part: Unit 8 — Strings as data -->
## Lesson 8.6 — Letters and digits

In lesson 4.4, `try` and `except` caught a typed word before `int()` could stop the program. In this lesson you meet two methods that ask about the characters themselves: are they all digits, or all letters?

### Warm-up

1. Predict what this prints, then press Check.

```python
song = "Yellow Submarine"
print(song.startswith("Yellow"))
print(song.endswith("Sub"))
print(song.lower().startswith("y"))
```

2. Which test is `True` for the file name `"report.PDF"`?

### All digits?

`isdigit()` gives back `True` if every character in the string is a digit, 0 to 9:

```python
print("2026".isdigit())
print("12a".isdigit())
print("-5".isdigit())
print("3.5".isdigit())
print("".isdigit())
```

Output:

```
True
False
False
False
False
```

A minus sign and a decimal point are not digits, so `"-5"` and `"3.5"` give `False`, though `int("-5")` works. The empty string has no digits at all, so it gives `False` too. So `isdigit()` fits a whole number of 0 or more.

That makes it a test you can put in a `while` loop, to ask again until a whole number is typed:

```python
age = input("Age: ")
while not age.isdigit():
    age = input("Please type a whole number: ")
print(int(age) + 1)
```

A sample run:

```
Age: ten
Please type a whole number: 10
11
```

Read, loop, read again, as in lesson 5.6. By the time the loop ends, `int()` is safe.

### Practice

3. Predict what this prints, then press Check.

```python
print("007".isdigit())
print("7 8".isdigit())
print("+7".isdigit())
print("".isdigit())
```

4. Tickets cost 5 each. Ask how many tickets, and ask again until the answer is a whole number of 0 or more. Then print the cost.

> Check it: try two, then 2, which costs 10. Then the awkward ones: -1, and 0, which costs 0.

### All letters?

`isalpha()` gives back `True` if every character is a letter:

```python
print("Ada".isalpha())
print("Ada Lovelace".isalpha())
print("R2D2".isalpha())
print("".isalpha())
```

Output:

```
True
False
False
False
```

A space is not a letter, so `"Ada Lovelace"` gives `False`. Like `isdigit()`, it gives `False` for the empty string. Both work on a single character too, which is how a loop asks about each one.

### Practice

5. Write a function `letters_only(text)` that gives back a new string of only the letters in `text`, in order. So `letters_only("Hi, Ada!")` gives back `"HiAda"`.

> Split it: build a new string, as in lesson 5.5: start with `""`, loop over the text, and add each character that is a letter.
> Check it: try `"R2-D2"`, which gives `"RD"`. Then the awkward ones: `""`, and `"123"`, which gives `""`.

### Try It

6. Write a function `valid_username(name)` that gives back `True` if `name` is a good username, and `False` if not. A good username has 3 to 12 characters, and every character in it is a letter or a digit.

> Say it: a username goes in; `True` comes out if its length is from 3 to 12 and every character is a letter or a digit, and `False` if not. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. if the length is below 3 or above 12, give back `False`. 2. loop over the characters: if one is not a letter and not a digit, give back `False`. 3. after the loop, give back `True`.
> Name it: the function and its parameter are named for you. What would you call one character in the loop?
> Check it: try `"ada99"`, which gives `True`, and `"ada_99"`, which gives `False`. Then the awkward ones: `""`; `"abc"`, exactly 3; and 13 letters, one too many.

### What you can do now

- Ask whether a string is all digits with `isdigit()`, and ask again until it is.
- Ask whether a string is all letters with `isalpha()`.
- Ask either question about one character at a time, in a loop.

Key words: **isdigit()**, **isalpha()**.
