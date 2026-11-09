<!-- part: Unit 8 — Strings as data -->
## Lesson 8.2 — Capital letters, and keeping the result

In lesson 7.3, `append()` was your first method: a function that belongs to a value, called after a dot. Strings have methods too. In this lesson you meet two that change capital letters, and find out what "change" means for a string that can't change.

### Warm-up

1. Predict what this prints, then press Check.

```python
word = "rocket"
print(word[1:4])
print(word[-1])
print(len(word))
```

2. `word` is `"rocket"`. What does `word[0] = "P"` do?

### Capitals and small letters

`upper()` gives back the string in capital letters, and `lower()` gives it back in small letters:

```python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

Output:

```
ADA LOVELACE
ada lovelace
```

Only letters change. Digits, spaces and signs stay as they are:

```python
print("R2-D2 says hi!".upper())
```

Output:

```
R2-D2 SAYS HI!
```

### Practice

3. Predict what this prints, then press Check.

```python
team = "Blue Jays 2"
print(team.upper())
print(team.lower())
```

4. Ask for a name, and print it in capital letters.

> Check it: try Ada Lovelace, which prints ADA LOVELACE. Then the awkward one: a name that is in capitals already.

### Keep the result

A string can't change (lesson 8.1), so `upper()` can't change one either. It makes a new string and gives it back. If nothing keeps that new string, it is lost:

```python
word = "python"
word.upper()
print(word)
```

Output:

```
python
```

To keep it, put it in a variable, with `=`. Here it goes back into `word`:

```python
word = "python"
word = word.upper()
print(word)
```

Output:

```
PYTHON
```

Every string method works this way: it gives back a new string, like `sorted()` in lesson 7.6, and the old one is left as it was.

### Practice

5. This program should print `SHOUT`, but it prints `shout`. Run it, then fix it.

```python
message = "shout"
message.upper()
print(message)
```

6. Predict what this prints, then press Check.

```python
city = "Oslo"
loud = city.upper()
city.lower()
print(city)
print(loud)
```

### Comparing text safely

Capitals are different characters (lesson 3.5), so a person who types `Yes` has not typed `yes`:

```python
answer = "Yes"
print(answer == "yes")
print(answer.lower() == "yes")
```

Output:

```
False
True
```

Turn what was typed into small letters before you compare it. Then `Yes`, `YES` and `yes` all match.

### Practice

7. Ask `Do you like pizza?`. If the answer is yes, typed in any capitals, print `Me too!`. Otherwise, print `Oh well.`

> Check it: try yes, then YES, then no. Each prints one line.

8. Write a function `same_word(first, second)` that gives back `True` if the two words are the same when you ignore capitals, and `False` if not.

> Split it: which side of the `==` needs `lower()`? Try `"ADA"` and `"Ada"`.
> Check it: try `"Ada"` and `"ada"`, which gives `True`. Then the awkward ones: `""` and `""`, which gives `True`, and `"Cat"` and `"cats"`, which gives `False`.

### Try It

9. Write a function `count_letter(text, letter)` that gives back how many times `letter` appears in `text`, ignoring capitals. So `count_letter("Banana", "b")` gives back 1, and `count_letter("Anna", "A")` gives back 2.

> Say it: a text and one letter go in; how many times that letter is in the text, capital or small, comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. make the text and the letter both small letters. 2. start a count at 0. 3. loop over the text, and add 1 for each character that is the letter. 4. after the loop, give back the count.
> Name it: the function and its parameters are named for you. What does the count count?
> Check it: try `"Banana"` and `"a"`, which gives 3. Then the awkward ones: an empty text, `""`, which gives 0; and a capital letter to look for, as in `"Anna"` and `"A"`.

### What you can do now

- Change a string to capital letters with `upper()`, or small letters with `lower()`.
- Keep what a string method gives back, because the old string never changes.
- Compare text safely, by making both sides small letters first.

Key words: **upper()**, **lower()**.
