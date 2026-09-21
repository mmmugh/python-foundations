# Worked solutions

One per Try It exercise that has no Check button, shown behind "Show a
solution" after the learner's own attempt. Drafted, and not yet in the
author's voice — the notes especially.

Each entry is `## <chapter slug>#<exercise number>`, then the code, then an
optional note of at most two sentences.

## ch01-your-first-programs#1

<!-- Write a program that prints your name, your school, and your favorite subject, each on its own line. -->

```python
# Prints my name, school, and favorite subject.
print("Ada Lovelace")
print("Somerville Academy")
print("Mathematics")
```

## ch01-your-first-programs#2

<!-- Make Python calculate and print the number of minutes in a week. Use a calculation, not the answer. -->

```python
# Calculates the number of minutes in a week.
print(7 * 24 * 60)
```

Python does the multiplication; nothing is typed in as a pre-computed number.

## ch01-your-first-programs#3

<!-- Write a program that prints a small shape out of asterisks, like a triangle four rows tall. -->

```python
# Prints a triangle of asterisks, four rows tall.
print("*")
print("**")
print("***")
print("****")
```

## ch02-variables-and-types#1

<!-- Create variables for a book's title, author, and page count, then print a sentence using all three. -->

```python
# Prints a sentence about a book using three variables.

title = "The Hobbit"
author = "J.R.R. Tolkien"
page_count = 310

print(title, "by", author, "has", page_count, "pages.")
```

f-strings aren't used because Chapter 2 hasn't taught them yet (the book itself introduces f-strings in Chapter 3); this matches how Chapter 2's own worked examples print.

## ch02-variables-and-types#3

<!-- Ask for a number of seconds and print it as minutes and seconds. (Chapter 3 introduces the operators that make this clean; try it with division first.) -->

```python
# Converts a number of seconds into minutes and seconds.

seconds = int(input("Enter a number of seconds: "))

minutes = int(seconds / 60)
remaining_seconds = seconds - minutes * 60

print(seconds, "seconds is", minutes, "minutes and", remaining_seconds, "seconds.")
```

This is the clunky 'division first' version the exercise asks for: int() truncates the division to get whole minutes, then multiplying back and subtracting finds the leftover seconds. Chapter 3's // and % do this in one step each.

## ch04-making-decisions#2

<!-- Ask for a year and print whether it is a leap year. (A year is a leap year if divisible by 4, except years divisible by 100, unless also divisible by 400.) -->

```python
# Asks for a year and reports whether it is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

The most specific rule (divisible by 400) goes first, exactly as Chapter 4 warns: an elif chain stops at the first true condition, so order decides the outcome for overlapping cases.

## ch04-making-decisions#3

<!-- Ask for two numbers and print the larger, handling the case where they are equal. -->

```python
# Asks for two numbers and prints the larger one.

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

if first > second:
    print(f"{first} is larger.")
elif second > first:
    print(f"{second} is larger.")
else:
    print("The numbers are equal.")
```

## ch04-making-decisions#6

<!-- Rewrite the grade program so it rejects scores below 0 or above 100 before grading. -->

```python
# Grades a test score, rejecting invalid values first.

score = int(input("Test score: "))

if score < 0 or score > 100:
    print("Score must be between 0 and 100.")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Score {score} earns a {grade}.")
```

The validation wraps the whole original grading chain in an else block—the same 'reject first, then work' shape as the chapter's own ticket-kiosk project.

## ch05-repetition#4

<!-- Print a right triangle of stars 6 rows tall using a nested loop. -->

```python
# Prints a right triangle of stars, 6 rows tall.

for row in range(1, 7):
    line = ""
    for star in range(row):
        line += "*"
    print(line)
```

The inner loop's length depends on the outer loop's current row, which is what makes it a nested loop rather than two separate ones.

## ch05-repetition#6

<!-- Write a guessing game: pick a secret number in the code, and keep asking until the user gets it, saying "too high" or "too low" each time. -->

```python
# A guessing game with a secret number hardcoded in the code.

secret = 42

guess = int(input("Guess a number: "))

while guess != secret:
    if guess < secret:
        print("Too low.")
    else:
        print("Too high.")
    guess = int(input("Guess a number: "))

