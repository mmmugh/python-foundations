<!-- part: Unit 10 — Tuples and records -->
## Lesson 10.4 — Records: a list of dictionaries

In lesson 7.9, a gradebook kept the names in one list and the scores in another, and the two lists had to stay in step. In lesson 9.6, one student's facts went into a dictionary. In this lesson you keep many such dictionaries in one list, and ask it questions: the shape most real data comes in.

### Warm-up

1. Predict what this prints, then press Check.

```python
points = [(1, 2), (3, 4)]
for x, y in points:
    print(x + y)
grid = {(0, 1): "X"}
print(grid.get((1, 0), "."))
```

2. `student = {"name": "Ada", "score": 88}`. Which of these gives 88?

### One record, then a list of them

A **record** is the facts about one thing, each stored under a name. In Python, that is a dictionary, and its keys are called the record's **fields**:

```python
student = {"name": "Ada", "grade": 9, "score": 88}
print(student["name"])
print(student["score"] + 2)
```

Output:

```
Ada
90
```

A list of records holds one dictionary for each thing:

```python
students = [
    {"name": "Ada", "grade": 9, "score": 88},
    {"name": "Grace", "grade": 10, "score": 92},
    {"name": "Alan", "grade": 9, "score": 45},
]
print(len(students))
print(students[1]["name"])
for student in students:
    print(f"{student['name']}: {student['score']}")
```

Output:

```
3
Grace
Ada: 88
Grace: 92
Alan: 45
```

`students[1]` is the second record, a whole dictionary, and `students[1]["name"]` is one field of it. Read it one level at a time, as in lesson 9.6. Each time round the loop, `student` is one record.

Compare lesson 7.9's two lists. Each student's facts now travel together, in one place. A new fact, like an email address, is a new field in each record, not a new list to keep in step.

### Practice

3. Predict what this prints, then press Check.

```python
books = [
    {"title": "Dune", "year": 1965},
    {"title": "Holes", "year": 1998},
]
print(books[0]["title"])
print(len(books))
for book in books:
    print(book["year"] + 1)
```

4. This program should print each book's title, but it stops with an error. Run it and read the last line of the error. Then fix it.

```python
books = [
    {"title": "Dune", "year": 1965},
    {"title": "Holes", "year": 1998},
]
for book in books:
    print(book["Title"])
```

### A field from each record

A list comprehension (lesson 7.9) can take one field from every record. Then `sum()` and `len()` give the average:

```python
students = [
    {"name": "Ada", "grade": 9, "score": 88},
    {"name": "Grace", "grade": 10, "score": 92},
    {"name": "Alan", "grade": 9, "score": 45},
]
scores = [student["score"] for student in students]
print(scores)
print(sum(scores) / len(scores))
```

Output:

```
[88, 92, 45]
75.0
```

An `if` keeps only the records you want. Here, the names of the students in grade 9:

```python
students = [
    {"name": "Ada", "grade": 9, "score": 88},
    {"name": "Grace", "grade": 10, "score": 92},
    {"name": "Alan", "grade": 9, "score": 45},
]
ninth = [student["name"] for student in students if student["grade"] == 9]
print(ninth)
```

Output:

```
['Ada', 'Alan']
```

A loop with `append()` does the same as either comprehension, one line at a time.

### Practice

5. Predict what this prints, then press Check.

```python
pets = [
    {"name": "Rex", "kind": "dog", "age": 3},
    {"name": "Tom", "kind": "cat", "age": 7},
    {"name": "Bo", "kind": "dog", "age": 12},
]
print([pet["age"] for pet in pets])
print([pet["name"] for pet in pets if pet["kind"] == "dog"])
```

6. Write a function `average_score(students)` that gives back the average of the `"score"` fields in the list of records `students`. For an empty list, give back 0.

> Split it: if the list is empty, give back 0. Otherwise, take the score from each record, and give back their sum divided by how many there are.
> Check it: try the three students above, which gives 75.0. Then the awkward one: `[]`, which gives 0.

### Finding one record

To find one record by a field, loop until you meet it, and give back the whole record. If the loop ends without finding it, give back `None`:

```python
def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None


students = [
    {"name": "Ada", "grade": 9},
    {"name": "Grace", "grade": 10},
]
found = find_student(students, "Grace")
print(found)
print(found["grade"])
print(find_student(students, "Bo"))
```

Output:

```
{'name': 'Grace', 'grade': 10}
10
None
```

`return` inside the loop stops as soon as the record turns up. `return None` is below the loop, so it runs only once every record has been looked at. The whole record comes back, not only the name, so whoever called the function can read any field of it.

### Practice

7. Write a function `find_book(books, title)` that gives back the record in the list `books` whose `"title"` field is `title`, or `None` if there is none.

> Split it: loop over the books. If a book's title is the one wanted, give back that book. After the loop, give back `None`.
> Check it: try `[{"title": "Dune", "year": 1965}, {"title": "Holes", "year": 1998}]` with `"Holes"`, which gives the whole Holes record. Then the awkward ones: `"Emma"`, which gives `None`, and an empty list, `[]`.

8. This version gives back `None` for `"Holes"`, though Holes is in the list. Why?

```python
def find_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
        else:
            return None
```

### Try It

9. Write a function `older_than(people, age)` that gives back a list of the names of everyone in the list of records `people` whose `"age"` field is more than `age`, in the order they are in the list.

> Say it: a list of people and an age go in; the names of everyone older than that age come out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start an empty list. 2. loop over the people. 3. if a person's age is more than `age`, add their name. 4. give the list back.
> Name it: the function and its parameters are named for you. What would you call one record, and the list of names?
> Check it: try `[{"name": "Ada", "age": 36}, {"name": "Bo", "age": 9}, {"name": "Cy", "age": 14}]` with 12, which gives `["Ada", "Cy"]`. Then the awkward ones: an age of exactly 14 does not count Cy, since 14 is not more than 14. An empty list, `[]`, gives `[]`, and so does an age nobody is older than.

### What you can do now

- Keep records as a list of dictionaries, and read a field of each.
- Take one field from every record, or only from the records you want.
- Find one record and give back the whole of it, or `None`.

Key words: **record**, **field**.
