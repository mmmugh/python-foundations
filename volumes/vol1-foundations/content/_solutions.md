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

## ch01-your-first-programs-practice#1

```python
print("======================================")
print("         RIVERSIDE FILM CLUB")
print("======================================")
```

The rule is typed out in full. String repetition would be shorter, but that is Chapter 3.

## ch01-your-first-programs-practice#2

```python
print("Feature:  The Quiet Harbour  (1998)")
```

One string, spaces and all, exactly as it should appear.

## ch01-your-first-programs-practice#3

```python
print("Feature:", "The Quiet Harbour  (1998)")
```

print() puts exactly one space between arguments, so the two spaces after Feature: become one. When the spacing matters, put it inside the string.

## ch01-your-first-programs-practice#4

```python
print("When:     Friday, 7:30 pm")
print("Where:    Room 14")
```

Two calls, and the values line up because the spaces are inside the strings.

## ch01-your-first-programs-practice#5

```python
print("Seats available:", 8 * 12)
```

8 * 12 rather than 96: change the row count and the flyer stays right.

## ch01-your-first-programs-practice#6

```python
print("Snack bar total:", 3 * 3.75 + 2 * 3.00)
```

The arithmetic happens before print() sees it. Note that print() adds the space after the colon.

## ch01-your-first-programs-practice#7

```python
# Prints the flyer for Friday's Riverside Film Club showing.

print("======================================")
print("         RIVERSIDE FILM CLUB")
print("======================================")
print()
print("Feature:  The Quiet Harbour  (1998)")
print("When:     Friday, 7:30 pm")
print("Where:    Room 14")
print()
print("Seats available:", 8 * 12)
print("Snack bar total:", 3 * 3.75 + 2 * 3.00)
print()
print("======================================")
```

The comment says what the program is for, not what each line does. Blank lines come from print() with nothing in it.

## ch04-making-decisions-practice#1

```python
wind = float(input("Wind speed in mph? "))
print(f"Wind: {wind:.1f} mph")
```

float() rather than int(), because a wind speed has a decimal point. The .1f keeps the display steady even when the reading is a whole number.

## ch04-making-decisions-practice#2

```python
wind = float(input("Wind speed in mph? "))
if wind < 30:
    print("Wind: OK")
else:
    print("Wind: TOO STRONG")
```

Under 30 means <, not <=. At exactly 30 the club stays on the ground.

## ch04-making-decisions-practice#3

```python
temperature = float(input("Temperature in C? "))
if temperature >= 2 and temperature <= 35:
    print("Temperature: OK")
else:
    print("Temperature: OUT OF RANGE")
```

Two comparisons joined with and. Both ends count as safe, so both are >= and <=.

## ch04-making-decisions-practice#4

```python
ceiling = float(input("Cloud ceiling in feet? "))
if ceiling >= 5000:
    print("Ceiling: CLEAR")
elif ceiling >= 2000:
    print("Ceiling: MARGINAL")
else:
    print("Ceiling: TOO LOW")
```

The narrow band goes first. With 2000 tested before 5000, a clear sky reads as marginal and the CLEAR branch never runs.

## ch04-making-decisions-practice#5

```python
typed = input("Fuel percentage? ")
if typed.isdigit():
    fuel = int(typed)
    print(f"Fuel: {fuel}%")
else:
    print("Fuel: NOT A NUMBER")
```

Check first, convert second: int() on 'full' would stop the program before it could print anything.

## ch04-making-decisions-practice#6

```python
wind = float(input("Wind speed in mph? "))
temperature = float(input("Temperature in C? "))
ceiling = float(input("Cloud ceiling in feet? "))
typed = input("Fuel percentage? ")
wind_ok = wind < 30
temperature_ok = temperature >= 2 and temperature <= 35
ceiling_ok = ceiling >= 2000
fuel_ok = typed.isdigit() and int(typed) >= 95
if wind_ok and temperature_ok and ceiling_ok and fuel_ok:
    print("LAUNCH: GO")
else:
    print("LAUNCH: NO GO")
```

Naming each condition keeps the verdict line readable, and the names are reused in the next step.

## ch04-making-decisions-practice#7

