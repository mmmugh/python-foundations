<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.6 — Loop or recursion?

Anything you can write with recursion, you can write with a loop, and the other way round. In this lesson you see the same jobs done both ways, then a search where recursion says the idea most plainly, and how to choose between the two.

### Warm-up

1. Predict what this prints, then press Check.

```python
def fast_fib(n, known):
    if n <= 1:
        return n
    if n in known:
        return known[n]
    answer = fast_fib(n - 1, known) + fast_fib(n - 2, known)
    known[n] = answer
    return answer


print(fast_fib(7, {}))
print(fast_fib(0, {}))
```

2. In memoization, what goes in the dictionary?

### The same job, with a loop

Here is `factorial()` from lesson 12.3, written with a loop instead:

```python
def factorial_loop(n):
    result = 1
    for number in range(2, n + 1):
        result = result * number
    return result


print(factorial_loop(5))
print(factorial_loop(0))
```

Output:

```
120
1
```

The loop multiplies 2, 3, 4 and 5 into `result`, one after another. For 0, `range(2, 1)` is empty, so `result` stays 1, as the base case gave.

The Fibonacci numbers need only the last two at each step. Keep them in two names, and move both one place along each time round, with the unpacking of lesson 10.1:

```python
def fib_loop(n):
    a = 0
    b = 1
    for step in range(n):
        a, b = b, a + b
    return a


print(fib_loop(7))
print(fib_loop(50))
```

Output:

```
13
12586269025
```

`a` and `b` start as numbers 0 and 1. Each time round, `a` takes the next number along and `b` the one after it. One pass for each number, nothing worked out twice, and only two numbers to remember.

### Practice

3. Predict what this prints, then press Check.

```python
a = 0
b = 1
for step in range(4):
    a, b = b, a + b
    print(a, b)
```

4. Predict what this prints, then press Check.

```python
def factorial_loop(n):
    result = 1
    for number in range(2, n + 1):
        result = result * number
    return result


print(factorial_loop(4))
print(factorial_loop(1))
```

### A search that halves itself

Some problems hold a smaller copy of themselves, and are called **self-similar**. A binary search (lesson 11.2) is one: to search a sorted list, look at the middle; if that is not the target, search one half, which is the same problem, half the size. That "search one half" becomes a call:

```python
def search(items, target, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    if items[middle] == target:
        return middle
    elif items[middle] < target:
        return search(items, target, middle + 1, high)
    else:
        return search(items, target, low, middle - 1)


numbers = [4, 8, 9, 15, 17, 23, 42]
print(search(numbers, 23, 0, len(numbers) - 1))
print(search(numbers, 5, 0, len(numbers) - 1))
```

Output:

```
5
-1
```

There are two base cases. If `low > high`, there is nothing left to search, and the answer is -1. If the middle item is the target, the answer is the middle. Every other call searches a range half the size, so the calls always reach one of the two. Lesson 11.2's loop changed `low` and `high` as it went; here each call is handed its own.

### Practice

5. Predict what this prints, then press Check.

```python
def search(items, target, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    if items[middle] == target:
        return middle
    elif items[middle] < target:
        return search(items, target, middle + 1, high)
    else:
        return search(items, target, low, middle - 1)


numbers = [4, 8, 9, 15, 17, 23, 42]
print(search(numbers, 4, 0, 6))
print(search(numbers, 42, 0, 6))
print(search([], 7, 0, -1))
```

6. In `search()`, which line stops the calls when the target is not in the list?

### Which to choose

Both ways work, so choose the one that says the idea more plainly:

- A loop fits when you go through things one after another: the items of a list, the numbers in a range. Adding up a list is plainer with a loop, or with `sum()`, than with `total()`.
- Recursion fits when the problem holds a smaller copy of itself: a search of half the list, a rule like Euclid's or the staircase's, or things inside things of the same kind, like folders inside folders.
- When recursion works out the same answers again, remember them, or use a loop.

One more thing tips the choice. Python allows about 1,000 calls waiting at once (lesson 12.4), so `total()` of a list of 5,000 numbers stops with a `RecursionError`, where a loop has no trouble.

### Practice

7. You need the total of a list of 5,000 prices. Which is the best choice?

8. Which of these jobs does recursion fit best?

### Try It

9. A palindrome reads the same backward and forward, like `level` (lesson 8.9). Said the recursive way: a text is a palindrome if its first and last letters are the same and the middle, without them, is a palindrome too. A text of 0 or 1 letters is always a palindrome. Write a recursive function `is_palindrome(text)` that gives back `True` or `False`.

> Say it: a text goes in; `True` comes out if it reads the same both ways, and `False` if not, worked out from the middle. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. the first base case: if the text has 0 or 1 letters, give back `True`. 2. the second: if the first and last letters differ, give back `False`. 3. the recursive case: give back `is_palindrome()` of the middle, `text[1:len(text) - 1]`.
> Name it: the function and its parameter are named for you.
> Check it: try `"level"`, which gives `True`, `"noon"`, which gives `True`, and `"lever"`, which gives `False`. Then the awkward ones: `""` and `"a"`, which give `True`, and `"ab"`, which gives `False`.
> Did it call itself? While you try it, add `print("called with", text)` as the first line inside the function: for `"level"` you see level, eve, then v. Take the print out before you press Check.

### What you can do now

- Write the same job with a loop or with recursion, and say which is plainer.
- Write a search that halves itself, with two base cases.
- Choose recursion for a problem that holds a smaller copy of itself, and a loop for going through things one after another.

Key words: **self-similar**.
