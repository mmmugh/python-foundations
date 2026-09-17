"""Python Foundations - a runner for the book's code.

Replit runs this file when you press Run. Pick a chapter from the menu and it
will run that chapter's examples or project.

You can also run any file directly. In the Replit Shell:

    python3 examples/ch07_lists.py
    python3 projects/ch05_guessing_game.py
"""

import subprocess
import sys

EXAMPLES = {
    "1": ("Chapter 1  - Your First Programs", "examples/ch01_first_programs.py"),
    "2": ("Chapter 2  - Variables and Types", "examples/ch02_variables_and_types.py"),
    "3": ("Chapter 3  - Expressions and Operators", "examples/ch03_expressions_and_operators.py"),
    "4": ("Chapter 4  - Making Decisions", "examples/ch04_making_decisions.py"),
    "5": ("Chapter 5  - Repetition", "examples/ch05_repetition.py"),
    "6": ("Chapter 6  - Functions", "examples/ch06_functions.py"),
    "7": ("Chapter 7  - Lists", "examples/ch07_lists.py"),
    "8": ("Chapter 8  - Strings as Data", "examples/ch08_strings_as_data.py"),
    "9": ("Chapter 9  - Dictionaries and Sets", "examples/ch09_dictionaries_and_sets.py"),
    "10": ("Chapter 10 - Tuples and Records", "examples/ch10_tuples_and_records.py"),
    "11": ("Chapter 11 - Searching and Sorting", "examples/ch11_searching_and_sorting.py"),
    "12": ("Chapter 12 - Recursion", "examples/ch12_recursion.py"),
}

PROJECTS = {
    "p1": ("Ch 1  - Receipt", "projects/ch01_receipt.py"),
    "p2": ("Ch 2  - Receipt, improved", "projects/ch02_receipt_improved.py"),
    "p3": ("Ch 3  - Change-making machine", "projects/ch03_change_maker.py"),
    "p4": ("Ch 4  - Ticket pricing kiosk", "projects/ch04_ticket_kiosk.py"),
    "p5": ("Ch 5  - Number-guessing game", "projects/ch05_guessing_game.py"),
    "p6": ("Ch 6  - Grade calculator", "projects/ch06_grade_calculator.py"),
    "p7": ("Ch 7  - Class gradebook", "projects/ch07_gradebook.py"),
    "p8": ("Ch 8  - Text analyzer", "projects/ch08_text_analyzer.py"),
    "p9": ("Ch 9  - Poll counter", "projects/ch09_poll_counter.py"),
    "p10": ("Ch 10 - Inventory system", "projects/ch10_inventory.py"),
    "p11": ("Ch 11 - Measuring algorithms", "projects/ch11_measuring_algorithms.py"),
    "p12": ("Ch 12 - Student records (capstone)", "projects/ch12_student_records.py"),
}


def show_menu():
    """Print the list of runnable files."""
    print("=" * 52)
    print("PYTHON FOUNDATIONS")
    print("=" * 52)
    print("\nCHAPTER EXAMPLES (type the number)")
    for key in sorted(EXAMPLES, key=int):
        print(f"  {key:<4}{EXAMPLES[key][0]}")

    print("\nCHAPTER PROJECTS (type p and the number, e.g. p5)")
    for key in sorted(PROJECTS, key=lambda k: int(k[1:])):
        print(f"  {key:<4}{PROJECTS[key][0]}")

    print("\n  q   Quit")
    print("-" * 52)


def run(path):
    """Run one file and wait for it to finish."""
    print(f"\n{'=' * 52}")
    print(f"Running {path}")
    print("=" * 52 + "\n")
    subprocess.run([sys.executable, path])
    print(f"\n{'-' * 52}")
    input("Press Enter to return to the menu. ")


def main():
    """Show the menu until the user quits."""
    while True:
        show_menu()
        choice = input("Choice: ").strip().lower()

        if choice == "q":
            print("Goodbye.")
            break
        elif choice in EXAMPLES:
            run(EXAMPLES[choice][1])
        elif choice in PROJECTS:
            run(PROJECTS[choice][1])
        else:
            print(f"\nNo such choice: {choice}\n")


if __name__ == "__main__":
    main()
