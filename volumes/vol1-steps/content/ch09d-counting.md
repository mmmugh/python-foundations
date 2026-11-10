<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.4 — Keys and values together, and counting

A loop over a dictionary gives you its keys, and you look up each value. In this lesson one method gives you both at once. Then you use a dictionary to count things: how many votes each answer got, or how many times each word turns up.

### Warm-up

1. Predict what this prints, then press Check.

```python
prices = {"tea": 2, "cake": 3}
for item in prices:
    print(item, prices[item] * 2)
print(sum(prices.values()))
```

2. What does a `for` loop over a dictionary give you, each time round?

### Keys and values together

`items()` gives each entry as a pair: a key and its value together. Name both in the `for` line, with a comma between, as you did with `enumerate()` in lesson 7.7. The first name gets the key, and the second gets its value:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
for name, score in scores.items():
    print(f"{name}: {score}")
```

Output:

```
Ada: 88
Grace: 92
Alan: 45
```

Without `.items()`, the loop gets the keys only. One key cannot be split between two names, so `for name, score in scores:` goes wrong.

### Practice

3. Predict what this prints, then press Check.

```python
stock = {"pens": 3, "pads": 0, "clips": 12}
for item, count in stock.items():
    if count > 0:
        print(item, count)
```

4. This loop should print each name with its score. What does it need?

```python
scores = {"Ada": 88, "Grace": 92}
for name, score in scores:
    print(name, score)
```

### Counting

A class votes yes or no. A dictionary can count the votes: each answer is a key, and its value is how many times it has turned up so far. The first time an answer turns up, it is not a key yet, so the loop asks:

```python
votes = ["yes", "no", "yes", "yes"]
counts = {}
for vote in votes:
    if vote in counts:
        counts[vote] += 1
    else:
        counts[vote] = 1
print(counts)
```

Output:

```
{'yes': 3, 'no': 1}
```

`counts[vote] += 1` adds one to the value stored under `vote`, just as `total += 1` adds one to `total`. It needs the key to be there already, which is why the `if` asks first. A new answer starts at 1.

`get()` with a default of 0 does both cases in one line:

```python
votes = ["yes", "no", "yes", "yes"]
counts = {}
for vote in votes:
    counts[vote] = counts.get(vote, 0) + 1
print(counts)
```

Output:

```
{'yes': 3, 'no': 1}
```

`counts.get(vote, 0)` gives the count so far, or 0 the first time a vote turns up. One more than that is stored back under the vote. This is the **counting pattern**. Here is its trace table, up to line 4:

| After line | vote | counts |
| --- | --- | --- |
| 1 |  |  |
| 2 |  | {} |
| 3 | "yes" | {} |
| 4 | "yes" | {"yes": 1} |
| 3 | "no" | {"yes": 1} |
| 4 | "no" | {"yes": 1, "no": 1} |
| 3 | "yes" | {"yes": 1, "no": 1} |
| 4 | "yes" | {"yes": 2, "no": 1} |
| 3 | "yes" | {"yes": 2, "no": 1} |
| 4 | "yes" | {"yes": 3, "no": 1} |
| 3 | "yes" | {"yes": 3, "no": 1} |

The keys go in the order each answer first turned up.

### Practice

5. Fill in the table, then press Check. Write each dictionary the way Python prints it.

```python
word = "aba"
counts = {}
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1
```

6. Predict what this prints, then press Check.

```python
tally = {"red": 2}
for color in ["blue", "red", "blue"]:
    if color in tally:
        tally[color] += 1
    else:
        tally[color] = 1
print(tally)
```

7. Write a function `count_words(text)` that gives back a dictionary of how many times each word appears in `text`. The words have spaces between them.

> Split it: split the text into words. Start an empty dictionary, and count each word into it with the counting pattern. Give the dictionary back.
> Check it: try `"the cat and the hat"`, which gives `{"the": 2, "cat": 1, "and": 1, "hat": 1}`. Then the awkward one: `""`, which has no words, and gives `{}`.

8. Write a function `repeated(words)` that gives back a list of the words in the list `words` that appear more than once. Each one goes in the list once, in the order it first appears.

> Split it: 1. count the words with the counting pattern. 2. start an empty list. 3. loop over the counts with `items()`, and add each word whose count is more than 1.
> Check it: try `["a", "b", "a", "c", "b", "a"]`, which gives `["a", "b"]`. Then the awkward ones: `[]`, and `["x", "y"]`, where nothing repeats. Both give `[]`.

### Try It

9. Write a function `letter_counts(text)` that gives back a dictionary of how many times each letter appears in `text`. Capitals count as small letters, and anything that is not a letter, like a space or a `!`, is not counted. So `letter_counts("Banana!")` gives back `{"b": 1, "a": 3, "n": 2}`.

> Say it: a text goes in; a dictionary from each letter to how many times it appears comes out, with capitals made small and everything else left out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start an empty dictionary. 2. loop over the text, made small, one character at a time. 3. if the character is a letter, count it with the counting pattern. 4. give the dictionary back.
> Name it: the function and its parameter are named for you. What would you call one character, and the dictionary?
> Check it: try `"Banana!"`. Then the awkward ones: `""`, and `"123"`, which has no letters. Both give `{}`. And `"A man"`, where the capital A and the small a count together: `{"a": 2, "m": 1, "n": 1}`.

### What you can do now

- Loop over a dictionary's keys and values together, with `items()`.
- Count things into a dictionary, with an `if` or with `get()` and a default of 0.
- Trace a dictionary as it is built.

Key words: **items()**, **counting pattern**.
