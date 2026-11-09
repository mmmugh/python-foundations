<!-- part: Unit 8 — Strings as data -->
## Lesson 8.11 — Lining up columns

A table is easier to read when its numbers line up. In this lesson you give a value a width in an f-string, so the columns of a table line up, however long each value is.

### Warm-up

1. Predict what this prints, then press Check.

```python
print("one\ttwo".split("\t"))
print(len("a\\b"))
print("Hi\nthere")
```

2. A string between three quotes on each side runs over three lines. What is in it where each line ends?

### Lining up columns

In lesson 3.3, `:.2f` after a name in an f-string said how to show a number. A format specifier can also give a **width**: how many characters the value fills, with spaces making up the rest. `<` puts the value at the left of its width, and `>` at the right:

```python
name = "Ada"
score = 88
print(f"[{name:<8}]")
print(f"[{score:>5}]")
```

Output:

```
[Ada     ]
[   88]
```

The brackets show the width: `Ada` and 5 spaces fill 8, and 3 spaces and `88` fill 5. Give every line the same widths, and the columns line up, however long each value is:

```python
names = ["Ada", "Katherine", "Bo"]
scores = [88, 95, 7]
for i in range(len(names)):
    print(f"{names[i]:<10}{scores[i]:>4}")
```

Output:

```
Ada         88
Katherine   95
Bo           7
```

A width goes before the decimal places, so `:>6.1f` means "6 wide, at the right, with 1 decimal place":

```python
average = 4.3333
print(f"[{average:>6.1f}]")
```

Output:

```
[   4.3]
```

### Practice

3. Predict what this prints, then press Check. Count the spaces.

```python
item = "tea"
price = 2.5
print(f"[{item:<6}]")
print(f"[{item:>6}]")
print(f"[{price:>6.2f}]")
```

4. Print the menu so that its prices line up: each item at the left of a column 8 wide, then each price at the right of a column 6 wide, with 2 decimal places. The first line is `tea       2.50`.

```python
items = ["tea", "cake", "soup"]
prices = [2.5, 3.25, 4.0]
```

> Split it: loop with each index, as in the scores example. One f-string per line: `<8` for the item, `>6.2f` for the price.

### Try It

5. Print a receipt with its prices lined up. Each item goes at the left of a column 12 wide, and each price at the right of a column 8 wide, with 2 decimal places. Under the items, print a line of 20 `-` signs, then `Total` and the total of the prices, in the same two columns. The first line is `notebook        3.50`, and the last is `Total           7.50`.

```python
items = ["notebook", "pens", "stickers"]
prices = [3.5, 2.25, 1.75]
```

> Say it: one line per item, with its price, in two columns; then a dashed line; then the total in the same columns. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. loop with each index, and print the item with `<12` and the price with `>8.2f`. 2. print 20 `-` signs, as in lesson 3.4. 3. work out the total of the prices. 4. print `Total` and the total, with the same widths.
> Name it: the lists are named for you. What would you call the total?
> Check it: run it and compare each line, spaces too. Then try a change: add `"glue"` at `0.99` to the ends of the two lists. Its line should line up, and the total become 8.49. Take it out again before you press Check.

### What you can do now

- Give a value a width in an f-string, at the left with `<` or at the right with `>`.
- Put a width before the decimal places, as in `:>6.2f`.
- Line up the columns of a table, however long each value is.

Key words: **width**.
