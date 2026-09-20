# A guessing game with a limited number of attempts.

import random

secret = random.randint(1, 100)
max_tries = 7
tries_used = 0
won = False

print("I am thinking of a number between 1 and 100.")
print(f"You have {max_tries} tries.\n")

while tries_used < max_tries:
    guess_text = input(f"Try {tries_used + 1}: ")

    if not guess_text.isdigit():
        print("Please enter a whole number.")
        continue

    guess = int(guess_text)
    tries_used += 1

    if guess == secret:
        won = True
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")

print()
if won:
    print(f"Correct. You got it in {tries_used} tries.")
else:
    print(f"Out of tries. The number was {secret}.")
