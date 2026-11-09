<!-- part: Unit 7 — Lists -->
## Lesson 7.4 — Putting items in, and taking them out

`append()` adds an item at the end. In this lesson you put an item anywhere in a list, and take items out again: by what they are, or by where they are.

### Warm-up

1. Predict what this prints, then press Check.

```python
queue = ["Kim", "Lee"]
queue.append("Max")
queue[0] = "Sam"
print(queue)
```

2. After `a = [1, 2]`, `b = a` and `b.append(3)`, what does `print(a)` show?

### Putting an item in anywhere

`insert()` puts an item at an index you choose. It takes two arguments: first where, then what:

```python
names = ["Ada", "Alan"]
names.insert(1, "Grace")
print(names)
names.insert(0, "Bo")
print(names)
```

Output:

```
['Ada', 'Grace', 'Alan']
['Bo', 'Ada', 'Grace', 'Alan']
```

`names.insert(1, "Grace")` puts `"Grace"` at index 1. `"Alan"`, which was at index 1, moves along to index 2 to make room. `insert(0, ...)` puts an item at the very front.

### Practice

3. Predict what this prints, then press Check.

```python
queue = ["Kim", "Lee"]
queue.insert(0, "Max")
queue.insert(2, "Sam")
print(queue)
```

### Taking out an item by what it is

`remove()` takes out an item, found by its value:

```python
fruit = ["apple", "pear", "plum", "pear"]
fruit.remove("pear")
print(fruit)
```

Output:

```
['apple', 'plum', 'pear']
```

There were two `"pear"` items. `remove()` takes out only the first one it finds, from the front. The items after it move back one place to close the gap.

### Practice

4. Predict what this prints, then press Check.

```python
votes = ["yes", "no", "yes", "yes"]
votes.remove("yes")
print(votes)
```

### Taking out an item by where it is

`pop()` takes out the last item, and gives it back, so you can keep it. With an index in its brackets, it takes out the item at that index instead:

```python
scores = [88, 92, 79, 95]
last = scores.pop()
print(last)
print(scores)
first = scores.pop(0)
print(first)
print(scores)
```

Output:

```
95
[88, 92, 79]
88
[92, 79]
```

`scores.pop()` took out 95, the last item, and `last` kept it. `scores.pop(0)` took out the item at index 0, 88. `append()`, `insert()` and `remove()` only change the list. `pop()` changes it and gives back what it took out, like a function with a `return` (lesson 6.2).

So there are two ways to take an item out: `remove()` when you know what it is, and `pop()` when you know where it is.

### Practice

5. Predict what this prints, then press Check.

```python
stack = ["a", "b", "c", "d"]
top = stack.pop()
print(top)
print(stack.pop(1))
print(stack)
```

6. `fruit` holds `"plum"` somewhere, but you don't know where. Which line takes it out?

7. Write a function `move_to_front(items, item)` that takes `item` out of the list `items` and puts it in at the front. Then it gives back the list.

> Split it: two steps. Take the item out, by what it is; then put it in at index 0.
> Check it: try `["a", "b", "c"]` with `"c"`, which gives `["c", "a", "b"]`. Then the awkward one: an item that is already at the front, like `[0, 5]` with `0`. Nothing should change.

### Try It

8. People wait in line for tickets, in the list `line`. Ask how many people to serve, a whole number from 0 to 3. Take that many people off the front of the line, one at a time, printing `Serving Ada` for each. Then print the people still waiting, as a list.

```python
line = ["Ada", "Bo", "Cy"]
```

> Say it: a number goes in; that many people leave the front of the line, each one named, and the rest of the line is printed. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. ask how many to serve. 2. that many times: take out the person at the front, and print `Serving` with their name. 3. print the line.
> Name it: the line is named for you. What would you call the number typed? And the person taken out?
> Check it: try 2, which serves Ada and Bo and leaves `['Cy']`. Then the awkward ones: 0, which serves nobody and leaves the whole line; and 3, which leaves an empty line, `[]`.

### What you can do now

- Put an item in at any index with `insert()`.
- Take out an item by its value with `remove()`, or by its index with `pop()`.
- Keep the item that `pop()` gives back.

Key words: **insert**, **remove**, **pop**.
