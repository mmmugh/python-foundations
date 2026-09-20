<!-- part: Part II — Structuring Data -->
## Chapter 9 — Dictionaries and Sets

Chapter 7's gradebook kept names in one list and scores in another, matched by position. That works until something disturbs the order, and then it fails quietly, handing out grades to the wrong students. The problem is that the connection between a name and a score lived nowhere in the program — it was a convention the programmer had to remember.

A **dictionary** stores that connection directly.

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

Curly braces create a dictionary. Each entry is a **key**, a colon, and a **value**. You look things up by key rather than by position, which is both clearer and — for reasons Chapter 11 makes precise — dramatically faster on large collections.

### Reading, adding, and changing

```python
scores = {"Ada": 88, "Grace": 92}

scores["Alan"] = 45
scores["Ada"] = 91
print(scores)

del scores["Alan"]
print(scores)
```

Output:

```
{'Ada': 91, 'Grace': 92, 'Alan': 45}
{'Ada': 91, 'Grace': 92}
```

Assigning to a key that exists changes its value; assigning to one that does not adds it. There is no separate "add" operation, which is convenient and occasionally lets a typo create an entry you did not intend.

Looking up a missing key raises an error:

```python
scores = {"Ada": 88}
print(scores["Grace"])
```

```
KeyError: 'Grace'
```

There are two ways to avoid that. Test with `in`, or use `.get()`, which returns `None` — or a default you supply — instead of raising:

```python
scores = {"Ada": 88}

if "Grace" in scores:
    print(scores["Grace"])
else:
    print("No score recorded.")

print(scores.get("Grace"))
print(scores.get("Grace", 0))
```

Output:

```
No score recorded.
None
0
```

`.get(key, default)` is the tool that makes counting work, as you will see shortly.

### Looping over a dictionary

Three loops, depending on what you need:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}

for name in scores:
    print(name)

print()

for score in scores.values():
    print(score)

print()

for name, score in scores.items():
    print(f"{name}: {score}")
```

Output:

```
Ada
Grace
Alan

88
92
45

Ada: 88
Grace: 92
Alan: 45
```

Looping over a dictionary directly gives you the **keys**. `.values()` gives the values, and `.items()` gives both at once — which is what you want most of the time.

Dictionaries remember insertion order, so these loops always produce entries in the order they were added.

The built-in functions work on values:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}

print(sum(scores.values()))
print(max(scores.values()))
print(sum(scores.values()) / len(scores))
```

Output:

```
225
92
75.0
```

To find *which key* has the largest value, `max()` accepts a `key` argument naming how to compare:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
top = max(scores, key=scores.get)
print(f"{top} has the highest score: {scores[top]}")
```

Output:

```
Grace has the highest score: 92
```

### Counting: the killer application

Counting occurrences is the thing dictionaries do best, and the pattern is worth memorizing.

```python
text = "the quick brown fox jumps over the lazy dog the end"
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1

print(counts["the"])
print(counts)
```

Output:

```
3
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'end': 1}
```

The whole trick is one line: `counts.get(word, 0)` returns the current count, or `0` if this is the first sighting, and adding one and storing it handles both cases identically. Without `.get()` you would need an `if` to check whether the key exists yet.

To see the most common items, sort by value:

```python
text = "the quick brown fox jumps over the lazy dog the end"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1

ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

for word, count in ranked[:3]:
    print(f"{word:<8}{count}")
```

Output:

```
the     3
quick   1
brown   1
```

That `key=lambda pair: pair[1]` says "compare these by their second element." A `lambda` is a small unnamed function; here it takes a `(word, count)` pair and returns the count. You do not need to write lambdas to work through this course, but they appear constantly in real code and this is by far their most common use.

### Nested dictionaries

A value can itself be a dictionary, which is how you store several facts about each key:

```python
students = {
    "Ada": {"score": 88, "grade": "B", "absences": 2},
    "Grace": {"score": 92, "grade": "A", "absences": 0},
}

print(students["Ada"]["score"])
print(students["Grace"]["absences"])

for name, record in students.items():
    print(f"{name}: {record['score']} ({record['grade']})")
```

Output:

```
88
0
Ada: 88 (B)
Grace: 92 (A)
```

Note the single quotes inside the f-string: `{record['score']}`. The f-string itself uses double quotes, so the key inside must use the other kind.

### Sets

A **set** is an unordered collection with no duplicates. It answers one question extremely well: is this thing in here?

```python
vowels = {"a", "e", "i", "o", "u"}

