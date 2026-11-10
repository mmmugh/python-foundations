<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.9 — Combining sets, and choosing a container

Two clubs share some members. Who is in both? Who is in only one? In this lesson you answer that with three operators you may know from math. Then you choose between a list, a dictionary and a set for a job.

### Warm-up

1. Predict what this prints, then press Check.

```python
letters = set(["b", "a", "n", "a", "n", "a"])
print(len(letters))
print(sorted(letters))
print("n" in letters)
```

2. How do you make an empty set?

### Combining two sets

Three operators combine two sets, as they do in math:

```python
band = {"Ada", "Grace", "Alan"}
chorus = {"Grace", "Alan", "Katherine"}
print(sorted(band | chorus))
print(sorted(band & chorus))
print(sorted(band - chorus))
print(sorted(chorus - band))
```

Output:

```
['Ada', 'Alan', 'Grace', 'Katherine']
['Alan', 'Grace']
['Ada']
['Katherine']
```

Each one makes a new set:

- `|`, the **union**, gives everyone in either set, each once. The `|` key is usually above Enter.
- `&`, the **intersection**, gives everyone in both sets.
- `-`, the **difference**, gives everyone in the first set who is not in the second.

For `|` and `&`, the order of the two sets makes no difference. For `-` it does: `band - chorus` is Ada, and `chorus - band` is Katherine.

To compare two lists, make a set of each first:

```python
mine = ["red", "blue", "red"]
yours = ["blue", "green"]
both = set(mine) & set(yours)
print(sorted(both))
```

Output:

```
['blue']
```

### Practice

3. Predict what this prints, then press Check.

```python
cats = {"Tom", "Kit", "Mo"}
dogs = {"Rex", "Mo"}
print(sorted(cats | dogs))
print(sorted(cats & dogs))
print(sorted(dogs - cats))
print(len(cats - dogs))
```

4. Write a function `in_both(left, right)` that gives back a sorted list of the names that are in both the list `left` and the list `right`, each once.

> Split it: make a set of each list, take the names in both, and give them back sorted.
> Check it: try `["Ada", "Bo"]` and `["Bo", "Cy"]`, which gives `["Bo"]`. Then the awkward ones: `[]` and `["Bo"]`, which gives `[]`; and repeats, like `["a", "a", "b"]` and `["b", "a"]`, which gives `["a", "b"]`.

5. Write a function `only_first(left, right)` that gives back a sorted list of the names in the list `left` that are not in the list `right`, each once.

> Split it: as in `in_both()`, with a different operator. Which way round do the two sets go?
> Check it: try `["Ada", "Bo", "Cy"]` and `["Bo"]`, which gives `["Ada", "Cy"]`. Then the awkward ones: `[]` and `["Bo"]`, which gives `[]`; and `["Bo"]` and `[]`, which gives `["Bo"]`.

### Choosing a container

You now have three ways to keep many values:

| Container | Use it when |
| --- | --- |
| list | the order matters, repeats are fine, and you find items by position |
| dictionary | you look values up by a name, or count things |
| set | all you ask is "is it in here?", or you want each item once |

Ask yourself: how will I look this up later? By position: a list. By name: a dictionary. Only "is it there?": a set. A good choice makes the rest of the program short. A poor one means writing loops to make up for it.

### Practice

6. A program keeps the capital city of each country, to look up by the country's name. Which container fits?

7. A program keeps the people waiting in a queue, in the order they arrived. Which container fits?

8. A word game must refuse any word that has been played already. Which container fits the words played so far?

### Try It

9. Print three lines about the two lists below, each a sorted list of names joined with `", "`: the names in both lists, as `Both: Alan, Grace`; the names only in the first, as `Only first: Ada, Edsger, Katherine`; and everyone, as `Everyone: Ada, Alan, Barbara, Edsger, Grace, Katherine, Margaret`.

```python
first = ["Ada", "Grace", "Alan", "Katherine", "Grace", "Edsger"]
second = ["Grace", "Alan", "Margaret", "Barbara"]
```

> Say it: three sorted lists of names, each printed on one line with a label. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. make a set of each list. 2. the names in both, sorted, joined, printed. 3. the names only in the first, the same way. 4. everyone, the same way.
> Name it: the lists are named for you. What would you call the two sets?
> Check it: Grace is in the first list twice, but each line names her once. Then try the awkward one: make `second` an empty list. `Both:` has no names, and the other two lines both list everyone in the first. Put it back before you press Check.

### What you can do now

- Combine two sets with `|`, `&` and `-`, and say which way round `-` goes.
- Compare two lists by making a set of each.
- Choose a list, a dictionary or a set for a job.

Key words: **union**, **intersection**, **difference**.
