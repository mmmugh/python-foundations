# A class gradebook using parallel lists.


def average(numbers):
    """Return the mean of a list of numbers, or 0.0 for an empty list."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def letter_grade(score):
    """Return the letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def print_roster(names, scores):
    """Print each student with their score and letter grade."""
    print(f"{'Student':<12}{'Score':>6}{'Grade':>7}")
    print("-" * 25)
    for i, name in enumerate(names):
        print(f"{name:<12}{scores[i]:>6}{letter_grade(scores[i]):>7}")


def print_summary(names, scores):
    """Print class statistics."""
    mean = average(scores)
    best = names[scores.index(max(scores))]
    passing = [s for s in scores if s >= 60]

    print("-" * 25)
    print(f"Class average: {mean:.1f}")
    print(f"Highest:       {max(scores)} ({best})")
    print(f"Lowest:        {min(scores)}")
    print(f"Passing:       {len(passing)} of {len(scores)}")


names = ["Ada", "Grace", "Alan", "Katherine", "Edsger"]
scores = [88, 92, 45, 95, 71]

print_roster(names, scores)
print_summary(names, scores)