print("You got it!")
```

The secret number is hardcoded, not randomized—random.randint() isn't introduced until this same chapter's project section, right after this exercise.

## ch07-lists#1

<!-- Make a list of ten numbers and print its total, average, largest, and smallest. -->

```python
numbers = [88, 92, 79, 95, 60, 73, 85, 91, 68, 77]
total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
```

Verified: runs correctly (Total 808, Average 80.8, Largest 95, Smallest 60), matches the exercise wording and the chapter's own 'Useful built-ins' example exactly. No change needed.

## ch07-lists#4

<!-- Given a list of numbers, build a new list containing only the even ones. -->

```python
numbers = [3, 8, 15, 22, 41, 56, 7, 10]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)
```

Verified: runs correctly ([8, 22, 56, 10]) and mirrors the chapter's filtering-loop pattern verbatim. No change needed.

## ch07-lists#5

<!-- Reverse a list without using `.reverse()` or `[::-1]`. -->

```python
original = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])

print(reversed_list)
```

range(len(original) - 1, -1, -1) walks the indexes backward from the last one to 0. Verified: correctly avoids both forbidden constructs and produces [5, 4, 3, 2, 1]. No change needed.

## ch07-lists#7

<!-- Build a 3-by-3 grid of zeros, set the center to 5, and print it row by row. -->

```python
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

grid[1][1] = 5

for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

Verified: prints the 3x3 grid with 5 at the center, matching the chapter's own nested-list/nested-loop example line for line. No change needed.

## ch08-strings-as-data#3

<!-- Ask for a full name and print the initials. -->

```python
full_name = input("Enter your full name: ")
words = full_name.split()

initials = ""
for word in words:
    initials += word[0].upper()

print(initials)
```

Verified: .split() with no argument (not .split(" ")) correctly collapses any extra whitespace between names, and word[0].upper() handles names typed in any case. Produces the right initials for 'Ada Lovelace' -> 'AL'. No change needed.

## ch08-strings-as-data#7

<!-- Given `"Ada,88\nGrace,92\nAlan,45"`, print each name with its score on its own line. -->

```python
data = "Ada,88\nGrace,92\nAlan,45"
lines = data.split("\n")

for line in lines:
    name, score = line.split(",")
    print(f"{name}: {score}")
```

Verified: prints each name/score pair on its own line, and the two-item unpacking (`name, score = line.split(",")`) is the exact pattern the chapter itself demonstrates with `row.split(",")`, so it isn't reaching ahead to tuples (ch10). No change needed.

## ch09-dictionaries-and-sets#1

<!-- Build a dictionary of five countries and their capitals, then let the user look one up. -->

```python
capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Egypt": "Cairo",
    "Brazil": "Brasilia",
    "Canada": "Ottawa",
}

country = input("Enter a country: ")

if country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")
else:
    print("I don't have that country.")
```

## ch09-dictionaries-and-sets#2

<!-- Count the letter frequencies in a word the user enters. -->

```python
word = input("Enter a word: ")

counts = {}
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1

for letter, count in counts.items():
    print(f"{letter}: {count}")
```

This is the counting pattern from the chapter — counts.get(letter, 0) + 1 handles a first sighting and a repeat with the same line.

## ch09-dictionaries-and-sets#3

<!-- Given two lists of names, print those in both, those in only the first, and the full set. -->

```python
list1 = ["Ada", "Grace", "Alan", "Katherine"]
list2 = ["Grace", "Alan", "Margaret"]

set1 = set(list1)
set2 = set(list2)

print("In both lists:", set1 & set2)
print("Only in the first list:", set1 - set2)
print("Everyone:", set1 | set2)
```

set(list) converts each list into a set, then &, -, and | do intersection, difference, and union directly, exactly as the chapter's band/chorus example does.

## ch09-dictionaries-and-sets#5

<!-- Store three students each with a name, grade level, and favorite subject, then print a formatted roster. -->

```python
students = {
    "Ada": {"grade_level": 9, "favorite_subject": "Math"},
    "Grace": {"grade_level": 10, "favorite_subject": "Science"},
    "Alan": {"grade_level": 9, "favorite_subject": "History"},
}

print(f"{'Name':<10}{'Grade':<8}Favorite Subject")
for name, info in students.items():
    print(f"{name:<10}{info['grade_level']:<8}{info['favorite_subject']}")
```

Each student's name is the outer key; its record is a nested dictionary, looked up the same way the chapter's students["Ada"]["score"] example does.

## ch09-dictionaries-and-sets#6

