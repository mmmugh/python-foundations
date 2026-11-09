<!-- Worked solutions for vol1-steps, one "## <page>#<n>" heading each. Never published. -->

## ch01a-printing#2

```python
print("I'm learning Python.")
```

The double quotes go around the outside, so the apostrophe is just one more character inside the string.

## ch01a-printing#4

```python
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
```

Two more rows, each one star longer than the row above it.

## ch01a-printing#6

```python
print("cats", "dogs", "fish")
```

## ch01a-printing#7

```python
print("Name:", "Ada")
print("School:", "Riverside Middle School")
print("Favorite subject:", "math")
```

Your answers will be different, and that is the point. Any three lines that start with those labels are right.

## ch01b-numbers-and-comments#3

```python
print(15 / 4)
```

Each friend gets 3.75 cookies. Python does not know cookies come whole; it just divides.

## ch01b-numbers-and-comments#4

```python
print(7 * 24 * 60)
```

Days times hours in a day gives the hours in a week; times 60 gives the minutes.

## ch01b-numbers-and-comments#6

```python
print("12 / 5 =", 12 / 5)
```

The part in quotes is printed as written. The part without quotes is worked out.

## ch01b-numbers-and-comments#8

```python
# seats on one bus: 12 rows of 4
print(12 * 4)
# seats on 3 of those buses
print(3 * 12 * 4)
```

The comments are not checked, but they are the part a reader thanks you for.

## ch01c-errors-and-a-receipt#3

```python
print("Good morning")
print("hi")
```

The last line of the error said `NameError: name 'Print' is not defined`. Python knows `print`, all lowercase, and nothing called `Print`. Capital letters matter.

## ch01c-errors-and-a-receipt#5

```python
print("CORNER STORE")
print()
print("Notebook 3.50")
print("Pens 2.25")
print("Stickers 1.75")
print()
print("Total", 3.50 + 2.25 + 1.75)
```

Yours can look different. What matters is a line for each item, and a total that Python works out rather than one you typed. However it went, read on: the next section is a way to start a problem like this.

## ch01c-errors-and-a-receipt#6

```python
# Say it: print a receipt for one popcorn, one drink and one pretzel,
# with a total that Python works out.
# Split it:
# 1. print the club's name
# 2. print a line for each item
# 3. print the total
print("RIVERSIDE FILM CLUB")
print()
print("Popcorn 3.75")
print("Drink 3.00")
print("Pretzel 2.50")
print()
print("Total", 3.75 + 3.00 + 2.50)
```

Your words can differ. What matters is a comment for each step, and a total that Python works out.

## ch02a-naming-a-value#3

```python
days = 7
print(days * 24)
```

## ch02a-naming-a-value#4

```python
total = 5
print(total)
```

Python runs top to bottom, so a name must get its value before anything uses it. The error said `NameError: name 'total' is not defined`, which means not defined *yet*.

## ch02a-naming-a-value#7

```python
# Say it: start with 5 coins, spend 2, find 4, show what is left.
# Split it:
# 1. start with 5 coins
# 2. spend 2
# 3. find 4 more
# 4. print the coins
coins = 5
coins = coins - 2
coins = coins + 4
print(coins)
```

## ch02b-names-and-kinds#5

```python
boxes = 3
pencils_per_box = 2
total_pencils = boxes * pencils_per_box
print(total_pencils)
```

Any names that say what each number is are right.

## ch02b-names-and-kinds#10

```python
# Say it: work out how many eggs 4 cakes need, at 3 eggs a cake.
# Split it:
# 1. store the eggs each cake needs
# 2. store how many cakes
# 3. multiply, and print the answer
eggs_per_cake = 3
cakes = 4
print(eggs_per_cake * cakes)
```

## ch02c-asking-the-user#3

```python
animal = input("What is your favorite animal? ")
print("I like", animal, "too!")
```

## ch02c-asking-the-user#4

