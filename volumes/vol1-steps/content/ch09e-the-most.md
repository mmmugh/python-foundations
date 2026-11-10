<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.5 — Which key has the most?

`max()` of a dictionary's values gives the top score, but not who got it. In this lesson you find the key with the biggest value, and put the keys in order by their values, from the most to the least.

### Warm-up

1. Predict what this prints, then press Check.

```python
counts = {}
for letter in "noon":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)
for letter, count in counts.items():
    print(letter, count)
```

2. In the counting pattern, `counts[letter] = counts.get(letter, 0) + 1`, what does `counts.get(letter, 0)` give back the first time a letter turns up?

### The key with the biggest value

Give `max()` a dictionary, and it looks at the keys, as a loop does. Keys that are text are compared in alphabetical order, as in lesson 7.6, so the "biggest" key is the one that comes last:

```python
scores = {"Ada": 88, "Zoe": 45, "Grace": 92}
print(max(scores.values()))
print(max(scores))
```

Output:

```
92
Zoe
```

Zoe has the lowest score, but her name comes last in the alphabet. To compare the keys by their values instead, tell `max()` how to compare them, with `key=`:

```python
scores = {"Ada": 88, "Zoe": 45, "Grace": 92, "Bo": 45}
best = max(scores, key=scores.get)
print(best, scores[best])
worst = min(scores, key=scores.get)
print(worst, scores[worst])
```

Output:

```
Grace 92
Zoe 45
```

`key=scores.get` means "compare each key by what `scores.get` gives back for it", which is its value. There are no brackets after `get`: you are not using the method yourself, but naming it, for `max()` to use on each key in turn. What comes back is still a key, the one with the biggest value. `min()` works the same way.

Zoe and Bo both scored 45. When values tie, `max()` and `min()` give back the first of them, in the dictionary's order.

### Practice

3. Predict what this prints, then press Check.

```python
votes = {"pizza": 6, "tacos": 4, "sushi": 4, "salad": 1}
print(max(votes))
print(max(votes, key=votes.get))
print(min(votes, key=votes.get))
ties = {"tacos": 4, "sushi": 4}
print(max(ties, key=ties.get))
```

4. Why are there no brackets after `get` in `max(scores, key=scores.get)`?

5. Write a function `top_scorer(scores)` that gives back the name with the highest score in the dictionary `scores`, or `None` if it is empty. If two names tie, give back the first of them.

> Split it: first, if `scores` has no entries, give back `None`. Otherwise, give back the key with the biggest value.
> Check it: try `{"Ada": 88, "Grace": 92, "Alan": 45}`, which gives `"Grace"`. Then the awkward ones: `{}`, which gives `None`, and `{"Mo": 70, "Kim": 70}`, which gives `"Mo"`.

### Ranking

`sorted()` of a dictionary gives back a list of its keys, in order. With `key=`, the order is by value, from the smallest up. `reverse=True` turns any sorted order around, so the biggest comes first:

```python
scores = {"Mo": 88, "Zoe": 45, "Grace": 92, "Ada": 88}
print(sorted(scores))
print(sorted(scores, key=scores.get))
print(sorted(scores, key=scores.get, reverse=True))
print(sorted([45, 92, 88], reverse=True))
```

Output:

```
['Ada', 'Grace', 'Mo', 'Zoe']
['Zoe', 'Mo', 'Ada', 'Grace']
['Grace', 'Mo', 'Ada', 'Zoe']
[92, 88, 45]
```

Mo and Ada both scored 88. Keys whose values tie stay in the dictionary's order, Mo before Ada, even with `reverse=True`.

A loop over the sorted keys prints a ranking, top first:

```python
scores = {"Mo": 88, "Zoe": 45, "Grace": 92, "Ada": 88}
for name in sorted(scores, key=scores.get, reverse=True):
    print(name, scores[name])
```

Output:

```
Grace 92
Mo 88
Ada 88
Zoe 45
```

### Practice

6. Predict what this prints, then press Check.

```python
stock = {"pens": 3, "pads": 7, "clips": 12, "caps": 3}
print(sorted(stock))
print(sorted(stock, key=stock.get))
print(sorted(stock, key=stock.get, reverse=True))
print(sorted([3, 1, 2], reverse=True))
```

7. Write a function `top_three(counts)` that gives back a list of the three keys in `counts` with the biggest values, biggest first. Keys whose values tie stay in the dictionary's order. If there are fewer than three keys, give back all of them, in the same order.

> Split it: sort the keys by their values, biggest first. Then give back a slice of the first three (lesson 7.2).
> Check it: try `{"a": 1, "b": 5, "c": 3, "d": 4}`, which gives `["b", "d", "c"]`. Then the awkward ones: `{}`, which gives `[]`, and `{"x": 2, "y": 2}`, which gives `["x", "y"]`.

### Try It

8. Write a function `most_common(text)` that gives back the character that appears most often in `text`, not counting spaces. Capitals and small letters are different characters. If two characters tie, give back the one that appears first. If there is nothing to count, give back `None`.

> Say it: a text goes in; the character it has the most of, apart from spaces, comes out, or `None`. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. count the characters that are not spaces, with the counting pattern. 2. if nothing was counted, give back `None`. 3. give back the key with the biggest count.
> Name it: the function and its parameter are named for you. What would you call one character, and the dictionary of counts?
> Check it: try `"hello world"`, which gives `"l"`. Then the awkward ones: `""` and `"   "`, which both give `None`; and `"abba"`, a tie, which gives `"a"`.

### What you can do now

- Find the key with the biggest or smallest value, with `key=`.
- Sort a dictionary's keys by their values, biggest first with `reverse=True`.
- Say what happens when values tie.

Key words: **key=**, **reverse=True**.
