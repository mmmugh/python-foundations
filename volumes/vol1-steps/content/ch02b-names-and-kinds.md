<!-- part: Unit 2 — Variables and types -->
## Lesson 2.2 — Names that explain, and kinds of value

In this lesson you learn to choose names that explain a program, and meet the kinds of value Python works with.

### Warm-up

1. Fill in the table, then press Check.

```python
x = 4
x = x * 2
```

2. Predict what this prints, then press Check.

```python
a = 3
b = a
a = 8
print(a, b)
```

### Names that explain

Here is a short program:

```python
d = 14
print(d * 24)
```

Output:

```
336
```

And here is the same program with a better name:

```python
days_until_exam = 14
print(days_until_exam * 24)
```

Output:

```
336
```

Same program, same answer. But a week from now, only the second one still tells you what it is about. Choosing names that say what each value means is **Name it**, the third step of the routine.

Python has a few rules for names:

- Letters, digits and underscores only. No spaces.
- A name cannot start with a digit.
- Capital letters matter: `Score` and `score` are two different names.

The habit most Python programmers follow is **snake_case**: lowercase words joined by underscores, like `days_until_exam`.

### Practice

1. Which name says what the number means?
2. Which of these is a name Python accepts?
3. This works out how many pencils are in 3 boxes of 2. Rename `a`, `b` and `c` so the program explains itself. It should still print 6.

```python
a = 3
b = 2
c = a * b
print(c)
```

### Kinds of value

Every value has a **type**, which is its kind. Here are three:

| Type | Kind | Examples |
| --- | --- | --- |
| `int` | whole number | `7`, `0`, `-250` |
| `float` | number with a decimal point | `3.14`, `7.0` |
| `str` | text, in quotes | `"hello"`, `"7"` |

`type()` tells you the kind of any value:

```python
print(type(7))
print(type(7.0))
print(type("7"))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
```

`7`, `7.0` and `"7"` look alike, but they are three different kinds of value, and they behave differently:

```python
print(7 + 7)
print("7" + "7")
```

Output:

```
14
77
```

Adding numbers adds. Adding strings glues them end to end, which is called **concatenation**.

### Practice

1. Predict what this prints, then press Check.

```python
print(type(2.5))
```

2. What kind of value is "42", with the quotes?

### True and False

There is one more kind of value. It has only two values, `True` and `False`, and it is called **bool**.

```python
game_over = False
print(game_over)
print(type(game_over))
```

Output:

```
False
<class 'bool'>
```

`True` and `False` start with a capital letter and have no quotes. With quotes, they would just be text:

```python
print(type(True))
print(type("True"))
```

Output:

```
<class 'bool'>
<class 'str'>
```

You will use `True` and `False` a lot. For now, it is enough to know they are their own kind of value.

### Practice

1. Which one is a True/False value, not text?
2. Fill in the table, then press Check.

```python
lights_on = False
lights_on = True
```

### Try It

1. A recipe uses 3 eggs for each cake. You are baking 4 cakes. Store each number in a variable whose name says what it is, then print how many eggs you need.

> Say it: what are you working out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: store the eggs per cake, store the number of cakes, multiply and print.
> Name it: a name for each number that a friend would understand, such as `eggs_per_cake`.

### What you can do now

- Choose names that explain a program.
- Tell `int`, `float`, `str` and `bool` apart with `type()`.
- Know that `"7"` and `7` are different kinds of value.

Key words: **snake_case**, **type**, **int**, **float**, **str**, **bool**, **concatenation**.
