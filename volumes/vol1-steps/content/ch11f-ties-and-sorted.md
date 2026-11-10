<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.6 — What Python does, and breaking ties

You have written two searches and two sorts by hand. In this lesson you see how Python's own sort compares with them, and you settle a question every sort has to answer: when two items tie, which comes first? Then you use the answer to put a new item in its place.

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

Every capital comes before every small letter, so `Cherry` sorts first. `key=str.lower` names the `lower()` method without calling it, as `key=scores.get` named `get()` in lesson 9.5. `sorted()` compares the small-letter copies, and gives back the words as they were.

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

Priya and Nadia tie, and Priya was first in the list, so she stays first. To break a tie with a rule of your own, by name say, you need tuples. Tuples are compared item by item: the first items decide, and only when they are equal do the second items get a say:

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

6. Write a function `ranked(results)` that gives back a new list of the race records in `results`, fastest first: smallest `"seconds"` first. When two runners tie, the one whose `"name"` comes first in the alphabet goes first.

> Split it: one line: give back `sorted()` of the results, with a `lambda` that gives back a tuple of the seconds and then the name.
> Check it: try the three runners above, which gives Nadia, Priya, then Omar. Then the awkward ones: `[]`, which gives `[]`, and two runners who tie, listed with the later name first.

### Where a new item goes

A new time has to go into a sorted list of times, and keep it sorted. A linear search finds its place: the position of the first time that is not smaller than it. If there is none, it goes at the end:

```python
def place_for(times, new_time):
    for position in range(len(times)):
        if times[position] >= new_time:
            return position
    return len(times)


times = [57.4, 58.2, 61.0]
print(place_for(times, 59.0))
print(place_for(times, 58.2))
print(place_for(times, 70.0))
times.insert(place_for(times, 59.0), 59.0)
print(times)
```

Output:

```
2
1
3
[57.4, 58.2, 59.0, 61.0]
```

The tie rule is in the `>=`. A new time equal to one already there stops the search at that one, so it goes before it: 58.2 goes in at position 1, ahead of the 58.2 already there. With `>`, it would go after. Either rule can be right, but a program has to pick one, and say which.

### Practice

7. Predict what this prints, then press Check.

```python
def place_for(times, new_time):
    for position in range(len(times)):
        if times[position] >= new_time:
            return position
    return len(times)


times = [10, 20, 20, 30]
print(place_for(times, 20))
print(place_for(times, 5))
print(place_for(times, 35))
print(place_for([], 7))
```

8. In `place_for()`, `>=` is changed to `>`. Where does a new time of 20 go in `[10, 20, 20, 30]` now?

### Try It

9. Write a function `insertion_sort(items)` that gives back a new sorted list of the items. Start with an empty list, and put each item into it at its place, found with `place_for()`. This is called **insertion sort**.

> Say it: a list goes in; a new sorted list comes out, built by putting each item in at its place. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. copy `place_for()` in above it. 2. start an empty list. 3. for each item, find its place in the new list with `place_for()`, and `insert()` it there. 4. give back the new list.
> Name it: the function and its parameter are named for you. What would you call the new list?
> Check it: try `[5, 2, 9, 1]`, which gives `[1, 2, 5, 9]`, and `[2, 1, 2]`, which gives `[1, 2, 2]`. Then the awkward ones: `[]`, which gives `[]`, and `[3]`.

### What you can do now

- Sort with `sorted()` in real programs, with `reverse=True` and a `key=`, including a method like `str.lower`.
- Break a tie with a key that gives back a tuple.
- Find where a new item goes in a sorted list, say where a tie goes, and sort by insertion.

Key words: **insertion sort**.
