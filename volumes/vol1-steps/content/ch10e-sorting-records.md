<!-- part: Unit 10 — Tuples and records -->
## Lesson 10.5 — Sorting records by a field

In lesson 9.5, `key=scores.get` told `sorted()` how to compare a dictionary's keys. A list of records needs the same help: Python cannot put dictionaries in order on its own. In this lesson you tell it which field to sort by, first with a function of your own, then with a shorter way to write one.

### Warm-up

1. Predict what this prints, then press Check.

```python
pets = [{"name": "Rex", "age": 3}, {"name": "Tom", "age": 7}]
print(pets[1]["name"])
print([pet["age"] * 2 for pet in pets])
```

2. A function loops over a list of records and gives back the one it is looking for. Where does `return None` go?

### Sorting by a field

Ask `sorted()` to sort a list of records, and it stops:

```python
students = [{"name": "Grace", "score": 92}, {"name": "Ada", "score": 88}]
print(sorted(students))
```

The last line of the error says `TypeError: '<' not supported between instances of 'dict' and 'dict'`. `<` is how `sorted()` compares two items, and an instance is Python's word for one value of a kind; you don't need to remember it. Python has no rule for which of two dictionaries comes first.

So give it one. Write a function that takes a record and gives back the field to sort by, and name it with `key=`:

```python
def score_of(student):
    return student["score"]


students = [
    {"name": "Grace", "score": 92},
    {"name": "Ada", "score": 88},
    {"name": "Alan", "score": 45},
]
for student in sorted(students, key=score_of):
    print(student["name"], student["score"])
```

Output:

```
Alan 45
Ada 88
Grace 92
```

`key=score_of` names the function, with no brackets, as `key=scores.get` did in lesson 9.5. `sorted()` uses it on each record, and compares what comes back: the scores. The whole records are what get sorted, so each name stays with its own score. Lesson 7.9's two lists could not promise that.

### Practice

3. Predict what this prints, then press Check.

```python
def year_of(book):
    return book["year"]


books = [
    {"title": "Holes", "year": 1998},
    {"title": "Emma", "year": 1815},
    {"title": "Dune", "year": 1965},
]
for book in sorted(books, key=year_of):
    print(book["title"])
print(books[0]["title"])
```

4. Why does `sorted(students)` stop with a `TypeError` when `students` is a list of records?

### A function without a name

`score_of()` is a whole function, used in one place, and all it does is give back one field. Python has a shorter way to write a function like that, right where it is used:

```python
students = [
    {"name": "Grace", "score": 92},
    {"name": "Ada", "score": 88},
    {"name": "Alan", "score": 45},
]
for student in sorted(students, key=lambda record: record["score"]):
    print(student["name"], student["score"])
```

Output:

```
Alan 45
Ada 88
Grace 92
```

`lambda record: record["score"]` is a function with no name. Before the colon is its parameter; after the colon is what it gives back, with no `return`. It is `score_of()` in one line. Lambda is a Greek letter that mathematicians used for functions, and Python borrowed the word; that is all it means.

`reverse=True` works as it did in lesson 9.5. `max()` and `min()` take `key=` too, and give back the whole record with the biggest or smallest field:

```python
students = [
    {"name": "Grace", "score": 92},
    {"name": "Ada", "score": 88},
    {"name": "Alan", "score": 45},
]
ranked = sorted(students, key=lambda record: record["score"], reverse=True)
print(ranked[0]["name"])
best = max(students, key=lambda record: record["score"])
print(best)
print(min(students, key=lambda record: record["score"])["name"])
```

Output:

```
Grace
{'name': 'Grace', 'score': 92}
Alan
```

### Practice

5. Which `lambda` does the same job as this function?

```python
def title_of(book):
    return book["title"]
```

6. Predict what this prints, then press Check.

```python
pets = [
    {"name": "Rex", "age": 3},
    {"name": "Tom", "age": 12},
    {"name": "Bo", "age": 7},
]
for pet in sorted(pets, key=lambda animal: animal["name"]):
    print(pet["name"])
print(sorted(pets, key=lambda animal: animal["age"], reverse=True)[0]["name"])
print(min(pets, key=lambda animal: animal["age"]))
```

7. Write a function `by_year(books)` that gives back a new list of the book records in `books`, sorted by their `"year"` field, oldest first.

> Split it: one line: give back `sorted()` of the books, with a `lambda` that gives back a book's year as the key.
> Check it: try `[{"title": "Holes", "year": 1998}, {"title": "Emma", "year": 1815}]`, which gives the Emma record first. Then the awkward one: `[]`, which gives `[]`.

### Try It

8. Write a function `oldest(books)` that gives back the whole record of the book with the earliest `"year"` in the list `books`. If two books share the earliest year, give back the first of them. For an empty list, give back `None`.

> Say it: a list of book records goes in; the record of the oldest book comes out, or `None`. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. if the list is empty, give back `None`. 2. otherwise, give back the book with the smallest year, using `min()` with a `key=`.
> Name it: the function and its parameter are named for you. What would you call the parameter of your `lambda`?
> Check it: try `[{"title": "Dune", "year": 1965}, {"title": "Emma", "year": 1815}]`, which gives the Emma record. Then the awkward ones: `[]`, which gives `None`, and two books from the same year, which gives the first.

### What you can do now

- Sort a list of records by any field, with `key=`.
- Write a short function in place, with `lambda`.
- Find the record with the biggest or smallest field, with `max()` or `min()`.

Key words: **lambda**.
