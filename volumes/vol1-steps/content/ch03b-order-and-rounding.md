<!-- part: Unit 3 — Expressions and operators -->
## Lesson 3.2 — Order of operations, and rounding

In this lesson you find out which part of a calculation Python works out first, and how to tidy a number that has more decimal places than you want.

### Warm-up

1. Predict what this prints, then press Check.

```python
print(17 // 5, 17 % 5)
```

2. A sticker album holds 10 stickers on a page, and you have 47 stickers. Which one tells you how many stickers are left over after the whole pages are full?

### Which part goes first

A calculation like `10 + 3 * 2` is an **expression**: anything Python can work out to a single value. Working it out is called **evaluating** it. When an expression has more than one operator, which one does Python do first?

```python
print(10 + 3 * 2)
```

Output:

```
16
```

Python does `*` before `+`, in the same order you use in math class: 3 * 2 is 6, then 10 + 6 is 16. Parentheses change the order, because whatever is inside them goes first:

```python
print((10 + 3) * 2)
```

Output:

```
26
```

Here is the whole order, from first to last. This is called the **order of operations**:

1. Parentheses `( )`
2. Powers `**`
3. `*`, `/`, `//` and `%`, from left to right
4. `+` and `-`, from left to right

So in this one, `**` goes before `*`:

```python
print(2 ** 3 * 4)
```

Output:

```
32
```

2 ** 3 is 8, then 8 * 4 is 32. When you are not sure of the order, add parentheses. They never hurt, and they make the order plain to anyone reading your code, including you.

### Practice

3. Predict what this prints, then press Check. The two lines differ only in their parentheses.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

4. Which line prints the average of 4 and 8?
5. Predict what this prints, then press Check. Use the order of operations: powers first, then `*`, `/`, `//` and `%` from left to right, then `+` and `-`.

```python
print(3 * 2 ** 2)
print(20 - 8 // 4)
print(12 // 2 * 3)
```

### A surprise

Try adding two small decimals:

```python
print(0.1 + 0.2)
```

Output:

```
0.30000000000000004
```

Nothing is wrong with your code. A computer stores decimals in binary, and 0.1 cannot be written exactly in binary, just as 1/3 cannot be written exactly as a decimal. The tiny error shows up when you add. It is far too small to matter, but it looks messy on screen.

### Practice

6. Your program prints `0.30000000000000004` for `0.1 + 0.2`. Is something wrong with your code?

### Rounding

`round()` tidies a number. Give it the number, a comma, and how many decimal places to keep:

```python
print(round(3.14159, 2))
print(round(0.1 + 0.2, 2))
```

Output:

```
3.14
0.3
```

Leave out the places, and it rounds to a whole number:

```python
print(round(3.7))
```

Output:

```
4
```

### Practice

7. Predict what this prints, then press Check.

```python
print(round(2.6))
print(round(2.66, 1))
```

8. Print 22 / 7 rounded to 3 decimal places.

### Try It

9. Ask for three test scores, and print their average, rounded to 1 decimal place.

> Say it: three scores go in; what comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for each score as a number, add them up, divide by 3, round to 1 place, print. Which of those must happen before the dividing?
> Name it: a name for each score, and one for the average.
> Check it: try 90, 85 and 82, which average 85.666... Then try three zeros.

### What you can do now

- Say which part of an expression Python evaluates first.
- Use parentheses to change the order, or just to make it plain.
- Round a number with `round()`.

Key words: **expression**, **evaluate**, **order of operations**, **round()**.
