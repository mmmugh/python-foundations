<!-- part: Unit 8 — Strings as data -->
## Lesson 8.10 — Special characters, and text over several lines

Some characters can't be typed straight into a string. A new line would end the line of code, and a `"` would end the string. In this lesson you write them another way, and write a string that runs over several lines.

### Warm-up

1. Predict what this prints, then press Check.

```python
word = "level"
print(word == word[::-1])
name = "Level"
print(name == name[::-1])
```

2. In lesson 8.9, `backward = letter + backward` turned a word around. Why?

### A backslash and a letter

Inside a string, a backslash, `\`, and the character after it stand for one special character. The pair is called an **escape sequence**. `\n` is a new line, and `\t` is a tab, a jump to the next column:

```python
print("Line one\nLine two")
print("Name:\tAda")
```

Output:

```
Line one
Line two
Name:	Ada
```

`\"` is a double quote that doesn't end the string, and `\'` does the same job inside single quotes. `\\` is one backslash. Each escape sequence is one character, so `len("\n")` is 1:

```python
print("She said, \"Hello.\"")
print('It\'s here.')
print("C:\\games")
print(len("\n"))
```

Output:

```
She said, "Hello."
It's here.
C:\games
1
```

### Practice

3. Predict what this prints, then press Check.

```python
print("up\ndown")
print("a \"b\" c")
print('don\'t')
print(len("a\nb"))
print("back\\slash")
```

4. With one `print()`, print `Name:`, a tab, `Ada`, then a new line, then `Age:`, a tab, and `13`.

> Split it: one string, with `\t` where each tab goes and `\n` where the new line goes.

5. `records` holds three lines of text, with `\n` between them. Print each line as a sentence, `Ada scored 88`, then `Grace scored 92`, then `Alan scored 45`.

```python
records = "Ada,88\nGrace,92\nAlan,45"
```

> Split it: split `records` at `"\n"`, to get a list of lines. Loop over the lines, and split each one at `","`.

### Text over several lines

A string with three quotes on each side can run over several lines. You met three quotes in lesson 6.3, around a docstring:

```python
menu = """1. Add a student
2. View the class
3. Quit"""
print(menu)
```

Output:

```
1. Add a student
2. View the class
3. Quit
```

The new lines inside are part of the string, just as if you had written `\n` for each.

### Practice

6. Predict what this prints, then press Check.

```python
poem = """Roses are red,
violets are blue."""
print(len(poem.split("\n")))
print(poem.upper())
```

### Try It

7. Write a function `make_list(items)` that gives back one string with each item in the list `items` on its own line, after a dash and a space. So `make_list(["eggs", "milk"])` gives back `"- eggs\n- milk"`, which prints as two lines. There is no new line after the last item.

> Say it: a list of items goes in; one string comes out, with a line for each item, each line starting with a dash and a space. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start a new, empty list of lines. 2. for each item, append a dash, a space and the item. 3. join the lines with `"\n"`, and give that back.
> Name it: the function and its parameter are named for you. What would you call the list of lines?
> Check it: print `make_list(["eggs", "milk"])` and look at the two lines. Then the awkward ones: `[]`, which gives `""`; and one item, `["tea"]`, which gives `"- tea"`, with no new line.

### What you can do now

- Write a new line with `\n` and a tab with `\t`.
- Put a quote or a backslash inside a string with `\"`, `\'` and `\\`.
- Write text over several lines between three quotes.

Key words: **escape sequence**.
