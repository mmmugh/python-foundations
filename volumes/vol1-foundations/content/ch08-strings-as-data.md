<!-- part: Part II — Structuring Data -->
## Chapter 8 — Strings as Data

You have used strings since Chapter 1 as labels and messages. This chapter treats them as data to be examined, taken apart, and rebuilt — which is what most real programs do with text.

A string is a **sequence of characters**, and nearly everything you learned about lists in Chapter 7 applies.

```python
word = "Python"

print(len(word))
print(word[0])
print(word[-1])
print(word[0:3])
print(word[::-1])
```

Output:

```
6
P
n
Pyt
nohtyP
```

Indexing counts from zero, negative indexes count from the end, and slices work identically. `[::-1]` — a step of negative one — reverses a string, which is the standard Python idiom for it.

### Strings are immutable

Here is the one large difference from lists: **a string cannot be changed after it is created.**

```python
word = "Python"
word[0] = "J"
```

```
TypeError: 'str' object does not support item assignment
```

This is not a limitation so much as a design decision, and it has a practical consequence: every string operation *returns a new string* rather than modifying the original.

```python
word = "python"
word.upper()
print(word)

word = word.upper()
print(word)
```

Output:

```
python
PYTHON
```

The first `word.upper()` computed `"PYTHON"` and threw it away, because nothing captured the result. This is the single most common string mistake, and the fix is always the same: **assign the result to something.**

### Essential string methods

| Method | Returns | Example → Result |
| --- | --- | --- |
| `.upper()` | All uppercase | `"abc".upper()` → `"ABC"` |
| `.lower()` | All lowercase | `"ABC".lower()` → `"abc"` |
| `.title()` | First Letter Of Each Word | `"ada lovelace".title()` → `"Ada Lovelace"` |
| `.strip()` | Whitespace removed from both ends | `"  hi  ".strip()` → `"hi"` |
| `.replace(a, b)` | Every `a` replaced with `b` | `"cat".replace("c", "b")` → `"bat"` |
| `.split()` | A list of the words | `"a b c".split()` → `["a", "b", "c"]` |
| `.count(x)` | How many times `x` occurs | `"banana".count("a")` → `3` |
| `.find(x)` | Index of first `x`, or `-1` | `"banana".find("n")` → `2` |
| `.startswith(x)` | `True` if it begins with `x` | `"hello".startswith("he")` → `True` |
| `.endswith(x)` | `True` if it ends with `x` | `"cat.py".endswith(".py")` → `True` |
| `.isdigit()` | `True` if all digits | `"123".isdigit()` → `True` |
| `.isalpha()` | `True` if all letters | `"abc".isalpha()` → `True` |

Methods chain left to right, each working on the result of the last:

```python
messy = "   Ada LOVELACE  \n"
clean = messy.strip().title()
print(f"[{clean}]")
```

Output:

```
[Ada Lovelace]
```

That combination — strip the whitespace, normalize the case — is what you want on almost any input a human typed.

### Comparing text safely

String comparison is case-sensitive and whitespace-sensitive, so raw user input rarely compares the way you want:

```python
answer = " Yes "

print(answer == "yes")
print(answer.strip().lower() == "yes")
```

Output:

```
False
True
```

Normalize before comparing. Every time.

The `in` operator tests whether one string appears inside another:

```python
sentence = "The quick brown fox"

print("quick" in sentence)
print("slow" in sentence)
print("quick" in sentence.lower())
```

Output:

```
True
False
True
```

### `split()` and `join()`

These two are opposites, and between them they handle most text processing.

`.split()` cuts a string into a list. With no argument it splits on whitespace; with an argument it splits on that character:

```python
sentence = "the quick brown fox"
print(sentence.split())

date = "2026-09-17"
print(date.split("-"))

row = "Ada,88,A"
name, score, grade = row.split(",")
print(f"{name} scored {score} for a {grade}")
```

Output:

```
['the', 'quick', 'brown', 'fox']
['2026', '09', '17']
Ada scored 88 for a A
```

That last pattern — split a comma-separated line into named variables — is how nearly every program reads data files.

`.join()` does the reverse, gluing a list of strings together with a separator. The separator is the string you call it on, which reads backward at first and quickly stops being strange:

```python
words = ["the", "quick", "brown", "fox"]

print(" ".join(words))
print("-".join(words))
print(", ".join(words))
```

Output:

```
the quick brown fox
the-quick-brown-fox
the, quick, brown, fox
```

`.join()` requires every item to be a string. To join numbers, convert them first:

```python
scores = [88, 92, 79]
print(", ".join(str(s) for s in scores))
```

Output:

```
88, 92, 79
```

### Processing character by character

A `for` loop over a string hands you one character at a time, which is how you examine text in detail:

```python
def count_vowels(text):
    """Return the number of vowels in a piece of text."""
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


print(count_vowels("Programming in Python"))
```

Output:

```
5
```

Note `letter in "aeiou"` — the `in` operator tests membership in a string just as it does in a list, which makes checking against a set of characters very compact.

