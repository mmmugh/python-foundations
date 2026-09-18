<!-- part: Part II — Structuring Data -->
## Chapter 10 — Tuples and Structured Records

A **tuple** is an ordered collection, like a list, that cannot be changed after it is made. Round brackets instead of square ones:

```python
point = (3, 4)
color = (255, 128, 0)

print(point[0])
print(len(color))

for value in color:
    print(value)
```

Output:

```
3
3
255
128
0
```

Indexing, slicing, `len()`, `in`, and `for` all work exactly as with lists. The only thing you cannot do is change it:

```python
point = (3, 4)
point[0] = 5
```

```
TypeError: 'tuple' object does not support item assignment
```

### Why have an unchangeable list?

The question is fair, and there are three answers.

**It documents intent.** A tuple says "these values belong together and this grouping will not change." A coordinate pair, an RGB color, a latitude and longitude, a month-and-day — these are single things that happen to have parts, not collections you will be adding to. A reader who sees a tuple knows not to look for code that modifies it.

**It cannot be corrupted by accident.** Because a tuple cannot be changed, passing one to a function carries no risk that the function will alter it behind your back.

**It can be a dictionary key.** This is the concrete, practical reason. Dictionary keys must be unchangeable, so a list cannot be a key but a tuple can:

```python
# Storing values on a grid, keyed by coordinate
board = {}
board[(0, 0)] = "X"
board[(1, 1)] = "O"
board[(2, 2)] = "X"

print(board[(1, 1)])
print((0, 0) in board)
print((0, 1) in board)
```

Output:

```
O
True
False
```

That is a clean way to represent a sparse grid — a chess or tic-tac-toe board where most squares are empty — without building a full nested list.

### Unpacking

Assigning a tuple to several names at once is called **unpacking**, and it is used everywhere in Python:

```python
point = (3, 4)
x, y = point
print(f"x is {x}, y is {y}")

# Swapping two variables, in one line
a = 1
b = 2
a, b = b, a
print(a, b)
```

Output:

```
x is 3, y is 4
2 1
```

That swap is a small piece of Python elegance. In most languages it takes a temporary variable.

The number of names must match the number of values, or Python raises a `ValueError`.

You have already been unpacking without knowing it. When a function returns several values, what actually comes back is a tuple:

```python
def min_max(numbers):
    """Return the smallest and largest values in a list."""
    return min(numbers), max(numbers)


result = min_max([5, 2, 9, 1])
print(result)
print(type(result))

lowest, highest = min_max([5, 2, 9, 1])
print(f"from {lowest} to {highest}")
```

Output:

```
(1, 9)
<class 'tuple'>
from 1 to 9
```

And `.items()` from Chapter 9 hands out tuples, which is why `for name, score in scores.items():` works — each pair is unpacked as the loop runs.

A single-item tuple needs a trailing comma: `(5,)` is a tuple, while `(5)` is just the number 5 in parentheses. This is a known wart in the language.

### Records: lists of dictionaries

Here is where Part II comes together. Real data is usually a **collection of records**, each record holding several named fields. In Python that is a list of dictionaries.

```python
students = [
    {"name": "Ada", "grade": 9, "score": 88},
    {"name": "Grace", "grade": 10, "score": 92},
    {"name": "Alan", "grade": 9, "score": 45},
    {"name": "Katherine", "grade": 11, "score": 95},
]

for student in students:
    print(f"{student['name']}: {student['score']}")
```

Output:

```
Ada: 88
Grace: 92
Alan: 45
Katherine: 95
```

Compare this with Chapter 7's parallel lists. Each student's facts now travel together in one place. Sorting the list rearranges whole records rather than breaking the correspondence between them, and adding a new field means adding a key rather than creating and maintaining a fourth list.

### Working with records

**Filtering:**

```python
ninth_graders = [s for s in students if s["grade"] == 9]
for s in ninth_graders:
    print(s["name"])
```

Output:

```
Ada
Alan
```

**Extracting one field:**

```python
all_scores = [s["score"] for s in students]
print(all_scores)
print(sum(all_scores) / len(all_scores))
```

Output:

```
[88, 92, 45, 95]
80.0
```

**Sorting by a field:**

```python
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
for s in by_score:
    print(f"{s['name']:<12}{s['score']}")
```

Output:

```
Katherine   95
Grace       92
Ada         88
Alan        45
```

That `key=lambda s: s["score"]` is the same idea as in Chapter 9: it tells `sorted()` what to compare. Crucially, the records stay intact — Katherine keeps her own score, which is exactly what parallel lists could not guarantee.

**Finding one record:**

```python
def find_student(students, name):
    """Return the record for a named student, or None if absent."""
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


found = find_student(students, "grace")
if found:
    print(f"{found['name']} is in grade {found['grade']}.")
else:
    print("Not found.")
```

Output:

```
Grace is in grade 10.
```

Returning `None` when nothing matches, and having the caller check, is a standard pattern. Chapter 11 looks at what this loop costs when the list gets long.

**Grouping into a dictionary:**

```python
by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

for grade in sorted(by_grade):
    print(f"Grade {grade}: {', '.join(by_grade[grade])}")
```

Output:

```
Grade 9: Ada, Alan
Grade 10: Grace
Grade 11: Katherine
```

