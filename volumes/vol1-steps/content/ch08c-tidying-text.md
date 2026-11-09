<!-- part: Unit 8 — Strings as data -->
## Lesson 8.3 — Tidying text

What people type is often untidy: a space too many, a word you want changed. In this lesson you meet two more string methods, one that trims spaces off the ends and one that swaps one piece of text for another, and you use two methods one after the other.

### Warm-up

1. Predict what this prints, then press Check.

```python
word = "Hello"
word.lower()
print(word)
print(word.upper())
```

2. `answer` holds what someone typed. Which test is `True` for `yes`, `YES` and `Yes`?

### Trimming the ends

`strip()` gives back the string without the spaces at its start and its end:

```python
typed = "   Ada   "
print(f"[{typed}]")
print(f"[{typed.strip()}]")
```

Output:

```
[   Ada   ]
[Ada]
```

The brackets show where the string starts and ends, as in lesson 5.3. Spaces in the middle are not at an end, so they stay:

```python
full_name = "  Ada Lovelace  "
print(f"[{full_name.strip()}]")
```

Output:

```
[Ada Lovelace]
```

### Practice

3. Predict what this prints, then press Check. Count the spaces.

```python
city = "  New York "
print(len(city))
tidy = city.strip()
print(f"[{tidy}]")
print(len(tidy))
```

### Two methods in a row

In lesson 8.2, `Yes` matched once it was made small. But people also type spaces, and then it doesn't:

```python
answer = "  Yes "
print(answer.lower() == "yes")
print(answer.strip().lower() == "yes")
```

Output:

```
False
True
```

Read the second line from left to right. `answer.strip()` gives back `"Yes"`, and `.lower()` works on that, and gives back `"yes"`. Each method works on what the one before it gave back. Strip the spaces, then fix the capitals: do both to anything a person types before you compare it.

### Practice

4. Write a function `is_yes(answer)` that gives back `True` if `answer` is yes, with any capitals and any spaces at its ends, and `False` if not.

> Check it: try `" YES "`, which gives `True`. Then the awkward ones: `""`, which gives `False`; and `"y e s"`, which also gives `False`, because its spaces are in the middle.

### Swapping text

`replace()` takes two strings: what to find, and what to put in its place. It gives back a new string with every match swapped:

```python
sentence = "I like cats. cats are fun. Cats too."
print(sentence.replace("cats", "dogs"))
```

Output:

```
I like dogs. dogs are fun. Cats too.
```

Both `cats` changed, but not `Cats`: a capital C is a different character. To take something out, put the empty string, `""`, in its place:

```python
phone = "555-867-5309"
print(phone.replace("-", ""))
print(phone)
```

Output:

```
5558675309
555-867-5309
```

And, as with every string method, `phone` itself is as it was.

### Practice

5. Predict what this prints, then press Check.

```python
spell = "Abracadabra"
print(spell.replace("a", "o"))
print(spell.replace("bra", ""))
print(spell)
```

6. Write a function `no_spaces(text)` that gives back `text` with every space taken out, the ones in the middle too. So `no_spaces("top spot")` gives back `"topspot"`.

> Split it: `strip()` only trims the ends. Which method can take out every space?
> Check it: try `"a b c"`, which gives `"abc"`. Then the awkward one: `""`.

### Try It

7. Write a function `tidy_name(name)` that gives back a name tidied up: no spaces at its ends, a capital first letter, and small letters after it. So `tidy_name("  aDA ")` gives back `"Ada"`. If nothing is left after the spaces are gone, give back `""`.

> Say it: a messy name goes in; the same name comes out with no spaces at its ends, a capital first, and small letters after. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. strip the spaces from the ends. 2. if what is left is `""`, give it back. 3. join the first character, in capitals, and the rest, in small letters (lesson 8.1's slice `[1:]` is the rest). 4. give that back.
> Name it: the function and its parameter are named for you. What would you call the name once it is stripped?
> Check it: try `"  aDA "`, which gives `"Ada"`, and `"grace"`, which gives `"Grace"`. Then the awkward ones: `""`, and a name that is only spaces, `"   "`. Both give `""`.

### What you can do now

- Trim the spaces off both ends of a string with `strip()`.
- Swap every match of one piece of text for another with `replace()`, or take it out with `""`.
- Use two methods in a row, each working on what the one before gave back.

Key words: **strip()**, **replace()**.
