<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.1 — A function that calls itself

In lesson 6.4 one function called another. In this lesson a function calls itself. That sounds as if it could never stop, and it would, except that each call asks a smaller question, and the smallest question has an answer of its own.

### Warm-up

1. Predict what this prints, then press Check.

```python
def double(number):
    return number * 2


def double_twice(number):
    return double(double(number))


print(double_twice(3))
print(double_twice(0))
```

2. Predict what this prints, then press Check.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1
print("Liftoff!")
```

### A countdown, said another way

The loop in the warm-up counts down from 3. Here is another way to say what a countdown is:

- To count down from 3: say 3, then count down from 2.
- To count down from 2: say 2, then count down from 1.
- To count down from 1: say 1, then count down from 0.
- To count down from 0: say "Liftoff!". There is nothing smaller to do.

Each line uses a smaller countdown, until the last one, which needs nothing smaller. That turns straight into a function:

```python
def countdown(n):
    if n == 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(3)
```

Output:

```
3
2
1
Liftoff!
```

Inside `countdown()` is a call to `countdown()`. A function that calls itself is **recursive**, and solving a problem this way is called **recursion**. It needs two parts:

- The **base case** is a question small enough to answer straight away, with no more calls. Here it is `n == 0`: print "Liftoff!".
- The **recursive case** calls the function again, on a smaller question. Here it prints `n`, then calls `countdown(n - 1)`.

Each call is one smaller, so the calls always reach 0, and stop there.

### Practice

3. Predict what this prints, then press Check.

```python
def countdown(n):
    if n == 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(2)
countdown(0)
```

4. In `countdown()`, which part is the base case?

### Following the calls

A **call table** follows recursion one call at a time: each call, what it prints, and what it calls next. Here is the one for `countdown(3)`:

| Call | n | Prints | Then calls |
| --- | --- | --- | --- |
| `countdown(3)` | 3 | 3 | `countdown(2)` |
| `countdown(2)` | 2 | 2 | `countdown(1)` |
| `countdown(1)` | 1 | 1 | `countdown(0)` |
| `countdown(0)` | 0 | Liftoff! | nothing: the base case |

Each call has its own `n`, as each call of a function in lesson 6.3 has its own local names. `countdown(2)` does not change the 3 that `countdown(3)` was given; it gets a new `n` of its own. The calls stop at the base case.

A recursive function can have more than one parameter. Here `word` is handed on unchanged to each call, and only `times` gets smaller:

```python
def cheer(word, times):
    if times == 0:
        print("Hooray!")
    else:
        print(word)
        cheer(word, times - 1)


cheer("Hip", 2)
```

Output:

```
Hip
Hip
Hooray!
```

Its call table:

| Call | word | times | Prints | Then calls |
| --- | --- | --- | --- | --- |
| `cheer("Hip", 2)` | "Hip" | 2 | Hip | `cheer("Hip", 1)` |
| `cheer("Hip", 1)` | "Hip" | 1 | Hip | `cheer("Hip", 0)` |
| `cheer("Hip", 0)` | "Hip" | 0 | Hooray! | nothing: the base case |

### Practice

5. In the call table for `countdown(3)`, which row is the call `countdown(1)`?

6. Predict what this prints, then press Check.

```python
def cheer(word, times):
    if times == 0:
        print("Hooray!")
    else:
        print(word)
        cheer(word, times - 1)


cheer("Go", 3)
cheer("Go", 0)
```

7. Write a recursive function `stars_down(n)`. It prints a row of `n` stars, then calls itself with one fewer, until `n` is 0, when it prints `Done.`. Write it above these lines, which use it, then run them all.

```python
stars_down(3)
stars_down(0)
```

> Split it: `countdown()`, with `"*" * n` where it prints `n` (lesson 3.4), and `Done.` where it prints "Liftoff!".
> Check it: the lines print three stars, two, one, then `Done.`, and then the awkward one, `stars_down(0)`, prints only `Done.`.
> Did it call itself? While you try it, add `print("called with", n)` as the first line inside the function: each call shows up, with `n` one smaller each time. Take the print out before you press Check.

### Try It

8. Write a recursive function `count_down_by(n, step)`. It prints `n`, then counts down from `n - step`, by the same step, until the number is 0 or below, when it prints `Liftoff!` instead. So `count_down_by(10, 3)` prints 10, 7, 4, 1, then `Liftoff!`. Write it above these lines, which use it, then run them all.

```python
count_down_by(10, 3)
count_down_by(6, 2)
count_down_by(0, 5)
```

> Say it: a number and a step go in; the numbers going down by the step are printed, then `Liftoff!`. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. the base case: if `n` is 0 or below, print `Liftoff!`. 2. the recursive case: otherwise print `n`, then call `count_down_by()` with `n - step` and the same `step`.
> Name it: the function and its parameters are named for you. `step` is handed on unchanged, as `word` is in `cheer()`.
> Check it: `count_down_by(6, 2)` prints 6, 4, 2, then `Liftoff!`. But 10 by 3 goes 10, 7, 4, 1, and then -2: it never lands on 0. That is why the base case is "0 or below", `n <= 0`, not `n == 0`. Then the awkward one: `count_down_by(0, 5)` prints only `Liftoff!`.
> Did it call itself? While you try it, add `print("called with", n)` as the first line inside the function: one line for each call, with `n` going down by `step`. Take the print out before you press Check.

### What you can do now

- Write a recursive function: a base case that stops, and a recursive case that calls itself on something smaller.
- Follow the calls with a call table: each call, what it prints, and what it calls next.
- Hand a value on unchanged from one call to the next.

Key words: **recursive**, **recursion**, **base case**, **recursive case**, **call table**.
