<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.7 — Numbering from 1, and planning a records system

This lesson and the next put the whole course together, on the largest problem in it: a report on a school's student records. A project that finishes a course like this is called a **capstone**, after the stone that finishes the top of a wall. First, one small new thing, a way to number lines from 1. Then the plan, split into functions, and the first of them built and checked.

### Warm-up

1. Predict what this prints, then press Check.

```python
books = [
    {"title": "Dune", "year": 1965},
    {"title": "Holes", "year": 1998},
    {"title": "Emma", "year": 1815},
]
for book in sorted(books, key=lambda record: record["year"], reverse=True):
    print(book["title"])
```

2. In `for position, name in enumerate(["Bo", "Cy"]):`, what is `position` the first time round?

### Numbering from 1

`enumerate()` (lesson 7.7) counts from 0, as positions do. People count from 1, so a numbered list needs a `+ 1`:

```python
names = ["Ada", "Grace", "Alan"]
for position, name in enumerate(names):
    print(position + 1, name)
```

Output:

```
1 Ada
2 Grace
3 Alan
```

`enumerate()` can count from 1 instead. Tell it where to start, with `start=`, the way `key=` tells `sorted()` how to compare:

```python
names = ["Ada", "Grace", "Alan"]
for rank, name in enumerate(names, start=1):
    print(rank, name)
```

Output:

```
1 Ada
2 Grace
3 Alan
```

Only the count changes. The items are the same, from the first one.

### Practice

3. Predict what this prints, then press Check.

```python
colors = ["red", "green", "blue"]
for number, color in enumerate(colors, start=1):
    print(f"{number}. {color}")
for number, color in enumerate(colors):
    print(number, color)
```

4. Write a function `numbered(names)` that gives back a list of the names, each with its number from 1 in front, like `"1. Ada"`. So `numbered(["Ada", "Bo"])` gives back `["1. Ada", "2. Bo"]`.

> Split it: start an empty list. Loop over the names with `enumerate()`, starting at 1, and add each line to the list. Give the list back.
> Check it: try `["Ada", "Bo"]`. Then the awkward one: `[]`, which gives `[]`.

### The plan

Here is the problem: "A school keeps each student as a record: an id number, a name, a grade level and a list of test scores. Print a report: a roster of the students, highest average first and numbered from 1; how many students each grade level has, and their average; the top student, and how many passed, with an average of 60 or more; the students whose names hold some text; and a look-up of students by id."

It is the largest problem in the course, so Say it and Split it matter most here. Split it into functions, each small enough to build and check on its own:

```python
# Say it: print a report on the students, from a ranked roster to a look-up by id.
# Split it:
# 1. a student's average: average(scores), from lesson 7.5
# 2. their letter grade: letter_grade(score), from lesson 6.5
# 3. the students, highest average first: ranked(records)
# 4. one line of the roster: roster_line(rank, record)
# 5. the roster, numbered from 1: print_roster(records)
# 6. the students in each grade level: group_by_grade(records)
# 7. "1 student" or "2 students": students_word(count)
# 8. how many passed: passing_count(records)
# 9. the students whose names hold some text: search_by_name(records, text)
# 10. a look-up by id, with a binary search: find_by_id(records, student_id)
# 11. the report: each part, in order
```

You have steps 1 and 2. In this lesson you build steps 3 to 5, the roster. For the students in the try-it, it looks like this:

```
Rank  ID     Name                Gr      Avg  Grade
---------------------------------------------------
1     1002   Katherine Johnson   11     96.7      A
2     1001   Grace Hopper        10     94.7      A
3     1004   Ada Lovelace        9      88.3      B
4     1009   Edsger Dijkstra     10     71.3      C
5     1007   Alan Turing         9      55.0      F
---------------------------------------------------
```

In each line, the rank is at the left of a column 6 wide, the id 7 wide, the name 20 wide and the grade level 4 wide, as in lesson 8.11. The average is at the right of a column 7 wide, with 1 decimal place, and the letter grade at the right of a column 7 wide. The heading line is lined up the same way, and the dashed lines are 51 dashes.

### Practice

5. Step 3: write `ranked(records)`, which gives back a new list of the records, highest average first. Records with the same average keep their order. Write it below `average()`, which it uses.

```python
def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)
```

> Split it: `sorted()` with a `lambda` that gives back a record's average, and `reverse=True`, as in lesson 10.5.
> Check it: a record with scores `[90, 80]` comes before one with `[50]`. Then the awkward ones: `[]`, which gives `[]`, and a record with no scores, whose average is 0, which comes last.

6. Step 4: write `roster_line(rank, record)`, which gives back one line of the roster, as text, for a rank and a record. Write it between the two functions and the lines that use it, then run them all.

```python
def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(roster_line(1, {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]}))
print(roster_line(12, {"id": 1010, "name": "New Student", "grade": 9, "scores": []}))
```

> Split it: work out the average once, and keep it. Then give back one f-string with each value and its column, as the plan says.
> Check it: the first line is the same as Katherine Johnson's line in the roster above. The second is the awkward one: no scores, so `0.0` and `F`, and a two-digit rank still fits its column.

### Try It

7. Step 5: write `print_roster(records)`, which prints the roster, ranked and numbered from 1. Then call it for these students, to print the roster exactly as shown above.

```python
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


students = [
    {"id": 1001, "name": "Grace Hopper", "grade": 10, "scores": [95, 91, 98]},
    {"id": 1004, "name": "Ada Lovelace", "grade": 9, "scores": [88, 92, 85]},
    {"id": 1007, "name": "Alan Turing", "grade": 9, "scores": [45, 62, 58]},
    {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]},
    {"id": 1009, "name": "Edsger Dijkstra", "grade": 10, "scores": [71, 68, 75]},
]
```

> Say it: a heading, the students' lines, best average first and numbered from 1, then a closing line. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: copy in `average()`, `ranked()` and `roster_line()` first. Then: 1. print the heading line, and 51 dashes. 2. loop over the ranked records with `enumerate()`, starting at 1, printing each `roster_line()`. 3. print 51 dashes again.
> Name it: the functions and the list are named for you. What would you call each number from `enumerate()`?
> Check it: run it and compare each line, spaces too. Then try the awkward one: `print_roster([])` prints the heading and the two dashed lines, and nothing between them. Take that call out before you press Check.

### What you can do now

- Number lines from 1 with `enumerate(..., start=1)`.
- Split the largest problem yet into functions, each small enough to check on its own.
- Build a ranked, numbered roster from records, one checked function at a time.

Key words: **capstone**.
