<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.7 — A copy of your own, and a new dictionary

Lesson 7.3 showed that `b = a` gives a list a second name, not a second list. Dictionaries work the same way. In this lesson you make a real copy of a dictionary, write functions that leave the dictionary they are handed as it was, and build a new dictionary from an old one.

### Warm-up

1. Predict what this prints, then press Check.

```python
books = {
    "Dune": {"pages": 412, "read": True},
    "Holes": {"pages": 233, "read": False},
}
print(books["Holes"]["pages"])
books["Holes"]["read"] = True
print(books["Holes"])
```

2. In `f"{name}: {details['score']}"`, why is `score` in single quotes?

### Two names, or two dictionaries

`=` gives a dictionary a second name, as it does for a list:

```python
stock = {"pens": 10}
same = stock
same["pens"] = 0
print(stock)
```

Output:

```
{'pens': 0}
```

`copy()` makes a new dictionary with the same entries. Change the copy, and the original stays as it was:

```python
stock = {"pens": 10}
mine = stock.copy()
mine["pens"] = 0
print(stock)
print(mine)
```

Output:

```
{'pens': 10}
{'pens': 0}
```

Lists have a `copy()` method too. It does what `[:]` did in lesson 7.3:

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
print(b)
```

Output:

```
[1, 2, 3]
[1, 2, 3, 4]
```

Inside a function, a parameter is a second name for the dictionary it was handed, just as it was for a list in lesson 7.6. A function that should give back a changed dictionary, and leave the one it was handed as it was, starts from a copy.

### Practice

3. Predict what this prints, then press Check.

```python
prices = {"tea": 2}
other = prices
spare = prices.copy()
other["tea"] = 3
spare["cake"] = 4
print(prices)
print(spare)
names = ["Mo"]
more_names = names.copy()
more_names.append("Kim")
print(names)
```

4. A lost property office keeps a register: each item it holds, and how many. Write a function `add_item(register, item)` that gives back a new register with one more `item`, whether or not it was there before, and leaves `register` as it was. Write it above the lines below, which call it, and keep them.

```python
register = {"umbrella": 3, "phone": 1}
print(add_item(register, "phone"))
print(add_item(register, "hat"))
print(register)
```

> Split it: 1. make a copy of `register`. 2. count one more `item` into the copy, with the counting pattern. 3. give back the copy.
> Check it: the first line should be `{'umbrella': 3, 'phone': 2}`, and the last line should still be `{'umbrella': 3, 'phone': 1}`. Then the awkward one: add `print(add_item({}, "hat"))`, which prints `{'hat': 1}`.

### A dictionary of dictionaries

`copy()` copies the outer dictionary only. The copy has its own keys, but each of its values is the very same inner dictionary that the original holds. So a change one level down shows through both names:

```python
books = {"Dune": {"pages": 412}, "Holes": {"pages": 233}}
mine = books.copy()
mine["Dune"]["pages"] = 500
print(books["Dune"])
```

Output:

```
{'pages': 500}
```

To change a value one level down and leave the original as it was, copy that inner dictionary too, and store the copy under its key:

```python
books = {"Dune": {"pages": 412}, "Holes": {"pages": 233}}
mine = books.copy()
mine["Dune"] = books["Dune"].copy()
mine["Dune"]["pages"] = 500
print(books["Dune"])
print(mine["Dune"])
```

Output:

```
{'pages': 412}
{'pages': 500}
```

Storing a whole new value under a key of the copy, as the third line does, never changes the original.

### Practice

5. Predict what this prints, then press Check.

```python
teams = {"red": {"wins": 2}, "blue": {"wins": 5}}
spare = teams.copy()
spare["red"]["wins"] = 3
spare["blue"] = teams["blue"].copy()
spare["blue"]["wins"] = 9
print(teams["red"])
print(teams["blue"])
print(spare["blue"])
```

### Changing a dictionary while looping over it

This loop should take out every item the shop has none of:

```python
stock = {"pens": 10, "pads": 0, "clips": 0}
for item in stock:
    if stock[item] == 0:
        del stock[item]