```python
height = float(input("Height in inches: "))
print("That is", height / 12, "feet")
```

`int()` works too, for whole inches.

## ch02c-asking-the-user#5

```python
first = int(input("First number: "))
second = int(input("Second number: "))
print(first + second)
```

## ch02c-asking-the-user#7

```python
# Say it: ask for a movie's length in minutes, and show it in hours.
# Split it:
# 1. ask for the minutes, as a number
# 2. divide by 60
# 3. print the hours
minutes = int(input("How many minutes is the movie? "))
hours = minutes / 60
print("That is", hours, "hours")
```

45 gives 0.75 hours, which is right: three quarters of an hour.

## ch02d-putting-it-together#3

```python
# Say it: ask who the customer is, then print a receipt whose total
# is worked out from the prices, each stored once.
# Split it:
# 1. ask for the customer's name and print it
# 2. store each price in a variable
# 3. print a line for each item
# 4. work out the total from the variables and print it
customer = input("Customer name: ")
print("Customer:", customer)
```

## ch02d-putting-it-together#4

```python
# Say it: ask who the customer is, then print a receipt whose total
# is worked out from the prices, each stored once.
# Split it:
# 1. ask for the customer's name and print it
# 2. store each price in a variable
# 3. print a line for each item
# 4. work out the total from the variables and print it
customer = input("Customer name: ")
print("Customer:", customer)

notebook_price = 3.50
pens_price = 2.25
stickers_price = 1.75

print("Notebook", notebook_price)
print("Pens", pens_price)
print("Stickers", stickers_price)
```

## ch02d-putting-it-together#5

```python
# Say it: ask who the customer is, then print a receipt whose total
# is worked out from the prices, each stored once.
# Split it:
# 1. ask for the customer's name and print it
# 2. store each price in a variable
# 3. print a line for each item
# 4. work out the total from the variables and print it
customer = input("Customer name: ")
print("Customer:", customer)

notebook_price = 3.50
pens_price = 2.25
stickers_price = 1.75

print("Notebook", notebook_price)
print("Pens", pens_price)
print("Stickers", stickers_price)

total = notebook_price + pens_price + stickers_price
print("Total", total)
```

## ch02d-putting-it-together#7

```python
# Say it: ask who the customer is, then print a receipt whose total
# is worked out from the prices, each stored once.
# Split it:
# 1. ask for the customer's name and print it
# 2. store each price in a variable, the ruler's too
# 3. print a line for each item, the ruler's too
# 4. work out the total from the variables and print it
customer = input("Customer name: ")
print("Customer:", customer)

notebook_price = 3.50
pens_price = 2.25
stickers_price = 1.75
ruler_price = 1.25

print("Notebook", notebook_price)
print("Pens", pens_price)
print("Stickers", stickers_price)
print("Ruler", ruler_price)

total = notebook_price + pens_price + stickers_price + ruler_price
print("Total", total)
```

The ruler needed three changes, one for each step it touches: its price, its line, and its place in the total.

## ch03a-more-arithmetic#4

```python
minutes = 135
print(minutes // 60, "hours and", minutes % 60, "minutes")
```

60 goes into 135 twice, with 15 left over: 2 hours and 15 minutes.

## ch03a-more-arithmetic#5

```python
side = 9
print(side ** 2)
```

`side * side` gives the same answer; `**` is the shorter way to say it.

## ch03a-more-arithmetic#7

```python
# Say it: turn a number of seconds into minutes and seconds.
# Split it:
# 1. ask for the seconds, as a whole number
# 2. work out the whole minutes
# 3. work out the seconds left over
# 4. print both
total_seconds = int(input("How many seconds? "))
minutes = total_seconds // 60
seconds_left = total_seconds % 60
print(minutes, "minutes and", seconds_left, "seconds")
```

It is how many whole, how many left, with 60 seconds in each minute. 59 gives 0 minutes and 59 seconds, and 0 gives 0 and 0: both make sense.
