<!-- part: Unit 7 — Lists -->
## Lesson 7.9 — Finding a position, and a gradebook

`max()` tells you the top score, but not where it is in the list. In this lesson you find an item's index, keep two lists side by side, and build a class gradebook from them, one function at a time.

### Warm-up

1. Predict what this prints, then press Check.

```python
grid = [[1, 2], [3, 4], [5, 6]]
print(grid[2][0])
for row in grid:
    print(sum(row))
```

2. What does `end=" "` do in `print(value, end=" ")`?

### Where is it, and how many?

`index()` gives the index of an item, and `count()` gives how many times it appears:

```python
names = ["Ada", "Grace", "Alan", "Grace"]
print(names.index("Alan"))
print(names.index("Grace"))
print(names.count("Grace"))
print(names.count("Bo"))
```

Output:

```
2
1
2
0
```

There are two `"Grace"` items, and `index()` gives the first one's index, 1. An item that is not in the list is counted 0 times.

### Practice

3. Predict what this prints, then press Check.

```python
votes = ["yes", "no", "yes", "maybe", "yes"]
print(votes.count("yes"))
print(votes.count("never"))
print(votes.index("maybe"))
print(votes.index("yes"))
```

### Two lists side by side

A teacher keeps the class's names in one list and their scores in another, in the same order. The same index finds a student in both, so `names[1]` and `scores[1]` belong together:

```python
names = ["Ada", "Grace", "Alan"]
scores = [88, 92, 45]
print(names[1], scores[1])
best = max(scores)
where = scores.index(best)
print(names[where], "has the top score,", best)
```

Output:

```
Grace 92
Grace has the top score, 92
```

`max()` finds the top score, `index()` finds where it is, and that index in `names` is the student who got it. The three steps fit in one line, read from the inside out, as in lesson 6.4:

```python
names = ["Ada", "Grace", "Alan"]
scores = [88, 92, 45]
print(names[scores.index(max(scores))])
```

Output:

```
Grace
```

`max(scores)` runs first and gives back 92; then `scores.index(92)` gives back 1; then `names[1]` is `"Grace"`. Lists kept side by side like this are called **parallel lists**. They only work while both stay in the same order.

### Practice

4. Predict what this prints, then press Check.

```python
cities = ["Oslo", "Lima", "Cairo"]
temps = [4, 19, 31]
print(cities[temps.index(min(temps))])
print(temps[cities.index("Lima")])
```

5. In the gradebook above, someone runs `scores.sort()`, but leaves `names` as it was. What happens?

### The gradebook

Here is the problem: "Print a line for each student with their name, score and letter grade. Then print the class average, the top score and who got it, and how many passed, with 60 or more." Say it and Split it come first:

```python
# Say it: print each student's line, then a summary of the class.
# Split it:
# 1. each student's line: name, score and letter_grade() from lesson 6.5
# 2. the class average: average() from lesson 7.5
# 3. who got the top score: top_student(names, scores)
# 4. how many passed: count_passing(scores)
# 5. print it all
```

Steps 1 and 2 use functions you already have. Steps 3 and 4 are new; build and check each one on its own.

### Practice

6. Step 3: write `top_student(names, scores)`, which gives back the name of the student with the highest score. For empty lists, it gives back `None`.

> Split it: first, if there are no scores, give back `None`. Otherwise: find the top score, find its index, and give back the name at that index.
> Check it: try `["Ada", "Grace", "Alan"]` with `[88, 92, 45]`, which gives `"Grace"`. Then the awkward ones: `[]` with `[]`; and a tie at the top, where the first of them is the answer.

7. Step 4: write `count_passing(scores)`, which gives back how many scores are 60 or more.

> Split it: it has the shape of `count_above()` in lesson 7.7. Is 60 itself a pass?
> Check it: try `[88, 92, 45, 95, 71]`, which gives 4. Then the awkward ones: `[]`, and `[60, 59]`, which gives 1.

### Another way to write it

In lesson 7.7, a loop with an `if` built `passing`, a new list of the passing scores. Python has a shorter way to write that loop, called a **list comprehension**:

```python
scores = [88, 92, 45, 95, 71]
passing = [score for score in scores if score >= 60]
print(passing)
```

Output:

```
[88, 92, 95, 71]
```

Read it as the loop, squeezed into the brackets of the new list: `for score in scores`, keep it `if score >= 60`, and what goes in the new list comes first, `score`. With no `if`, every item goes in, changed however you say:

```python
numbers = [1, 2, 3]
print([number * 10 for number in numbers])
```

Output:

```
[10, 20, 30]
```

You don't need it: no exercise asks for it, and the loop does the same job. But you will meet it in other people's Python, so it is worth being able to read.

### Practice

8. Predict what this prints, then press Check.

```python
numbers = [4, 7, 2, 9]
print([number + 1 for number in numbers])
print([number for number in numbers if number > 5])
```

### Try It

9. Print the gradebook for this class. Its first five lines are `Ada 88 B`, `Grace 92 A`, `Alan 45 F`, `Katherine 95 A` and `Edsger 71 C`, and the last three are `Average: 78.2`, `Top: Katherine 95` and `Passing: 4 of 5`, exactly like that.

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

names = ["Ada", "Grace", "Alan", "Katherine", "Edsger"]
scores = [88, 92, 45, 95, 71]
```

> Say it: one line per student, then three lines about the class. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: the plan above. Copy in `average()`, `top_student()` and `count_passing()` first. Then a loop with each index prints the students' lines; then the three summary lines, from your functions.
> Name it: the lists and functions are named for you. What would you call the index in the loop?
> Check it: run it and compare each line. Then try a change: make Alan's score 60. He gets a D, and `Passing: 5 of 5`. Put it back to 45 before you press Check.

### What you can do now

- Find where an item is with `index()`, and how many times it appears with `count()`.
- Keep two lists side by side, and find a name from the position of a score.
- Build a program from small functions, each checked on its own.

Key words: **index()**, **count()**, **parallel lists**, **list comprehension**.

That is the end of unit 7. Its quiz is below: fill it in, then show or print it.