print(stock)
```

It stops, and the last line of the error says `RuntimeError: dictionary changed size during iteration`. Iteration is Python's word for going round a loop; you don't need to remember it. A loop over a dictionary cannot take entries out of that same dictionary as it goes. Loop over a copy instead, and take the entries out of the original:

```python
stock = {"pens": 10, "pads": 0, "clips": 0}
for item in stock.copy():
    if stock[item] == 0:
        del stock[item]
print(stock)
```

Output:

```
{'pens': 10}
```

### Practice

6. This program should take out everyone under 13, and print `{'Kim': 15, 'Ada': 14, 'Bo': 13}`. It stops with an error. Run it and read the last line of the error. Then fix it.

```python
ages = {"Mo": 12, "Kim": 15, "Lee": 11, "Ada": 14, "Bo": 13}
for name in ages:
    if ages[name] < 13:
        del ages[name]
print(ages)
```

### A new dictionary from an old one

Another way to leave a dictionary as it was is to build a new one from it. Start with an empty dictionary, and store something worked out from each entry:

```python
prices = {"apple": 0.5, "pear": 0.75}
doubled = {}
for item, price in prices.items():
    doubled[item] = price * 2
print(doubled)
print(prices)
```

Output:

```
{'apple': 1.0, 'pear': 1.5}
{'apple': 0.5, 'pear': 0.75}
```

The new key can be worked out from the old entry too. Here it is the name with a capital letter:

```python
scores = {"ada": 88, "grace": 92}
by_capital = {}
for name, score in scores.items():
    by_capital[name.title()] = score
print(by_capital)
```

Output:

```
{'Ada': 88, 'Grace': 92}
```

### Practice

7. Write a function `invert(original)` that gives back a new dictionary with the keys and values of `original` swapped: each value becomes a key, with its old key as its value. In this exercise, every value in `original` is different. So `invert({"one": "uno", "two": "dos"})` gives back `{"uno": "one", "dos": "two"}`.

> Split it: start an empty dictionary. Loop over the entries of `original` with `items()`, and store each key under its value. Give the new dictionary back.
> Check it: try the example. Then the awkward one: `{}`, which gives `{}`.

8. Here two keys share a value. Predict what this prints, then press Check.

```python
grades = {"Ada": "A", "Grace": "A", "Alan": "B"}
flipped = {}
for name, grade in grades.items():
    flipped[grade] = name
print(flipped)
```

### Try It

9. Write a function `remove_item(register, item)` that gives back a new register with one fewer `item`, and leaves `register` as it was. When the last one goes, its entry comes out. If `item` is not held, the new register has the same entries. Write it above the lines below, and keep them.

```python
register = {"umbrella": 3, "phone": 1}
print(remove_item(register, "umbrella"))
print(remove_item(register, "phone"))
print(remove_item(register, "hat"))
print(remove_item({}, "hat"))
print(register)
```

> Say it: a register and an item go in; a new register with one fewer of the item comes out, and the old one is not changed. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. make a copy of the register. 2. if the item is not in the copy, give the copy back. 3. if the copy holds exactly 1, take the entry out of the copy; otherwise, store one less. 4. give back the copy.
> Name it: the function and its parameters are named for you. What would you call the copy?
> Check it: the lines should be `{'umbrella': 2, 'phone': 1}`, `{'umbrella': 3}`, `{'umbrella': 3, 'phone': 1}`, `{}`, and last, the register as it started, `{'umbrella': 3, 'phone': 1}`.

### What you can do now

- Copy a dictionary or a list with `copy()`, and copy an inner dictionary too before changing it.
- Loop over a copy of a dictionary to take entries out of it.
- Build a new dictionary from an old one, even with keys and values swapped.

Key words: **copy()**.
