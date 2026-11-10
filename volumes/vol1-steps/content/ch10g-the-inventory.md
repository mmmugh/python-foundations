<!-- part: Unit 10 — Tuples and records -->
## Lesson 10.7 — Choosing a value, and an inventory

This unit has given you tuples, records, sorting by a field and grouping. In this lesson you meet a one-line way to choose between two values, and then put the unit together: a report on a shop's stock, built one function at a time.

### Warm-up

1. Predict what this prints, then press Check.

```python
groups = {}
for word in ["fig", "kiwi", "fig"]:
    groups.setdefault(len(word), []).append(word)
print(groups)
```

2. `items` is a list of records, each with a `"price"` field. Which of these sorts them by price, cheapest first?

### Choosing between two values

An `if` and an `else` choose which lines run. Sometimes all you want is to choose between two values. A **conditional expression** does that in one line:

```python
quantity = 0
label = "OUT OF STOCK" if quantity == 0 else f"{quantity} left"
print(label)
quantity = 8
label = "OUT OF STOCK" if quantity == 0 else f"{quantity} left"
print(label)
```

Output:

```
OUT OF STOCK
8 left
```

Read it as: this value if the condition is true, else that value. It does the same job as these four lines:

```python
quantity = 8
if quantity == 0:
    label = "OUT OF STOCK"
else:
    label = f"{quantity} left"
print(label)
```

Output:

```
8 left
```

Use it only when it fits easily on one line. When it doesn't, the four lines are clearer.

### Practice

3. Predict what this prints, then press Check.

```python
for score in [45, 50, 92]:
    result = "pass" if score >= 50 else "fail"
    print(score, result)
count = 1
print(f"{count} {'item' if count == 1 else 'items'}")
```

4. Write a function `stock_label(quantity)` that gives back `"OUT OF STOCK"` when `quantity` is 0, and otherwise the quantity and the word `left`, like `"8 left"`. Use a conditional expression.

> Split it: one line: give back the first text if the quantity is 0, else the second.
> Check it: try 8, which gives `"8 left"`, and 1, which gives `"1 left"`. Then the awkward one: 0, which gives `"OUT OF STOCK"`.

### A value that stays the same

The report lists the items that are running low: those with 10 or fewer left. That 10 is used in more than one place, so it gets a name:

```python
LOW_STOCK = 10
for quantity in [3, 10, 42]:
    if quantity <= LOW_STOCK:
        print(quantity, "is low")
```

Output:

```
3 is low
10 is low
```

A name in capitals is a **constant**: a value fixed for the whole program. Python does not stop you changing it, but the capitals tell whoever reads the code not to. And to change the limit, you change one line, instead of hunting for every 10.

### Practice

5. Why is `LOW_STOCK` written in capitals?

### The plan

Here is the problem: "A shop keeps each item it sells as a record: its name, category, price and how many are left. Print a report: a line for each item, in order of name, with its value; the total value of all the stock; the items running low, fewest first, with how many are left; and, for each category, how many items it has and what they are worth."

`item_line()` prints one item's line, in columns, as in lesson 8.11. Its value is the price times the quantity:

```python
def item_line(item):
    """Print one item's line: name, category, price, quantity and value."""
    value = item["price"] * item["quantity"]
    words = f"{item['name']:<12}{item['category']:<10}"
    numbers = f"{item['price']:>7.2f}{item['quantity']:>5}{value:>9.2f}"
    print(words + numbers)


item_line({"name": "Pens", "category": "writing", "price": 2.25, "quantity": 8})
```

Output:

```
Pens        writing      2.25    8    18.00
```

Now Say it and Split it, as comments:

```python
# Say it: print a report on the shop's stock.
# Split it:
# 1. a line for each item, in order of name: sorted() with a lambda, and item_line()
# 2. the total value of all the stock: total_value(items)
# 3. the items at or below LOW_STOCK, fewest first: low_stock(items, LOW_STOCK)
# 4. a label for each of those: stock_label(quantity)
# 5. the items in each category: by_category(items)
# 6. a line for each category, in order: how many items, and total_value() of them
```

You have `stock_label()` already. Build and check the other three one at a time.

