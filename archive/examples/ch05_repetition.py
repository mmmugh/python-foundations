"""Chapter 5 - Repetition

Worked examples from the chapter. Interactive ones are wrapped in functions
at the bottom.
"""

# --- The while loop --------------------------------------------------------

count = 1

while count <= 5:
    print(f"Count is {count}")
    count += 1

print("Done.")

# --- The for loop and range() ----------------------------------------------

for i in range(5):
    print(f"i is {i}")

print("Countdown:")
for i in range(5, 0, -1):
    print(i)
print("Liftoff.")

# A nested loop
for table in range(1, 4):
    for multiplier in range(1, 4):
        print(f"{table} x {multiplier} = {table * multiplier}")
    print()

# --- Looping over a string -------------------------------------------------

for letter in "Python":
    print(letter)

# --- The accumulator pattern -----------------------------------------------

# Summing
total = 0

for number in range(1, 101):
    total += number

print(f"The numbers 1 to 100 add up to {total}.")

# Counting things that match a test
evens = 0

for number in range(1, 51):
    if number % 2 == 0:
        evens += 1

print(f"There are {evens} even numbers from 1 to 50.")

# Building a string
bar = ""

for i in range(10):
    bar += "#"
    print(bar)

# --- continue --------------------------------------------------------------

for number in range(1, 21):
    if number % 3 != 0:
        continue
    print(number)

# --- Try It #7: predict the output -----------------------------------------

total = 0
for i in range(1, 6):
    if i == 3:
        continue
    total += i
print(total)


# --- The interactive examples ----------------------------------------------

def validation_loop_demo():
    """Keeps asking until the answer is a valid number."""
    answer = input("Enter a number: ")

    while not answer.isdigit():
        print("That is not a whole number.")
        answer = input("Enter a number: ")

    print(f"Thank you. You entered {int(answer)}.")


def largest_demo():
    """Tracking the largest value seen so far.

    Note the bug discussed in the chapter: starting at 0 gives the wrong
    answer if every number entered is negative.
    """
    largest = 0

    for i in range(5):
        value = int(input("Enter a number: "))
        if value > largest:
            largest = value

    print(f"The largest was {largest}.")


def menu_demo():
    """`while True` with a break as the only exit."""
    while True:
        command = input("Enter a command (or 'quit'): ")
        if command == "quit":
            break
        print(f"You said: {command}")

    print("Goodbye.")


# Uncomment any of these to run it:
# validation_loop_demo()
# largest_demo()
# menu_demo()
