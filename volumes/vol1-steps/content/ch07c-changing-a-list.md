<!-- part: Unit 7 — Lists -->
## Lesson 7.3 — Changing a list, and two names for one list

So far you have read items from a list. A list can also be changed after it is made: one item replaced, or a new item added to the end. In this lesson you do both, and meet the one surprise that comes with it.

### Warm-up

1. Predict what this prints, then press Check.

```python
colors = ["red", "orange", "yellow", "green", "blue"]
print(colors[1:3])
print(colors[:2])
print(colors[::2])
```

2. With `days = ["Mon", "Tue", "Wed", "Thu", "Fri"]`, how many items does `days[1:3]` have?

### Changing an item

Put an index on the left of `=`, and the item at that index is replaced:

```python
scores = [88, 92, 79, 95]
scores[2] = 85
print(scores)
```

Output:

```
[88, 92, 85, 95]
```

The item at index 2 was 79; now it is 85. The other items stay where they were. A list can be changed after it is made: it is **mutable**.

In a trace table, a list's cell holds the whole list, written as Python prints it:

| After line | scores |
| --- | --- |
| 1 | [88, 92, 79, 95] |
| 2 | [88, 92, 85, 95] |
| 3 | [88, 92, 85, 95] |

### Practice

3. Fill in the table: the whole list `temps` after each line. Then press Check.

```python
temps = [12, 15, 11]
temps[0] = 13
temps[-1] = temps[-1] + 2
```

### Adding to the end

To add an item to the end of a list, use `append()`:

```python
scores = [88, 92, 79]
scores.append(95)
print(scores)
```

Output:

```
[88, 92, 79, 95]
```

`append()` is a **method**: a function that belongs to a value. You call it with a dot after the value's name, so `scores.append(95)` means "add 95 to the end of `scores`". It changes the list itself, so there is no `=`.

A list can start empty and grow, one `append()` at a time. In a loop, that builds a list the way an accumulator builds a total (lesson 5.5):

```python
squares = []
for number in range(1, 5):
    squares.append(number * number)
print(squares)
```

Output:

```
[1, 4, 9, 16]
```

`append()` takes exactly one item. Give it two, and Python stops:

```python
guests = ["Ada"]
guests.append("Grace", "Alan")
```

The last line of the error says `TypeError: list.append() takes exactly one argument (2 given)`. To add two items, call `append()` twice.

### Practice

4. Predict what this prints, then press Check.

```python
pets = ["cat"]
pets.append("dog")
pets.append("fish")
print(pets)
print(pets[-1])
```

5. Make the list of the first five multiples of 3, `[3, 6, 9, 12, 15]`, with a `for` loop and `append()`. Then print it.

```python
multiples = []
print(multiples)
```

> Split it: start from `squares` above. Which numbers does the loop need, and what do you append for each one?

6. This program should add two more scores, 79 and 95, to the list, but it stops with an error. Run it and read the last line of the error. Then fix it, so that it prints `[88, 92, 79, 95]`.

```python
scores = [88, 92]
scores.append(79, 95)
print(scores)
```

### Two names for one list

In lesson 2.1, `b = a` gave `b` the value `a` had, and changing `a` afterward left `b` alone. With a list, something new happens:

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
```

Output:

```
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Only `b` was changed, yet `a` changed too. `b = a` does not make a second list. It gives the same list a second name. `append()` changes that one list, and both names see the change. Lesson 2.1 still holds: pointing a name at a new value, with `=`, never changes another name. But `append()`, or replacing an item, changes the list itself, and both names share it:

| After line | a | b |
| --- | --- | --- |
| 1 | [1, 2, 3] |  |
| 2 | [1, 2, 3] | [1, 2, 3] |
| 3 | [1, 2, 3, 4] | [1, 2, 3, 4] |
| 4 | [1, 2, 3, 4] | [1, 2, 3, 4] |

To get a second list of your own, make a copy. A slice always makes a new list (lesson 7.2), and a slice with both ends left out, `a[:]`, takes every item:

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)
print(b)
```

Output:

```
[1, 2, 3]
[1, 2, 3, 4]
```

Now `b` is a new list with the same items, and changing it leaves `a` alone.

### Practice

7. Fill in the table for both names. As before, leave a cell empty (or write -) while a name has no value yet. Then press Check.

```python
mine = ["pen"]
yours = mine
yours.append("cap")
mine[0] = "pencil"
```

8. Predict what this prints, then press Check.

```python
mine = ["pen"]
yours = mine[:]
yours.append("cap")
print(mine)
print(yours)
```

### Try It

9. Ask for things to buy, one at a time, until the user presses Enter without typing anything. Then print the shopping list, as a list.

> Say it: items go in one at a time until an empty one; the list of them comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start with an empty list. 2. ask for the first item. 3. while it is not empty: append it, then ask for the next. 4. after the loop, print the list. This is the stop-value loop of lesson 5.6, with an empty answer as the stop value.
> Name it: what would you call the list? And one thing that was typed?
> Check it: try milk, eggs and bread, then Enter. Then the awkward one: press Enter straight away. The list should be empty, `[]`, with no empty item in it.

### What you can do now

- Replace an item by its index, and trace a list as it changes.
- Add items to the end of a list with `append()`, and build a list in a loop.
- Tell a second name for a list from a copy of it, made with `[:]`.

Key words: **mutable**, **method**, **append**.