Building a new string works by accumulation, exactly as with lists:

```python
def remove_vowels(text):
    """Return the text with all vowels removed."""
    result = ""
    for letter in text:
        if letter.lower() not in "aeiou":
            result += letter
    return result


print(remove_vowels("Programming in Python"))
```

Output:

```
Prgrmmng n Pythn
```

### A worked example: palindromes

A palindrome reads the same forward and backward, ignoring case, spaces, and punctuation. Checking for one combines most of this chapter.

```python
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
```

Output:

```
True  racecar
True  A man, a plan, a canal: Panama
True  Was it a car or a cat I saw?
False  hello world
```

The structure is worth studying. `clean_text` does one job — strip the text down to comparable characters — and `is_palindrome` does one job, given clean text. Splitting the work that way makes the actual test a single readable line. `.isalnum()` returns `True` for letters and digits, which is exactly the filter needed.

### Escape sequences

Some characters cannot be typed directly inside a string, so they are written with a backslash:

| Sequence | Means |
| --- | --- |
| `\n` | New line |
| `\t` | Tab |
| `\"` | A double quote |
| `\'` | A single quote |
| `\\` | A backslash |

```python
print("Name:\tAda\nRole:\tMathematician")
print("She said, \"Hello.\"")
```

Output:

```
Name:	Ada
Role:	Mathematician
She said, "Hello."
```

Triple-quoted strings span multiple lines without needing `\n`:

```python
menu = """
1. Add a student
2. View the roster
3. Quit
"""
print(menu)
```

### Common mistakes

| Mistake | What happens |
| --- | --- |
| `word.upper()` without assigning | Nothing changes; strings are immutable |
| `word[0] = "J"` | `TypeError` — use slicing to build a new string |
| `answer == "yes"` on raw input | Fails on `"Yes"` or `" yes"` |
| `"a,b".split(", ")` | The separator must match exactly |
| `", ".join([1, 2])` | `TypeError` — convert to strings first |
| `.find(x)` returning `0` read as "not found" | `0` means position 0; not-found is `-1` |

### Try It

1. Ask for a word and print it forward, backward, in uppercase, and its length.
2. Write `count_letter(text, letter)` returning how many times the letter appears, ignoring case.
3. Ask for a full name and print the initials.
4. Write `title_case(sentence)` that capitalizes each word without using `.title()`.
5. Count the words in a sentence the user enters.
6. Write `caesar_shift(text, n)` that shifts each letter `n` places through the alphabet, wrapping from z to a.
7. Given `"Ada,88\nGrace,92\nAlan,45"`, print each name with its score on its own line.

### Chapter project: a text analyzer

Write a program that reports statistics about a passage of text.

```python
# Reports statistics about a passage of text.


def word_list(text):
    """Return the words of the text, stripped of punctuation and lowercased."""
    words = []
    for raw in text.split():
        cleaned = ""
        for character in raw.lower():
            if character.isalpha() or character == "'":
                cleaned += character
        if cleaned:
            words.append(cleaned)
    return words


def count_vowels(text):
    """Return the number of vowels in the text."""
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def longest_word(words):
    """Return the longest word in a list, or an empty string if there are none."""
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def average_word_length(words):
    """Return the mean length of the words, or 0.0 for an empty list."""
    if not words:
        return 0.0
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)


def analyze(text):
    """Print a report of statistics about the text."""
    words = word_list(text)
    sentences = 0
    for character in text:
        if character in ".!?":
            sentences += 1

    print("=" * 34)
    print(f"{'Characters:':<22}{len(text):>11}")
    print(f"{'Characters (no spaces):':<22}{len(text.replace(' ', '')):>11}")
    print(f"{'Words:':<22}{len(words):>11}")
    print(f"{'Sentences:':<22}{sentences:>11}")
    print(f"{'Vowels:':<22}{count_vowels(text):>11}")
    print(f"{'Longest word:':<22}{longest_word(words):>11}")
    print(f"{'Average word length:':<22}{average_word_length(words):>11.1f}")
    print("=" * 34)


sample = (
    "The quick brown fox jumps over the lazy dog. "
    "Programming is the art of telling another human what one wants "
    "the computer to do. Is that not remarkable?"
)

analyze(sample)
```

Output:

```
==================================
Characters:                   151
Characters (no spaces):        124
Words:                         28
Sentences:                      3
Vowels:                        42
Longest word:         programming
Average word length:          4.3
==================================
```

Two notes.

The sample text is written as several strings on consecutive lines inside parentheses. Python joins adjacent string literals automatically, which is the standard way to write a long piece of text without an enormous line.

The sentence count is a heuristic, not a fact. It counts `.`, `!`, and `?`, which means `Dr. Smith` would count as a sentence ending and `...` as three. Real sentence detection is a hard problem. A program that is approximately right is often the correct engineering answer, but you should know which of your numbers are exact and which are estimates — and say so in a comment when it matters.

`longest_word` also quietly picks the *first* longest word when several tie. That is a reasonable choice, and it is a choice; someone reading the output has no way to know a tie occurred.