<!-- Given a list of words, print the ones that appear more than once. -->

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat", "fish"]

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    if count > 1:
        print(word)
```

Same counting pattern as exercise 2, then a plain if while looping over .items() picks out the repeats.

## ch09-dictionaries-and-sets#7

<!-- Find the most common character in a sentence, ignoring spaces. -->

```python
sentence = input("Enter a sentence: ")

counts = {}
for char in sentence:
    if char != " ":
        counts[char] = counts.get(char, 0) + 1

most_common = max(counts, key=counts.get)
print(f"The most common character is '{most_common}', appearing {counts[most_common]} times.")
```

max(counts, key=counts.get) finds the key with the highest value, the same trick the chapter uses to find the top scorer.

## ch10-tuples-and-structured-records#1

<!-- Store five cities as `(name, latitude, longitude)` tuples and print each formatted. -->

```python
cities = [
    ("Tokyo", 35.68, 139.69),
    ("Cairo", 30.04, 31.24),
    ("Lima", -12.05, -77.04),
    ("Oslo", 59.91, 10.75),
    ("Perth", -31.95, 115.86),
]

for name, latitude, longitude in cities:
    print(f"{name}: ({latitude:.2f}, {longitude:.2f})")
```

## ch10-tuples-and-structured-records#3

<!-- Build a list of book records with title, author, and year, then print them sorted by year. -->

```python
books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Project Hail Mary", "author": "Andy Weir", "year": 2021},
    {"title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]

by_year = sorted(books, key=lambda b: b["year"])
for book in by_year:
    print(f"{book['year']}: {book['title']} by {book['author']}")
```

## ch10-tuples-and-structured-records#4

<!-- From that list, print only books published after 2000. -->

```python
books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Project Hail Mary", "author": "Andy Weir", "year": 2021},
    {"title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]

recent = [b for b in books if b["year"] > 2000]
for book in recent:
    print(f"{book['title']} ({book['year']})")
```

## ch10-tuples-and-structured-records#5

<!-- Group the books by author into a dictionary. -->

```python
books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Project Hail Mary", "author": "Andy Weir", "year": 2021},
    {"title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]

by_author = {}
for book in books:
    author = book["author"]
    if author not in by_author:
        by_author[author] = []
    by_author[author].append(book["title"])

for author in sorted(by_author):
    print(f"{author}: {', '.join(by_author[author])}")
```

## ch10-tuples-and-structured-records#6

<!-- Write `oldest(books)` returning the record — not just the title — of the earliest book. -->

```python
books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Project Hail Mary", "author": "Andy Weir", "year": 2021},
    {"title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]


def oldest(books):
    """Return the record of the earliest published book."""
    earliest = books[0]
    for book in books:
        if book["year"] < earliest["year"]:
            earliest = book
    return earliest


result = oldest(books)
print(f"{result['title']} ({result['year']}) by {result['author']}")
```

## ch10-tuples-and-structured-records#7

<!-- Use a dictionary with tuple keys to store a 3-by-3 tic-tac-toe board and print it as a grid. -->

```python
board = {}
board[(0, 0)] = "X"
board[(1, 1)] = "O"
board[(0, 2)] = "X"
board[(2, 0)] = "O"

for row in range(3):
    cells = []
    for col in range(3):
        cells.append(board.get((row, col), "."))
    print(" ".join(cells))
```

## ch11-searching-and-sorting#2

<!-- Add a step counter to both searches and compare them on a list of 1,000 items. -->

```python
def linear_search_counted(items, target):
    """Return (index, count) for a linear search, counting comparisons."""
    count = 0
    for i in range(len(items)):
        count += 1
        if items[i] == target:
            return i, count
    return -1, count


def binary_search_counted(items, target):
    """Return (index, count) for a binary search, counting comparisons."""
    low = 0
    high = len(items) - 1
    count = 0

    while low <= high:
        count += 1
        middle = (low + high) // 2
        if items[middle] == target:
            return middle, count
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1, count


numbers = list(range(1000))
target = 999

linear_index, linear_count = linear_search_counted(numbers, target)
binary_index, binary_count = binary_search_counted(numbers, target)

print(f"Linear search: found at {linear_index} in {linear_count} steps")
print(f"Binary search: found at {binary_index} in {binary_count} steps")
```

Unchanged from the draft. It runs and matches the chapter's own linear_search_counted/binary_search_counted (the chapter project reuses this exact pattern), so it is already in voice.

## ch11-searching-and-sorting#4

<!-- Implement insertion sort: take each item and slide it back to its place. -->

```python
def insertion_sort(items):
    """Return a new sorted list, using insertion sort."""
    result = items.copy()

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current

    return result


print(insertion_sort([64, 25, 12, 22, 11]))
```

Unchanged from the draft. It runs correctly and mirrors selection_sort's own copy-then-sort-in-place shape.

## ch11-searching-and-sorting#5

<!-- Sort a list of student records by score, then by name, using sorted() with a key. -->

```python
students = [
    {"name": "Ada", "score": 88},
    {"name": "Grace", "score": 95},
    {"name": "Alan", "score": 88},
    {"name": "Katherine", "score": 99},
]


def score_then_name(record):
    """Return the sort key: score first, then name."""
    return record["score"], record["name"]


ranked = sorted(students, key=score_then_name)

for student in ranked:
    print(f"{student['name']:<10}{student['score']:>5}")
```

Unchanged from the draft; ran it and confirmed Ada/Alan (tied at 88) sort alphabetically before Grace/Katherine. Flagging one judgment call rather than a bug: the course never explicitly teaches that sorted() compares tuples item-by-item for tie-breaking (it only shows single-field keys), so this is a small, reasonable extension of taught material rather than something demonstrated verbatim — worth a human's sign-off, but not something to rewrite since no simpler in-vocabulary approach exists.

## ch11-searching-and-sorting#7

<!-- Find the two closest values in a list. First try every pair, then try sorting first — and compare the work each does. -->

```python
def closest_pair_brute(numbers):
    """Return the two closest values and the comparison count, checking every pair."""
    best_gap = None
    best_pair = None
    comparisons = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            comparisons += 1
            first = numbers[i]
            second = numbers[j]
            if first > second:
                gap = first - second
            else:
                gap = second - first
            if best_gap is None or gap < best_gap:
                best_gap = gap
                best_pair = (first, second)

    return best_pair, best_gap, comparisons


def closest_pair_sorted(numbers):
    """Return the two closest values and the comparison count, by sorting first."""
    ordered = sorted(numbers)
    best_gap = None
    best_pair = None
    comparisons = 0

    for i in range(len(ordered) - 1):
        comparisons += 1
        gap = ordered[i + 1] - ordered[i]
        if best_gap is None or gap < best_gap:
            best_gap = gap
            best_pair = (ordered[i], ordered[i + 1])

    return best_pair, best_gap, comparisons


values = [17, 4, 23, 8, 42, 15, 9, 41]

pair, gap, count = closest_pair_brute(values)
print(f"Brute force:  {pair}, gap {gap}, {count} comparisons")

pair, gap, count = closest_pair_sorted(values)
print(f"Sorted first: {pair}, gap {gap}, {count} comparisons")
```

FIXED: the draft called abs() to get the gap between an unsorted pair, but abs() is never introduced anywhere in this course (checked all of content/ch01 through ch12 and 99-appendices — round(), min(), max() are each explicitly taught, abs() never appears). Replaced it with a plain if/else that picks the larger-minus-smaller, which only uses comparisons and subtraction; re-ran it and the output is identical (8, 9), gap 1, 28 vs 7 comparisons. closest_pair_sorted never needed abs() since a sorted list's adjacent gap is already non-negative, so it is untouched.

## ch12-recursion-and-problem-solving#2

<!-- Write count_down_up(n) printing n to 1, then 1 back to n, using one recursive function. -->

```python
def count_down_up(n):
    """Print n down to 1, then back up to n, using one recursive function."""
    if n <= 0:
        return
    print(n)
    count_down_up(n - 1)
    print(n)


count_down_up(3)
```

Unchanged from the draft. Ran it: output is 3 2 1 1 2 3, which is exactly n-down-to-1 then 1-back-up-to-n.

## ch12-recursion-and-problem-solving#7

<!-- Solve the Towers of Hanoi for 3 disks, printing each move. -->

```python
def hanoi(n, source, target, auxiliary):
    """Print the moves to solve Towers of Hanoi with n disks."""
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)


hanoi(3, "A", "C", "B")
```

Unchanged from the draft. Ran it: prints exactly 7 moves (2^3 - 1), all legal, ending with everything moved from A to C.

