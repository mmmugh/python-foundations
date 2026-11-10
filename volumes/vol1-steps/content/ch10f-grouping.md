<!-- part: Unit 10 — Tuples and records -->
## Lesson 10.6 — Grouping, and setdefault()

Lesson 9.4 counted how many votes each answer got. Sometimes you want more than how many: you want which ones. In this lesson you sort records into groups, with a list for each value of a field, and meet a method that makes the empty list for you.

### Warm-up

1. Predict what this prints, then press Check.

```python
books = [{"title": "Holes", "year": 1998}, {"title": "Emma", "year": 1815}]
for book in sorted(books, key=lambda book: book["year"]):
    print(book["title"])
print(max(books, key=lambda book: book["year"])["title"])
```

2. In this counting loop, why does it ask `if vote in counts:` first?

```python
counts = {}
for vote in ["yes", "no", "yes"]:
    if vote in counts:
        counts[vote] += 1
    else:
        counts[vote] = 1
```

### Grouping

Counting stores a number under each key. Grouping stores a list: every record that shares a value of a field goes into the same list. The first time a value turns up, it has no list yet, so the loop makes an empty one:

```python
students = [
    {"name": "Ada", "grade": 9},
    {"name": "Grace", "grade": 10},
    {"name": "Alan", "grade": 9},
]
by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])
print(by_grade)
```

Output:

```
{9: ['Ada', 'Alan'], 10: ['Grace']}
```

`by_grade[grade]` is a list, so `append()` adds to that list, inside the dictionary. A dictionary whose values are lists is how you **group** things by something they share. It is lesson 9.4's counting loop with a list in place of a number.

To print the groups, loop over the keys in order, and join each list:

```python
by_grade = {10: ["Grace"], 9: ["Ada", "Alan"]}
for grade in sorted(by_grade):
    print(f"Grade {grade}: {', '.join(by_grade[grade])}")
```

Output:

```
Grade 9: Ada, Alan
Grade 10: Grace
```

### Practice

3. Predict what this prints, then press Check.

```python
pets = [("Rex", "dog"), ("Tom", "cat"), ("Bo", "dog")]
by_kind = {}
for name, kind in pets:
    if kind not in by_kind:
        by_kind[kind] = []
    by_kind[kind].append(name)
print(by_kind)
print(len(by_kind["dog"]))
```

4. Write a function `by_first_letter(words)` that gives back a dictionary from each first letter to a list of the words in `words` that start with it, in the order they are in the list.

> Split it: start an empty dictionary. For each word, take its first letter. If that letter is not a key yet, store an empty list under it. Then add the word to the letter's list. Give the dictionary back.
> Check it: try `["ant", "bee", "ape"]`, which gives `{"a": ["ant", "ape"], "b": ["bee"]}`. Then the awkward one: `[]`, which gives `{}`.

### setdefault()

The `if` that makes the empty list is so common that dictionaries have a method for it. `setdefault(key, default)` gives back the value stored under `key`. If the key is missing, it first stores `default` under it, then gives that back:

```python
groups = {"dog": ["Rex"]}
print(groups.setdefault("dog", []))
print(groups.setdefault("cat", []))
print(groups)
```

Output:

```
['Rex']
[]
{'dog': ['Rex'], 'cat': []}
```

Compare `get()` from lesson 9.2: `get()` gives back its default, but never stores it. `setdefault()` stores it.

So the grouping loop's three lines become one:

```python
students = [
    {"name": "Ada", "grade": 9},
    {"name": "Grace", "grade": 10},
    {"name": "Alan", "grade": 9},
]
by_grade = {}
for student in students:
    by_grade.setdefault(student["grade"], []).append(student["name"])
print(by_grade)
```

Output:

```
{9: ['Ada', 'Alan'], 10: ['Grace']}
```

`setdefault()` gives back the list stored under the grade, new or not, and `append()` adds the name to that same list.

### Practice

5. Predict what this prints, then press Check.

```python
stock = {"pens": 3}
print(stock.setdefault("pens", 0))
print(stock.setdefault("pads", 0))
print(stock.get("clips", 0))
print(stock)
```

6. A key is missing. What is the difference between `get(key, [])` and `setdefault(key, [])`?

7. Write a function `count_routes(routes)` that gives back a dictionary of how many times each route appears in the list `routes`. Use `setdefault()` to start each new route at 0, then add 1.

> Split it: start an empty dictionary. For each route, `setdefault()` it to 0, then add 1 to the count stored under it. Give the dictionary back.
> Check it: try `["47", "12", "47"]`, which gives `{"47": 2, "12": 1}`. Then the awkward one: `[]`, which gives `{}`.

### Try It

8. Write a function `titles_by_author(books)` that gives back a dictionary from each author to a list of the titles of their books in the list of records `books`, in the order they are in the list. Each record has a `"title"` and an `"author"` field.

> Say it: a list of book records goes in; a dictionary from each author to their titles comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start an empty dictionary. 2. loop over the books. 3. add each book's title to its author's list, with `setdefault()` or with an `if`. 4. give the dictionary back.
> Name it: the function and its parameter are named for you. What would you call one record, and the dictionary of groups?
> Check it: try `[{"title": "Emma", "author": "Austen"}, {"title": "Dune", "author": "Herbert"}, {"title": "Persuasion", "author": "Austen"}]`, which gives `{"Austen": ["Emma", "Persuasion"], "Herbert": ["Dune"]}`. Then the awkward one: `[]`, which gives `{}`.

### What you can do now

- Group records into a dictionary of lists, by a field they share.
- Store a starting value only when a key is missing, with `setdefault()`.
- Print each group, with its keys in order.

Key words: **group**, **setdefault()**.
