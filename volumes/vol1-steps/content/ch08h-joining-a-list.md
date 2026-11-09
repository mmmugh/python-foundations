<!-- part: Unit 8 — Strings as data -->
## Lesson 8.8 — Joining a list into text

`split()` turns a string into a list. In this lesson you go the other way: glue a list of strings into one string, with whatever you like between the pieces.

### Warm-up

1. Predict what this prints, then press Check.

```python
parts = "10:30".split(":")
print(parts)
print(int(parts[0]) * 60 + int(parts[1]))
```

2. What does `"Ada, Grace".split(",")` give back?

### Gluing a list together

`join()` glues the strings in a list into one string. The glue is the string you call it on, before the dot, and the list goes in the brackets:

```python
words = ["the", "quick", "brown", "fox"]
print(" ".join(words))
print("-".join(words))
print(", ".join(words))
```

Output:

```
the quick brown fox
the-quick-brown-fox
the, quick, brown, fox
```

It reads backward at first: the glue comes first, then the list. The glue goes only between the items, never after the last one. With the empty string as glue, the pieces touch:

```python
letters = ["c", "a", "t"]
print("".join(letters))
```

Output:

```
cat
```

### Practice

3. Predict what this prints, then press Check.

```python
parts = ["2026", "09", "17"]
print("/".join(parts))
print("".join(parts))
print(" - ".join(["a", "b"]))
```

4. Write a function `dashes(sentence)` that gives back the words of `sentence` with a dash between each two. So `dashes("the quick fox")` gives back `"the-quick-fox"`.

> Split it: split the sentence into words, then join them with `"-"`.
> Check it: try `"  hi  there "`, which gives `"hi-there"`. Then the awkward one: `""`, which gives `""`.

### Joining numbers

`join()` glues strings only. Give it a list of numbers, and Python stops:

```python
scores = [88, 92, 79]
print(", ".join(scores))
```

The last line of the error says `TypeError: sequence item 0: expected str instance, int found`. Item 0 is the item at index 0, and an instance is Python's word for one value of a kind; you don't need to remember it. It means: the first item is a whole number, and `join()` wanted a string.

So turn each number into a string first, with `str()` (lesson 3.4), in a loop that builds a new list (lesson 7.7):

```python
scores = [88, 92, 79]
texts = []
for score in scores:
    texts.append(str(score))
print(", ".join(texts))
```

Output:

```
88, 92, 79
```

### Practice

5. This program should print `3 + 1 + 4`, but it stops with an error. Run it and read the last line of the error. Then fix it.

```python
numbers = [3, 1, 4]
print(" + ".join(numbers))
```

6. Write a function `capitalize_words(sentence)` that gives back the words of `sentence`, each with a capital first letter and small letters after it, with one space between each two. So `capitalize_words("ada LOVELACE")` gives back `"Ada Lovelace"`.

> Split it: 1. split the sentence into words. 2. start a new, empty list. 3. for each word, append its first letter in capitals joined to the rest in small letters, as in `tidy_name()` from lesson 8.3. 4. join the new list with spaces, and give it back.
> Check it: try `"hello WORLD"`, which gives `"Hello World"`. Then the awkward one: `""`, which gives `""`.

### Another way to write it

Python has a method that does what `capitalize_words()` does, called `title()`, because book titles are written this way:

```python
print("the hobbit".title())
print("ada LOVELACE".title())
```

Output:

```
The Hobbit
Ada Lovelace
```

Writing it yourself first showed you how it works. Now you can use either.

### Practice

7. Predict what this prints, then press Check.

```python
name = "  grace HOPPER "
print(name.strip().title())
print(name.strip().upper())
```

### Try It

8. Write a function `initials(full_name)` that gives back the first letter of each word in `full_name`, in capitals, with nothing between them. So `initials("ada lovelace")` gives back `"AL"`.

> Say it: a full name goes in; the first letter of each of its words, in capitals, comes out as one string. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. split the name into words. 2. start a new, empty list. 3. for each word, append its first letter, in capitals. 4. join the list with `""`, and give it back.
> Name it: the function and its parameter are named for you. What would you call one word, and the list of letters?
> Check it: try `"Grace Brewster Hopper"`, which gives `"GBH"`. Then the awkward ones: `""`, which gives `""`, and a name with extra spaces, like `"  bo  "`, which gives `"B"`.

### What you can do now

- Glue a list of strings into one string with `join()`, and choose the glue.
- Turn numbers into strings with `str()` before you join them.
- Give every word a capital first letter with `title()`, or by hand.

Key words: **join()**, **title()**.