```python
wind = float(input("Wind speed in mph? "))
temperature = float(input("Temperature in C? "))
ceiling = float(input("Cloud ceiling in feet? "))
typed = input("Fuel percentage? ")
wind_ok = wind < 30
temperature_ok = temperature >= 2 and temperature <= 35
ceiling_ok = ceiling >= 2000
fuel_ok = typed.isdigit() and int(typed) >= 95
if wind_ok and temperature_ok and ceiling_ok and fuel_ok:
    print("LAUNCH: GO")
else:
    print("LAUNCH: NO GO")
    if not wind_ok:
        print("HOLD: wind")
    elif not temperature_ok:
        print("HOLD: temperature")
    elif not ceiling_ok:
        print("HOLD: ceiling")
    else:
        print("HOLD: fuel")
```

elif rather than four ifs, so only the first failure is reported. Fuel is the else because it is the only one left.

## ch04-making-decisions-practice#8

```python
wind = float(input("Wind speed in mph? "))
temperature = float(input("Temperature in C? "))
ceiling = float(input("Cloud ceiling in feet? "))
typed = input("Fuel percentage? ")
wind_ok = wind < 30
temperature_ok = temperature >= 2 and temperature <= 35
ceiling_ok = ceiling >= 2000
fuel_ok = typed.isdigit() and int(typed) >= 95
if wind_ok:
    print("Wind: OK")
else:
    print("Wind: TOO STRONG")
if temperature_ok:
    print("Temperature: OK")
else:
    print("Temperature: OUT OF RANGE")
if ceiling >= 5000:
    print("Ceiling: CLEAR")
elif ceiling >= 2000:
    print("Ceiling: MARGINAL")
else:
    print("Ceiling: TOO LOW")
if typed.isdigit():
    print(f"Fuel: {int(typed)}%")
else:
    print("Fuel: NOT A NUMBER")
if wind_ok and temperature_ok and ceiling_ok and fuel_ok:
    print("LAUNCH: GO")
else:
    print("LAUNCH: NO GO")
    if not wind_ok:
        print("HOLD: wind")
    elif not temperature_ok:
        print("HOLD: temperature")
    elif not ceiling_ok:
        print("HOLD: ceiling")
    else:
        print("HOLD: fuel")
```

Nothing new, only assembly: the status lines from steps 2 to 5, then the verdict, then the reason.

## ch02-variables-and-types-practice#1

```python
trail = "Kettle Ridge"
distance_km = 12.4
print(trail, "is", distance_km, "km")
```

print() puts a space between each piece, so the commas do the spacing and no spaces are typed inside the strings.

## ch02-variables-and-types-practice#2

```python
distance_km = 12.4
pace = float(input("Pace in minutes per km? "))
minutes = distance_km * pace
print("That takes", minutes, "minutes")
```

float() and not int(), because a pace can be 10.5. Without the conversion Python is asked to multiply a number by a piece of text, and says so.

## ch02-variables-and-types-practice#3

```python
distance_km = 12.4
pace = float(input("Pace in minutes per km? "))
minutes = distance_km * pace
hours = minutes / 60
print("That takes", minutes, "minutes, which is", hours, "hours")
```

Sixty minutes in an hour. The answer is a long decimal for now; Chapter 3 has round().

## ch02-variables-and-types-practice#4

```python
distance_km = 12.4
pace = float(input("Pace in minutes per km? "))
minutes = distance_km * pace
hours = minutes / 60
water = hours * 0.75
print("Water per person:", water, "liters")
```

Per hour, so it multiplies the hours. Multiplying the minutes asks for 102 liters, which is a clue that the units were wrong.

## ch02-variables-and-types-practice#5

```python
distance_km = 12.4
pace = float(input("Pace in minutes per km? "))
minutes = distance_km * pace
hours = minutes / 60
water = hours * 0.75
people = int(input("How many people? "))
print("Water for the group:", water * people, "liters")
```

int() for a head count, since half a walker does not turn up.

## ch02-variables-and-types-practice#6

```python
people = int(input("How many people? "))
print("Permits:", 4.50 * people)
```

Without int(), 4.50 * '4' is not a price. Python refuses to multiply a decimal by text.

## ch02-variables-and-types-practice#7

```python
distance_km = float(input("Trail length in km? "))
pace = float(input("Pace in minutes per km? "))
people = int(input("How many people? "))

minutes = distance_km * pace
hours = minutes / 60
water = hours * 0.75

print("Length:", distance_km, "km")
print("Time:", minutes, "minutes")
print("Time:", hours, "hours")
print("Water each:", water, "liters")
print("Water total:", water * people, "liters")
print("Permits:", 4.50 * people)
```

