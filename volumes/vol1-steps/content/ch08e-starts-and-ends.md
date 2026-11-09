<!-- part: Unit 8 — Strings as data -->
## Lesson 8.5 — How text starts and ends

`in` looks for text anywhere in a string. Often you care about one place only: is this a `.txt` file, does this title begin with `The`? In this lesson two methods ask about the start and the end.

### Warm-up

1. Predict what this prints, then press Check.

```python
word = "mississippi"
print("ss" in word)
print(word.find("ss"))
print(word.count("ss"))
print(word.find("z"))
```

2. `guests` is `["Ada", "Grace"]`. What is `"Ada" not in guests`?

### The start and the end

Is `notes.txt` a text file? A slice can ask, `file_name[-4:] == ".txt"`, but you have to count the characters in `.txt` first, and get the count right. `endswith()` asks without counting, and so does `startswith()` for the start:

```python
file_name = "notes.txt"
print(file_name.endswith(".txt"))
print(file_name.endswith(".py"))
print(file_name.startswith("notes"))
```

Output:

```
True
False
True
```

Both answer `True` or `False`. Capitals matter, as they do everywhere in text. And unlike `in`, they look only at one end:

```python
title = "The Hobbit"
print(title.startswith("The"))
print(title.startswith("the"))
print("Hobbit" in title)
print(title.startswith("Hobbit"))
```

Output:

```
True
False
True
False
```

### Practice

3. Predict what this prints, then press Check.

```python
photo = "Beach.JPG"
print(photo.endswith(".jpg"))
print(photo.lower().endswith(".jpg"))
print(photo.startswith("B"))
print(photo.startswith("Beach.JPG"))
```

4. Write a function `is_python_file(name)` that gives back `True` if `name` ends with `.py`, in any capitals, and `False` if not.

> Check it: try `"game.py"` and `"GAME.PY"`, which give `True`. Then the awkward ones: `""`, and `"game.pyc"`, which has `.py` in it but does not end with it.

5. Which test is `True` only when `word` begins with `un`?

6. Ask for a sentence. If it ends with a question mark, print `That is a question.` Otherwise, print `That is not a question.`

> Check it: try `Is it raining?`, then `It is raining.` Then the awkward one: press Enter without typing anything.

### Try It

7. A library files a book called `The Hobbit` under H, as `Hobbit`. Write a function `drop_the(title)` that gives back `title` without `The ` at its start (a capital T, and a space after `The`). Any other title comes back as it was.

> Say it: a title goes in; if it starts with `The ` it comes out without those four characters, and otherwise it comes out unchanged. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. if the title starts with `The `, with its space, give back the rest of it, from index 4 on. 2. otherwise, give back the title as it was.
> Name it: the function and its parameter are named for you.
> Check it: try `"The Hobbit"`, which gives `"Hobbit"`, and `"Dune"`, which gives `"Dune"`. Then the awkward ones: `""`; and `"Theory of Everything"`, which starts with `The` but not with `The ` and a space, so it comes back as it was.

### What you can do now

- Ask whether a string starts with some text, with `startswith()`.
- Ask whether it ends with some text, with `endswith()`.
- Choose between them and `in`, which looks anywhere.

Key words: **startswith()**, **endswith()**.
