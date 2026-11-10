<!-- part: Unit 10 — Tuples and records -->
## Lesson 10.3 — Lists of tuples, and tuples as keys

A tuple holds the parts of one thing: a city's name and where it is, or a bus's route, time and stop. In this lesson you keep many such things in a list, and loop over them. Then you use a tuple where a list can never go: as a dictionary key.

### Warm-up

1. Predict what this prints, then press Check.

```python
def split_time(total_seconds):
    return total_seconds // 60, total_seconds % 60


print(split_time(125))
minutes, seconds = split_time(59)
print(minutes, seconds)
```

2. What does `return low, high` give back?

### A list of tuples

A list can hold tuples, one for each thing. Here each city is a tuple of its name, its latitude and its longitude:

```python
cities = [
    ("Paris", 48.9, 2.4),
    ("Tokyo", 35.7, 139.7),
    ("Lima", -12.0, -77.0),
]
for name, latitude, longitude in cities:
    print(f"{name}: {latitude}, {longitude}")
```

Output:

```
Paris: 48.9, 2.4
Tokyo: 35.7, 139.7
Lima: -12.0, -77.0
```

Each time round, the loop unpacks one tuple into three names, in order. That is what `items()` does too: it gives each entry as a tuple of a key and its value. With one name in the `for` line, you get each tuple whole:

```python
scores = {"Ada": 88, "Grace": 92}
for pair in scores.items():
    print(pair)
```

Output:

```
('Ada', 88)
('Grace', 92)
```

### Practice

3. Predict what this prints, then press Check.

```python
services = [("47", 415, "Harbour"), ("12", 380, "Museum"), ("9", 1000, "Airport")]
for route, minute, place in services:
    if minute < 500:
        print(route, place)
stock = {"pens": 3}
for pair in stock.items():
    print(pair)
```

4. Add a loop that prints each city on its own line, like `Paris is at 48.9, 2.4`.

```python
cities = [
    ("Paris", 48.9, 2.4),
    ("Tokyo", 35.7, 139.7),
    ("Lima", -12.0, -77.0),
    ("Cairo", 30.0, 31.2),
    ("Oslo", 59.9, 10.8),
]
```

> Split it: one `for` line that unpacks each tuple into three names, then one `print()` inside it.

5. Write a function `destinations(services)` that gives back a list of the places the services in the list go to, in the same order. Each service is a tuple of its route, its time and its place. Write it above these lines, then run them all.

```python
services = [("47", 415, "Harbour"), ("12", 380, "Museum"), ("9", 1000, "Airport")]
print(destinations(services))
print(destinations([]))
```

> Split it: start an empty list. Loop over the services, unpacking each one, and add its place to the list. Give the list back.
> Check it: the lines print `['Harbour', 'Museum', 'Airport']`, then the awkward one, `[]`.

### Tuples as keys

A dictionary key must never change while it is in the dictionary, or the dictionary could no longer find it. That is why a list cannot be a key (lesson 9.8). A tuple cannot change, so it can be one. Here is a tic-tac-toe board, keyed by (row, column):

```python
board = {}
board[(0, 0)] = "X"
board[(1, 1)] = "O"
board[(2, 2)] = "X"
print(board[(1, 1)])
print((0, 0) in board)
print((0, 1) in board)
print(board)
```

Output:

```
O
True
False
{(0, 0): 'X', (1, 1): 'O', (2, 2): 'X'}
```

Only the squares with a mark are stored. `get()` with a default fills in the rest, so one row prints like this:

```python
board = {(0, 0): "X", (1, 1): "O", (2, 2): "X"}
row = 0
line = ""
for column in range(3):
    line += board.get((row, column), ".")
print(line)
```

Output:

```
X..
```

The key is made from the names each time round the loop: (0, 0), then (0, 1), then (0, 2).

### Practice

6. Predict what this prints, then press Check.

```python
seats = {("A", 1): "Ada", ("B", 3): "Bo"}
print(seats[("B", 3)])
print(("A", 2) in seats)
print(seats.get(("A", 2), "empty"))
seats[("A", 2)] = "Cy"
print(len(seats))
```

7. Why can a tuple be a dictionary key, when a list cannot?

### Try It

8. Print the whole board as a grid of three lines, with a `.` for each empty square. For this board, the first line is `X.O`.

```python
board = {(0, 0): "X", (1, 1): "O", (2, 2): "X", (0, 2): "O"}
```

> Say it: the board goes in; three lines of three squares come out, a mark or a `.` for each. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. loop over the rows, 0 to 2. 2. for each row, build its line as the example does: start it empty, and loop over the columns, adding the mark or a `.`. 3. print the line.
> Name it: what would you call the row, the column, and the line being built?
> Check it: the three lines are X.O, then .O., then ..X. Then the awkward one: change the board to `{}`, an empty board, and you get three lines of dots. Put the board back before you press Check.

### What you can do now

- Loop over a list of tuples, unpacking each one in the `for` line.
- Use a tuple as a dictionary key, where a list cannot go.
- Print a grid from a dictionary keyed by (row, column).

Key words: **list of tuples**.