Every printed number comes from the three that were typed in. Change the trail length and the whole plan follows.

## ch03-expressions-and-operators-practice#1

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
print(f"You need {slices} slices")
```

Both inputs need int(). Without it, '5' * 3 is the text 555, which is a lot of pizza.

## ch03-expressions-and-operators-practice#2

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
pizzas = (slices + 7) // 8
print(f"Order {pizzas} pizzas")
```

Plain // rounds down, which orders one pizza for fifteen slices and leaves someone hungry. The +7 rounds up without needing an if.

## ch03-expressions-and-operators-practice#3

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
pizzas = (slices + 7) // 8
print(f"{pizzas * 8 - slices} slices left over")
```

What is left is what was ordered minus what is eaten. slices % 8 answers a different question and happens to agree sometimes, which is worse than always being wrong.

## ch03-expressions-and-operators-practice#4

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
pizzas = (slices + 7) // 8
cost = pizzas * 13.50
print(f"That comes to {cost:.2f}")
```

:.2f shows money properly, so 27.0 prints as 27.00.

## ch03-expressions-and-operators-practice#5

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
pizzas = (slices + 7) // 8
cost = pizzas * 13.50
print(f"Each of you owes {round(cost / people, 2):.2f}")
```

Split between people, not between slices. Both are numbers in scope, which is exactly how that mistake happens.

## ch03-expressions-and-operators-practice#6

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
print(f"Would one pizza have done? {slices <= 8}")
```

A comparison is a value in its own right and can be printed. Chapter 4 puts the same expression inside an if.

## ch03-expressions-and-operators-practice#7

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
pizzas = (slices + 7) // 8
cost = pizzas * 13.50
delivered = cost * 1.15
print(f"With delivery: {delivered:.2f}")
print(f"Each: {delivered / people:.2f}")
```

Multiplying by 1.15 adds the 15% and keeps the original. Multiplying by 0.15 throws the pizza away and bills for the delivery.

## ch03-expressions-and-operators-practice#8

```python
people = int(input("How many people? "))
each = int(input("Slices each? "))
slices = people * each
pizzas = (slices + 7) // 8
cost = pizzas * 13.50
delivered = cost * 1.15

print(f"Slices needed:  {slices}")
print(f"Pizzas to order: {pizzas}")
print(f"Slices left:    {pizzas * 8 - slices}")
print(f"Cost:           {cost:.2f}")
print(f"With delivery:  {delivered:.2f}")
print(f"Each of you:    {delivered / people:.2f}")
```

Nothing new, only arrangement. The f-strings line the numbers up in a column by padding the labels.

## ch05-repetition-practice#1

```python
for week in range(1, 9):
    print("Week", week)
```

range(1, 9) starts at 1 and stops before 9. range(8) would start at 0 and label the first week zero.

## ch05-repetition-practice#2

```python
weekly = float(input("Saving how much a week? "))
total = 0
for week in range(1, 9):
    total += weekly
    print(f"Week {week}: {total}")
```

total starts at 0 outside the loop and survives each turn. Declared inside, it would reset every week.

## ch05-repetition-practice#3

```python
weekly = float(input("Saving how much a week? "))
total = 0
weeks = 0
while total < 240:
    total += weekly
    weeks += 1
print("Weeks needed:", weeks)
```

while total < 240 stops the moment the goal is met. Using <= keeps going for one more week after it is already reached.

## ch05-repetition-practice#4

```python
weekly = float(input("Saving how much a week? "))
total = 0
week = 0
for week in range(1, 53):
    total += weekly
    if total >= 240:
        break

if total >= 240:
    print("Reached in week", week)
else:
    print("Not this year")
```

The break leaves week holding the week it stopped on, and the report happens once, afterwards. Without it the loop runs all 52 weeks and reports week 52.

## ch05-repetition-practice#5

```python
weekly = float(input("Saving how much a week? "))
total = 0
for week in range(1, 200):
    if week % 5 == 0:
        continue
    total += weekly
    if total >= 240:
        print("Reached in week", week)
        break
