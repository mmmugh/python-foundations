<!-- part: Unit 8 — Strings as data -->
## Lesson 8.9 — One character at a time, and palindromes

String methods do a lot, but not everything. When none of them does the job, a loop can look at each character and decide what to do with it. In this lesson you build new text one character at a time, then use the routine to test for palindromes: words that read the same both ways.

### Warm-up

1. Predict what this prints, then press Check.

```python
words = ["to", "be", "or"]
print("-".join(words))
print(" ".join(words).upper())
```

2. What does `" ".join([1, 2])` do?

### Building new text

In lesson 5.5, an accumulator built a string with `+=`. With an `if` inside the loop, you choose which characters go in, the way lesson 7.7 chose which items went into a new list:

```python
def remove_vowels(text):
    """Give back the text with its vowels taken out."""
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

Where each character goes matters too. Add each one to the front, instead of the end, and the text comes out turned around:

```python
word = "top"
backward = ""
for letter in word:
    backward = letter + backward
print(backward)
```

Output:

```
pot
```

Here is its trace table, up to line 4. On each pass, the new letter goes in front of what `backward` already holds.

| After line | letter | backward |
| --- | --- | --- |
| 1 |  |  |
| 2 |  | "" |
| 3 | "t" | "" |
| 4 | "t" | "t" |
| 3 | "o" | "t" |
| 4 | "o" | "ot" |
| 3 | "p" | "ot" |
| 4 | "p" | "pot" |
| 3 | "p" | "pot" |

### Practice

3. Predict what this prints, then press Check.

```python
result = ""
for letter in "a-b.c":
    if letter not in "-.":
        result += letter.upper()
print(result)
```

4. Fill in the table, then press Check. Text can go in with or without its quotes.

```python
word = "abc"
result = ""
for letter in word:
    result = letter + "-" + result
```

5. Write a function `hide_digits(text)` that gives back `text` with every digit changed to `#`, and every other character left as it was. So `hide_digits("Call 555-1234")` gives back `"Call ###-####"`.

> Split it: start from `remove_vowels()`. This time every character goes in: a `#` if it is a digit, and the character itself if not. That is an `if` and an `else`.
> Check it: try `"Call 555-1234"`. Then the awkward ones: `""`, and `"abc"`, with no digits at all.

### A worked example: palindromes

A **palindrome** reads the same forward and backward, like `racecar`. Here is the problem: "Is a word a palindrome?" Say it and Split it come first, as comments:

```python
# Say it: True if the word reads the same forward and backward.
# Split it:
# 1. turn the word around
# 2. compare it with the word as it was
def is_palindrome(word):
    backward = word[::-1]
    return word == backward


print(is_palindrome("racecar"))
print(is_palindrome("rocket"))
# Check it, with two awkward words:
print(is_palindrome("Racecar"))
print(is_palindrome("top spot"))
```

Output:

```
True
False
False
False
```

Name it gave `backward` a name that says what the turned-around word is. Check it tried two awkward words, and the last two lines show the trouble. People call both of them palindromes, but the function doesn't. `Racecar` turned around is `racecaR`, and a capital R is not a small r. `top spot` turned around is `tops pot`: the space moves. Check it has found what the function must ignore. You fix it in the try-it.

### Practice

6. What does `is_palindrome("")` give back?

### Try It

7. Write a new `is_palindrome(text)` that ignores spaces and capitals. So `is_palindrome("Racecar")`, `is_palindrome("top spot")` and `is_palindrome("Never odd or even")` all give back `True`, and `is_palindrome("rocket")` gives back `False`.

> Say it: a text goes in; `True` comes out if it reads the same both ways once its spaces are gone and its capitals are small, and `False` if not. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. make a cleaned text: the spaces taken out, and the letters made small. 2. turn the cleaned text around. 3. compare the two.
> Name it: the function and its parameter are named for you. What would you call the cleaned text?
> Check it: try `"Never odd or even"`, which gives `True`, and `"rocket"`, which gives `False`. Then the awkward ones: `""`, which gives `True`; and `"ab ba c"`, which gives `False`.

### What you can do now

- Build new text one character at a time, choosing what goes in.
- Add to the front of a string to turn it around, and trace it.
- Test for a palindrome, ignoring spaces and capitals.

Key words: **palindrome**.
