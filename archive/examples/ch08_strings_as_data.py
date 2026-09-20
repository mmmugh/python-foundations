"""Chapter 8 - Strings as Data

Every worked example from the chapter.
"""

# --- Strings are sequences -------------------------------------------------

word = "Python"

print(len(word))
print(word[0])
print(word[-1])
print(word[0:3])
print(word[::-1])

# --- Strings are immutable -------------------------------------------------

# word[0] = "J" would raise TypeError. Uncomment to see it.
# word[0] = "J"

word = "python"
word.upper()          # computed and thrown away
print(word)

word = word.upper()   # the result is kept
print(word)

# --- Chaining methods ------------------------------------------------------

messy = "   Ada LOVELACE  \n"
clean = messy.strip().title()
print(f"[{clean}]")

# --- Comparing text safely -------------------------------------------------

answer = " Yes "

print(answer == "yes")
print(answer.strip().lower() == "yes")

sentence = "The quick brown fox"

print("quick" in sentence)
print("slow" in sentence)
print("quick" in sentence.lower())

# --- split() and join() ----------------------------------------------------

sentence = "the quick brown fox"
print(sentence.split())

date = "2026-09-17"
print(date.split("-"))

row = "Ada,88,A"
name, score, grade = row.split(",")
print(f"{name} scored {score} for a {grade}")

words = ["the", "quick", "brown", "fox"]

print(" ".join(words))
print("-".join(words))
print(", ".join(words))

scores = [88, 92, 79]
print(", ".join(str(s) for s in scores))

# --- Processing character by character -------------------------------------


def count_vowels(text):
    """Return the number of vowels in a piece of text."""
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


print(count_vowels("Programming in Python"))


def remove_vowels(text):
    """Return the text with all vowels removed."""
    result = ""
    for letter in text:
        if letter.lower() not in "aeiou":
            result += letter
    return result


print(remove_vowels("Programming in Python"))


# --- A worked example: palindromes -----------------------------------------


def clean_text(text):
    """Return only the letters and digits of a text, in lowercase."""
    result = ""
    for character in text.lower():
        if character.isalnum():
            result += character
    return result


def is_palindrome(text):
    """Return True if the text reads the same forward and backward."""
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]


tests = [
    "racecar",
    "A man, a plan, a canal: Panama",
    "Was it a car or a cat I saw?",
    "hello world",
]

for test in tests:
    print(f"{is_palindrome(test)}  {test}")

# --- Escape sequences ------------------------------------------------------

print("Name:\tAda\nRole:\tMathematician")
print("She said, \"Hello.\"")

menu = """
1. Add a student
2. View the roster
3. Quit
"""
print(menu)
