<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.8 — Sets

Sometimes the only question is "is it in here?", or "how many different ones are there?". A list can answer both, but it keeps every repeat. In this lesson you meet a set, which keeps each item once.

### Warm-up

1. Predict what this prints, then press Check.

```python
a = {"x": 1}
b = a
c = a.copy()
b["x"] = 2
c["y"] = 3
print(a)
print(c)
```

2. A loop takes entries out of the dictionary it is looping over, and stops with a RuntimeError. What fixes it?

### Is it in here?

A **set** is a collection of items, with no keys and no positions. Curly braces make it too, with items between them and no colons:

```python
vowels = {"a", "e", "i", "o", "u"}
print("e" in vowels)
print("y" in vowels)
print(len(vowels))
```

Output:

```
True
False
5
```

A set holds each item once. `set()` makes a set from a list, and the repeats drop out. `sorted()` gives back a set's items as a list, in order:

```python
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print(len(numbers))
print(len(unique))
print(sorted(unique))
```

Output:

```
6
3
[1, 2, 3]
```

A set has no order. When you print one, Python shows its items in an order of its own, which can change from one run to the next:

```python
fruit = {"pear", "apple", "fig"}
print(fruit)
```

Output:

```
{'fig', 'pear', 'apple'}
```

Run it a few times, and the order may change. So never count on a set's order: when the order matters, use `sorted()`.

### Practice

3. Predict what this prints, then press Check.

```python
pets = ["cat", "dog", "cat", "fish", "dog"]
kinds = set(pets)
print(len(pets))
print(len(kinds))
print(sorted(kinds))
print("dog" in kinds)
print("bird" in kinds)
```

4. Write a function `distinct_count(items)` that gives back how many different items the list `items` holds.

> Split it: make a set from the list, and give back how many items it holds.
> Check it: try `["a", "b", "a"]`, which gives 2. Then the awkward one: `[]`, which gives 0.

5. Why does exercise 3 print `sorted(kinds)`, and not `kinds` itself?

### Two things to watch

`{}` with nothing between the braces is an empty dictionary, not a set: dictionaries had the braces first. An empty set is `set()`:

```python
empty = set()
print(len(empty))
print(type({}))
print(type(set()))
```

Output:

```
0
<class 'dict'>
<class 'set'>
```

A list cannot be a key in a dictionary, or an item in a set:

```python
teams = {["Ada", "Grace"]: "red"}
```

The last line of the error says `TypeError`, then that the list is an `unhashable type`. Unhashable is Python's word for "can't be a key, or an item in a set"; you don't need to remember it. A list can change, and a key must stay the same, so keys and set items are values that can't change, like numbers and text.

### Practice

6. What does `{}` make?

7. Which of these could be a key in a dictionary?

### Try It

8. Ask for a sentence, and print how many different words it has. Words that differ only in their capitals count as the same word, so `go Go GO` has 1 different word.

> Say it: a sentence goes in; the number of different words in it comes out, with capitals ignored. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. ask for the sentence. 2. make it small, and split it into words. 3. make a set of the words. 4. print how many items the set holds.
> Name it: what would you call the sentence, the list of words, and the set?
> Check it: try `The cat and the hat`, which has 4 different words. Then the awkward ones: `go Go GO`, which has 1, and pressing Enter without typing anything, which has 0.

### What you can do now

- Keep items in a set, with no repeats, and ask whether one is in it.
- Take the repeats out of a list with `set()`, and put the items in order with `sorted()`.
- Make an empty set with `set()`, and keep lists out of sets and keys.

Key words: **set**.
