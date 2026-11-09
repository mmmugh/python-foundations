<!-- part: Unit 8 — Strings as data -->
## Lesson 8.4 — Is it there, and where?

In lesson 5.3, testing for a vowel took five comparisons joined with `or`. In this lesson one word, `in`, does that job, and a method tells you where in a string a piece of text is.

### Warm-up

1. Predict what this prints, then press Check.

```python
code = "  ab-12  "
tidy = code.strip()
print(tidy.upper())
print(tidy.replace("-", ""))
```

2. What does `"a b c".strip()` give back?

### Is it in there?

`in` asks whether one string is inside another. The answer is `True` or `False`:

```python
sentence = "The quick brown fox"
print("quick" in sentence)
print("slow" in sentence)
print("Quick" in sentence)
```

Output:

```
True
False
False
```

`Quick` is not there, because a capital Q is a different character. One character can be looked for in a string of them, so this is the vowel test from lesson 5.3, in one comparison:

```python
letter = "e"
print(letter in "aeiou")
print("z" in "aeiou")
```

Output:

```
True
False
```

`in` works on a list too, where it looks for a whole item, never part of one. And `not in` asks the opposite question:

```python
guests = ["Ada", "Grace", "Alan"]
print("Grace" in guests)
print("Gra" in guests)
print("Bo" not in guests)
```

Output:

```
True
False
True
```

### Practice

3. Predict what this prints, then press Check.

```python
word = "banana"
print("nan" in word)
print("Nan" in word)
print("x" not in word)
pets = ["cat", "dog"]
print("ca" in pets)
```

4. Write a function `count_vowels(text)` that gives back how many vowels are in `text`: `a`, `e`, `i`, `o` and `u`, small or capital.

> Split it: loop over the text with a counter, as in lesson 5.3. The test is one `in`. Which method makes the capitals count too?
> Check it: try `"Hello World"`, which gives 3. Then the awkward ones: `""`, which gives 0, and `"AEIOU"`, which gives 5.

### Where is it?

`in` tells you whether. `find()` tells you where: the index where the first match starts, or -1 if there is no match:

```python
word = "banana"
print(word.find("n"))
print(word.find("nan"))
print(word.find("b"))
print(word.find("x"))
```

Output:

```
2
2
0
-1
```

0 is a real place, the very start. -1 means "not found", so a test for "not found" compares with -1, never with 0.

`count()` works on a string as it does on a list in lesson 7.9. It counts how many times the text appears:

```python
word = "banana"
print(word.count("a"))
print(word.count("an"))
print(word.count("x"))
```

Output:

```
3
2
0
```

### Practice

5. Predict what this prints, then press Check.

```python
email = "ada@example.com"
print(email.find("@"))
print(email.find("a"))
print(email.find("!"))
print(email.count("a"))
```

6. `text.find("cat")` gives back 0. What does that tell you?

7. Write a function `before_at(email)` that gives back the part of `email` before its `@`. If there is no `@`, give back the whole of `email`. So `before_at("ada@example.com")` gives back `"ada"`.

> Split it: 1. find where the `@` is. 2. if it is not found, give back the whole email. 3. otherwise give back a slice that stops at the `@`.
> Check it: try `"ada@example.com"`, which gives `"ada"`. Then the awkward ones: `"no-at-sign"`, which gives `"no-at-sign"`; `""`; and `"@home"`, which gives `""`.

### Try It

8. Write a function `is_spam(message)` that gives back `True` if `message` has `free` or `winner` anywhere in it, in any capitals, and `False` if not.

> Say it: a message goes in; `True` comes out if it has either of two words in it, capital or small, and `False` if not. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. make the message small letters. 2. ask whether `free` is in it, or `winner` is. 3. give back the answer.
> Name it: the function and its parameter are named for you. What would you call the message in small letters?
> Check it: try `"FREE pizza!"` and `"You are a Winner"`, which both give `True`, and `"See you at 6"`, which gives `False`. Then the awkward one: `""`.

### What you can do now

- Ask whether text is in a string, or an item in a list, with `in` and `not in`.
- Find where text starts with `find()`, which gives back -1 when it is not there.
- Count how many times text appears with `count()`.

Key words: **in**, **find()**.
