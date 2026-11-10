<!-- part: Unit 9 — Dictionaries and sets -->
## Lesson 9.2 — When a key might be missing

A program that asks for a name cannot know what will be typed. In lesson 9.1, a key that was not there stopped the program with a `KeyError`. In this lesson you ask whether a key is there first, or use a lookup that never stops the program. Then you take an entry out.

### Warm-up

1. Predict what this prints, then press Check.

```python
stock = {"pens": 10, "pads": 4}
stock["pens"] = 8
stock["clips"] = 50
print(stock)
print(len(stock))
```

2. What happens when this runs?

```python
scores = {"Ada": 88}
print(scores["ada"])
```

### Is the key there?

`in`, from lesson 8.4, works on a dictionary too. It asks about the keys:

```python
scores = {"Ada": 88, "Grace": 92}
print("Ada" in scores)
print("Alan" in scores)
print(88 in scores)
print("Alan" not in scores)
```

Output:

```
True
False
False
True
```

88 is a value in `scores`, but not a key, so `88 in scores` is `False`. `not in` gives the opposite answer, as it does for text and lists.

With an `if`, the program looks the key up only when it is there, so it never meets a `KeyError`:

```python
scores = {"Ada": 88, "Grace": 92}
name = "Alan"
if name in scores:
    print(name, "scored", scores[name])
else:
    print("No score for", name)
```

Output:

```
No score for Alan
```

### Practice

3. Predict what this prints, then press Check.

```python
pets = {"cat": 2, "dog": 1}
print("dog" in pets)
print(2 in pets)
print("Cat" in pets)
print("fish" not in pets)
```

4. Write a function `price_of(prices, item)` that gives back the price of `item` in the dictionary `prices`, or 0 if `prices` does not have it.

> Split it: if `item` is a key of `prices`, give back its value. Otherwise, give back 0.
> Check it: try `{"apple": 0.5, "pear": 0.75}` with `"pear"`, which gives 0.75. Then the awkward ones: `"Apple"`, with a capital, which gives 0; and an empty dictionary, `{}`, which gives 0 for anything.

### A lookup that never stops the program

`get()` is a dictionary method that looks a key up without the risk of a `KeyError`:

```python
scores = {"Ada": 88, "Grace": 92}
print(scores.get("Ada"))
print(scores.get("Alan"))
print(scores.get("Alan", 0))
print(scores.get("Ada", 0))
```

Output:

```
88
None
0
88
```

If the key is there, `get()` gives back its value, just as the square brackets do. If it is not, `get()` gives back `None`, Python's value for "nothing at all" (lesson 6.2), and the program goes on. Put a second value in its brackets, and that is what comes back instead of `None`. It is called the **default**, and it is used only when the key is missing: Ada's score is still 88. So `price_of()` above can be one line, `return prices.get(item, 0)`.

### Practice

5. Predict what this prints, then press Check.

```python
colors = {"sky": "blue", "grass": "green"}
print(colors.get("sky"))
print(colors.get("sea"))
print(colors.get("sea", "unknown"))
print(colors.get("grass", "unknown"))
```

6. Some people go by a shorter name. Write a function `nickname(nicknames, name)` that gives back the nickname stored for `name` in `nicknames`, or `name` itself if there is none. So with `{"Katherine": "Kat", "Alexander": "Alex"}`, `"Katherine"` gives `"Kat"` and `"Bo"` gives `"Bo"`.

> Split it: one lookup with a default. The default can be any value, even the key you looked up.
> Check it: try `"Alexander"`, which gives `"Alex"`. Then the awkward ones: an empty dictionary, `{}`, which gives back the name as it is; and the name `""`, which gives `""`.

### Taking an entry out

`del`, then the dictionary's name with a key in square brackets, takes that entry out, key and value together:

```python
scores = {"Ada": 88, "Grace": 92, "Alan": 45}
del scores["Alan"]
print(scores)
```

Output:

```
{'Ada': 88, 'Grace': 92}
```

Taking out a key that is not there is a `KeyError`, like looking one up. When you are not sure the key is there, ask first:

```python
scores = {"Ada": 88}
name = "Bo"
if name in scores:
    del scores[name]
print(scores)
```

Output:

```
{'Ada': 88}
```

### Practice

7. Predict what this prints, then press Check.

```python
stock = {"pens": 3, "pads": 0, "clips": 9}
del stock["pads"]
print(stock)
print(len(stock))
print(stock.get("pads", 0))
```

8. A shop keeps a dictionary of how many of each item it holds. Write a function `take_one(stock, item)` that changes `stock` so it holds one fewer `item`, and gives back `stock`. When the last one goes, its entry comes out: an item held 0 times is not held. Taking an item that is not there changes nothing.

> Split it: 1. if `item` is not a key of `stock`, give back `stock` as it is. 2. if there is exactly 1, take the entry out with `del`. 3. otherwise, store one less under the key. Then give back `stock`.
> Check it: try `{"pens": 2, "pads": 1}` with `"pens"`, which gives `{"pens": 1, "pads": 1}`, and with `"pads"`, which gives `{"pens": 2}`. Then the awkward ones: `"caps"`, which is not there, and an empty dictionary, `{}`.

### Try It

9. Ask for a name. If it is in the phone book, print the name and its number, as `Ada: 555-0100`. If it is not, print `No number for Bo.`, with the name that was typed in.

```python
phone_book = {"Ada": "555-0100", "Grace": "555-0142", "Lee": "555-0199"}
```

> Say it: a name goes in; its number comes out, or a message if the book does not have that name. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. ask for the name. 2. if the name is a key of the book, print it and its number. 3. otherwise, print the message.
> Name it: the book is named for you. What would you call the name that was typed in?
> Check it: try `Ada`, which prints `Ada: 555-0100`, and `Bo`, which prints `No number for Bo.` Then the awkward ones: `ada`, with a small a, and pressing Enter without typing anything. Neither is a key, so both get the message.

### What you can do now

- Ask whether a dictionary has a key, with `in` and `not in`.
- Look a key up with `get()`, which gives back `None` or a default instead of stopping.
- Take an entry out with `del`, after asking whether it is there.

Key words: **get()**, **default**, **del**.