```

continue skips the rest of this turn and moves to the next week. break would end the loop entirely, which here means giving up in week 5.

## ch05-repetition-practice#6

```python
weekly = float(input("Saving how much a week? "))
total = 0
for week in range(1, 200):
    total += weekly
    if week % 4 == 0:
        total += 10
    if total >= 240:
        print("Reached in week", week)
        break
```

week % 4 == 0 is every fourth week: 4, 8, 12. Comparing to 1 picks weeks 1, 5 and 9 instead, which pays the bonus a week early and forever after.

## ch05-repetition-practice#7

```python
weekly = float(input("Saving how much a week? "))
total = 0
for week in range(1, 200):
    total += weekly
    total = total * 1.01
    if total >= 240:
        print("Reached in week", week)
        break
```

The deposit goes in first, then the interest is worked out on the new balance. Doing it the other way round pays nothing on the money just paid in.

## ch05-repetition-practice#8

```python
weekly = float(input("Saving how much a week? "))
total = 0
for week in range(1, 9):
    total += weekly
    print(f"Week {week}: {total}")

total = 0
for week in range(1, 200):
    if week % 5 == 0:
        continue
    total += weekly
    if week % 4 == 0:
        total += 10
    if total >= 240:
        print("Goal reached in week", week)
        break
```

The bonus and the skipped weeks pull in opposite directions, and together they land on week 17 rather than either answer on its own.

## ch06-functions-practice#1

```python
def c_to_f(celsius):
    return round(celsius * 9 / 5 + 32, 1)
```

Multiply first, then add 32. Adding first is the classic way to get this wrong, and it even looks right at a glance.

## ch06-functions-practice#2

```python
def f_to_c(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 1)
```

Going back the other way means subtracting first and turning the fraction upside down. -40 is the temperature where the two scales meet.

## ch06-functions-practice#3

```python
def km_to_miles(km):
    return round(km * 0.621371, 2)
```

A mile is longer than a kilometre, so the number gets smaller. Dividing gives 1.61, which is the answer to the opposite question.

## ch06-functions-practice#4

```python
def cups_to_ml(cups):
    return round(cups * 236.588, 1)
```

A cup is not 250 ml, however tempting the round number is. The error is small per cup and ruins bread at three.

## ch06-functions-practice#5

```python
def c_to_f(celsius):
    return round(celsius * 9 / 5 + 32, 1)


def oven_setting(celsius):
    return round(c_to_f(celsius) / 25) * 25
```

Dividing by 25, rounding, then multiplying back is how you snap a number to a step of any size. Calling c_to_f() means the conversion lives in one place.

## ch06-functions-practice#6

```python
def minutes_to_h_m(total):
    return total // 60, total % 60

print(minutes_to_h_m(90))
print(minutes_to_h_m(45))
print(minutes_to_h_m(125))
```

A return with a comma in it hands back a tuple, and printing one shows the brackets. Hours come from // and minutes from %, and swapping them is silent until the numbers happen to differ.

## ch06-functions-practice#7

```python
def scale_recipe(amount, factor):
    return round(amount * factor, 2)
```

Two parameters, in the order the name suggests. Scaling by 1 should give the amount back, which is a quick way to check you have not mixed them up.

## ch06-functions-practice#8

```python
def c_to_f(celsius):
    return round(celsius * 9 / 5 + 32, 1)
def km_to_miles(km):
    return round(km * 0.621371, 2)
def cups_to_ml(cups):
    return round(cups * 236.588, 1)

print("180 C is", c_to_f(180), "F")
print("5 km is", km_to_miles(5), "miles")
print("2 cups is", cups_to_ml(2), "ml")
```

Three functions defined once and called once each. The program reads as the table it prints, which is the whole point of giving the arithmetic a name.

## ch07-lists-practice#1

```python
def total_seconds(seconds):
    return sum(seconds)
```

sum() over a list of numbers. The empty case falls out for free, which a hand-written loop only manages if the total starts at 0.

## ch07-lists-practice#2

```python
def average_seconds(seconds):
    return round(sum(seconds) / len(seconds), 1)
```

Divide by len(), not by the number of songs you happen to be testing with.

## ch07-lists-practice#3

```python
def longest_title(titles):
    best = titles[0]
    for title in titles:
        if len(title) > len(best):
            best = title
    return best
```

Comparing titles with > compares them alphabetically, which answers a different question and gets 'Ribbons' most of the time by luck.

## ch07-lists-practice#4

```python
def playlist_with(titles, title):
    new = titles.copy()
    new.append(title)
    return new
