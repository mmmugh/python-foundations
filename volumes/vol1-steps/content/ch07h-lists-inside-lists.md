<!-- part: Unit 7 — Lists -->
## Lesson 7.8 — Lists inside lists

An item of a list can be any value, and that includes another list. In this lesson a list of lists holds a grid, like a game board or a table, and you print it row by row.

### Warm-up

1. Predict what this prints, then press Check.

```python
scores = [55, 82, 91, 40]
passing = []
for score in scores:
    if score >= 60:
        passing.append(score)
for position, score in enumerate(passing):
    print(position, score)
```

2. A loop removes items from the very list it is looping over, and some items get skipped. Why?

### A list of rows

Each item of `grid` is a list of three numbers: one **row** of the grid. A list inside a list is called a **nested list**.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(grid[0])
print(grid[1][2])
```

Output:

```
[1, 2, 3]
6
```

Between its brackets, a list can run over several lines, so the code looks like the grid it holds. The comma after the last row is allowed, and makes adding a row easy.

`grid[0]` is the first item of `grid`, which is a whole row. Two indexes reach one number: the first picks the row, and the second picks the item in that row. Read `grid[1][2]` from left to right: `grid[1]` is the row `[4, 5, 6]`, and index 2 of that row is 6.

Two indexes on the left of `=` change one item of a row:

```python
grid = [[0, 0, 0], [0, 0, 0]]
grid[1][2] = 7
print(grid)
```

Output:

```
[[0, 0, 0], [0, 0, 7]]
```

### Practice

3. Predict what this prints, then press Check.

```python
seats = [
    ["A1", "A2"],
    ["B1", "B2"],
    ["C1", "C2"],
]
print(seats[2])
print(seats[0][1])
print(seats[-1][0])
```

4. Fill in the table: the whole list `board` after each line. Then press Check.

```python
board = [[0, 0], [0, 0]]
board[0][1] = 5
board[1][0] = board[0][1] + 1
```

### Printing row by row

A `for` loop over `grid` gets one row each time round:

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in grid:
    print(row)
```

Output:

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

To print the numbers without brackets, a loop inside the loop goes through each row (lesson 5.4). `print()` usually ends with a new line, so each number would land on a line of its own. `end=" "` tells `print()` to end with a space instead:

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

Output:

```
1 2 3
4 5 6
7 8 9
```

The numbers of one row stay on one line. Then `print()` with nothing in its brackets ends that line, after the inner loop and before the next row.

### Practice

5. Predict what this prints, then press Check.

```python
rows = [["a", "b"], ["c", "d"]]
for row in rows:
    for letter in row:
        print(letter, end=" ")
    print()
print("done")
```

6. Print the total of each row of `sales`, one total per line.

```python
sales = [[3, 5, 2], [4, 0, 6], [1, 1, 1]]
```

> Check it: the totals are 10, 10 and 3. A row with a 0 in it still adds up.

### Try It

7. A tic-tac-toe board is a list of three rows, each a list of three squares, all `"."` to start. Put an `"X"` in the center square and an `"O"` in the top right corner. Then print the board, one row per line, with a space between the squares, so that the first line is `. . O`.

```python
board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
]
```

> Say it: change two squares of the board, then print it as three rows of three. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. put the X in the center: which row is it in, and which index in that row? 2. put the O in the top right corner. 3. for each row: print each square with a space after it, then end the line.
> Name it: the board is named for you. What would you call one row, and one square?
> Check it: the lines should be `. . O`, `. X .` and `. . .`. Then the awkward one: try `board[0][-1]` for the corner. Is it the same square?

### What you can do now

- Keep a grid as a list of rows, and reach one item with two indexes.
- Change one item of a row.
- Print a grid row by row, with `end=" "` and a nested loop.

Key words: **nested list**, **row**.
