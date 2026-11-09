<!-- part: Unit 8 — Strings as data -->
## Lesson 8.1 — Text is a sequence, and it can't change

Since lesson 1.1 you have printed strings as labels and messages. In this unit you treat text as data: you look inside it, take it apart and build new text from it. You already know most of the tools, because a string works a lot like a list.

### Warm-up

1. Predict what this prints, then press Check.

```python
names = ["Ada", "Grace", "Ada"]
print(names.index("Ada"))
print(names.count("Ada"))
print(len(names))
```

2. `names` and `scores` are parallel lists. Where is the score of the student in `names[2]`?

### A string is a sequence

A list is a sequence of items. A string is a **sequence** of characters, in order, so `len()` and indexes work on it as they do on a list in lesson 7.1:

```python
word = "Python"
print(len(word))
print(word[0])
print(word[-1])
```

Output:

```
6
P
n
```

`len()` counts the characters. Index 0 is the first character, and -1 is the last. A space is a character too, as in lesson 5.3, so `len("hi there")` is 8.

Slices work as they do in lesson 7.2. A slice of a string is a new string:

```python
word = "Python"
print(word[0:3])
print(word[2:])
print(word[::-1])
```

Output:

```
Pyt
thon
nohtyP
```

`[::-1]` steps backward through the whole string, so it gives the string turned around.

### Practice

3. Predict what this prints, then press Check.

```python
city = "Lisbon"
print(len(city))
print(city[1])
print(city[-2])
print(city[:3])
```

4. Predict what this prints, then press Check. Count the space.

```python
phrase = "top spot"
print(len(phrase))
print(phrase[4:])
print(phrase[::-1])
```

5. Write a function `ends(word)` that gives back the first and last characters of `word`, joined, so `ends("planet")` gives back `"pt"`. An empty word has no first character: give back `""` for it.

> Split it: first, if the word is `""`, give back `""`. Otherwise, join the character at index 0 and the one at index -1 with `+`.
> Check it: try `"planet"`, which gives `"pt"`. Then the awkward ones: `""`, and a word of one letter, `"a"`, which gives `"aa"`.

### A string can't change

Here is the big difference from a list. In lesson 7.3 you changed one item of a list with `=`. Try that on a string, and Python stops:

```python
word = "Python"
word[0] = "J"
```

The last line of the error says `TypeError: 'str' object does not support item assignment`. Item assignment is Python's name for changing one item with `=`; you don't need to remember it. A string is **immutable**: once it is made, it never changes.

What you can do is make a new string from pieces of the old one, with `+` and a slice:

```python
word = "Python"
new_word = "J" + word[1:]
print(new_word)
print(word)
```

Output:

```
Jython
Python
```

`word[1:]` is everything after the first character. The old string is still there, as it was.

### Practice

6. This program should print `Grace`, but it stops with an error. Run it and read the last line of the error. Then fix it, so that it makes a new string.

```python
name = "grace"
name[0] = "G"
print(name)
```

> Split it: keep everything after the first character, with a slice, and put a capital `G` in front of it with `+`.

7. After these two lines, what is in `word`?

```python
word = "cat"
new_word = "b" + word[1:]
```

### Try It

8. Ask for a word. Print it forward, then backward, then how many characters it has, one per line, like this for `stressed`: `Forward: stressed`, then `Backward: desserts`, then `Length: 8`.

> Say it: a word goes in; it comes out as it is, then turned around, then its length. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. ask for the word. 2. print it. 3. print it turned around, with a slice. 4. print its length.
> Name it: what would you call the word that was typed? And the turned-around one, if you give it a name?
> Check it: try stressed, which turns into desserts. Then the awkward ones: a word of one letter, and a phrase with a space in it, like `top spot`, where the space counts.

### What you can do now

- Find a character in a string by its index, and count the characters with `len()`.
- Slice a string, and turn it around with `[::-1]`.
- Make a new string from pieces of an old one, because a string can't change.

Key words: **sequence**, **immutable**.
