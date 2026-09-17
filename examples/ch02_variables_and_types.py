"""Chapter 2 - Variables and Types

Worked examples from the chapter. The two programs that call input() are at
the bottom, wrapped in a function so this file runs start to finish without
stopping. Call them yourself to try them interactively.
"""

# --- Variables -------------------------------------------------------------

score = 42
player = "Ada"
print(player, "scored", score)

count = 5
count = count + 1
print(count)

# --- The four basic types --------------------------------------------------

print(type(7))
print(type(7.0))
print(type("7"))
print(type(True))

print(7 + 7)
print("7" + "7")

# --- Naming variables ------------------------------------------------------

# Clear
days_until_exam = 14
average_rainfall_mm = 82.4

# Legal, but you will regret it
d = 14
x1 = 82.4

print(days_until_exam, average_rainfall_mm, d, x1)

# --- Try It #4: what does this print, and why? -----------------------------

a = 10
b = a
a = 99
print(a, b)


# --- The interactive examples ----------------------------------------------

def greeting_demo():
    """Chapter 2's input() example."""
    name = input("What is your name? ")
    print("Nice to meet you,", name)


def age_demo():
    """The int(input(...)) idiom."""
    age = int(input("How old are you? "))
    print("Next year you will be", age + 1)


def temperature_demo():
    """Worked example: unit conversion."""
    fahrenheit = float(input("Temperature in degrees F: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "degrees F is", celsius, "degrees C")


# Uncomment any of these to run it:
# greeting_demo()
# age_demo()
# temperature_demo()

# The conversion itself, without the prompt, so you can see the output:
fahrenheit = 100.0
celsius = (fahrenheit - 32) * 5 / 9
print(fahrenheit, "degrees F is", celsius, "degrees C")