```

copy() first, so the caller's playlist is left alone. titles + [title] builds a new list too and says the same thing more briefly.

## ch07-lists-practice#5

```python
def first_three(titles):
    return titles[:3]
```

A slice that runs off the end simply stops, which is why the short playlist does not raise. Indexing three times does raise.

## ch07-lists-practice#6

```python
def has_song(titles, title):
    return title in titles
```

in asks whether the list contains it. == asks whether the title IS the list, which is never true.

## ch07-lists-practice#7

```python
def positions(titles, title):
    return [i for i, t in enumerate(titles) if t == title]
```

enumerate() hands you the index and the item together. index() finds only the first, and raises when there is none.

## ch07-lists-practice#8

```python
def by_length(titles, seconds):
    pairs = []
    for i in range(len(titles)):
        pairs.append([seconds[i], titles[i]])
    pairs.sort()
    return [pair[1] for pair in pairs]
```

Putting the length first makes the pair sort by length. Sorting the titles themselves sorts them alphabetically, which is a different playlist entirely.

## ch08-strings-as-data-practice#1

```python
def level_of(line):
    return line.split("|")[0]
```

Splitting on the separator the format actually uses. Splitting on a space happens to work here and breaks the moment a level is followed by anything else.

## ch08-strings-as-data-practice#2

```python
def time_of(line):
    return line.split("|")[1]
```

Index 1 is the second field. Counting from 0 is the whole of this mistake.

## ch08-strings-as-data-practice#3

```python
def message_of(line):
    return line.split("|")[2]
```

The message is the last field, so [2] and [-1] both find it.

## ch08-strings-as-data-practice#4

```python
def is_warning(line):
    return line.split("|")[0].upper() == "WARN"
```

Put both sides in the same case before comparing. Without that, half the services are never warned about.

## ch08-strings-as-data-practice#5

```python
def tidy(line):
    level, time, message = line.split("|")
    return "|".join([level.upper(), time, message.strip()])
```

join() is the opposite of split(): it puts the separator back between the pieces. A line that was already tidy must come back unchanged.

## ch08-strings-as-data-practice#6

```python
def words_in(message):
    return [word for word in message.split() if word.isalpha()]
```

split() with no argument splits on any run of whitespace. isalpha() is False for '91', which is how the number drops out.

## ch08-strings-as-data-practice#7

```python
def redact(line, word):
    return line.replace(word, "****")
```

replace() changes every appearance, not just the first, and leaves the line alone when the word is not there.

## ch08-strings-as-data-practice#8

```python
def warning_messages(lines):
    out = []
    for line in lines:
        if line.split("|")[0].upper() == "WARN":
            out.append(line.split("|")[2].strip())
    return out
```

The messages, not the lines. The lowercase line has to be caught and its message tidied, which is why the earlier steps were worth writing separately.

## ch09-dictionaries-and-sets-practice#1

```python
def count_of(register, item):
    return register.get(item, 0)
```

get() with a second argument answers for something that was never handed in. Square brackets raise a KeyError instead.

## ch09-dictionaries-and-sets-practice#2

```python
def total_items(register):
    return sum(register.values())
```

values() is the counts. len() is how many kinds of thing are held, which is a different number and looks plausible until someone hands in a second umbrella.

## ch09-dictionaries-and-sets-practice#3

```python
def add_item(register, item):
    new = register.copy()
    new[item] = new.get(item, 0) + 1
    return new
```

get(item, 0) + 1 covers both cases at once: a new item starts from 0, an existing one carries on. Setting it to 1 loses the two umbrellas already there.

## ch09-dictionaries-and-sets-practice#4

```python
def remove_item(register, item):
    new = register.copy()
    if item not in new:
        return new
    new[item] = new[item] - 1
    if new[item] == 0:
        del new[item]
    return new
```

One fewer, and the entry disappears only when it reaches zero. Deleting outright hands back all three umbrellas to someone who claimed one.

## ch09-dictionaries-and-sets-practice#5

```python
def sorted_items(register):
    return sorted(register)
```

Looping over a dictionary, or sorting one, works on its keys. values() would sort the counts and lose the names.

## ch09-dictionaries-and-sets-practice#6

```python
def busiest(register):
    return max(register, key=lambda item: register[item])
