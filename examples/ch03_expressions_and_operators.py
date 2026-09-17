"""Chapter 3 - Expressions and Operators

Every worked example from the chapter.
"""

# --- Modulo and floor division ---------------------------------------------

# Is a number even? Even numbers have remainder 0 when divided by 2.
print(24 % 2)
print(25 % 2)

# Split a total into units: 500 seconds is how many minutes and seconds?
total_seconds = 500
print(total_seconds // 60, "minutes and", total_seconds % 60, "seconds")

# --- Order of operations ---------------------------------------------------

print(10 + 3 * 2)
print((10 + 3) * 2)
print(2 ** 3 * 4)

# --- Why 0.1 + 0.2 is not 0.3 ----------------------------------------------

print(0.1 + 0.2)

# --- Rounding and formatting -----------------------------------------------

print(round(3.14159))
print(round(3.14159, 2))
print(round(0.1 + 0.2, 2))

name = "Ada"
score = 91.5

print(f"{name} scored {score} points.")
print(f"{name} scored {score:.1f} points.")
print(f"Half of that is {score / 2:.2f}.")

total = 7.5
print(f"Total: ${total:.2f}")

width = 7
height = 4
print(f"A {width} by {height} rectangle has area {width * height}.")

# --- String operators ------------------------------------------------------

first = "Ada"
last = "Lovelace"

print(first + " " + last)
print("-" * 30)
print("ab" * 3)

# --- Comparison and boolean operators --------------------------------------

print("apple" < "banana")
print("Zebra" < "apple")

age = 15
has_permission = True

print(age >= 13 and age <= 19)
print(age < 13 or has_permission)
print(not has_permission)

print(13 <= age <= 19)

# --- Shorthand assignment --------------------------------------------------

score = 0
score += 10
score += 25
score *= 2
print(score)

# --- Try It #4: predict the output -----------------------------------------

print(7 // 2, 7 % 2, 7 / 2)
print(2 ** 3 ** 2)
print("5" * 3)
print(int("5") * 3)
