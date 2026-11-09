<!-- part: Unit 5 — Repetition -->
## Lesson 5.3 — Looping over a string

A `for` loop can step through more than numbers. In this lesson it steps through a string, one character at a time, and counts what it finds on the way.

### Warm-up

1. Predict what this prints, then press Check.

```python
for number in range(2, 9, 3):
    print(number)
```

2. Which one gives the numbers 1 to 5?

### One character at a time

Put a string where `range()` was:

```python
for letter in "Python":
    print(letter)
```

Output:

```
P
y
t
h
o
n
```

On each pass, `letter` holds the next character of the string, starting from the left. The string has six characters, so the loop makes six passes.

The string can be in a variable. Here each character is printed between brackets, so you can see exactly what it is:

```python
word = "hi there"
for letter in word:
    print(f"[{letter}]")
```

Output:

```
[h]
[i]
[ ]
[t]
[h]
[e]
[r]
[e]
```

A space is a character too, so it gets a pass of its own.

### Practice

3. Predict what this prints, then press Check.

```python
for letter in "cat":
    print(letter + "!")
```

4. Predict what this prints, then press Check.

```python
for letter in "a b":
    print(f"<{letter}>")
```

### Counting as you go

How many times does `a` appear in `banana`? You can count by eye, but a loop can count for you. Use a counter, as in lesson 5.1, and add 1 to it only when the letter matches:

```python
count = 0
for letter in "banana":
    if letter == "a":
        count += 1
print(count)
```

Output:

```
3
```

The counter starts at 0, before the loop. On each pass, the `if` asks about one letter, and only an `a` adds 1. The last line is not indented, so it runs once, after the loop, when the counting is done.

Capitals are different characters, as in lesson 3.5. To count both, ask about both, joined with `or`:

```python
word = "Anna"
count = 0
for letter in word:
    if letter == "a" or letter == "A":
        count += 1
print(count)
```

Output:

```
2
```

Without `or letter == "A"`, it would count only 1.

### Practice

5. Predict what this prints, then press Check.

```python
count = 0
for letter in "Banana bread":
    if letter == "b":
        count += 1
print(count)
```

6. Ask for a word, and print how many times the small letter `s` appears in it, once, after counting, like this: `s: 4`.

### Try It

7. Ask for a word. Print it one letter per line, then print how many vowels it has: `a`, `e`, `i`, `o` or `u`, in small letters.

> Say it: a word goes in; its letters come out, one per line, and then the number of vowels in it. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the word; set a count to 0; loop over the word: print the letter, and if it is a vowel, add 1 to the count; after the loop, print the count. A letter is a vowel when it is "a", or "e", or "i", or "o", or "u": five tests joined with `or`.
> Name it: what does the count count? Its name can say so.
> Check it: try banana, which has 3. Then the awkward ones: a word with no vowels, like rhythm, and one that is nearly all vowels, like queue.

### What you can do now

- Loop over a string, one character at a time.
- Count the characters that match a test.
- Print a result once, after the loop has finished.

Key words: **character**, **counter**.