print("e" in vowels)
print(len(vowels))

numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)
print(len(unique))
```

Output:

```
True
5
{1, 2, 3, 4}
4
```

Passing a list to `set()` removes duplicates in one step, which is by far its most common use. Note that `{}` alone creates an empty *dictionary*, not a set; for an empty set you need `set()`.

Sets support the operations from mathematics:

```python
band = {"Ada", "Grace", "Alan"}
chorus = {"Grace", "Alan", "Katherine"}

print(band | chorus)
print(band & chorus)
print(band - chorus)
```

Output:

```
{'Ada', 'Grace', 'Alan', 'Katherine'}
{'Grace', 'Alan'}
{'Ada'}
```

Union (`|`) is everyone in either; intersection (`&`) is those in both; difference (`-`) is those in the first but not the second. Sets are unordered, so the display order may vary between runs — do not rely on it.

### Choosing a container

This is the practical payoff of Part II.

| Use | When |
| --- | --- |
| **List** | Order matters, duplicates are fine, you access by position |
| **Dictionary** | You look things up by a name or ID |
| **Set** | You care only about membership and uniqueness |

Ask yourself: *how will I look this up later?* By position → list. By name → dictionary. Only "is it there?" → set. Choosing well makes the rest of the program shorter; choosing badly means writing loops to compensate for the wrong structure, which is most of what a struggling program is doing.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| `scores["Bob"]` when Bob is absent | `KeyError` — use `.get()` or test with `in` |
| `{}` expecting an empty set | It is an empty dictionary; use `set()` |
| Using a list as a key | `TypeError` — keys must be unchangeable |
| Expecting a set to keep order | Sets are unordered by design |
| Two identical keys in one literal | The last one silently wins |
| `for name, score in scores:` | Needs `.items()`; without it you get keys only |

### Try It

1. Build a dictionary of five countries and their capitals, then let the user look one up.
2. Count the letter frequencies in a word the user enters.
3. Given two lists of names, print those in both, those in only the first, and the full set.
4. Write `invert(d)` that swaps keys and values.
5. Store three students each with a name, grade level, and favorite subject, then print a formatted roster.
6. Given a list of words, print the ones that appear more than once.
7. Find the most common character in a sentence, ignoring spaces.

### Chapter project: a poll counter

Build a program that tallies votes, reports the results with a bar chart, and handles ties correctly.

```python
# Tallies votes and displays the results as a text bar chart.


def tally(votes):
    """Return a dictionary mapping each option to its number of votes."""
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts


def winners(counts):
    """Return a list of every option tied for the most votes."""
    if not counts:
        return []
    best = max(counts.values())
    return [option for option, count in counts.items() if count == best]


def report(counts, total):
    """Print each option with its count, percentage, and a bar."""
    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

    print(f"{'Option':<12}{'Votes':>6}{'Share':>8}  Chart")
    print("-" * 46)
    for option, count in ranked:
        share = count / total * 100
        bar = "#" * round(share / 4)
        print(f"{option:<12}{count:>6}{share:>7.1f}%  {bar}")
    print("-" * 46)


votes = [
    "pizza", "tacos", "pizza", "sushi", "pizza",
    "tacos", "salad", "sushi", "pizza", "tacos",
    "sushi", "pizza", "tacos", "pizza", "sushi",
]

counts = tally(votes)
report(counts, len(votes))

print(f"Total votes:  {len(votes)}")
print(f"Options used: {len(set(votes))}")

leaders = winners(counts)
if len(leaders) == 1:
    print(f"Winner:       {leaders[0]}")
else:
    print(f"Tied:         {', '.join(sorted(leaders))}")
```

Output:

```
Option       Votes   Share  Chart
----------------------------------------------
pizza            6   40.0%  ##########
tacos            4   26.7%  #######
sushi            4   26.7%  #######
salad            1    6.7%  ##
----------------------------------------------
Total votes:  15
Options used: 4
Winner:       pizza
```

Three points.

`winners()` returns a **list**, not a single option, because ties are possible and a program that assumes otherwise reports a false result the first time two options match. Deciding what to do about ties is a design question, and the honest answer is usually to report them rather than to pick arbitrarily.

`len(set(votes))` counts the distinct options in one expression. That is the set doing exactly the job it is for.

The bar chart divides the percentage by 4 so that 100% is 25 characters wide. Scaling a chart to fit the space available is a small thing that makes text output far more readable, and `round()` keeps the bars to whole characters.

Try changing the vote list so that two options tie for first, and confirm the program says so.
