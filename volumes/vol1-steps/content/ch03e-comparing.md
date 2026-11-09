<!-- part: Unit 3 — Expressions and operators -->
## Lesson 3.5 — Comparing values

In this lesson Python answers questions about values: is this bigger than that, are these two the same? You also learn to tell apart two signs that look alike, `=` and `==`.

### Warm-up

1. Predict what this prints, then press Check.

```python
print("=" * 8)
```

2. Predict what this prints, then press Check.

```python
score = 7
print("Score: " + str(score))
```

### Asking a question

In lesson 2.2 you met `True` and `False`, a kind of value of their own. Here is where they come from. A **comparison** asks Python a question about two values, and the answer is `True` or `False`:

```python
print(5 > 3)
print(5 < 3)
```

Output:

```
True
False
```

There are six comparison operators:

| Operator | Asks | Example | Answer |
| --- | --- | --- | --- |
| `==` | equal to? | `5 == 5` | `True` |
| `!=` | not equal to? | `5 != 3` | `True` |
| `<` | less than? | `5 < 3` | `False` |
| `>` | greater than? | `5 > 3` | `True` |
| `<=` | less than or equal to? | `5 <= 5` | `True` |
| `>=` | greater than or equal to? | `3 >= 5` | `False` |

"Equal to?" is two equals signs, `==`. Comparisons work on variables too:

```python
age = 13
print(age >= 13)
print(age <= 12)
print(age == 12)
print(age != 12)
```

Output:

```
True
False
False
True
```

The answer to a comparison is a value, so you can store it in a variable, like any other value:

```python
points = 40
passed = points >= 50
print(passed)
```

Output:

```
False
```

Here is its trace table. After line 2, `passed` holds `False`:

| After line | points | passed |
| --- | --- | --- |
| 1 | 40 |  |
| 2 | 40 | False |
| 3 | 40 | False |

Strings can be compared too. They go in alphabetical order, with one twist: every capital letter comes before every small letter. And for `==`, capitals matter:

```python
print("apple" < "banana")
print("Zebra" < "apple")
print("cat" == "Cat")
```

Output:

```
True
True
False
```

Remember `0.1 + 0.2` from lesson 3.2? Its tiny error makes `==` say `False`. Round decimals before you compare them:

```python
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)
```

Output:

```
False
True
```

### Practice

3. Predict what this prints, then press Check.

```python
temperature = 30
print(temperature < 0)
print(temperature != 0)
print(temperature <= 30)
print(temperature >= 31)
```

4. Fill in the table, then press Check. Write `True` and `False` with capitals and no quotes.

```python
score = 7
won = score > 10
score = score + 5
won = score > 10
```

5. Predict what this prints, then press Check. Remember the twist: capitals come first.

```python
print("cat" < "dog")
print("Dog" < "cat")
print("dog" == "Dog")
```

6. Which line prints `True`?

### One = or two

`=` and `==` look alike, and mixing them up is the most common mistake in Python. They do different jobs:

- `=` stores. `score = 10` makes `score` hold 10.
- `==` asks. `score == 10` asks whether `score` is 10, and the answer is `True` or `False`.

Here is what happens when one `=` is used to ask:

```python
age = 14
print(age = 14)
```

Python responds with something like:

```
TypeError: print() got an unexpected keyword argument 'age'
```

Read it from the bottom. A keyword argument is Python's name for a `name = value` inside brackets; you don't need to remember it. Python took `age = 14` as an instruction to store something, and `print()` has no idea what to do with that. One `=` never asks a question. The question needs `==`:

```python
age = 14
print(age == 14)
```

Output:

```
True
```

### Practice

7. This program should print whether `score` is 10. It stops with an error. Run it and read the last line of the error. Then fix it.

```python
score = 10
print(score = 10)
```

8. Which one asks whether `lives` is 0, without changing `lives`?

### Try It

9. Ask for a whole number. Print `True` if it is even, and `False` if it is not.

> Say it: a number goes in, and `True` or `False` comes out. What makes a number even? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the number, as a whole number; find the remainder when it is divided by 2; ask whether that remainder is 0; print the answer.
> Name it: what would you call the number?
> Check it: try 4, then 7. Then the awkward ones: 0, and -3.

### What you can do now

- Compare two values, and get `True` or `False`.
- Store the answer to a comparison in a variable.
- Tell `=`, which stores, from `==`, which asks.

Key words: **comparison**, **`==`**, **`!=`**, **`<=`**, **`>=`**.
