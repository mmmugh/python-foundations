<!-- part: Unit 7 — Lists -->
## Lesson 7.1 — Lists, and finding an item

Every variable so far has held one value. Four test scores would need four variables, and a class of thirty would need thirty. In this lesson you keep many values under one name, and pick out any one of them.

### Warm-up

1. Predict what this prints, then press Check.

```python
def tax(price, rate=10):
    return price * rate / 100

print(tax(50))
print(tax(50, 20))
```

2. In `def area(width, height):`, what are `width` and `height`?

### Many values under one name

A **list** holds many values, in order, under one name:

```python
scores = [88, 92, 79, 95]
print(scores)
```

Output:

```
[88, 92, 79, 95]
```

Square brackets make the list, and commas go between the values. Each value is an **item** of the list.

Items can be text, or any other kind of value, and a list can even have no items at all:

```python
names = ["Ada", "Grace", "Alan"]
mixed = [7, "seven", 7.0]
empty = []
print(names)
print(mixed)
print(empty)
```

Output:

```
['Ada', 'Grace', 'Alan']
[7, 'seven', 7.0]
[]
```

When Python prints a list, it puts quotes around each text item, so you can tell the text `'7'` from the number `7`. It uses single quotes, even if you typed double ones. An empty list prints as `[]`.

A list can mix kinds of value, like `mixed` does, but a list of one kind of thing is far more useful: all scores, or all names. Name it for what its items are, like `scores` or `names`. Don't call it `list`: Python already uses that word for lists themselves.

### Practice

3. Predict what this prints, then press Check.

```python
colors = ["red", "green"]
sizes = [4, "four", 4.5]
nothing = []
print(colors)
print(sizes)
print(nothing)
```

4. A list holds the price of everything in a shopping cart. Which is the clearest name for it?

### Finding an item

Each item has a position in the list, called its **index**. Put the index in square brackets after the list's name, and you get that item:

```python
names = ["Ada", "Grace", "Alan", "Katherine"]
print(names[0])
print(names[2])
```

Output:

```
Ada
Alan
```

Python counts positions from 0, not 1, just as `range(5)` starts at 0 (lesson 5.2). So `names[0]` is the first item, and `names[2]` is the third:

| Item | `Ada` | `Grace` | `Alan` | `Katherine` |
| --- | --- | --- | --- | --- |
| Index | 0 | 1 | 2 | 3 |

### Practice

5. Predict what this prints, then press Check.

```python
planets = ["Mercury", "Venus", "Earth", "Mars"]
print(planets[1])
print(planets[3])
```

### Counting from the end

An index below 0 counts back from the end. `-1` is the last item, `-2` the one before it:

```python
names = ["Ada", "Grace", "Alan", "Katherine"]
print(names[-1])
print(names[-2])
```

Output:

```
Katherine
Alan
```

| Item | `Ada` | `Grace` | `Alan` | `Katherine` |
| --- | --- | --- | --- | --- |
| Index | 0 | 1 | 2 | 3 |
| From the end | -4 | -3 | -2 | -1 |

`names[-1]` is the last item however long the list is, so you never need to count the items to find it.

### Practice

6. Predict what this prints, then press Check.

```python
planets = ["Mercury", "Venus", "Earth", "Mars"]
print(planets[-1])
print(planets[-3])
```

### An index that is not there

Ask for an index the list does not have, and Python stops:

```python
names = ["Ada", "Grace"]
print(names[2])
```

The last line of the error says `IndexError: list index out of range`. Out of range means past the end of the list. This list has two items, at index 0 and index 1, so there is no index 2. The last index is always one less than the number of items, because counting starts at 0.

### Practice

7. This program should print the last of the four seasons, `winter`, but it stops with an error. Run it and read the last line of the error. Then fix it.

```python
seasons = ["spring", "summer", "fall", "winter"]
print(seasons[4])
```

### Try It

8. A race's finishers are in a list, in the order they finished. Print exactly two lines: the winner, as `Winner: Mo`, then who came last, as `Last: Bo`.

```python
finishers = ["Mo", "Ada", "Kim", "Lee", "Bo"]
```

> Say it: the list is in finishing order; print its first name and its last name, each with a label. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. print `Winner:` and the item at the first index. 2. print `Last:` and the item at the last index.
> Name it: the list is named for you. Which index is the first? Which index is always the last, however long the list is?
> Check it: run it and compare with the two lines asked for. Then the awkward one: add a sixth name to the end of the list and run it again. Does `Last:` change to the new name, with no other change to your code? Take the sixth name out before you press Check.

### What you can do now

- Keep many values under one name, in a list.
- Pick out one item by its index, counting from 0.
- Count from the end with -1, and read an `IndexError`.

Key words: **list**, **item**, **index**.
