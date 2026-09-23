"""Reference solutions and deliberate mutants, used only to validate the test
cases in content/_checks.json. NOT part of the site."""

GOOD = {
"is_even": "def is_even(n):\n    return n % 2 == 0",
"bmi": "def bmi(weight_kg, height_m):\n    return round(weight_kg / height_m ** 2, 1)",
"largest_of_three": "def largest_of_three(a, b, c):\n    biggest = a\n    if b > biggest:\n        biggest = b\n    if c > biggest:\n        biggest = c\n    return biggest",
"count_vowels": "def count_vowels(word):\n    total = 0\n    for letter in word:\n        if letter in 'aeiou':\n            total += 1\n    return total",
"is_prime": "def is_prime(n):\n    if n < 2:\n        return False\n    for d in range(2, int(n ** 0.5) + 1):\n        if n % d == 0:\n            return False\n    return True",
"count_above": "def count_above(numbers, threshold):\n    return sum(1 for n in numbers if n > threshold)",
"second_largest": "def second_largest(numbers):\n    return sorted(set(numbers))[-2]",
"count_letter": "def count_letter(text, letter):\n    return text.lower().count(letter.lower())",
"title_case": "def title_case(sentence):\n    return ' '.join(w[0].upper() + w[1:] for w in sentence.split(' '))",
"caesar_shift": "def caesar_shift(text, n):\n    out = ''\n    for ch in text:\n        out += chr((ord(ch) - 97 + n) % 26 + 97)\n    return out",
"invert": "def invert(d):\n    return {v: k for k, v in d.items()}",
"distance": "def distance(p1, p2):\n    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5",
"linear_search": "def linear_search(items, target):\n    return [i for i, x in enumerate(items) if x == target]",
"binary_search": "def binary_search(items, target):\n    lo, hi = 0, len(items)\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if items[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid\n    return lo",
"is_sorted": "def is_sorted(items):\n    for i in range(len(items) - 1):\n        if items[i] > items[i+1]:\n            return False\n    return True",
"power": "def power(base, exponent):\n    if exponent == 0:\n        return 1\n    return base * power(base, exponent - 1)",
"digit_sum": "def digit_sum(n):\n    if n < 10:\n        return n\n    return n % 10 + digit_sum(n // 10)",
"is_palindrome": "def is_palindrome(text):\n    if len(text) < 2:\n        return True\n    if text[0] != text[-1]:\n        return False\n    return is_palindrome(text[1:-1])",
"count_item": "def count_item(items, target):\n    if not items:\n        return 0\n    return (items[0] == target) + count_item(items[1:], target)",
"gcd": "def gcd(a, b):\n    if b == 0:\n        return a\n    return gcd(b, a % b)",
}

# Each is a mistake a real beginner makes. The test cases must catch every one.
MUTANT = {
"is_even": "def is_even(n):\n    return n % 2 == 1",
"bmi": "def bmi(weight_kg, height_m):\n    return weight_kg / height_m ** 2",
"largest_of_three": "def largest_of_three(a, b, c):\n    return a if a > b else b",
"count_vowels": "def count_vowels(word):\n    return sum(1 for c in word if c in 'aeio')",
"is_prime": "def is_prime(n):\n    for d in range(2, n):\n        if n % d == 0:\n            return False\n    return True",
"count_above": "def count_above(numbers, threshold):\n    return sum(1 for n in numbers if n >= threshold)",
"second_largest": "def second_largest(numbers):\n    return max(numbers)",
"count_letter": "def count_letter(text, letter):\n    return text.count(letter)",
"title_case": "def title_case(sentence):\n    return sentence[0].upper() + sentence[1:]",
"caesar_shift": "def caesar_shift(text, n):\n    return ''.join(chr(ord(c) + n) for c in text)",
"invert": "def invert(d):\n    return d",
"distance": "def distance(p1, p2):\n    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2",
"linear_search": "def linear_search(items, target):\n    for i, x in enumerate(items):\n        if x == target:\n            return [i]\n    return []",
"binary_search": "def binary_search(items, target):\n    lo, hi = 0, len(items) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if items[mid] == target:\n            return mid\n        if items[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1",
"is_sorted": "def is_sorted(items):\n    return True",
"power": "def power(base, exponent):\n    return base * exponent",
"digit_sum": "def digit_sum(n):\n    return n",
"is_palindrome": "def is_palindrome(text):\n    return len(text) % 2 == 1",
"count_item": "def count_item(items, target):\n    return 1 if target in items else 0",
"gcd": "def gcd(a, b):\n    return min(a, b)",
}

OUTPUT_GOOD = {
"ch03-expressions-and-operators#3": "for row in range(5):\n    print('#' * 20)",
"ch05-repetition#1": "for n in range(1, 21):\n    print(n * n)",
}
OUTPUT_MUTANT = {
"ch03-expressions-and-operators#3": "for row in range(4):\n    print('#' * 20)",
"ch05-repetition#1": "for n in range(1, 21):\n    print(n)",
}

# Practice pages. The flyer is pinned line for line, so these are
# checked by exact output rather than by calling anything.
OUTPUT_GOOD.update({
 "ch01-your-first-programs-practice#1": "print(\"======================================\")\nprint(\"         RIVERSIDE FILM CLUB\")\nprint(\"======================================\")",
 "ch01-your-first-programs-practice#2": "print(\"Feature:  The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#3": "print(\"Feature:\", \"The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#4": "print(\"When:     Friday, 7:30 pm\")\nprint(\"Where:    Room 14\")",
 "ch01-your-first-programs-practice#5": "print(\"Seats available:\", 8 * 12)",
 "ch01-your-first-programs-practice#6": "print(\"Snack bar total:\", 3 * 3.75 + 2 * 3.00)",
 "ch01-your-first-programs-practice#7": "# Prints the flyer for Friday's Riverside Film Club showing.\n\nprint(\"======================================\")\nprint(\"         RIVERSIDE FILM CLUB\")\nprint(\"======================================\")\nprint()\nprint(\"Feature:  The Quiet Harbour  (1998)\")\nprint(\"When:     Friday, 7:30 pm\")\nprint(\"Where:    Room 14\")\nprint()\nprint(\"Seats available:\", 8 * 12)\nprint(\"Snack bar total:\", 3 * 3.75 + 2 * 3.00)\nprint()\nprint(\"======================================\")"
})

OUTPUT_MUTANT.update({
 "ch01-your-first-programs-practice#1": "print(\"======================================\")\nprint(\"RIVERSIDE FILM CLUB\")\nprint(\"======================================\")",
 "ch01-your-first-programs-practice#2": "print(\"Feature: The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#3": "print(\"Feature:  The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#4": "print(\"When: Friday, 7:30 pm\")\nprint(\"Where: Room 14\")",
 "ch01-your-first-programs-practice#5": "print(\"Seats available:\", 8 * 11)",
 "ch01-your-first-programs-practice#6": "print(\"Snack bar total:\", 3 * 3.75 + 2 * 3.50)",
 "ch01-your-first-programs-practice#7": "# Prints the flyer for Friday's Riverside Film Club showing.\n\nprint(\"======================================\")\nprint(\"         RIVERSIDE FILM CLUB\")\nprint(\"======================================\")\nprint()\nprint(\"Feature:  The Quiet Harbour  (1998)\")\nprint(\"When:     Friday, 7:30 pm\")\nprint(\"Where:    Room 14\")\nprint(\"Seats available:\", 8 * 12)\nprint(\"Snack bar total:\", 3 * 3.75 + 2 * 3.00)\nprint()\nprint(\"======================================\")"
})
