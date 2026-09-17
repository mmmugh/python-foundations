"""Chapter 4 - Making Decisions

Worked examples from the chapter. Interactive ones are wrapped in functions
at the bottom.
"""

# --- Anatomy of an if ------------------------------------------------------

temperature = 95

if temperature > 90:
    print("It is hot out.")
    print("Bring water.")

print("Have a good day.")

# Indentation decides what belongs to the if.
score = 45

if score >= 60:
    print("You passed.")
    print("Congratulations.")

print("--- and with the second line moved left: ---")

if score >= 60:
    print("You passed.")
print("Congratulations.")

# --- elif chains -----------------------------------------------------------

score = 85

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

# BROKEN - the same chain in the wrong order. Do not copy this.
score = 95

if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 90:
    grade = "A"

print(grade)

# --- Nesting ---------------------------------------------------------------

has_ticket = True
age = 15

if has_ticket:
    if age >= 13:
        print("Enjoy the show.")
    else:
        print("You need an adult with you.")
else:
    print("Please buy a ticket first.")

# The same decision written with `and`
if has_ticket and age >= 13:
    print("Enjoy the show.")

# --- Try It #5: trace this by hand first -----------------------------------

x = 12
if x > 10:
    if x > 20:
        print("big")
    else:
        print("medium")
else:
    print("small")


# --- The interactive examples ----------------------------------------------

def voting_demo():
    """if / else on the user's age."""
    age = int(input("Your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print(f"You can vote in {18 - age} years.")


def truthiness_demo():
    """An empty string counts as False."""
    name = input("Your name (or press Enter to skip): ")
    if name:
        print(f"Hello, {name}.")
    else:
        print("Hello, stranger.")


def isdigit_demo():
    """Validating input with .isdigit()."""
    answer = input("How many tickets? ")
    if answer.isdigit():
        tickets = int(answer)
        print(f"That will be ${tickets * 12}.")
    else:
        print("Please enter a whole number.")


def try_except_demo():
    """Validating input with try / except."""
    answer = input("Enter a price: ")
    try:
        price = float(answer)
        print(f"With tax: ${price * 1.08:.2f}")
    except ValueError:
        print("That is not a number.")


# Uncomment any of these to run it:
# voting_demo()
# truthiness_demo()
# isdigit_demo()
# try_except_demo()
