# A student records system: add, search, sort, and report.

students = [
    {"id": 1004, "name": "Ada Lovelace", "grade": 9, "scores": [88, 92, 85]},
    {"id": 1001, "name": "Grace Hopper", "grade": 10, "scores": [95, 91, 98]},
    {"id": 1007, "name": "Alan Turing", "grade": 9, "scores": [45, 62, 58]},
    {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]},
    {"id": 1009, "name": "Edsger Dijkstra", "grade": 10, "scores": [71, 68, 75]},
]


def average(numbers):
    """Return the mean of a list of numbers, or 0.0 if empty."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def letter_grade(score):
    """Return the letter grade for a numeric average."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def find_by_id(records, student_id):
    """Binary search a list sorted by id. Returns the record or None."""
    low = 0
    high = len(records) - 1

    while low <= high:
        middle = (low + high) // 2
        if records[middle]["id"] == student_id:
            return records[middle]
        elif records[middle]["id"] < student_id:
            low = middle + 1
        else:
            high = middle - 1

    return None


def search_by_name(records, text):
    """Return every record whose name contains the text, ignoring case."""
    return [r for r in records if text.lower() in r["name"].lower()]


def group_by_grade(records):
    """Return a dictionary mapping each grade level to its records."""
    groups = {}
    for record in records:
        groups.setdefault(record["grade"], []).append(record)
    return groups


def print_roster(records):
    """Print all records, ranked by average, highest first."""
    ranked = sorted(records, key=lambda r: average(r["scores"]), reverse=True)

    print(f"{'Rank':<6}{'ID':<7}{'Name':<20}{'Gr':<4}{'Avg':>7}{'Grade':>7}")
    print("-" * 51)
    for position, record in enumerate(ranked, start=1):
        mean = average(record["scores"])
        print(
            f"{position:<6}{record['id']:<7}{record['name']:<20}"
            f"{record['grade']:<4}{mean:>7.1f}{letter_grade(mean):>7}"
        )
    print("-" * 51)


def print_grade_summary(records):
    """Print a per-grade-level summary."""
    print("\nBy grade level")
    groups = group_by_grade(records)
    for grade in sorted(groups):
        members = groups[grade]
        means = [average(r["scores"]) for r in members]
        print(f"  Grade {grade}: {len(members)} students, average {average(means):.1f}")


def print_class_stats(records):
    """Print statistics for the whole class."""
    means = [average(r["scores"]) for r in records]
    passing = [m for m in means if m >= 60]
    best = max(records, key=lambda r: average(r["scores"]))

    print("\nClass statistics")
    print(f"  Students:      {len(records)}")
    print(f"  Class average: {average(means):.1f}")
    print(f"  Top student:   {best['name']} ({average(best['scores']):.1f})")
    print(f"  Passing:       {len(passing)} of {len(records)}")


print_roster(students)
print_grade_summary(students)
print_class_stats(students)

by_id = sorted(students, key=lambda r: r["id"])
found = find_by_id(by_id, 1007)
print(f"\nLookup 1007:   {found['name'] if found else 'not found'}")
print(f"Lookup 9999:   {find_by_id(by_id, 9999)}")

matches = search_by_name(students, "a")
print(f"Names with 'a': {len(matches)}")
