<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.3 — Looping over a dictionary

A dictionary can hold a whole class's scores, or everything in a shopping cart. In this lesson a `for` loop goes through every entry, and you add up the values, as you did for lists in unit 7.

### Warm-up

1. Predict what this prints, then press Check.

```python
ages = {"Mo": 12, "Kim": 13}
print(ages.get("Kim", 0))
print(ages.get("Lee", 0))
print("Mo" in ages)
del ages["Mo"]
print(ages)
```

2. With `ages = {"Mo": 12}`, what does `ages.get("Lee")` give back?

### A loop over the keys

A `for` loop over a dictionary gets its keys, one each time round, in the order they went in:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
for name in scores:
    print(name)
```

Output:

```
Ada
Grace
Alan
```

The key is all the loop gives you. To get its value, look it up with square brackets. That lookup is safe: every key the loop gives you is in the dictionary.

```python
prices = {"apple": 0.5, "pear": 0.75, "plum": 0.4}
for item in prices:
    print(item, prices[item])
```

Output:

```
apple 0.5
pear 0.75
plum 0.4
```

### Practice

3. Predict what this prints, then press Check.

```python
ages = {"Mo": 12, "Kim": 13}
ages["Lee"] = 11
ages["Mo"] = 14
for name in ages:
    print(name, ages[name])
```

4. Write a function `names_over(scores, limit)` that gives back a list of the names in `scores` whose score is above `limit`, in the dictionary's order.

> Split it: start an empty list. Loop over the names; if a name's score is above `limit`, add the name to the list. Then give the list back.
> Check it: try `{"Ada": 88, "Grace": 92, "Alan": 45}` with 60, which gives `["Ada", "Grace"]`. Then the awkward ones: a limit of 92, which gives `[]`, because 92 is not above 92; and an empty dictionary, `{}`.

### Just the values

`values()` gives the values without the keys, in the same order:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
for score in scores.values():
    print(score)
```

Output:

```
88
92
45
```

`sum()`, `max()` and `min()` from lesson 7.5 work on the values too. With `len()`, which counts the entries, that gives an average:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
print(sum(scores.values()))
print(max(scores.values()))
print(sum(scores.values()) / len(scores))
```

Output:

```
225
92
75.0
```

An empty dictionary has no average. Its `len()` is 0, so the division stops with a `ZeroDivisionError`, as in lesson 3.1. Test for it first.

### Practice

5. Predict what this prints, then press Check.

```python
stock = {"pens": 3, "pads": 0, "clips": 12}
for count in stock.values():
    print(count * 2)
print(sum(stock.values()))
print(min(stock.values()))
```

6. Write a function `average_score(scores)` that gives back the average of the scores in the dictionary `scores`, or 0 if it is empty.

> Split it: first, if `scores` has no entries, give back 0. Otherwise, give back the total of the values divided by how many entries there are.
> Check it: try `{"Ada": 88, "Grace": 92, "Alan": 45}`, which gives 75.0. Then the awkward one: `{}`, which gives 0.

### Try It

7. Print the cart: each item and its price, with 2 decimal places, one per line in the cart's order, as `bread: 2.50`. Then print the total, as `Total: 6.75`.

```python
cart = {"bread": 2.5, "milk": 1.25, "eggs": 3.0}
```

> Say it: one line for each item in the cart, then one line for the total. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. loop over the cart: print each item and its price, to 2 decimal places. 2. print the total of the prices, to 2 decimal places.
> Name it: the cart is named for you. What would you call one item, inside the loop?
> Check it: run it and compare each line. Then the awkward one: add jam to the cart, at a price of 0. It should print a line for jam, with 0.00 as its price, and the total stays the same. Take it out again before you press Check.

### What you can do now

- Loop over a dictionary's keys, in the order they went in, and look up each value.
- Loop over just the values with `values()`.
- Add up, average and find the largest of a dictionary's values.

Key words: **values()**.
