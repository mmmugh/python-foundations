<!-- part: Unit 3 — Expressions and operators -->
## Lesson 3.4 — Joining and repeating text

Two arithmetic signs, `+` and `*`, also work on text. In this lesson you join strings, repeat them, and find out what to do when a string and a number need to go together.

### Warm-up

1. Predict what this prints, then press Check.

```python
name = "Ada"
print(f"Hi, {name}!")
```

2. `total` holds `7.5`. Which one shows it as `7.50`?

### Joining text with +

You met `+` on strings in lesson 2.2: it glues them end to end.

```python
word = "sun"
print(word + "flower")
```

Output:

```
sunflower
```

`+` adds no space of its own. If you want one, add it as a string of its own, a space between quotes:

```python
first = "Ada"
last = "Lovelace"
print(first + " " + last)
```

Output:

```
Ada Lovelace
```

### Practice

3. Predict what this prints, then press Check.

```python
start = "rain"
print(start + "bow")
print(start + " " + "coat")
```

### Repeating text with *

`*` with a whole number repeats a string that many times:

```python
print("ab" * 3)
```

Output:

```
ababab
```

It is a quick way to draw a line:

```python
print("-" * 20)
```

Output:

```
--------------------
```

A repeated string can be stored in a variable and used more than once:

```python
line = "=" * 10
print(line)
print("Menu")
print(line)
```

Output:

```
==========
Menu
==========
```

### Practice

4. Predict what this prints, then press Check.

```python
print("ho" * 3)
```

5. Print a rectangle of `#` characters, 20 wide and 5 tall. Use `*`, so you never type more than one `#` at a time.

### Text and numbers

`+` needs text on both sides. Give it a string and a number, and Python stops:

```python
score = 42
print("Score: " + score)
```

Python responds with something like:

```
TypeError: can only concatenate str (not "int") to str
```

Concatenate is the word from lesson 2.2: gluing strings together. Python can glue a string only to another string, and `score` is an `int`. It is the same mix-up as `age + 1` in lesson 2.3, the other way round.

There are two fixes. `str()` turns a number into text, the way `int()` turns text into a number. Or use an f-string, which turns the number into text for you:

```python
score = 42
print("Score: " + str(score))
print(f"Score: {score}")
```

Output:

```
Score: 42
Score: 42
```

### Practice

6. What does `str(42)` give back?
7. This program stops with an error. Run it and read the last line of the error. Then fix it, so it prints `Age: 13`.

```python
age = 13
print("Age: " + age)
```

### Try It

8. Ask for a name and an age. Print one sentence, joined with `+`, that says how old they will be next year: with `Ada` and 13, it prints `Next year, Ada will be 14.`

> Say it: a name and an age go in; what sentence comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the name; ask for the age, as a whole number; add 1; turn that number into text with `str()`; join the pieces with `+` and print.
> Name it: what would you call the name, the age, and next year's age?
> Check it: try Ada and 13. Then an awkward age, 0: does the sentence still make sense?

### What you can do now

- Join strings with `+`, adding your own spaces.
- Repeat a string with `*`.
- Turn a number into text with `str()`, or use an f-string, before joining it to a string.

Key words: **`+`** (on strings), **`*`** (on strings), **str()**.
