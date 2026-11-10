<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.1 — Looking things up by name

In lesson 7.9, a gradebook kept the names in one list and the scores in another, matched by position. Sort one list and not the other, and the scores belong to the wrong students. In this lesson you keep each name together with its own score, and look the score up by the name.

### Warm-up

1. Predict what this prints, then press Check.

```python
words = "to be or not to be".split()
print(len(words))
print(words.count("be"))
print(words[3])
```

2. What does this print?

```python
names = ["Ada", "Grace", "Alan"]
scores = [88, 92, 45]
scores.sort()
print(names[0], scores[0])
```

### Looking up by name

A **dictionary** keeps values under names of your choosing:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
print(scores["Grace"])
print(len(scores))
```

Output:

```
92
3
```

Curly braces, `{ }`, the ones f-strings use, make a dictionary. Each entry is a **key**, a colon, and its **value**, and commas go between the entries. Here the keys are names and the values are scores. Put a key in square brackets after the dictionary's name, and you get its value, the way an index gets an item from a list. `len()` counts the entries: three keys, each with its value.

When Python prints a whole dictionary, it shows every entry, with single quotes around text, as it does for a list. `{}` is a dictionary with no entries:

```python
prices = {"apple": 0.5, "pear": 0.75}
print(prices)
ages = {}
print(ages)
```

Output:

```
{'apple': 0.5, 'pear': 0.75}
{}
```

### A key that is not there

Ask for a key the dictionary does not have, and Python stops:

```python
scores = {"Ada": 88, "Grace": 92}
print(scores["Alan"])
```

The last line of the error says `KeyError: 'Alan'`. A `KeyError` is Python's way of saying "there is no such key", and it names the key it could not find. Capitals matter, as they do for `==`: `"ada"` is not the key `"Ada"`.

A dictionary has no positions, so `scores[0]` is a `KeyError` too, unless 0 is one of the keys. And a lookup only goes one way, from a key to its value: `scores[88]` asks for a key called 88, not for whoever scored 88.

### Practice

3. Predict what this prints, then press Check.

```python
capitals = {"France": "Paris", "Japan": "Tokyo", "Peru": "Lima"}
print(capitals["Japan"])
print(len(capitals))
print(capitals)
stock = {}
print(stock)
```

4. Which of these gives Grace's score, 92?

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
```

5. This program should print the price of an apple, 0.5, but it stops with an error. Run it and read the last line of the error. Then fix it.

```python
prices = {"apple": 0.5, "pear": 0.75}
print(prices["Apple"])
```

### Adding and changing

Put a key in square brackets on the left of `=`, and you store a value under it. If the key is new, a new entry goes at the end. If the key is there already, its value changes:

```python
scores = {"Ada": 88, "Grace": 92}
scores["Alan"] = 45
scores["Ada"] = 91
print(scores)
```

Output:

```
{'Ada': 91, 'Grace': 92, 'Alan': 45}
```

The same line adds or changes, so a slip in a key adds an entry you did not mean. Capitals matter here too:

```python
stock = {"pens": 10}
stock["Pens"] = 3
print(stock)
```

Output:

```
{'pens': 10, 'Pens': 3}
```

A key can be in a dictionary only once. Write the same key twice between the braces, and the second one wins, just as if you had stored a value under it again:

```python
colors = {"sky": "blue", "sky": "grey"}
print(colors)
```

Output:

```
{'sky': 'grey'}
```

### Practice

6. Predict what this prints, then press Check.

```python
ages = {"Mo": 12, "Kim": 13}
ages["Lee"] = 12
ages["Mo"] = 13
ages["kim"] = 14
print(ages)
print(len(ages))
```

7. Fill in the table: the whole dictionary `fruit` after each line, written the way Python prints it. Then press Check.

```python
fruit = {"apple": 3, "apple": 5}
fruit["pear"] = 2
fruit["apple"] = fruit["apple"] + 1
```

8. A dictionary holds each friend's phone number, looked up by the friend's name. Which is the clearest name for it?

### Try It

9. Here is a phone book: names, each with a phone number. Add Lee, whose number is `555-0199`. Change Ada's number to `555-0111`. Then print exactly two lines: Ada's number, as `Ada: 555-0111`, and how many numbers the book holds, as `Numbers: 3`.

```python
phone_book = {"Ada": "555-0100", "Grace": "555-0142"}
```

> Say it: change the phone book in two ways, then print one number and how many there are. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. store Lee's number under the key `"Lee"`. 2. store Ada's new number under `"Ada"`. 3. print `Ada:` and the value under `"Ada"`. 4. print `Numbers:` and how many entries the book has.
> Name it: the book is named for you. A number with dashes in it is text, so it goes in quotes.
> Check it: run it and compare with the two lines asked for. Then the awkward one: change your step 2 to store the number under `"ada"`, with a small a. What does it print now, and why? Put the capital back before you press Check.

### What you can do now

- Keep values under keys, in a dictionary, and look one up by its key.
- Add an entry, or change one, by storing a value under its key.
- Read a `KeyError`, and fix a key that is not there.

Key words: **dictionary**, **key**, **value**, **KeyError**.
