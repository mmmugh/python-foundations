<!-- part: Unit 6 — Functions -->
## Lesson 6.1 — Making your own function

You have used functions since lesson 1.1: `print()`, `input()`, `int()` and `range()` are all functions, written by someone else. In this lesson you write your own, and give them values to work with.

### Warm-up

1. Predict what this prints, then press Check.

```python
total = 0
for number in range(1, 5):
    if number == 2:
        continue
    total += number
print(total)
```

2. Before a loop, `found = False`. Inside it, `found = True` when a letter matches. After the loop, an `if` reads it. What is `found` called?

### The same lines, again

A game prints its title at the start of every round:

```python
print("==========")
print("SPACE QUEST")
print("==========")
print("Round 1 begins.")
print("==========")
print("SPACE QUEST")
print("==========")
print("Round 2 begins.")
```

The same three lines appear twice. To change the title, you would have to change it in two places, and with ten rounds, in ten. A **function** gives some lines a name. Then you run them whenever you like, by using the name:

```python
def banner():
    print("==========")
    print("SPACE QUEST")
    print("==========")

banner()
print("Round 1 begins.")
banner()
print("Round 2 begins.")
```

Output:

```
==========
SPACE QUEST
==========
Round 1 begins.
==========
SPACE QUEST
==========
Round 2 begins.
```

`def` starts the function. It is short for define. After it come the name, empty brackets and a colon, then an indented block, as with `if` and `while`.

**Defining** a function stores its lines under the name. It does not run them. **Calling** the function, by writing its name with brackets, `banner()`, runs the whole block. Each call runs it again.

So a `def` on its own prints nothing. Nor does the name without brackets:

```python
def banner():
    print("SPACE QUEST")

banner
```

This program prints nothing at all. The `def` only stores the line, and `banner` without brackets names the function without calling it. Only `banner()` runs it.

### Practice

3. Predict what this prints, then press Check.

```python
print("Ready")
def cheer():
    print("Go!")
    print("Go!")
print("Set")
cheer()
```

4. Which line runs the function `banner`?

5. Write a function `draw_line()` that prints ten dashes, `----------`. Then call it three times.

> Check it: three lines of ten dashes, and nothing else.

### Giving a function a value

`print()` takes a value in its brackets and uses it. Your functions can take one too:

```python
def welcome(player):
    print(f"Welcome aboard, {player}!")

welcome("Ada")
welcome("Grace")
```

Output:

```
Welcome aboard, Ada!
Welcome aboard, Grace!
```

`player`, in the `def` line, is a **parameter**: a variable that gets its value from the call. The value in the call, like `"Ada"`, is an **argument**. On the first call, `player` holds `"Ada"`. On the second, it holds `"Grace"`.

A function can have several parameters, with commas between them. The arguments are matched to them in order: the first argument goes to the first parameter, the second to the second.

```python
def describe(width, height):
    print(f"{width} wide and {height} tall")

describe(7, 4)
describe(4, 7)
```

Output:

```
7 wide and 4 tall
4 wide and 7 tall
```

A call needs one argument for each parameter. Leave one out, and Python stops:

```python
def welcome(player):
    print(f"Welcome aboard, {player}!")

welcome()
```

The last line of the error says `TypeError: welcome() missing 1 required positional argument: 'player'`. (Positional is Python's word for matched by position; you don't need to remember it.)

### Practice

6. Predict what this prints, then press Check.

```python
def label(item, price):
    print(f"{item}: ${price}")

label("pen", 2)
label(5, "book")
```

7. With `def welcome(player):` as above, what does `welcome("Ada", "Bo")` do?

8. Write a function `show_square(number)` that prints a number and its square, like `7 squared is 49`. Then ask for a whole number, and call your function with it.

> Split it: first the `def` and its block; then, below it and not indented, the `input()` line and the call.
> Check it: try 7, which is 49. Then the awkward ones: 0, and -3, which is 9.

### Try It

9. Write a function `greet(name)` that prints `Hello, Ada!` for the name Ada. If the name is empty, it prints `Hello, stranger!` instead. Then ask for a name, and call `greet()` with it.

> Say it: a name goes in; a greeting comes out, and an empty name gets a greeting too. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: in the function, if the name is empty, print the stranger line; otherwise print the hello line. Below the function, ask for a name, then call `greet()` with it.
> Name it: the function and its parameter are named for you. What would you call the name that was typed?
> Check it: try Ada. Then the awkward one: press Enter without typing anything.

### What you can do now

- Give some lines a name with `def`, and run them by calling the name.
- Give a function values to work with, through its parameters.
- Match arguments to parameters, in order.

Key words: **function**, **define**, **call**, **parameter**, **argument**.
