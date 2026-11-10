<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.7 — Measuring the work

This unit has given you two searches, three sorts, and a way to count the work each one does. In this lesson you put them side by side: a program that measures them on lists of several sizes, and prints the counts in a table, built one function at a time.

### Warm-up

1. Predict what this prints, then press Check.

```python
words = ["Kiwi", "fig", "apple"]
print(sorted(words, key=str.lower))
print((2, "fig") < (2, "Kiwi"))
print(sorted([(2, "fig"), (1, "pear"), (2, "Kiwi")]))
```

2. In `place_for()` from lesson 11.6, what makes a new item that ties with one already in the list go before it?

### The plan

Here is the problem: "Measure this unit's searches and sorts. For lists of 4, 8, 16 and 32 numbers, print how many comparisons each one makes: a linear search and a binary search of a sorted list, for a number that is not in it; and a selection sort and a bubble sort of a list that is nearly in order, with only its first two numbers the wrong way round. Print a heading line first."

A nearly sorted list is common: race times handed in almost in the order the runners finished, say. `row()` prints one line of the table, each value at the right of a column 10 wide. Text lines up the same way as numbers, so it prints the heading line too:

```python
def row(size, linear, binary, selection, bubble):
    """Print one line of the table, each value at the right of a column 10 wide."""
    print(f"{size:>10}{linear:>10}{binary:>10}{selection:>10}{bubble:>10}")


row("size", "linear", "binary", "selection", "bubble")
row(4, 4, 3, 6, 5)
```

Output:

```
      size    linear    binary selection    bubble
         4         4         3         6         5
```

Now Say it and Split it, as comments:

```python
# Say it: print how many comparisons each search and sort makes, for lists of 4, 8, 16 and 32 numbers.
# Split it:
# 1. the heading line: row() with the five column names
# 2. for each size, a sorted list of that many numbers, and a copy with its first two numbers swapped
# 3. the searches' counts on the sorted list, for the target size: linear_count(), binary_count()
# 4. the sorts' counts on the nearly sorted list: selection_count(), bubble_count()
# 5. the line for that size: row()
```

You have `linear_count()` and `binary_count()` from lesson 11.3, and `selection_count()` from lesson 11.4. `bubble_count()` is new, so build it first, then step 2.

### Practice

3. Step 4: write `bubble_count(items)`, which gives back how many comparisons lesson 11.5's bubble sort makes when it sorts `items`: the one that skips the settled end with `- done`, and stops early.

> Split it: the bubble sort with `swapped` from lesson 11.5, on a copy. Add one to a count each time two neighbors are compared, just before the `if`. Give back the count.
> Check it: try `[1, 2, 3, 4]`, which gives 3: one pass, then it stops. And `[4, 3, 2, 1]`, which gives 6. Then the awkward ones: `[]` and `[7]`, which give 0.

4. Step 2: predict what this prints, then press Check.

```python
size = 5
numbers = [number for number in range(size)]
nearly = numbers.copy()
nearly[0], nearly[1] = nearly[1], nearly[0]
print(numbers)
print(nearly)
```

### The finished table

For the four sizes, the table looks like this:

```
      size    linear    binary selection    bubble
         4         4         3         6         5
         8         8         4        28        13
        16        16         5       120        29
        32        32         6       496        61
```

### Practice

5. In the table, a bubble sort makes far fewer comparisons than a selection sort. Why?

6. From 16 numbers to 32, the list doubles. What happens to the selection sort's count?

### Try It

7. Print the table, exactly as shown above.

> Say it: a heading line, then a line for each size, with the comparisons each search and sort makes. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: the plan above. Copy in `row()`, `linear_count()`, `binary_count()`, `selection_count()` and your `bubble_count()` first. Then print the heading line, and loop over the sizes, working through steps 2 to 5 for each.
> Name it: `row()` and the four counting functions are named for you. What would you call the sorted list, and the nearly sorted one?
> Check it: run it and compare each line, spaces too. The binary column goes up by one each time the size doubles, and the selection column about four times. Then try an awkward size: put 2 at the start of the list of sizes. Its line is 2, 2, 2, 1 and 1, in columns: two numbers swapped need one comparison to sort. Take the 2 out again before you press Check.

### What you can do now

- Measure an algorithm by counting its comparisons on lists of several sizes.
- Build a program that compares searches and sorts, one checked function at a time.
- Read a table of counts: which work doubles, which goes up by one, which goes up four times, and which stays small on a list that is nearly in order.

Key words: **nearly sorted**.

That is the end of unit 11. Its quiz is below: fill it in, then show or print it.
