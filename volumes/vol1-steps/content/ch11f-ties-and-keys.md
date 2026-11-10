<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.6 — What Python does, and breaking ties

You have written two searches and two sorts by hand. In this lesson you see how Python's own sort compares with them, and you settle a question every sort has to answer: when two items tie, which comes first?

### Warm-up

1. Predict what this prints, then press Check.

```python
def is_sorted(items):
    for position in range(len(items) - 1):
        if items[position] > items[position + 1]:
            return False
    return True


print(is_sorted([1, 4, 4, 9]))
print(is_sorted([2, 1]))
print(is_sorted([]))
```

2. A bubble sort that stops early is given a list that is sorted already. How many passes does it make?

### What Python does

`sorted()` and `sort()` use a cleverer method than either of your sorts. For 1,000 jumbled numbers, a selection sort makes 499,500 comparisons; Python's sort makes fewer than 9,000. It has also been tested on far more lists than you could try. So in your own programs, sort with `sorted()` or `sort()`. The sorts you wrote by hand are for seeing how sorting works, not for everyday use.

You know `reverse=True` and `key=` already. A method can be the key too:

```python
words = ["banana", "Cherry", "apple"]
print(sorted(words))
print(sorted(words, reverse=True))
print(sorted(words, key=str.lower))
```

Output:

```
['Cherry', 'apple', 'banana']
['banana', 'apple', 'Cherry']
['apple', 'banana', 'Cherry']
```

Every capital comes before every small letter, so `Cherry` sorts first. `str.lower` is the `lower()` method that every piece of text has, named without brackets so it is not called yet, as `key=scores.get` named `get()` in lesson 9.5. `sorted()` is handed the method, and calls it on each word itself, as if it ran `word.lower()`. It compares the small-letter copies, and gives back the words as they were.

### Practice

3. Predict what this prints, then press Check.

```python
names = ["bo", "Cy", "ada", "Al"]
print(sorted(names))
print(sorted(names, key=str.lower))
print(sorted(names, key=str.lower, reverse=True))
```

4. Why should a real program sort with `sorted()`, rather than with a sort you wrote yourself?

### Breaking ties

Two items that compare equal tie, as two options did in lesson 9.10's poll. `sorted()` keeps tied items in the order they had, as in lesson 9.5, and so does your bubble sort: it swaps only when the left item is bigger, so equal items never pass each other:

```python
results = [
    {"name": "Omar", "seconds": 61.0},
    {"name": "Priya", "seconds": 58.2},
    {"name": "Nadia", "seconds": 58.2},
]
for runner in sorted(results, key=lambda record: record["seconds"]):
    print(runner["name"], runner["seconds"])
```

Output:

```
Priya 58.2
Nadia 58.2
Omar 61.0
```

Priya and Nadia tie, and Priya was first in the list, so she stays first. To **break a tie** with a rule of your own, by name say, you need tuples. Tuples are compared item by item: the first items decide, and only when they are equal do the second items get a say:

```python
print((58.2, "Priya") < (58.2, "Nadia"))
print((57.4, "Zed") < (58.2, "Ada"))
```

Output:

```
False
True
```

So a key that gives back a tuple, the time and then the name, sorts by time, and breaks a tie by name:

```python
results = [
    {"name": "Omar", "seconds": 61.0},
    {"name": "Priya", "seconds": 58.2},
    {"name": "Nadia", "seconds": 58.2},
]
for runner in sorted(results, key=lambda record: (record["seconds"], record["name"])):
    print(runner["name"], runner["seconds"])
```

Output:

```
Nadia 58.2
Priya 58.2
Omar 61.0
```

### Practice

5. Predict what this prints, then press Check.

```python
print((3, "b") < (3, "a"))
print((2, "z") < (3, "a"))
pairs = [(2, "kiwi"), (1, "pear"), (2, "fig")]
print(sorted(pairs))
print(sorted(pairs, key=lambda pair: pair[0]))
```

6. Which `key=` sorts the records by `"seconds"`, and breaks a tie by `"name"`?

### Try It

7. Write a function `ranked(results)` that gives back a new list of the race records in `results`, fastest first: smallest `"seconds"` first. When two runners tie, the one whose `"name"` comes first in the alphabet goes first.

> Say it: a list of race records goes in; a new list comes out, fastest first, with ties in alphabetical order of name. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. give back `sorted()` of the results. 2. as the key, a `lambda` that gives back a tuple: the seconds, then the name.
> Name it: the function and its parameter are named for you. What would you call the parameter of your `lambda`?
> Check it: try the three runners above, which gives Nadia, Priya, then Omar. Then the awkward ones: `[]`, which gives `[]`, and two runners who tie, listed with the later name first.

### What you can do now

- Sort with `sorted()` in real programs, with `reverse=True` and a `key=`, including a method like `str.lower`.
- Say which of two tied items comes first, and why.
- Break a tie with a key that gives back a tuple.

Key words: **break a tie**.
