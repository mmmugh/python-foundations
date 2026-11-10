<!-- part: Unit 12 — Recursion and problem solving -->
## Lesson 12.3 — Three shapes of recursion

Every recursive function so far has worked on a whole number that gets smaller by one. In this lesson you meet three shapes, one section each: a number multiplied on the way back, text that gets one letter shorter, and a list that gets one item shorter. Each shape has a practice of its own.

### Warm-up

1. Predict what this prints, then press Check.

```python
def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)


print(sum_to(3))
print(sum_to(0))
```

2. In `power_of_two(n)` from lesson 12.2, why does the base case give back 1, not 0?

### A number, multiplied

The **factorial** of 5, written 5!, is 5 × 4 × 3 × 2 × 1, which is 120. It counts the orders 5 things can be put in. Said the recursive way: 5! is 5 × 4!. And 0! is 1: there is exactly one way to put no things in order.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(0))
```

Output:

```
120
1
```

It is `power_of_two()` with `n` where the 2 was. The base case gives back 1 for the same reason: the answers are multiplied on the way back, and multiplying by 1 changes nothing, where multiplying by 0 would make every answer 0.

### Practice

3. Predict what this prints, then press Check.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
print(factorial(1))
```

4. Write a recursive function `power(base, exponent)` that gives back `base` to the power `exponent`, without using `**`. So `power(2, 3)` gives back 8.

> Split it: `power_of_two()`, with `base` where the 2 was. `base` is handed on unchanged, as `word` was in `cheer()`; only `exponent` gets smaller.
> Check it: try `power(2, 3)`, which gives 8, and `power(10, 2)`, which gives 100. Then the awkward ones: `power(5, 0)`, which gives 1, and `power(-2, 3)`, which gives -8.
> Did it call itself? While you try it, add `print("called with", base, exponent)` as the first line inside the function: one line for each call, with `exponent` one smaller each time. Take the print out before you press Check.

### Text, one letter shorter

`text[1:]` is the text without its first letter (lesson 8.1). It is one letter shorter, so it is a smaller question. The smallest text is `""`, with no letters at all. To reverse a text: reverse the rest of it, then put the first letter at the end:

```python
def reverse(text):
    if text == "":
        return ""
    else:
        return reverse(text[1:]) + text[0]


print(reverse("stop"))
print(reverse("a"))
```

Output:

```
pots
a
```

The call table for `reverse("abc")`:

| Call | Waits for | Gives back |
| --- | --- | --- |
| `reverse("abc")` | `reverse("bc")` | "cb" + "a" = "cba" |
| `reverse("bc")` | `reverse("c")` | "c" + "b" = "cb" |
| `reverse("c")` | `reverse("")` | "" + "c" = "c" |
| `reverse("")` | nothing: the base case | "" |

`"c"[1:]` is `""`, so a text of one letter reaches the base case in one more call.

### Practice

5. Predict what this prints, then press Check.

```python
def reverse(text):
    if text == "":
        return ""
    else:
        return reverse(text[1:]) + text[0]


print(reverse("tops"))
print(reverse("x"))
```

6. Write a recursive function `double_letters(text)` that gives back the text with every character written twice. So `double_letters("hi")` gives back `"hhii"`.

> Split it: the base case: `""` gives back `""`. The recursive case: the first character twice, then `double_letters()` of the rest.
> Check it: try `"hi"`, which gives `"hhii"`, and `"abc"`, which gives `"aabbcc"`. Then the awkward one: `""`, which gives `""`.
> Did it call itself? While you try it, add `print("called with", text)` as the first line inside the function: one line for each call, with the text one letter shorter each time. Take the print out before you press Check.

### A list, one item shorter

A list shrinks the same way: `numbers[1:]` is the list without its first item (lesson 7.2), and the smallest list is `[]`. The total of a list is its first item plus the total of the rest. The total of `[]` is 0:

```python
def total(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + total(numbers[1:])


print(total([4, 5, 6]))
print(total([]))
```

Output:

```
15
0
```

The call table for `total([4, 5, 6])`:

| Call | Waits for | Gives back |
| --- | --- | --- |
| `total([4, 5, 6])` | `total([5, 6])` | 4 + 11 = 15 |
| `total([5, 6])` | `total([6])` | 5 + 6 = 11 |
| `total([6])` | `total([])` | 6 + 0 = 6 |
| `total([])` | nothing: the base case | 0 |

`sum()` does this job already (lesson 7.5). Writing it yourself shows the shape, and the shape does jobs `sum()` cannot.

### Practice

7. Predict what this prints, then press Check.

```python
def total(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + total(numbers[1:])


print(total([10]))
print(total([1, 2, 3, 4]))
```

8. Write a recursive function `product(numbers)` that gives back all the numbers in the list multiplied together. So `product([2, 3, 4])` gives back 24.

> Split it: `total()`, with `*` where it adds. What should the base case give back for `[]`? Think of `factorial(0)`: the answers are multiplied on the way back.
> Check it: try `[2, 3, 4]`, which gives 24. Then the awkward ones: `[]`, which gives 1, and `[0, 9]`, which gives 0.
> Did it call itself? While you try it, add `print("called with", numbers)` as the first line inside the function: one line for each call, with the list one item shorter each time. Take the print out before you press Check.

### Try It

9. Write a recursive function `count_item(items, target)` that gives back how many times `target` is in the list `items`. So `count_item([1, 2, 1], 1)` gives back 2.

> Say it: a list and a target go in; how many times the target is in the list comes out, worked out from the rest of the list. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. the base case: an empty list holds the target 0 times. 2. the recursive case: count the first item, 1 if it is the target and 0 if not. 3. add that to `count_item()` of the rest of the list, and give it back.
> Name it: the function and its parameters are named for you. What would you call the 1 or 0 that counts the first item?
> Check it: try `[1, 2, 1]` with 1, which gives 2, and `["a", "b"]` with `"c"`, which gives 0. Then the awkward one: `[]`, which gives 0 whatever the target.
> Did it call itself? While you try it, add `print("called with", items)` as the first line inside the function: one line for each call, with the list one item shorter each time. Take the print out before you press Check.

### What you can do now

- Write a recursive function on a number, on text, or on a list.
- Make the question smaller with `n - 1`, `text[1:]` or `numbers[1:]`, down to 0, `""` or `[]`.
- Choose a base case's answer: 0 when the answers are added, 1 when they are multiplied.

Key words: **factorial**.
