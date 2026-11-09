<!-- part: Unit 7 — Lists -->
## Lesson 7.2 — Slicing

An index picks out one item. In this lesson you take a piece of a list: the first three items, the last two, or every second one.

### Warm-up

1. Predict what this prints, then press Check.

```python
pets = ["cat", "dog", "fish", "bird"]
print(pets[0])
print(pets[-1])
print(pets[2])
```

2. In the list `letters = ["a", "b", "c"]`, which one gives `"c"`?

### A piece of a list

A **slice** takes a piece of a list. Inside the square brackets go two indexes with a colon between them, the start and the stop:

```python
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[1:4])
```

Output:

```
['b', 'c', 'd']
```

The slice starts at index 1 and stops just before index 4, so it takes the items at index 1, 2 and 3. That is the same rule as `range(1, 4)`, which gives 1, 2 and 3 (lesson 5.2). The stop minus the start, 4 - 1, is how many items you get.

A slice is a list too, so Python prints it with square brackets.

### Practice

3. Predict what this prints, then press Check.

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days[0:2])
print(days[2:5])
```

### Leaving out an end

Leave out the start, and the slice starts at the beginning. Leave out the stop, and it goes to the end:

```python
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[:3])
print(letters[3:])
```

Output:

```
['a', 'b', 'c']
['d', 'e', 'f']
```

`letters[:3]` is the first three items, and `letters[3:]` is everything from index 3 on.

Counting from the end works in a slice too, and a slice is never out of range:

```python
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[-2:])
print(letters[4:100])
print(letters[10:])
```

Output:

```
['e', 'f']
['e', 'f']
[]
```

`letters[-2:]` starts at the second item from the end, so it is the last two items. `letters[4:100]` stops far past the end, and you get the items that are there. `letters[10:]` starts past the end, so there is nothing to take: you get an empty list. An index past the end is an `IndexError` (lesson 7.1), but a slice past the end never is.

### Practice

4. Predict what this prints, then press Check.

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days[:2])
print(days[3:])
```

5. Predict what this prints, then press Check.

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days[-3:])
print(days[3:10])
print(days[7:])
```

6. Print the weekend, the last two days of `week`, as a list. Use one slice.

```python
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
```

### Every second item

A third number, after a second colon, is the **step**, as in `range(1, 10, 2)`. A step of 2 takes every second item:

```python
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[::2])
print(letters[1::2])
```

Output:

```
['a', 'c', 'e']
['b', 'd', 'f']
```

`letters[::2]` leaves out the start and the stop, so it runs from the beginning to the end, taking every second item. `letters[1::2]` does the same, starting at index 1.

A step of -1 goes backward, from the end to the beginning:

```python
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[::-1])
```

Output:

```
['f', 'e', 'd', 'c', 'b', 'a']
```

A slice always makes a new list. The list you sliced is left as it was:

```python
letters = ["a", "b", "c", "d", "e", "f"]
first_three = letters[:3]
print(first_three)
print(letters)
```

Output:

```
['a', 'b', 'c']
['a', 'b', 'c', 'd', 'e', 'f']
```

### Practice

7. Predict what this prints, then press Check.

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[::3])
print(numbers[1::2])
print(numbers[::-1])
print(numbers)
```

### Try It

8. Five judges score a dive, and the scores come in order, lowest first. The lowest and the highest scores are thrown out. Write a function `middle_three(scores)` that gives back the middle three scores, as a list. For an empty list, it gives back an empty list.

> Say it: a list of five scores goes in; a list of the three in the middle comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. which indexes do the middle three have, in a list of five? 2. slice from the first of them, and stop just past the last of them. 3. give back the slice.
> Name it: the function and its parameter are named for you. Would a name for the slice make the `return` line easier to read?
> Check it: try `[5, 6, 7, 8, 9]`, which gives `[6, 7, 8]`. Then the awkward one: an empty list, `[]`. A slice is never out of range, so what comes back?

### What you can do now

- Take a piece of a list with a slice, from a start up to just before a stop.
- Leave out the start or the stop, count from the end, and take every second item with a step.
- Know that a slice makes a new list, and leaves the old one as it was.

Key words: **slice**, **step**.
