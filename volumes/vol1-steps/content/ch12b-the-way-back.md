<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.2 — The way back, and giving back an answer

In lesson 12.1 each call did its work and then made the next call. In this lesson some of the work comes after the call, and you see when it runs. Then a recursive function gives back an answer, built from the answer to a smaller question.

### Warm-up

1. Predict what this prints, then press Check.

```python
def cheer(word, times):
    if times == 0:
        print("Hooray!")
    else:
        print(word)
        cheer(word, times - 1)


cheer("Hey", 1)
cheer("Ho", 2)
```

2. In `cheer(word, times)`, which value is handed on unchanged from one call to the next?

### The way back

Here the `print()` comes after the call instead of before it:

```python
def count_up(n):
    if n == 0:
        print("Go!")
    else:
        count_up(n - 1)
        print(n)


count_up(3)
```

Output:

```
Go!
1
2
3
```

It counts up, though `n` goes down. The call table shows why:

| Call | First calls | Then prints |
| --- | --- | --- |
| `count_up(3)` | `count_up(2)` | 3 |
| `count_up(2)` | `count_up(1)` | 2 |
| `count_up(1)` | `count_up(0)` | 1 |
| `count_up(0)` | nothing: the base case | Go! |

Read the middle column down, then the last column up. `count_up(3)` cannot print 3 until its call to `count_up(2)` has finished, and that call is waiting for `count_up(1)`, which is waiting for `count_up(0)`. Each call waits, holding its own `n`. The base case prints first. Then the waiting calls finish one by one, the last one first: 1, then 2, then 3.

So the calls go down to the base case, and anything after the call runs on the way back up.

### Practice

3. Predict what this prints, then press Check. It prints before the call and after it.

```python
def down_and_up(n):
    if n == 0:
        print("turn")
    else:
        print(n)
        down_and_up(n - 1)
        print(n)


down_and_up(2)
```

4. Why does `count_up(3)` print 1 before it prints 3?

### Giving back an answer

2 to the power 3 is 2 × 2 × 2, which is 8. Said the recursive way: 2 to the power 3 is 2 times 2 to the power 2. And 2 to the power 0 is 1, with nothing smaller to work out. That is a base case and a recursive case again, but this time each call gives back a value:

```python
def power_of_two(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_two(n - 1)


print(power_of_two(3))
print(power_of_two(0))
```

Output:

```
8
1
```

`return 2 * power_of_two(n - 1)` cannot multiply until the smaller call has given back its answer. The call table now has a column for what each call waits for, and one for what it gives back:

| Call | Waits for | Gives back |
| --- | --- | --- |
| `power_of_two(3)` | `power_of_two(2)` | 2 * 4 = 8 |
| `power_of_two(2)` | `power_of_two(1)` | 2 * 2 = 4 |
| `power_of_two(1)` | `power_of_two(0)` | 2 * 1 = 2 |
| `power_of_two(0)` | nothing: the base case | 1 |

Fill it in the same way: the middle column down, then the last column up. The base case's 1 is the first answer anyone knows. Each call above it takes the answer from below, multiplies it by 2, and gives that back to the call above. Nothing is multiplied until the bottom is reached.

### Practice

5. Predict what this prints, then press Check.

```python
def power_of_two(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_two(n - 1)


print(power_of_two(4))
print(power_of_two(1))
```

6. In the call table for `power_of_two(3)`, which call knows its answer first?

7. Write a recursive function `power_of_three(n)` that gives back 3 to the power `n`. So `power_of_three(2)` gives back 9.

> Split it: `power_of_two()`, with 3 where it multiplies by 2. The base case stays the same: anything to the power 0 is 1.
> Check it: try 2, which gives 9, and 4, which gives 81. Then the awkward one: 0, which gives 1.
> Did it call itself? While you try it, add `print("called with", n)` as the first line inside the function: one line for each call, with `n` one smaller each time. Take the print out before you press Check.

### Try It

8. Write a recursive function `sum_to(n)` that gives back 1 + 2 + ... + `n`. So `sum_to(4)` gives back 1 + 2 + 3 + 4, which is 10. `sum_to(0)` gives back 0: there is nothing to add.

> Say it: a whole number goes in; the sum of 1 up to that number comes out, worked out from a smaller sum. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. the base case: if `n` is 0, give back 0. 2. the recursive case: the sum up to `n` is `n` plus the sum up to `n - 1`, so give back `n + sum_to(n - 1)`.
> Name it: the function and its parameter are named for you.
> Check it: try 4, which gives 10, and 100, which gives 5050. Fill in a call table for `sum_to(3)`, the middle column down and the last column up: it gives back 6. Then the awkward one: 0, which gives 0.
> Did it call itself? While you try it, add `print("called with", n)` as the first line inside the function: one line for each call, with `n` one smaller each time. Take the print out before you press Check.

### What you can do now

- Say when a line after a recursive call runs: on the way back, the last call first.
- Write a recursive function that gives back an answer built from a smaller call's answer.
- Fill in a call table: what each call waits for, down; what it gives back, up.

Key words: **the way back**.
