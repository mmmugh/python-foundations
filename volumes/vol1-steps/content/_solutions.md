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

## ch03a-more-arithmetic#8

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

## ch03b-order-and-rounding#8

```python
print(round(22 / 7, 3))
```

Python works out `22 / 7` inside the brackets first, then rounds the answer.

## ch03b-order-and-rounding#9

```python
# Say it: work out the average of three test scores, to 1 decimal place.
# Split it:
# 1. ask for each score, as a number
# 2. add them up, then divide by 3
# 3. round to 1 place, and print it
first_score = int(input("First score: "))
second_score = int(input("Second score: "))
third_score = int(input("Third score: "))
average = (first_score + second_score + third_score) / 3
print("Average:", round(average, 1))
```

The parentheses matter: without them, Python would divide only the third score by 3. Three zeros give 0.0, which is right.

## ch03c-formatting#5

```python
pet = input("Your pet's name: ")
print(f"Good morning, {pet}!")
```

## ch03c-formatting#7

```python
price = 4.5
print(f"${price:.2f}")
```

## ch03c-formatting#8

```python
# Say it: work out what some items cost, and show it as dollars and cents.
# Split it:
# 1. ask for the price of one item, as a decimal number
# 2. ask how many, as a whole number
# 3. multiply them
# 4. print the total with two decimal places
price = float(input("Price of one item: "))
how_many = int(input("How many? "))
total = price * how_many
print(f"Total: ${total:.2f}")
```

0 items gives `Total: $0.00`, which is right: nothing bought, nothing to pay.

## ch03d-joining-text#5

```python
print("#" * 20)
print("#" * 20)
print("#" * 20)
print("#" * 20)
print("#" * 20)
```

Every row is the same, so every line is the same.

## ch03d-joining-text#7

```python
age = 13
print("Age: " + str(age))
```

`str()` turns 13 into the text `"13"`, which `+` can join. `print(f"Age: {age}")` works too.

## ch03d-joining-text#8

```python
# Say it: say how old someone will be next year, in one sentence.
# Split it:
# 1. ask for the name
# 2. ask for the age, as a whole number
# 3. add 1, and turn the answer into text
# 4. join the pieces with + and print
name = input("Name: ")
age = int(input("Age: "))
next_age = age + 1
print("Next year, " + name + " will be " + str(next_age) + ".")
```

`str()` is needed because `next_age` is a number, and `+` joins only text to text. With 0, it prints `Next year, Bo will be 1.`, which makes sense.

## ch03e-comparing#7

```python
score = 10
print(score == 10)
```

One `=` stores; two ask. The error said `print()` got something it did not expect: an instruction to store, where a question belonged.

## ch03e-comparing#9

```python
# Say it: say whether a whole number is even, as True or False.
# Split it:
# 1. ask for the number, as a whole number
# 2. find the remainder when it is divided by 2
# 3. ask whether that remainder is 0, and print the answer
number = int(input("Whole number: "))
remainder = number % 2
print(remainder == 0)
```

A number is even when 2 goes into it with nothing left over. 0 is even, and prints `True`; -3 is odd, and prints `False`.

## ch03f-combining-and-change#7

```python
# Say it: ask for an amount in cents, and show how to pay it
# with the fewest quarters, dimes, nickels and pennies.
cents = int(input("Amount in cents: "))
print(f"{cents} cents is ${cents / 100:.2f}")
```

There are 100 cents in a dollar, so dividing by 100 gives dollars.

## ch03f-combining-and-change#8

```python
# Say it: ask for an amount in cents, and show how to pay it
# with the fewest quarters, dimes, nickels and pennies.
cents = int(input("Amount in cents: "))
print(f"{cents} cents is ${cents / 100:.2f}")

quarters = cents // 25
cents_left = cents % 25
print(f"Quarters: {quarters}, leaving {cents_left} cents")
```

It is how many whole, how many left, with 25 cents in each quarter.

## ch03f-combining-and-change#9

```python
# Say it: ask for an amount in cents, and show how to pay it
# with the fewest quarters, dimes, nickels and pennies.
# Split it:
# 1. ask for the cents, and show them in dollars
# 2. as many quarters as fit, and keep what is left
# 3. as many dimes as fit in that, and keep what is left
# 4. as many nickels as fit in that; what is left is pennies
# 5. print each coin, then the total number of coins
cents = int(input("Amount in cents: "))
print(f"{cents} cents is ${cents / 100:.2f}")

quarters = cents // 25
cents_left = cents % 25

dimes = cents_left // 10
cents_left = cents_left % 10

nickels = cents_left // 5
pennies = cents_left % 5

print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")
print(f"Total coins: {quarters + dimes + nickels + pennies}")
```

Each coin is the same two lines: `//` takes as many as fit, and `%` keeps what is left for the next coin. Taking the biggest coin first is what makes the number of coins the fewest. 0 cents gives 0 of everything, which is right.
