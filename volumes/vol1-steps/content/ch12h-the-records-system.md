<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.8 — Putting it all together: a records system

In lesson 12.7 you split the records report into eleven functions, and built the roster. In this lesson you build the rest, each one checked on its own, then put every part together into the course's largest program. There is nothing new to learn here: every piece is something you have done before.

### Warm-up

1. Predict what this prints, then press Check.

```python
names = ["Grace", "Ada", "Alan"]
for rank, name in enumerate(sorted(names), start=1):
    print(f"{rank}. {name}")
```

2. `find_by_id()` will look students up with a binary search, by id. What must be true of the list it searches?

### The grade levels and the class

Steps 6 to 8 of the plan group the students by grade level, word a count, and count who passed. Each is a shape you have met: grouping in lesson 10.6, a conditional expression in lesson 10.7, and a count of the items that pass a test in lesson 7.9.

### Practice

3. Step 6: write `group_by_grade(records)`, which gives back a dictionary from each grade level to a list of the records at that level, in the order they are in `records`. Write it above these lines, which use it, then run them all.

```python
students = [
    {"id": 1001, "name": "Grace Hopper", "grade": 10, "scores": [95, 91, 98]},
    {"id": 1004, "name": "Ada Lovelace", "grade": 9, "scores": [88, 92, 85]},
    {"id": 1007, "name": "Alan Turing", "grade": 9, "scores": [45, 62, 58]},
    {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]},
    {"id": 1009, "name": "Edsger Dijkstra", "grade": 10, "scores": [71, 68, 75]},
]

groups = group_by_grade(students)
for grade in sorted(groups):
    print(grade, [record["name"] for record in groups[grade]])
print(group_by_grade([]))
```

> Split it: lesson 10.6's grouping loop, with the grade level as the key and the whole record added to its list.
> Check it: grade 9 has Ada Lovelace, then Alan Turing, in that order. Then the awkward one: `[]` gives `{}`.

4. Step 7: write `students_word(count)`, which gives back the count and the word `student`, or `students` for any count but 1. So `students_word(1)` gives back `"1 student"`, and `students_word(2)` gives back `"2 students"`.

> Split it: one line: a conditional expression, as in lesson 10.7's `stock_label()`.
> Check it: try 1 and 2. Then the awkward one: 0, which gives `"0 students"`.

5. Step 8: write `passing_count(records)`, which gives back how many of the records have an average of 60 or more. Write it below `average()`, which it uses.

```python
def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)
```

> Split it: count the records whose average is 60 or more, with a loop or a list comprehension and `len()`.
> Check it: a record with scores `[60, 60]` passes, and one with `[59, 60]` does not. Then the awkward one: `[]`, which gives 0.

6. You met `max()` with a key in lesson 10.5. Predict what this prints, then press Check.

```python
def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


students = [
    {"name": "Ada Lovelace", "scores": [88, 92, 85]},
    {"name": "Grace Hopper", "scores": [95, 91, 98]},
    {"name": "Alan Turing", "scores": [45, 62, 58]},
]
best = max(students, key=lambda record: average(record["scores"]))
print(best["name"])
print(f"{average(best['scores']):.1f}")
```

### Searching the records

Step 9 searches by name, and step 10 looks a student up by id. A search by name has to look at every record, since the names are in no order that helps, so it is a linear search (lesson 11.1). A look-up by id can halve, as lesson 11.2 did, but only in a list sorted by id.

Something that must be true before a function is called is its **precondition**. Say it in the docstring, so whoever calls the function knows. A binary search of a list in the wrong order gives no error, just a wrong answer, so this one matters:

```python
def find_by_id(records, student_id):
    """Give back the record with this id, or None. records must be sorted by id."""
```

### Practice

7. Step 9: write `search_by_name(records, text)`, which gives back a list of the records whose name holds `text`, ignoring capitals, in the order they are in `records`.

> Split it: keep each record if `text.lower()` is in its name, lowered too. A loop or a list comprehension, as you like.
> Check it: `"er"` finds Grace Hopper, Katherine Johnson and Edsger Dijkstra, and so does `"ER"`. Then the awkward ones: `[]` gives `[]`; and `""`, which is in every name, gives every record.

8. Step 10: write `find_by_id(records, student_id)`, with its docstring, which gives back the record with that id from a list sorted by id, or `None`. Use a binary search.

> Split it: lesson 11.2's binary search, comparing each middle record's `"id"` with `student_id`. Give back the record, not its position, and `None` below the loop.
> Check it: in a list sorted by id, look up the first id, the last, and one in the middle. Then the awkward ones: an id that is not there, and `[]`, which both give `None`.
> Did it halve? While you try it, add `print(low, high, middle)` as the first line inside the loop: for 5 records you see at most 3 lines. Take the print out before you press Check.

9. The report looks students up in `students`, which is in no order of id. Why does it sort a copy by id first?

### The finished report

For the students in the try-it, the whole report looks like this:

```
Rank  ID     Name                Gr      Avg  Grade
---------------------------------------------------
1     1002   Katherine Johnson   11     96.7      A
2     1001   Grace Hopper        10     94.7      A
3     1004   Ada Lovelace        9      88.3      B
4     1009   Edsger Dijkstra     10     71.3      C
5     1007   Alan Turing         9      55.0      F
---------------------------------------------------
By grade level:
Grade 9: 2 students, average 71.7
Grade 10: 2 students, average 83.0
Grade 11: 1 student, average 96.7
Top student: Katherine Johnson (96.7)
Passing: 4 of 5
Names with er: Grace Hopper, Katherine Johnson, Edsger Dijkstra
Lookup 1002: Katherine Johnson
Lookup 9999: not found
```

The grade levels are in order. A grade level's average is the average of its students' averages, with 1 decimal place, as is the top student's. The names found by `search_by_name()` are joined with a comma and a space (lesson 8.8). Each look-up prints the student's name, or `not found`.

### Try It

10. Step 11: print the whole report for these students, exactly as shown above.

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

> Say it: the roster, then the grade levels, the top student and the passing count, a search by name, and two look-ups by id. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: copy in your functions from steps 1 to 10 first. Then: 1. `print_roster()`. 2. the `By grade level:` line, then a line for each grade level in order. 3. the top student, with `max()`. 4. the passing count. 5. the names with `er`. 6. a copy of the students sorted by id, and a look-up of 1002 and of 9999 in it.
> Name it: the functions are named in the plan. What would you call the copy sorted by id, and the list of averages in one grade level?
> Check it: run it and compare each line, spaces too. Then try a change: make Alan Turing's scores `[65, 62, 58]`. He passes, with a D, and the passing count is 5 of 5. Put them back before you press Check.

### What you can do now

- Split a big problem into small functions, and build and check each one on its own.
- Put records, sorting, searching, grouping and lined-up columns together into one program.
- Start any problem the same way: Say it, Split it, Name it, Build it, Check it.

Key words: **precondition**.

That is the end of unit 12, and of the course. Its quiz is below: fill it in, then show or print it.

You began with one line, a `print()`. You can now plan a program of a dozen functions, build it one checked piece at a time, and find and fix what goes wrong. Well done.
