<!-- part: Unit 6 — Functions -->
## Lesson 6.5 — Splitting a problem into functions

In lessons 2.4, 4.5 and 5.7, you split a problem into steps, wrote them as comments, and built them one at a time. Now a step can become a function: a name for that step, which you check on its own before you build the next. In this lesson you do that from nothing but a problem's sentence.

### Warm-up

1. Predict what this prints, then press Check.

```python
def square(number):
    return number * number

def double_square(number):
    return square(number) * 2

print(double_square(3))
```

2. What does `greet("Bo")` print?

```python
def greet(name, greeting="Hi"):
    print(f"{greeting}, {name}!")
```

### A step becomes a function

Here is a problem: "Ask for the width and the length of a room, in whole meters, and print its area. If someone types something that is not a whole number, ask again." Say it and Split it come first, as always:

```python
# Say it: ask for a room's width and length, and print its area.
# Split it:
# 1. ask for the width, again until it is a whole number
# 2. ask for the length, the same way
# 3. work out the area
# 4. print it
```

Steps 1 and 2 are the same job, so they become one function, used twice: `get_whole_number(prompt)`, which gives back the number. Step 3 becomes `area(width, length)`. Build the first one, and check it on its own, before going on:

```python
def get_whole_number(prompt):
    """Ask until a whole number is typed, and give it back."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type a whole number.")

print(get_whole_number("Width: "))
```

A sample run:

```
Width: four
Please type a whole number.
Width: 4
4
```

`return` inside a loop ends the loop and the function at once. When `int()` fails, the `return` never happens: the `except` block prints the message, and the loop goes round to ask again. It is lesson 5.6's asking-until-good loop, inside a function.

Step 3 is one line. Last, one more function runs the whole program, calling the others in the order of the plan. By habit, it is called `main()`, and the program's last line calls it:

```python
# Say it: ask for a room's width and length, and print its area.
# Split it:
# 1. ask for the width, again until it is a whole number
# 2. ask for the length, the same way
# 3. work out the area
# 4. print it
def get_whole_number(prompt):
    """Ask until a whole number is typed, and give it back."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type a whole number.")

def area(width, length):
    """Give back the area of a rectangle."""
    return width * length

def main():
    width = get_whole_number("Width: ")
    length = get_whole_number("Length: ")
    print(f"The room is {area(width, length)} square meters.")

main()
```

A sample run:

```
Width: 4
Length: five
Please type a whole number.
Length: 5
The room is 20 square meters.
```

Read `main()` first: it is the plan from Split it, as code. Each line of it uses a name you can trust, because you checked that function on its own. Splitting a problem into functions like this is called **decomposition**.

### Practice

3. The room now needs its volume too. Add a function `volume(width, length, height)`. Then change `main()` so that it also asks for the height, and prints the volume, like `The room holds 60 cubic meters.`

```python
def get_whole_number(prompt):
    """Ask until a whole number is typed, and give it back."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type a whole number.")

def area(width, length):
    """Give back the area of a rectangle."""
    return width * length

def main():
    width = get_whole_number("Width: ")
    length = get_whole_number("Length: ")
    print(f"The room is {area(width, length)} square meters.")

main()
```

> Check it: try 3, 4 and 5, which is 60. Then a word for the height, which should be asked again.

### The grade calculator

Now a bigger problem, from its sentence alone:

A teacher types a student's name, then four scores. Each score must be a whole number from 0 to 100; anything else is asked for again. The program prints the student's average and letter grade: A for 90 and above, B for 80 and above, C for 70 and above, D for 60 and above, and F below 60.

### Practice

4. Say it and Split it: in this box, write the problem in your own words, then its steps, as comments. Next to each step that could be a function, write a name for it.

> Split it: which step is the same job, done four times? Which step takes one number and gives back one answer?

5. Step 1: write `letter_grade(average)`, which gives back the letter for an average, as a string, like `"B"`.

> Split it: it has the shape of `ticket_price()` in lesson 6.2: one branch for each row of the rule, the highest first.
> Check it: try 95 and 85. Then the edges, 90 and 89.5. Then the awkward one: 0.

6. Step 2: write `get_score(prompt)`, which asks until a whole number from 0 to 100 is typed, and gives it back. Anything else gets `Please type a whole number from 0 to 100.` Below it, check it on its own with `print(get_score("Score: "))`.

> Split it: start from `get_whole_number()`. Inside the `try` block, return the number only if it is from 0 to 100; otherwise, print the message. The `except` block prints it too.
> Check it: try 105, then abc, then 92. Then the edges: 0 and 100 must be taken, and -1 must not.

7. Step 3: write `main()`. It asks for the student's name, uses `get_score()` four times, and `letter_grade()` once. It prints two lines, like `Ada: average 88.5` and `Grade: B`. Call `main()` on the last line. Copy your functions from steps 1 and 2 into this box first.

> Check it: try Ada with 88, 105, 92, 79 and 95: 105 is asked again, and the average is 88.5, a B. Then the awkward ones: four 100s, and four 0s.

### Searching with return

`return` inside a `for` loop ends it early too, which makes a search short. This function looks through a word for a letter, and gives back `True` at the first match:

```python
def has_letter(word, letter):
    for character in word:
        if character == letter:
            return True
    return False

print(has_letter("rhythm", "y"))
print(has_letter("rhythm", "a"))
```

Output:

```
True
False
```

In lesson 5.7, the same search needed a flag and `break`. Here, `return True` ends the search as soon as it finds a match. `return False` is after the loop, not inside it. It runs only when the loop has looked at every letter and found none.

### Practice

8. Predict what this prints, then press Check. Look at where `return False` is.

```python
def has_letter(word, letter):
    for character in word:
        if character == letter:
            return True
        return False

print(has_letter("rhythm", "r"))
print(has_letter("rhythm", "y"))
```

### Try It

9. A prime number is a whole number above 1 that no whole number divides evenly, except 1 and itself: 2, 3, 5, 7, 11 and so on. Write `is_prime(number)`, which gives back `True` for a prime and `False` for anything else. Then use it to print every prime below 50.

> Say it: a whole number goes in; `True` comes out if it is prime, and `False` if not. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: what does prime mean, step by step? A number below 2 is not prime: return `False`. Try each number from 2 up to one less than the number: if it divides the number evenly (`%` gives 0), the number is not prime: return `False`. If the loop ends without finding one, return `True`, after the loop, as in `has_letter()`.
> Name it: what would you call the number you try dividing by?
> Check it: try 7 and 9. Then the awkward ones: 2, where the loop has nothing to try; 1, 0 and -7; and 49, which is 7 times 7.

### What you can do now

- Turn the steps of a plan into functions, and check each one on its own.
- Run a whole program from a `main()` function.
- Use `return` inside a loop, to stop as soon as the answer is known.

Key words: **decomposition**, **main()**.

That is the end of unit 6. Its quiz is below: fill it in, then show or print it.
