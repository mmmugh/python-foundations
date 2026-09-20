# Computes a student's average and letter grade from scores entered one at a time.


def get_score(prompt):
    """Ask repeatedly until the user enters a number from 0 to 100, and return it."""
    while True:
        answer = input(prompt)
        if answer.isdigit() and 0 <= int(answer) <= 100:
            return int(answer)
        print("Please enter a whole number from 0 to 100.")


def letter_grade(average):
    """Return the letter grade for a numeric average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def print_report(name, average, grade):
    """Display a formatted grade report."""
    print()
    print("=" * 32)
    print(f"Student: {name}")
    print(f"Average: {average:.1f}")
    print(f"Grade:   {grade}")
    print("=" * 32)


def main():
    """Run the grade calculator."""
    name = input("Student name: ")

    total = 0
    count = 4
    for i in range(count):
        total += get_score(f"Score {i + 1} of {count}: ")

    average = total / count
    print_report(name, average, letter_grade(average))


main()
