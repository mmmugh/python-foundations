<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.1 — Looking through a list

`in` tells you whether an item is in a list, and `index()` tells you where. In this lesson you write that search yourself, one item at a time, and trace it. A set of steps like this, which always ends with the answer, is called an **algorithm**. It is only a name for a recipe a computer can follow.

### Warm-up

1. Predict what this prints, then press Check.

```python
def find_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
    return None


books = [{"title": "Dune", "year": 1965}, {"title": "Holes", "year": 1998}]
found = find_book(books, "Emma")
print("missing" if found == None else found["year"])
print(find_book(books, "Holes")["year"])
```

2. `names = ["Ada", "Bo", "Ada"]`. What does `names.index("Ada")` give back?

### One item at a time

To find out whether a name is in a list, look at each name in turn, and stop as soon as one matches:

```python
names = ["Bo", "Ada", "Cy"]
target = "Ada"
found = False
for name in names:
    if name == target:
        found = True
        break
print(found)
```

Output:

```
True
```

`found` starts as `False`. If a name matches, it becomes `True`, and `break` ends the loop (lesson 5.6). If no name matches, the loop runs out and `found` stays `False`. Looking along the list from the start, one item after another, is called a **linear search**: it goes in a line.

Here is its trace table:

| After line | name | found |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  | False |
| 4 | "Bo" | False |
| 5 | "Bo" | False |
| 4 | "Ada" | False |
| 5 | "Ada" | False |
| 6 | "Ada" | True |
| 7 | "Ada" | True |
| 8 | "Ada" | True |

On the first pass, `"Bo" == "Ada"` is `False`, so line 6 is skipped and the loop goes round again. On the second pass the names match: line 6 runs, then line 7 ends the loop. `"Cy"` is never looked at.

### Practice

3. Fill in the table, then press Check.

```python
numbers = [7, 3, 9]
target = 9
found = False
for number in numbers:
    if number == target:
        found = True
        break
```

4. Predict what this prints, then press Check.

```python
numbers = [7, 3, 9, 3]
target = 3
found = False
for number in numbers:
    print(number)
    if number == target:
        found = True
        break
print(found)
target = 5
found = False
for number in numbers:
    if number == target:
        found = True
        break
print(found)
```

### A search that gives back an answer

Inside a function, `return` does the job of `break`: it ends the loop, and the function, as soon as the answer is known:

```python
def contains(items, target):
    for item in items:
        if item == target:
            return True
    return False


print(contains([4, 8, 15], 8))
print(contains([4, 8, 15], 16))
print(contains([], 8))
```

Output:

```
True
False
False
```

`return True` is inside the loop, so it runs at the first match. `return False` is below the loop, so it runs only once every item has been looked at, as `return None` did in lesson 10.4. An empty list has nothing to look at: the loop never runs, and the answer is `False`.

### Practice

5. Write a function `any_over(numbers, limit)` that gives back `True` as soon as it finds a number in `numbers` bigger than `limit`, and `False` if there is none.

> Split it: loop over the numbers. If one is bigger than the limit, give back `True`. Below the loop, give back `False`.
> Check it: try `[3, 8, 2]` with 5, which gives `True`, and `[1, 2, 9]` with 5, where the big one is last. Then the awkward ones: `[]` with 5, which gives `False`, and `[5]` with 5, since 5 is not bigger than 5.

### Where is it?

`index()` gives the position of the first match. But for an item that is not there, it stops the program:

```python
names = ["Bo", "Ada", "Cy"]
print(names.index("Ada"))
print(names.index("Zed"))
```

It prints 1, then stops. The last line of the error says `ValueError: list.index(x): x not in list`, where x stands for the item you asked about; you don't need to remember the wording.

A search of your own can give an answer instead of stopping. Loop over the positions, with `range(len())` as in lesson 7.7, and keep the position of the first match:

```python
names = ["Bo", "Ada", "Cy", "Ada"]
target = "Ada"
where = -1
for position in range(len(names)):
    if names[position] == target:
        where = position
        break
print(where)
```

Output:

```
1
```

`where` starts at -1, which means "not found", as it did for `find()` in lesson 8.4. Positions counted from the front start at 0, so -1 is never the position of a match: if `where` is still -1 after the loop, nothing matched. The `break` keeps the first match, so the second `"Ada"`, at position 3, is never reached.

### Practice

6. Predict what this prints, then press Check.

```python
letters = ["c", "a", "t", "a"]
where = -1
for position in range(len(letters)):
    if letters[position] == "a":
        where = position
        break
print(where)
where = -1
for position in range(len(letters)):
    if letters[position] == "z":
        where = position
        break
print(where)
```

7. `names = ["Bo", "Ada", "Cy"]`. What does `names.index("Zed")` do?

8. Write a function `all_positions(items, target)` that gives back a list of every position where `target` is in `items`, in order. So `all_positions([4, 8, 4], 4)` gives `[0, 2]`. This search does not stop at the first match.

> Split it: start an empty list. Loop over the positions. If the item at a position is the target, add the position to the list. Give the list back after the loop.
> Check it: try `[4, 8, 4]` with 4, which gives `[0, 2]`. Then the awkward ones: `[]` with 4, and `[4, 8]` with 9, which both give `[]`.

### Try It

9. Write a function `find_position(items, target)` that gives back the position of the first match for `target` in the list `items`, or -1 if it is not there.

> Say it: a list and a target go in; the position of the first match comes out, or -1. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. loop over the positions. 2. if the item at a position is the target, give back that position. 3. below the loop, give back -1.
> Name it: the function and its parameters are named for you. What would you call each position as the loop goes?
> Check it: try `[4, 8, 15, 8]` with 8, which gives 1, the first match. Then the awkward ones: `[4, 8]` with 4, which gives 0, a real position; `[4, 8]` with 16, which gives -1; and `[]`, an empty list, which gives -1 whatever the target.

### What you can do now

- Search a list one item at a time, and stop at the first match.
- Give back `True` or `False`, or a position or -1, from a search of your own.
- Trace a search, and see which items it never looks at.

Key words: **algorithm**, **linear search**.
