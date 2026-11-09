<!-- part: Unit 8 — Strings as data -->
## Lesson 8.11 — Lining up columns, and a text analyzer

A report is easier to read when its numbers line up. In this lesson you give a value a width, so columns line up, and then build a program that reports on a passage of text, one function at a time.

### Warm-up

1. Predict what this prints, then press Check.

```python
print("one\ttwo".split("\t"))
print(len("a\\b"))
print("Hi\nthere")
```

2. A string between three quotes on each side runs over three lines. What is in it where each line ends?

### Lining up columns

In lesson 3.3, `:.2f` after a name in an f-string said how to show a number. A format specifier can also give a **width**: how many characters the value fills, with spaces making up the rest. `<` puts the value at the left of its width, and `>` at the right:

```python
name = "Ada"
score = 88
print(f"[{name:<8}]")
print(f"[{score:>5}]")
```

Output:

```
[Ada     ]
[   88]
```

The brackets show the width: `Ada` and 5 spaces fill 8, and 3 spaces and `88` fill 5. Give every line the same widths, and the columns line up, however long each value is:

```python
names = ["Ada", "Katherine", "Bo"]
scores = [88, 95, 7]
for i in range(len(names)):
    print(f"{names[i]:<10}{scores[i]:>4}")
```

Output:

```
Ada         88
Katherine   95
Bo           7
```

A width goes before the decimal places, so `:>6.1f` means "6 wide, at the right, with 1 decimal place":

```python
average = 4.3333
print(f"[{average:>6.1f}]")
```

Output:

```
[   4.3]
```

### Practice

3. Predict what this prints, then press Check. Count the spaces.

```python
item = "tea"
price = 2.5
print(f"[{item:<6}]")
print(f"[{item:>6}]")
print(f"[{price:>6.2f}]")
```

4. Print the menu so that its prices line up: each item at the left of a column 8 wide, then each price at the right of a column 6 wide, with 2 decimal places. The first line is `tea       2.50`.

```python
items = ["tea", "cake", "soup"]
prices = [2.5, 3.25, 4.0]
```

> Split it: loop with each index, as in the scores example. One f-string per line: `<8` for the item, `>6.2f` for the price.

### The text analyzer

Here is the problem: "Report on a passage of text: how many characters it has, with and without spaces; how many words, sentences and vowels; its longest word; and the average length of its words." First, the shape of the report. Each line has its label at the left of a column 24 wide, and its value at the right of a column 12 wide. One small function prints a line like that:

```python
def report_line(label, value):
    """Print one line of the report: the label at the left, the value at the right."""
    print(f"{label:<24}{value:>12}")


print("=" * 36)
report_line("Words:", 28)
report_line("Longest word:", "programming")
report_line("Average word length:", 4.3)
print("=" * 36)
```

Output:

```
====================================
Words:                            28
Longest word:            programming
Average word length:             4.3
====================================
```

Now Say it and Split it, as comments:

```python
# Say it: print a report on a passage of text.
# Split it:
# 1. the characters: len() of the text, then of the text with its spaces taken out
# 2. the words: word_list(text), then len() of it
# 3. the sentences: count_sentences(text)
# 4. the vowels: count_vowels() from lesson 8.4
# 5. the longest word: longest_word(words)
# 6. the average word length: average_length(words), rounded to 1 place
# 7. print each one with report_line()
```

Steps 1 and 4 use what you already have. Build and check the four new functions one at a time.

Step 3 counts `.`, `!` and `?`. That is a good guess at the number of sentences, not a sure count: `Dr. Who` would count as a sentence end, and `...` as three. Real programs often settle for a good guess. Know which of your numbers are guesses, and say so in a comment.

When every step is built, the report for the sample text in the try-it will look like this, line for line:

```
====================================
Characters:                      125
Characters (no spaces):          102
Words:                            24
Sentences:                         3
Vowels:                           34
Longest word:            programming
Average word length:             4.1
====================================
```

### Practice

5. Step 2: write `word_list(text)`, which gives back a list of the words in `text`, each in small letters with only its letters kept. A word with no letters at all is left out. So `word_list("Hi, Ada! 42")` gives back `["hi", "ada"]`.

> Split it: copy in `letters_only()` from lesson 8.6. Start an empty list; loop over the text split into words; keep each word's letters only, in small letters, and append it if it is not `""`.
> Check it: try `"The end."`, which gives `["the", "end"]`. Then the awkward ones: `""`, which gives `[]`, and `"- 42 -"`, which also gives `[]`.

6. Step 3: write `count_sentences(text)`, which gives back how many `.`, `!` and `?` characters are in `text`.

> Check it: try `"Hi. Bye!"`, which gives 2. Then the awkward one: `""`, which gives 0.

7. Step 5: write `longest_word(words)`, which gives back the longest word in the list `words`. If two are equally long, give back the first of them. For an empty list, give back `""`.

> Split it: keep the longest so far, starting from `""`, as lesson 5.5 kept the largest so far. A word replaces it only if it is longer.
> Check it: try `["a", "abc", "ab"]`, which gives `"abc"`. Then the awkward ones: `[]`, and a tie, `["hi", "yo"]`, which gives `"hi"`.

8. Step 6: write `average_length(words)`, which gives back the average number of letters in the words of the list `words`. For an empty list, give back `0.0`.

> Check it: try `["ab", "abcd"]`, which gives 3.0. Then the awkward one: `[]`.

### Try It

9. Print the report for `sample`, exactly as it is shown after the plan above: a line of 36 `=` signs, the seven lines of facts, and another line of `=` signs.

```python
def letters_only(text):
    letters = ""
    for character in text:
        if character.isalpha():
            letters += character
    return letters

def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

sample = "The quick brown fox jumps over the lazy dog. Programming is the art of telling a computer what to do! Is that not remarkable?"
```

> Say it: one line for each fact about the sample, between two lines of `=` signs. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: the plan above. Copy in `report_line()` and your four new functions first. Then make the list of words once, and print each line with `report_line()`, in the order shown.
> Name it: the sample and the functions are named for you. What would you call the list of words?
> Check it: run it and compare each line, spaces too. Then try a change: put a `!` at the end of the sample. Sentences becomes 4, and nothing else changes. Take it out again before you press Check.

### What you can do now

- Give a value a width in an f-string, at the left with `<` or the right with `>`, so columns line up.
- Build a program from small functions, each checked on its own.
- Tell a sure count from a good guess, and say which is which.

Key words: **width**.

That is the end of unit 8. Its quiz is below: fill it in, then show or print it.