```

Without a key, max() compares the names themselves and returns the last one alphabetically. The zebra case is there to catch exactly that.

## ch09-dictionaries-and-sets-practice#7

```python
def in_both(left, right):
    return sorted(set(left) & set(right))
```

& is what both have in common, | is everything either has. The repeated 'a' collapses because a set holds one of each.

## ch09-dictionaries-and-sets-practice#8

```python
def register_from(found):
    register = {}
    for item in found:
        register[item] = register.get(item, 0) + 1
    return register
```

The same get(item, 0) + 1 as step 3, now in a loop. This is the counting pattern, and it turns up everywhere once you have seen it.

## ch10-tuples-and-structured-records-practice#1

```python
def route_of(service):
    route, departs, destination = service
    return route
```

Unpacking names the fields once, at the top, so the rest of the function reads in words rather than in numbers.

## ch10-tuples-and-structured-records-practice#2

```python
def clock(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"
```

02d pads to two digits with a zero. Without it, five past ten prints as 10:5 and the timetable stops lining up.

## ch10-tuples-and-structured-records-practice#3

```python
def destinations(services):
    return sorted(set(service[2] for service in services))
```

Two services run to the Harbour, so without the set it appears twice.

## ch10-tuples-and-structured-records-practice#4

```python
def by_time(services):
    return sorted(services, key=lambda service: service[1])

def next_after(services, minute):
    for service in by_time(services):
        if service[1] > minute:
            return service
    return None
```

Strictly after, so the bus leaving at exactly that minute is the one you just missed. Sorting first means the first match found is the earliest.

## ch10-tuples-and-structured-records-practice#5

```python
def by_time(services):
    return sorted(services, key=lambda service: service[1])
```

The key says which part to sort on. Without it, sorted() compares whole records and starts with the route, so route 12 comes before route 9 as text.

## ch10-tuples-and-structured-records-practice#6

```python
def count_by_route(services):
    counts = {}
    for service in services:
        counts.setdefault(service[0], 0)
        counts[service[0]] += 1
    return counts
```

setdefault() puts a 0 there only if nothing is there yet, so the line after it can always add. Route 47 runs twice, which is what catches the version that assigns 1.

## ch10-tuples-and-structured-records-practice#7

```python
def label(minute):
    return "peak" if 420 <= minute < 560 or 960 <= minute < 1140 else "off-peak"
```

Up to but not including, so 560 is already off-peak. The cases sit on both boundaries because that is the only place this can be wrong.

## ch10-tuples-and-structured-records-practice#8

```python
def clock(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"
def by_time(services):
    return sorted(services, key=lambda service: service[1])

def timetable_lines(services):
    lines = []
    for route, departs, destination in by_time(services):
        lines.append(f"{route} {clock(departs)} {destination}")
    return lines
```

Two functions you already wrote, used rather than repeated. The test passes the services out of order on purpose.

## ch11-searching-and-sorting-practice#1

```python
def fastest_name(results):
    best = results[0]
    for result in results:
        if result[1] < best[1]:
            best = result
    return best[0]
```

Fastest is the smallest time, so the comparison is <. Everything about a race says 'best' and means 'least'.

## ch11-searching-and-sorting-practice#2

```python
def ranked(results):
    return sorted(results, key=lambda result: result[1])
```

The key picks the time out of each record. Without it sorted() compares the names, and the leaderboard comes out alphabetical.

## ch11-searching-and-sorting-practice#3

```python
def ranked(results):
    return sorted(results, key=lambda result: result[1])

def place_of(results, name):
    for place, result in enumerate(ranked(results), 1):
        if result[0] == name:
            return place
    return None
```

enumerate() takes a starting number, which saves adding 1 in two places and forgetting it in one. Nobody finishes in place 0.

## ch11-searching-and-sorting-practice#4

```python
def result_for(results, name):
    for result in results:
        if result[0] == name:
            return result
    return None
```

The whole record, not the name that was passed in. A binary search is no use here: the list is not sorted by name.

## ch11-searching-and-sorting-practice#5

```python
def insertion_point(times, target):
    low = 0
    high = len(times)
    while low < high:
        middle = (low + high) // 2
        if times[middle] < target:
            low = middle + 1
        else:
            high = middle
    return low
```

< rather than <= is what puts an equal time before the one already there. The two versions differ only on that case, which is why it is tested.

## ch11-searching-and-sorting-practice#6

```python
def ranked(results):
    return sorted(results, key=lambda result: result[1])

def podium(results):
    return [r[0] for r in ranked(results)[:3]]
```

A slice stops politely at the end of a short list. Indexing 0, 1 and 2 raises when only two people ran.

## ch11-searching-and-sorting-practice#7

```python
def sort_times(times):
    out = times.copy()
    for i in range(1, len(out)):
        current = out[i]
        j = i - 1
        while j >= 0 and out[j] > current:
            out[j + 1] = out[j]
            j -= 1
        out[j + 1] = current
    return out
```

After the while loop stops, j has gone one too far, so the value belongs at j + 1. Putting it at j is the classic off-by-one here, and it leaves the list almost sorted, which is the hardest kind of wrong to spot.

## ch11-searching-and-sorting-practice#8

```python
def ranked(results):
    return sorted(results, key=lambda result: result[1])

def leaderboard_lines(results):
    lines = []
    for place, result in enumerate(ranked(results), 1):
        lines.append(f"{place}. {result[0]} {result[1]}")
    return lines
```

Rank first, then number. Numbering the clipboard order gives everyone a place and gets all of them wrong.

## ch12-recursion-and-problem-solving-practice#1

```python
def total_size(folder):
    size = sum(folder["files"])
    for inner in folder["folders"]:
        size += total_size(inner)
    return size
```

Its own files, plus whatever each folder inside reports. No base case is written out: a folder with no folders inside simply never enters the loop.

## ch12-recursion-and-problem-solving-practice#2

```python
def file_count(folder):
    count = len(folder["files"])
    for inner in folder["folders"]:
        count += file_count(inner)
    return count
```

The same shape as step 1 with len() in place of sum(). Most recursive functions over a tree look like this.

## ch12-recursion-and-problem-solving-practice#3

```python
def depth(folder):
    deepest = 0
    for inner in folder["folders"]:
        if depth(inner) > deepest:
            deepest = depth(inner)
    return 1 + deepest
```

One for this folder, plus the deepest of what is inside — not how many are inside. On this tree those two happen to agree everywhere, so the wide case and the deep chain are there to pull them apart.

## ch12-recursion-and-problem-solving-practice#4

```python
def folder_names(folder):
    names = [folder["name"]]
    for inner in folder["folders"]:
        names += folder_names(inner)
    return names
```

This folder first, then each subtree in full. The version that lists only the folders one level down misses raw entirely.

## ch12-recursion-and-problem-solving-practice#5

```python
def largest_file(folder):
    biggest = None
    for size in folder["files"]:
        if biggest is None or size > biggest:
            biggest = size
    for inner in folder["folders"]:
        inner_biggest = largest_file(inner)
        if inner_biggest is None:
            continue
        if biggest is None or inner_biggest > biggest:
            biggest = inner_biggest
    return biggest
```

None is not zero: an empty folder has no biggest file, and a real file of size 0 would be a different answer. That is why the comparisons check for None rather than starting from 0.

## ch12-recursion-and-problem-solving-practice#6

```python
def find_folder(folder, name):
    if folder["name"] == name:
        return folder
    for inner in folder["folders"]:
        found = find_folder(inner, name)
        if found:
            return found
    return None
```

A folder that was found is a dictionary, which is truthy, and None is not, so a plain if separates them. Stop as soon as something is found, and keep looking otherwise. Checking only the children finds docs and images but never raw, which is two levels down.

## ch12-recursion-and-problem-solving-practice#7

```python
def all_sizes(folder):
    sizes = list(folder["files"])
    for inner in folder["folders"]:
        sizes += all_sizes(inner)
    return sizes
```

list() takes a copy, so adding to it does not grow the folder's own list. Returning folder['files'] hands back the real list, and the caller can then change the tree by accident.

## ch12-recursion-and-problem-solving-practice#8

```python
def total_size(folder):
    size = sum(folder["files"])
    for inner in folder["folders"]:
        size += total_size(inner)
    return size

def size_report(folder):
    lines = [f"{folder['name']}: {total_size(folder)}"]
    for inner in folder["folders"]:
        lines += size_report(inner)
    return lines
```

Two recursions working together: size_report walks the tree, and total_size walks each subtree again to add it up. Slow on a big tree, and perfectly clear on this one.
