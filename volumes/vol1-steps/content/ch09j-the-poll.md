<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.10 — A poll counter

This unit has given you dictionaries, counting, ranking and sets. In this lesson you put them together: a program that counts the votes in a poll and reports on them, built one function at a time.

### Warm-up

1. Predict what this prints, then press Check.

```python
red = {"Ada", "Bo", "Cy"}
blue = {"Cy", "Di"}
print(sorted(red | blue))
print(sorted(red & blue))
print(sorted(blue - red))
```

2. A program keeps how many votes each option in a poll has had. Which container fits?

### The poll counter

Here is the problem: "A class voted on what to have for lunch. Count the votes, and print a report: each option, most votes first, with its votes, its share of all the votes, and a bar. Then print the total, how many different options got votes, and the winner. If two or more options tie for the most votes, say so, and name them all."

First, the shape of one line of the report. The option is at the left of a column 10 wide, its votes at the right of a column 4 wide, and its share at the right of a column 7 wide, as in lesson 8.11. The bar has one `#` for every 4 percent of the votes, so 100% would be 25 wide, and `round()` keeps it to whole characters:

```python
def report_line(option, count, total):
    """Print one option's line: its votes, its share of all the votes, and a bar."""
    share = count / total * 100
    bar = "#" * round(share / 4)
    print(f"{option:<10}{count:>4}{share:>7.1f}%  {bar}")


report_line("pizza", 6, 15)
report_line("salad", 1, 15)
```

Output:

```
pizza        6   40.0%  ##########
salad        1    6.7%  ##
```

### Practice

3. Predict what this prints, then press Check. It is `report_line()` from above, without its docstring.

```python
def report_line(option, count, total):
    share = count / total * 100
    bar = "#" * round(share / 4)
    print(f"{option:<10}{count:>4}{share:>7.1f}%  {bar}")


report_line("chips", 3, 12)
report_line("soup", 0, 12)
```

### The plan

Now Say it and Split it, as comments:

```python
# Say it: count the votes, and print a report on them.
# Split it:
# 1. count the votes: tally(votes) gives back a dictionary of counts
# 2. rank the options, most votes first: sorted() with key= and reverse=True
# 3. print a line for each option, with report_line()
# 4. print the total, and how many different options got votes: len() and set()
# 5. find every option with the most votes: winners(counts)
# 6. print the winner, or the options that tied: winner_line(leaders)
```

Steps 2, 3 and 4 use what you already have. Build and check the three new functions one at a time.

Why does `winners()` give back a list, not one option? Because two options can **tie**: have the same number of votes. A program that assumes there is always one winner reports a false result the first time two options match.

### Practice

4. Step 1: write `tally(votes)`, which gives back a dictionary of how many times each option appears in the list `votes`.

> Split it: the counting pattern from lesson 9.4, over a list.
> Check it: try `["pizza", "tacos", "pizza"]`, which gives `{"pizza": 2, "tacos": 1}`. Then the awkward one: `[]`, which gives `{}`.

5. Step 5: write `winners(counts)`, which gives back a list of every option in `counts` that has the most votes, in the dictionary's order. For an empty dictionary, it gives back `[]`.

> Split it: first, if `counts` is empty, give back `[]`. Otherwise: find the most votes, with `max()` of the values. Then loop over the counts with `items()`, and add each option whose count is that many.
> Check it: try `{"pizza": 6, "tacos": 4}`, which gives `["pizza"]`, and `{"sushi": 4, "tacos": 4, "salad": 1}`, which gives `["sushi", "tacos"]`. Then the awkward one: `{}`.

6. Step 6: write `winner_line(leaders)`, which gives back the last line of the report from the list of leaders. One leader gives `"Winner: pizza"`. Two or more give `"Tied: "` and their names in alphabetical order, with `", "` between, like `"Tied: sushi, tacos"`. No leaders at all, `[]`, gives `"No votes"`.

> Split it: three cases, so an `if`, an `elif` and an `else`, on how many leaders there are. For a tie, sort the leaders and join them.
> Check it: try `["pizza"]` and `["tacos", "sushi"]`. Then the awkward one: `[]`.

### The finished report

For the votes in the try-it, the report looks like this:

```
pizza        6   40.0%  ##########
tacos        4   26.7%  #######
sushi        4   26.7%  #######
salad        1    6.7%  ##
Total votes: 15
Options: 4
Winner: pizza
```

### Try It

7. Print the report for these votes, exactly as shown above.

```python
def report_line(option, count, total):
    """Print one option's line: its votes, its share of all the votes, and a bar."""
    share = count / total * 100
    bar = "#" * round(share / 4)
    print(f"{option:<10}{count:>4}{share:>7.1f}%  {bar}")


votes = [
    "tacos", "pizza", "pizza", "sushi", "pizza",
    "tacos", "salad", "sushi", "pizza", "tacos",
    "sushi", "pizza", "tacos", "pizza", "sushi",
]
```

> Say it: one line for each option, most votes first, then the total, the number of options and the winner. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: the plan above. Copy in `tally()`, `winners()` and `winner_line()` first. Then count the votes once, and work through steps 2 to 6.
> Name it: the votes and `report_line()` are named for you. What would you call the dictionary of counts, and the list of leaders?
> Check it: run it and compare each line, spaces too. Then try a change: make the last `"pizza"` in the list a `"tacos"`. Now pizza and tacos tie with 5, and the last line says `Tied: pizza, tacos`. Put it back before you press Check.

### What you can do now

- Count, rank and report on votes, with a dictionary, `sorted()` and `key=`.
- Find every option that tied, and say so, rather than pick one.
- Build a program from small functions, each checked on its own.

Key words: **tie**.

That is the end of unit 9. Its quiz is below: fill it in, then show or print it.