That pattern — a dictionary whose values are lists — is how you group anything by a shared property, and it shows up constantly once you start handling real data.

### Common mistakes

| Mistake | What happens |
| --- | --- |
| `point[0] = 5` on a tuple | `TypeError` — tuples cannot be changed |
| `(5)` expecting a tuple | That is the number 5; use `(5,)` |
| `a, b = (1, 2, 3)` | `ValueError` — the counts must match |
| Using a list as a dictionary key | `TypeError` — use a tuple |
| `student.name` instead of `student["name"]` | `AttributeError` — dictionaries use brackets |
| Sorting a list of records without `key=` | `TypeError` — Python cannot compare dictionaries |

### Try It

1. Store five cities as `(name, latitude, longitude)` tuples and print each formatted.
2. Write `distance(p1, p2)` taking two `(x, y)` tuples and returning the distance between them.
3. Build a list of book records with title, author, and year, then print them sorted by year.
4. From that list, print only books published after 2000.
5. Group the books by author into a dictionary.
6. Write `oldest(books)` returning the record — not just the title — of the earliest book.
7. Use a dictionary with tuple keys to store a 3-by-3 tic-tac-toe board and print it as a grid.

### Chapter project: an inventory system

Build an inventory that stores items as records and answers real questions about them.

```python
# An inventory of items stored as records, with reports.

inventory = [
    {"name": "Notebook", "category": "paper", "price": 3.50, "quantity": 42},
    {"name": "Pens", "category": "writing", "price": 2.25, "quantity": 8},
    {"name": "Stickers", "category": "paper", "price": 1.75, "quantity": 120},
    {"name": "Backpack", "category": "bags", "price": 34.99, "quantity": 5},
    {"name": "Pencils", "category": "writing", "price": 1.20, "quantity": 3},
    {"name": "Lunch box", "category": "bags", "price": 12.00, "quantity": 0},
]

LOW_STOCK = 10


def item_value(item):
    """Return the total value of one item's stock."""
    return item["price"] * item["quantity"]


def total_value(items):
    """Return the total value of all stock."""
    total = 0.0
    for item in items:
        total += item_value(item)
    return total


def low_stock(items, threshold):
    """Return the items at or below a stock threshold, fewest first."""
    low = [i for i in items if i["quantity"] <= threshold]
    return sorted(low, key=lambda i: i["quantity"])


def by_category(items):
    """Return a dictionary mapping each category to its items."""
    groups = {}
    for item in items:
        groups.setdefault(item["category"], []).append(item)
    return groups


def print_inventory(items):
    """Print the full inventory table."""
    print(f"{'Item':<12}{'Category':<10}{'Price':>8}{'Qty':>6}{'Value':>10}")
    print("-" * 46)
    for item in sorted(items, key=lambda i: i["name"]):
        print(
            f"{item['name']:<12}{item['category']:<10}"
            f"${item['price']:>7.2f}{item['quantity']:>6}"
            f"${item_value(item):>9.2f}"
        )
    print("-" * 46)
    print(f"{'TOTAL':<36}${total_value(items):>9.2f}")


def print_alerts(items):
    """Print low-stock and out-of-stock warnings."""
    print(f"\nLow stock (at or below {LOW_STOCK}):")
    for item in low_stock(items, LOW_STOCK):
        state = "OUT OF STOCK" if item["quantity"] == 0 else f"{item['quantity']} left"
        print(f"  {item['name']:<12}{state}")


def print_categories(items):
    """Print a summary of each category."""
    print("\nBy category:")
    groups = by_category(items)
    for category in sorted(groups):
        members = groups[category]
        value = total_value(members)
        print(f"  {category:<10}{len(members)} items{value:>10.2f}")


print_inventory(inventory)
print_alerts(inventory)
print_categories(inventory)
```

Output:

```
Item        Category     Price   Qty     Value
----------------------------------------------
Backpack    bags      $  34.99     5$   174.95
Lunch box   bags      $  12.00     0$     0.00
Notebook    paper     $   3.50    42$   147.00
Pencils     writing   $   1.20     3$     3.60
Pens        writing   $   2.25     8$    18.00
Stickers    paper     $   1.75   120$   210.00
----------------------------------------------
TOTAL                               $   553.55

Low stock (at or below 10):
  Lunch box   OUT OF STOCK
  Pencils     3 left
  Backpack    5 left
  Pens        8 left

By category:
  bags      2 items    174.95
  paper     2 items    357.00
  writing   2 items     21.60
```

Four things to notice.

`LOW_STOCK = 10` is written in capitals, the Python convention for a **constant** — a value fixed for the whole program. Python does not enforce it, but the capitals tell a reader not to change it, and having the threshold in one named place beats scattering `10` through the code.

`.setdefault(key, [])` returns the value for a key, inserting a default first if the key is absent. It collapses the three-line grouping pattern from earlier in this chapter into one line.

The long f-strings in `print_inventory` are split across several lines inside parentheses, using the same adjacent-string-literal rule from Chapter 8. A formatting line that runs past 80 characters is hard to check, and this keeps each piece readable.

Finally: `state = "OUT OF STOCK" if item["quantity"] == 0 else ...` is a **conditional expression** — an `if`/`else` that produces a value rather than choosing statements. It is a compact form of the four-line `if`/`else` you already know, and is worth using only when it fits comfortably on one line.
