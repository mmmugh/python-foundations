<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.5 — Repeated work, and remembering answers

A recursive rule can be correct and still be slow. In this lesson a function calls itself twice, you count its calls as you counted comparisons in lesson 11.3, and you find the same answers being worked out over and over. Then a dictionary remembers each answer, so it is worked out only once.

### Warm-up

1. Predict what this prints, then press Check.

```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(8, 12))
print(gcd(5, 0))
```

2. A recursive case forgets its `return`. What does that call give back?

### Two calls at once

The **Fibonacci numbers** start 0 and 1, and each one after that is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13, and on. Numbered from 0, number `n` is number `n - 1` plus number `n - 2`. That rule is recursive already, with two calls instead of one:

```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(8)])
```

Output:

```
[0, 1, 1, 2, 3, 5, 8, 13]
```

`if n <= 1:` covers both base cases at once, because number 0 is 0 and number 1 is 1: each is its own answer. Every other call waits for two smaller calls, and adds their answers on the way back.

### Practice

3. Predict what this prints, then press Check.

```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))
print(fib(1))
```

### Counting the calls

To count the calls, hand every call the same list, and have each call add its `n` to it. Inside the function, `calls` is a second name for the one list (lesson 7.6), so every call adds to the same list:

```python
def fib(n, calls):
    calls.append(n)
    if n <= 1:
        return n
    else:
        return fib(n - 1, calls) + fib(n - 2, calls)


calls = []
print(fib(5, calls))
print(len(calls))
print(calls.count(2))
```

Output:

```
5
15
3
```

Fifteen calls, to work out 5. `fib(5)` asks for `fib(4)` and `fib(3)`. But `fib(4)` asks for `fib(3)` as well, and that one is worked out again from the start, with all its own calls. `fib(2)` is worked out three times, and `fib(1)` five times.

The repeats pile up fast:

| n | fib(n) | Calls |
| --- | --- | --- |
| 5 | 5 | 15 |
| 10 | 55 | 177 |
| 20 | 6,765 | 21,891 |
| 30 | 832,040 | 2,692,537 |

Each step of 1 in `n` multiplies the calls by about 1.6. `fib(50)` would need about 40 billion calls, far longer than you would wait.

### Practice

4. Predict what this prints, then press Check.

```python
def fib(n, calls):
    calls.append(n)
    if n <= 1:
        return n
    else:
        return fib(n - 1, calls) + fib(n - 2, calls)


calls = []
print(fib(4, calls))
print(len(calls))
print(calls.count(1))
```

5. Why does `fib(30)` make millions of calls, when there are only 31 numbers from 0 to 30?

### Remembering answers

The fix is to remember each answer the first time it is worked out, and look it up after that. A dictionary does it: its keys are the numbers worked out so far, and its values are their answers. Keeping a note of answers like this is called **memoization**, from memo, a note to yourself.

```python
def fast_fib(n, known):
    if n <= 1:
        return n
    if n in known:
        return known[n]
    answer = fast_fib(n - 1, known) + fast_fib(n - 2, known)
    known[n] = answer
    return answer


print(fast_fib(50, {}))
```

Output:

```
12586269025
```

That comes back at once. `known` is handed on to every call, and it is the same dictionary each time, as `calls` was the same list. The first time a number is asked for, it is worked out and stored. Every time after that, `n in known` (lesson 9.2) finds it, and the call gives back the stored answer with no more calls. `fast_fib(50, {})` makes 99 calls instead of about 40 billion.

### Practice

6. Predict what this prints, then press Check.

```python
def fast_fib(n, known):
    if n <= 1:
        return n
    if n in known:
        return known[n]
    answer = fast_fib(n - 1, known) + fast_fib(n - 2, known)
    known[n] = answer
    return answer


known = {}
print(fast_fib(5, known))
print(known)
```

7. In `fast_fib()`, what does the line `if n in known:` save?

### Try It

8. You climb a staircase of `n` stairs, taking 1 or 2 stairs at each step. How many different ways are there to get to the top? Your last step was either 1 stair or 2, so the ways for `n` stairs are the ways for `n - 1` plus the ways for `n - 2`. For 0 stairs and for 1 stair there is just 1 way. Write a recursive function `ways(n, known)` that gives back the number of ways, and remembers its answers in the dictionary `known`, so that `ways(40, {})` comes back at once.

> Say it: a number of stairs and a dictionary of answers go in; the number of ways to climb the stairs comes out, each answer worked out once. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. the base case: if `n` is 0 or 1, give back 1. 2. if `n` is in `known`, give back its answer. 3. otherwise add the ways for `n - 1` and `n - 2`, handing on `known`. 4. store the answer in `known`, then give it back.
> Name it: the function and its parameters are named for you. What would you call the answer before you store it?
> Check it: try 3 stairs, which gives 3 (1+1+1, 1+2 and 2+1), and 4, which gives 5. Then the awkward one: 0 stairs, which gives 1. If Check says `ways()` never finished, the answers are being worked out again and again: look at steps 2 and 4.
> Did it remember? While you try it, add `print("working out", n)` just before step 3: each number shows up only once. Take the print out before you press Check.

### What you can do now

- Follow a recursive function that calls itself twice.
- Count a recursive function's calls, and spot the same answers being worked out again.
- Remember answers in a dictionary, so each is worked out only once.

Key words: **Fibonacci numbers**, **memoization**.
