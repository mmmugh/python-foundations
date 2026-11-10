<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.6 — Dictionaries inside dictionaries

A dictionary of scores keeps one fact about each student. To keep several, like a score, a grade and how many days they missed, each student can have a dictionary of their own. In this lesson you put dictionaries inside a dictionary, and reach into them one level at a time.

### Warm-up

1. Predict what this prints, then press Check.

```python
points = {"red": 5, "blue": 9, "green": 9}
print(max(points, key=points.get))
print(sorted(points, key=points.get))
print(sorted(points, key=points.get, reverse=True))
```

2. What does `max({"Ada": 88, "Zoe": 45})` give back?

### Several facts about one thing

The keys of a dictionary can name facts about one thing:

```python
ada = {"score": 88, "grade": "B", "absences": 2}
print(ada["grade"])
print(ada["absences"])
```

Output:

```
B
2
```

A value in a dictionary can be any value, and that includes another dictionary. Here each student's name is a key, and its value is that student's own dictionary of facts:

```python
students = {
    "Ada": {"score": 88, "grade": "B"},
    "Grace": {"score": 92, "grade": "A"},
}
print(students["Ada"])
print(students["Ada"]["score"])
```

Output:

```
{'score': 88, 'grade': 'B'}
88
```

A dictionary inside a dictionary is called a **nested dictionary**, like the nested lists of lesson 7.8, and between its braces it can run over several lines, like the grid there. Read `students["Ada"]["score"]` one level at a time, from left to right, as you read `grid[1][2]`. `students["Ada"]` is Ada's whole dictionary, and `["score"]` picks the score out of it.

### Practice

3. Predict what this prints, then press Check.

```python
pets = {
    "Rex": {"kind": "dog", "age": 3},
    "Tom": {"kind": "cat", "age": 5},
}
print(pets["Tom"])
print(pets["Rex"]["kind"])
print(pets["Tom"]["age"] + 1)
print(len(pets))
print(len(pets["Rex"]))
```

4. Which of these gives Grace's grade, `"A"`?

```python
students = {
    "Ada": {"score": 88, "grade": "B"},
    "Grace": {"score": 92, "grade": "A"},
}
```

### Changing one level down

Two keys on the left of `=` change one fact in one student's dictionary. One key stores a whole new dictionary, for a new student:

```python
students = {
    "Ada": {"score": 88, "grade": "B"},
    "Grace": {"score": 92, "grade": "A"},
}
students["Ada"]["score"] = 91
students["Alan"] = {"score": 45, "grade": "F"}
print(students["Ada"])
print(students["Alan"]["grade"])
```

Output:

```
{'score': 91, 'grade': 'B'}
F
```

A loop with `items()` gets each name with its dictionary:

```python
students = {
    "Ada": {"score": 88, "grade": "B"},
    "Grace": {"score": 92, "grade": "A"},
}
for name, details in students.items():
    print(f"{name}: {details['score']} ({details['grade']})")
```

Output:

```
Ada: 88 (B)
Grace: 92 (A)
```

Look at the quotes in the f-string. The string itself is in double quotes, so the keys inside its braces are in single quotes. Use the other kind: some versions of Python read a second double quote there as the end of the string.

### Practice

5. Predict what this prints, then press Check.

```python
team = {"Mo": {"goals": 2}, "Kim": {"goals": 0}}
team["Kim"]["goals"] += 1
team["Lee"] = {"goals": 4}
for name, stats in team.items():
    print(name, stats["goals"])
print(team["Kim"])
```

6. Print the roster, one line per student, in the dictionary's order, as `Ada: grade 7, likes math`.

```python
students = {
    "Ada": {"grade": 7, "subject": "math"},
    "Grace": {"grade": 8, "subject": "science"},
    "Alan": {"grade": 7, "subject": "art"},
}
```

> Split it: loop over the students with `items()`. For each one, print the name, then the grade and the subject from that student's own dictionary.
> Check it: the first line is `Ada: grade 7, likes math`, and there are three lines.

7. Write a function `class_average(students)` that gives back the average score of the students in `students`, a dictionary like the one in the examples, or 0 if it is empty.

> Split it: if there are no students, give back 0. Otherwise, add up each student's score, one level down, and divide by how many students there are.
> Check it: try the `students` above with Ada's score at 88 and Grace's at 92, which gives 90.0. Then the awkward one: `{}`, which gives 0.

### Try It

8. Ask for the name of a club. If there is a club by that name, print where and when it meets, as `chess meets in B12 on Monday.` If there is not, print `No club called knitting.`, with the name that was typed in.

```python
clubs = {
    "chess": {"room": "B12", "day": "Monday"},
    "drama": {"room": "Hall", "day": "Wednesday"},
    "robots": {"room": "Lab 2", "day": "Friday"},
}
```

> Say it: a club's name goes in; its room and day come out, or a message if there is no such club. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. ask for the club's name. 2. if it is a key of `clubs`, print the sentence, with the room and the day from that club's own dictionary. 3. otherwise, print the message.
> Name it: `clubs` is named for you. What would you call the name typed in, and one club's dictionary?
> Check it: try `chess` and `robots`. Then the awkward ones: `Chess`, with a capital, and pressing Enter without typing anything. Neither is a key, so both get the message.

### What you can do now

- Keep several facts about each thing in a dictionary inside a dictionary.
- Reach a value two levels down, one level at a time, and change it.
- Print each entry's facts, with the other kind of quote inside an f-string's braces.

Key words: **nested dictionary**.
