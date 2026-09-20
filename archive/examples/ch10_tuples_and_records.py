"""Chapter 10 - Tuples and Structured Records

Every worked example from the chapter.
"""

# --- Tuples ----------------------------------------------------------------

point = (3, 4)
color = (255, 128, 0)

print(point[0])
print(len(color))

for value in color:
    print(value)

# point[0] = 5 would raise TypeError. Uncomment to see it.
# point[0] = 5

# --- A tuple can be a dictionary key ---------------------------------------

# Storing values on a grid, keyed by coordinate
board = {}
board[(0, 0)] = "X"
board[(1, 1)] = "O"
board[(2, 2)] = "X"

print(board[(1, 1)])
print((0, 0) in board)
print((0, 1) in board)

# --- Unpacking -------------------------------------------------------------

point = (3, 4)
x, y = point
print(f"x is {x}, y is {y}")

# Swapping two variables, in one line
a = 1
b = 2
a, b = b, a
print(a, b)


def min_max(numbers):
    """Return the smallest and largest values in a list."""
    return min(numbers), max(numbers)


result = min_max([5, 2, 9, 1])
print(result)
print(type(result))

lowest, highest = min_max([5, 2, 9, 1])
print(f"from {lowest} to {highest}")

# --- Records: lists of dictionaries ----------------------------------------

students = [
    {"name": "Ada", "grade": 9, "score": 88},
    {"name": "Grace", "grade": 10, "score": 92},
    {"name": "Alan", "grade": 9, "score": 45},
    {"name": "Katherine", "grade": 11, "score": 95},
]

for student in students:
    print(f"{student['name']}: {student['score']}")

# Filtering
ninth_graders = [s for s in students if s["grade"] == 9]
for s in ninth_graders:
    print(s["name"])

# Extracting one field
all_scores = [s["score"] for s in students]
print(all_scores)
print(sum(all_scores) / len(all_scores))

# Sorting by a field
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
for s in by_score:
    print(f"{s['name']:<12}{s['score']}")


# Finding one record
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

# Grouping into a dictionary
by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

for grade in sorted(by_grade):
    print(f"Grade {grade}: {', '.join(by_grade[grade])}")