### Practice

6. Step 2: write `total_value(items)`, which gives back the value of all the stock in the list of records `items`: each item's price times its quantity, added up.

> Split it: start a total at 0. For each item, add its price times its quantity. Give the total back.
> Check it: try `[{"name": "Pens", "category": "writing", "price": 2.25, "quantity": 8}]`, which gives 18.0. Then the awkward one: `[]`, which gives 0.

7. Step 3: write `low_stock(items, limit)`, which gives back a list of the records in `items` whose quantity is at or below `limit`, fewest first. Records with the same quantity keep their order.

> Split it: keep the items whose quantity is at or below the limit, with a list comprehension or a loop. Then give back that list sorted by quantity, with a `lambda`.
> Check it: with a limit of 10, an item with 10 left is in the list, and one with 11 is not. Then the awkward one: `[]`, which gives `[]`.

8. Step 5: write `by_category(items)`, which gives back a dictionary from each category to a list of the records in that category, in the order they are in `items`.

> Split it: lesson 10.6's grouping loop, with the category as the key and the whole record added to its list.
> Check it: two items in the same category end up in one list. Then the awkward one: `[]`, which gives `{}`.

### The finished report

For the stock in the try-it, the report looks like this:

```
Backpack    bags        34.99    5   174.95
Lunch box   bags        12.00    0     0.00
Notebook    paper        3.50   42   147.00
Pencils     writing      1.20    3     3.60
Pens        writing      2.25   10    22.50
Ruler       writing      0.85   15    12.75
Stickers    paper        1.75  120   210.00
Total value: 570.80
Low stock, at or below 10:
Lunch box   OUT OF STOCK
Pencils     3 left
Backpack    5 left
Pens        10 left
By category:
bags        2 items   174.95
paper       2 items   357.00
writing     3 items    38.85
```

The total has 2 decimal places. In the low-stock lines, the name is at the left of a column 12 wide, then the label. In the category lines, the category is at the left of a column 12 wide, then the number of items and the word `items`, then the value at the right of a column 9 wide, with 2 decimal places.

### Try It

9. Print the report for this stock, exactly as shown above.

```python
def item_line(item):
    """Print one item's line: name, category, price, quantity and value."""
    value = item["price"] * item["quantity"]
    words = f"{item['name']:<12}{item['category']:<10}"
    numbers = f"{item['price']:>7.2f}{item['quantity']:>5}{value:>9.2f}"
    print(words + numbers)


LOW_STOCK = 10

inventory = [
    {"name": "Notebook", "category": "paper", "price": 3.50, "quantity": 42},
    {"name": "Pens", "category": "writing", "price": 2.25, "quantity": 10},
    {"name": "Stickers", "category": "paper", "price": 1.75, "quantity": 120},
    {"name": "Backpack", "category": "bags", "price": 34.99, "quantity": 5},
    {"name": "Pencils", "category": "writing", "price": 1.20, "quantity": 3},
    {"name": "Lunch box", "category": "bags", "price": 12.00, "quantity": 0},
    {"name": "Ruler", "category": "writing", "price": 0.85, "quantity": 15},
]
```

> Say it: a line for each item in order of name, the total, the low-stock lines, then a line for each category. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: the plan above. Copy in `stock_label()`, `total_value()`, `low_stock()` and `by_category()` first. Then work through steps 1 to 6, printing the two heading lines where they go.
> Name it: the stock, the limit and `item_line()` are named for you. What would you call the dictionary of categories, and the list of records in one category?
> Check it: run it and compare each line, spaces too. Pens, with exactly 10 left, is on the low-stock list, because the limit is at or below 10. Then try a change: set `LOW_STOCK` to 5. Now Pens drops out of the low-stock lines, and the heading says 5, if it prints `LOW_STOCK` rather than a 10 of its own. Put it back before you press Check.

### What you can do now

- Choose between two values in one line, with a conditional expression.
- Name a value that stays the same, as a constant in capitals.
- Build a report on a list of records from small functions, each checked on its own.

Key words: **conditional expression**, **constant**.

That is the end of unit 10. Its quiz is below: fill it in, then show or print it.
