<!-- part: Unit 8 — Strings as data -->
## Lesson 8.7 — Splitting text into a list

A sentence is made of words, and a line like `Ada,88,92` is made of pieces with commas between them. In this lesson one method cuts a string into those pieces, and gives them back as a list, which you already know how to use.

### Warm-up

1. Predict what this prints, then press Check.

```python
print("42".isdigit())
print("4 2".isdigit())
print("Ada".isalpha())
print("Ada!".isalpha())
```

2. Lesson 8.6 asked for a whole number with `while not age.isdigit():`. Why `while`, and not `if`?

### Cutting at the spaces

`split()` cuts a string into pieces, and gives back a list of them. With nothing in its brackets, it cuts at the spaces, so the pieces are the words:

```python
sentence = "the quick brown fox"
words = sentence.split()
print(words)
print(len(words))
```

Output:

```
['the', 'quick', 'brown', 'fox']
4
```

A run of several spaces counts as one cut, and spaces at the ends are dropped, so there are no empty pieces:

```python
messy = "  one   two three "
print(messy.split())
```

Output:

```
['one', 'two', 'three']
```

What comes back is a list like any in unit 7: you can index it, slice it, take its `len()` or loop over it.

### Practice

3. Predict what this prints, then press Check.

```python
line = "red  green blue"
colors = line.split()
print(colors)
print(colors[1])
print(len(colors))
```

4. Write a function `first_word(sentence)` that gives back the first word of `sentence`, or `""` if it has no words.

> Split it: split the sentence into words. If the list of words is empty, give back `""`; otherwise give back the word at index 0.
> Check it: try `"  hello world"`, which gives `"hello"`. Then the awkward ones: `""` and `"   "`, which both give `""`.

### Cutting at something else

Put a string in the brackets, and `split()` cuts wherever that string is:

```python
date = "2026-09-17"
parts = date.split("-")
print(parts)
print(parts[0])
```

Output:

```
['2026', '09', '17']
2026
```

The pieces are strings, even when they look like numbers. To do arithmetic with one, turn it into a number with `int()`, as in lesson 2.3:

```python
row = "Ada,88,92"
parts = row.split(",")
print(parts[0])
print(int(parts[1]) + int(parts[2]))
```

Output:

```
Ada
180
```

The separator has to match exactly. Here the names have a comma and a space between them. Cut at the comma alone, and the space stays at the start of the next piece:

```python
names = "Ada, Grace, Alan"
print(names.split(","))
print(names.split(", "))
```

Output:

```
['Ada', ' Grace', ' Alan']
['Ada', 'Grace', 'Alan']
```

### Practice

5. Predict what this prints, then press Check.

```python
time = "14:05:30"
pieces = time.split(":")
print(pieces)
print(int(pieces[1]) + 1)
print("x; y".split(";"))
```

6. Write a function `total_of(line)` that gives back the total of the whole numbers in `line`, which has commas between them, like `"3,4,5"`. An empty line, `""`, has no numbers: give back 0 for it.

> Split it: first, if the line is `""`, give back 0. Otherwise: split at the commas; start a total at 0; loop over the pieces, and add each one, turned into a number.
> Check it: try `"3,4,5"`, which gives 12. Then the awkward ones: `""`, and numbers below 0, like `"-2,5"`, which gives 3.

### Try It

7. Ask for a sentence, and print how many words it has.

> Say it: a sentence goes in; the number of words in it comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. ask for the sentence. 2. split it into a list of words. 3. print how many items the list has.
> Name it: what would you call the sentence, and the list of its words?
> Check it: try `the quick brown fox`, which has 4. Then the awkward ones: extra spaces, as in `  hello   world  `, which has 2; and pressing Enter without typing anything, which has 0.

### What you can do now

- Cut a string into a list of words with `split()`.
- Cut it at a separator of your choice, like `split(",")`, which must match exactly.
- Turn the pieces into numbers with `int()` when you need to add them.

Key words: **split()**, **separator**.
