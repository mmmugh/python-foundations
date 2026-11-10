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

## ch01-practice#1

```python
print("======================================")
print("         RIVERSIDE FILM CLUB")
print("======================================")
```

Copying the lines from the flyer is the easy way to get 38 equals signs and nine spaces exactly right.

## ch01-practice#2

```python
print("Feature:  The Quiet Harbor  (1998)")
```

One string, spaces and all, exactly as it should look.

## ch01-practice#3

```python
print("Feature:", "The Quiet Harbor  (1998)")
```

The comma always puts in exactly one space. When the spacing matters, put the spaces inside the string, as in step 2.

## ch01-practice#4

```python
print("When:     Friday, 7:30 pm")
print("Where:    Room 14")
```

The words line up because the spaces are inside the strings: five after `When:`, four after `Where:`.

## ch01-practice#5

```python
print("Seats available:", 8 * 12)
```

`8 * 12` rather than 96: if the room gets another row, you change one number and Python does the rest. The comma puts in the space after the colon.

## ch01-practice#6

```python
print("Popcorn for 3:", 3 * 3.75)
```

The calculation is worked out before `print()` shows it.

## ch01-practice#7

```python
# Say it: print the film club's flyer for Friday, with the seats
# and the popcorn price worked out by Python.
# Split it:
# 1. print the top: the line, the club's name, the line
# 2. print the feature, when and where
# 3. print the seats and the popcorn
# 4. print the line at the bottom
print("======================================")
print("         RIVERSIDE FILM CLUB")
print("======================================")
print()
print("Feature:  The Quiet Harbor  (1998)")
print("When:     Friday, 7:30 pm")
print("Where:    Room 14")
print()
print("Seats available:", 8 * 12)
print("Popcorn for 3:", 3 * 3.75)
print()
print("======================================")
```

Your comments can say it in your own words. What matters is a comment for each part, the blank lines from an empty `print()`, and the two numbers worked out by Python.

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


## ch02-practice#1

```python
trail = "Kettle Ridge"
distance_km = 12.4
print(trail, "is", distance_km, "km")
```

Each comma puts in one space, so there are no spaces inside the strings.

## ch02-practice#2

```python
trail = "Kettle Ridge"
distance_km = 12.4
pace = float(input("Pace, in minutes per km? "))
minutes = distance_km * pace
print("That takes", minutes, "minutes")
```

`float()`, not `int()`, because a pace can be 10.5, and `int()` cannot turn the text `10.5` into a whole number. Without either one, Python is asked to multiply a number by a piece of text, and stops.

## ch02-practice#3

```python
trail = "Kettle Ridge"
distance_km = 12.4
pace = float(input("Pace, in minutes per km? "))
minutes = distance_km * pace
hours = minutes / 60
print("That takes", minutes, "minutes")
print("That is", hours, "hours")
```

Sixty minutes make an hour, so the hours are the minutes divided by 60. The answer has a lot of decimal places, and that is fine for now.

## ch02-practice#4

```python
trail = "Kettle Ridge"
distance_km = 12.4
pace = float(input("Pace, in minutes per km? "))
minutes = distance_km * pace
hours = minutes / 60
water = hours * 0.75
print("That takes", minutes, "minutes")
print("That is", hours, "hours")
print("Water for one person:", water, "liters")
```

It is 0.75 for each hour, so it multiplies the hours. Multiplying the minutes asks for over 100 liters, which is a clue that the wrong variable went in.

## ch02-practice#5

```python
trail = "Kettle Ridge"
distance_km = 12.4
pace = float(input("Pace, in minutes per km? "))
minutes = distance_km * pace
people = int(input("How many people? "))
hours = minutes / 60
water = hours * 0.75
print("That takes", minutes, "minutes")
print("That is", hours, "hours")
print("Water for one person:", water, "liters")
print("Water for the group:", water * people, "liters")
```

`int()` for a number of people, since nobody brings half a walker.

## ch02-practice#6

```python
trail = "Kettle Ridge"
distance_km = 12.4
pace = float(input("Pace, in minutes per km? "))
minutes = distance_km * pace
people = int(input("How many people? "))
hours = minutes / 60
water = hours * 0.75
print("That takes", minutes, "minutes")
print("That is", hours, "hours")
print("Water for one person:", water, "liters")
print("Water for the group:", water * people, "liters")
print("Permits:", 4.50 * people)
```

The permits read the same `people` variable as the water, so the number is typed in once and used twice.

## ch02-practice#7

```python
# Say it: ask for the trail length, the pace and the group size, then
# print the time, the water and the permits for the day.
# Split it:
# 1. ask for the length, the pace and how many people
# 2. work out the minutes, the hours and the water for one person
# 3. print each line of the plan
distance_km = float(input("Trail length, in km? "))
pace = float(input("Pace, in minutes per km? "))
people = int(input("How many people? "))

minutes = distance_km * pace
hours = minutes / 60
water = hours * 0.75

print("Length:", distance_km, "km")
print("Time:", minutes, "minutes")
print("Time:", hours, "hours")
print("Water for one person:", water, "liters")
print("Water for the group:", water * people, "liters")
print("Permits:", 4.50 * people)
```

Every number on the plan comes from the three that were typed in, so the planner works for any trail. With 0 people, the group needs no water and no permits, which makes sense.

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

## ch03-practice#1

```python
pizzas = int(input("How many pizzas? "))
people = int(input("How many people? "))
slices = pizzas * 8
print("Slices:", slices)
```

`int()` on both answers. Without it, `pizzas` is text, and `"2" * 8` is `22222222`, which is a lot of pizza.

## ch03-practice#2

```python
pizzas = int(input("How many pizzas? "))
people = int(input("How many people? "))
slices = pizzas * 8
slices_each = slices // people
slices_left = slices % people
print("Slices:", slices)
print("Slices each:", slices_each)
print("Slices left over:", slices_left)
```

`//` says how many whole slices each person gets, and `%` says how many are left. With 1 pizza and 10 people, each gets 0 and all 8 are left.

## ch03-practice#3

```python
pizzas = int(input("How many pizzas? "))
people = int(input("How many people? "))
slices = pizzas * 8
slices_each = slices // people
slices_left = slices % people
print("Slices:", slices)
print("Slices each:", slices_each)
print("Slices left over:", slices_left)
print("Any left over?", slices_left > 0)
```

A comparison is a value, so `print()` can show it. `slices_left != 0` is just as right.

## ch03-practice#4

```python
pizzas = int(input("How many pizzas? "))
people = int(input("How many people? "))
slices = pizzas * 8
slices_each = slices // people
slices_left = slices % people
print("Slices:", slices)
print("Slices each:", slices_each)
print("Slices left over:", slices_left)
print("Any left over?", slices_left > 0)
cost = pizzas * 13.50
print(f"Cost: ${cost:.2f}")
```

`:.2f` shows 27.0 as 27.00, the way money is written.

## ch03-practice#5

```python
pizzas = int(input("How many pizzas? "))
people = int(input("How many people? "))
tax_rate = float(input("Tax rate, as a percent? "))
slices = pizzas * 8
slices_each = slices // people
slices_left = slices % people
print("Slices:", slices)
print("Slices each:", slices_each)
print("Slices left over:", slices_left)
print("Any left over?", slices_left > 0)
cost = pizzas * 13.50
tax = cost * tax_rate / 100
total = cost + tax
print(f"Cost: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
```

The tax rate is asked for with `float()`, since 7.5 percent is a rate too. At 7.5 percent the tax is 3.0375, and `:.2f` shows it as 3.04.

## ch03-practice#6

```python
pizzas = int(input("How many pizzas? "))
people = int(input("How many people? "))
tax_rate = float(input("Tax rate, as a percent? "))
slices = pizzas * 8
slices_each = slices // people
slices_left = slices % people
print("Slices:", slices)
print("Slices each:", slices_each)
print("Slices left over:", slices_left)
print("Any left over?", slices_left > 0)
cost = pizzas * 13.50
tax = cost * tax_rate / 100
total = cost + tax
print(f"Cost: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
share = round(total / people, 2)
print("Each person owes:", share)
```

Split the total with the tax, not the cost: everybody pays their part of the tax too. `round(..., 2)` keeps 2 decimal places, and `:.2f` would show the same cents.

## ch03-practice#7

```python
# Say it: ask how many pizzas, how many people and the tax rate, then
# print a bill that splits the slices and the money evenly.
# Split it:
# 1. ask the three questions
# 2. work out the slices each and the slices left
# 3. work out the cost, the tax, the total and each share
# 4. print each line, with a line of - above the total
pizzas = int(input("How many pizzas? "))
people = int(input("How many people? "))
tax_rate = float(input("Tax rate, as a percent? "))

slices = pizzas * 8
slices_each = slices // people
slices_left = slices % people

cost = pizzas * 13.50
tax = cost * tax_rate / 100
total = cost + tax
share = total / people

print("Slices each:", slices_each)
print("Slices left over:", slices_left)
print("Any left over?", slices_left > 0)
print(f"Cost: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print("-" * 20)
print(f"Total: ${total:.2f}")
print(f"Each person owes: ${share:.2f}")
```

Every line comes from the three answers. With 0 people, Python stops with a `ZeroDivisionError` at `slices // people`: there is nobody to share between, so there is no answer.

## ch04a-if-and-else#8

```python
age = int(input("How old are you? "))
if age > 12:
    print("You are a teenager or older.")
else:
    print("You are 12 or younger.")
```

`input()` always gives back text, as in lesson 2.3, and `>` cannot compare text with a number. `int()` turns the text into a whole number first. `if int(age) > 12:` works too.

## ch04a-if-and-else#9

```python
# Say it: say whether a test score passes or fails.
# Split it:
# 1. ask for the score, as a whole number
# 2. if it is 50 or more, print Pass
# 3. otherwise, print Fail
score = int(input("Test score: "))
if score >= 50:
    print("Pass")
else:
    print("Fail")
```

`>=` is what makes exactly 50 a pass: with `>`, a score of 50 would fail. 0 fails, which is right.

## ch04b-elif-and-rules#5

```python
number = int(input("Whole number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
```

Three possibilities, so two tests and an `else`. Whatever is neither more than 0 nor less than 0 must be 0.

## ch04b-elif-and-rules#6

```python
first = int(input("First number: "))
second = int(input("Second number: "))
if first > second:
    print(f"Larger: {first}")
elif second > first:
    print(f"Larger: {second}")
else:
    print("Same")
```

The `else` catches the one case the two tests leave: neither number is larger, so they are equal. With -2 and -7, -2 is larger, and the program says so.

## ch04b-elif-and-rules#9

```python
# Say it: say whether a year is a leap year.
# Split it, narrowest clause first:
# 1. a multiple of 400 is a leap year
# 2. any other multiple of 100 is not
# 3. any other multiple of 4 is a leap year
# 4. every other year is not
year = int(input("Year: "))
if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("ordinary year")
elif year % 4 == 0:
    print("leap year")
else:
    print("ordinary year")
```

It is the raffle's shape with 4, 100 and 400. 2000 is a multiple of 400, so it is a leap year. 1900 is a multiple of 100 but not of 400, so it is not, even though 4 goes into it.

## ch04c-nesting-and-truthiness#9

```python
# Say it: let someone into the club if they give a name and are 13 or older.
# Split it:
# 1. ask for the name
# 2. ask for the age, as a whole number
# 3. if a name was typed:
#    welcome them if they are 13 or older, otherwise say sorry
# 4. if no name was typed, ask for one
name = input("Name: ")
age = int(input("Age: "))
if name:
    if age >= 13:
        print(f"Welcome, {name}!")
    else:
        print(f"Sorry, {name}, you must be 13.")
else:
    print("Please type your name.")
```

`if name:` is True whenever something was typed, because only the empty string counts as False. The age question is nested inside, so it only matters once there is a name. `>=` makes exactly 13 welcome.

## ch04d-checking-input#4

```python
score = int(input("Test score: "))
if score < 0 or score > 100:
    print("A score must be from 0 to 100.")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Grade: {grade}")
```

The check comes first, and the grading moves inside its `else`, one level deeper, so a bad score is never graded. 0 and 100 are real scores, so they still get a grade.

## ch04d-checking-input#7

```python
try:
    pets = int(input("How many pets? "))
    print(f"You have {pets} pets.")
except ValueError:
    print("Please type a whole number.")
```

Both lines go in the `try` block: the one that might fail, and the one that needs its answer.

## ch04d-checking-input#8

```python
# Say it: say how many days a month has, or ask for a real month.
# Split it:
# 1. in a try block, ask for the month, as a whole number
# 2. if it is outside 1 to 12, print the message
# 3. February has 28
# 4. April, June, September and November have 30
# 5. every other month has 31
# 6. if a word was typed, print the message
try:
    month = int(input("Month (1 to 12): "))
    if month < 1 or month > 12:
        print("Please type a month from 1 to 12.")
    elif month == 2:
        print("28 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30 days")
    else:
        print("31 days")
except ValueError:
    print("Please type a month from 1 to 12.")
```

The check comes first, so 0 and 13 never reach the days. The `else` catches the seven 31-day months, which is shorter than naming them all. A word stops `int()`, so Python jumps to the `except` block.

## ch04e-the-ticket-kiosk#3

```python
# Say it: work out the price of a cinema ticket from the
# customer's age and the day of the week.
age = int(input("Customer age: "))
if age < 5:
    price = 0
elif age <= 12:
    price = 8
elif age <= 64:
    price = 14
else:
    price = 10
print(f"Price: ${price}")
```

Each `elif` only has to check the top of its row, because Python stops at the first test that is True. Keeping the price in a variable, and printing it once at the end, leaves room for step 2.

## ch04e-the-ticket-kiosk#4

```python
# Say it: work out the price of a cinema ticket from the
# customer's age and the day of the week.
age = int(input("Customer age: "))
if age < 5:
    price = 0
elif age <= 12:
    price = 8
elif age <= 64:
    price = 14
else:
    price = 10

day = input("Day of the week: ")
if day == "Tuesday" and price > 0:
    price -= 3
print(f"Price: ${price}")
```

`price > 0` is the guard on the edge case: a free ticket is not a paying customer, so it gets no discount and stays at $0.

## ch04e-the-ticket-kiosk#5

```python
# Say it: work out the price of a cinema ticket from the
# customer's age and the day of the week, refusing an age
# the kiosk can't use.
# Split it:
# 1. in a try block, ask for the age, as a whole number
# 2. if it is outside 0 to 120, say so
# 3. otherwise, work out the price from the age,
#    ask for the day, take $3 off a paying Tuesday ticket,
#    and print the price
# 4. if the age was not a whole number, say so
try:
    age = int(input("Customer age: "))
    if age < 0 or age > 120:
        print("Please enter a realistic age.")
    else:
        if age < 5:
            price = 0
        elif age <= 12:
            price = 8
        elif age <= 64:
            price = 14
        else:
            price = 10

        day = input("Day of the week: ")
        if day == "Tuesday" and price > 0:
            price -= 3
        print(f"Price: ${price}")
except ValueError:
    print("Age must be a whole number.")
```

Step 2's program moved one level deeper, into the `else` block, and it did not otherwise change. That is what building one decision at a time looks like. A word or an unrealistic age never reaches the price, and a free ticket stays free on a Tuesday.

## ch04-practice#1

```python
wind = float(input("Wind speed, in mph? "))
if wind < 30:
    print("Wind: OK")
else:
    print("Wind: TOO STRONG")
```

`float()`, because the wind can have a decimal point. `<` rather than `<=`, because 30 exactly is too strong.

## ch04-practice#2

```python
temperature = float(input("Temperature, in degrees C? "))
if temperature >= 2 and temperature <= 35:
    print("Temperature: OK")
else:
    print("Temperature: OUT OF RANGE")
```

Both ends are allowed, so both tests have an `=` in them. `2 <= temperature <= 35` says the same thing, the way you would write it on paper.

## ch04-practice#3

```python
ceiling = int(input("Cloud ceiling, in feet? "))
if ceiling >= 5000:
    print("Ceiling: CLEAR")
elif ceiling >= 2000:
    print("Ceiling: MARGINAL")
else:
    print("Ceiling: TOO LOW")
```

5000 or more is the narrowest band, so it goes first. The other way round, `ceiling >= 2000` would catch 6000 too, and a clear sky would come out marginal.

## ch04-practice#4

```python
try:
    fuel = int(input("Fuel, in percent? "))
    if fuel < 0 or fuel > 100:
        print("Fuel: BAD READING")
    elif fuel >= 95:
        print("Fuel: OK")
    else:
        print("Fuel: LOW")
except ValueError:
    print("Fuel: BAD READING")
```

A word stops `int()`, and Python jumps to the `except` block. A number outside 0 to 100 gets through `int()`, so the `if` catches it first, before the fuel is judged.

## ch04-practice#5

```python
wind = float(input("Wind speed, in mph? "))
temperature = float(input("Temperature, in degrees C? "))
ceiling = int(input("Cloud ceiling, in feet? "))
try:
    fuel = int(input("Fuel, in percent? "))
    if fuel < 0 or fuel > 100:
        fuel_status = "BAD READING"
    elif fuel >= 95:
        fuel_status = "OK"
    else:
        fuel_status = "LOW"
except ValueError:
    fuel_status = "BAD READING"

if wind < 30 and 2 <= temperature <= 35 and ceiling >= 2000 and fuel_status == "OK":
    print("LAUNCH: GO")
else:
    print("LAUNCH: NO GO")
```

`and` is `True` only when every part is. A marginal ceiling is 2000 or more, so `ceiling >= 2000` lets it through. `fuel_status` has a value whichever way the fuel question went, so the verdict can always ask about it.

## ch04-practice#6

```python
wind = float(input("Wind speed, in mph? "))
temperature = float(input("Temperature, in degrees C? "))
ceiling = int(input("Cloud ceiling, in feet? "))
try:
    fuel = int(input("Fuel, in percent? "))
    if fuel < 0 or fuel > 100:
        fuel_status = "BAD READING"
    elif fuel >= 95:
        fuel_status = "OK"
    else:
        fuel_status = "LOW"
except ValueError:
    fuel_status = "BAD READING"

if wind < 30 and 2 <= temperature <= 35 and ceiling >= 2000 and fuel_status == "OK":
    print("LAUNCH: GO")
else:
    print("LAUNCH: NO GO")
    if wind >= 30:
        print("HOLD: wind")
    elif temperature < 2 or temperature > 35:
        print("HOLD: temperature")
    elif ceiling < 2000:
        print("HOLD: ceiling")
    else:
        print("HOLD: fuel")
```

The `HOLD:` lines sit inside the `else`, so a GO never reaches them. Python stops at the first test that is `True`, so only the first failure is named. If the wind, the temperature and the ceiling are all fine, the fuel must be what failed, so it is the `else`.

## ch04-practice#7

```python
# Say it: read the wind, temperature, ceiling and fuel; print a line for
# each, then whether the rocket can launch, and if not, what to fix first.
# Split it:
# 1. ask the four questions, keeping the fuel's word in a variable
# 2. print the wind, temperature and ceiling lines
# 3. print the fuel line
# 4. print the verdict
# 5. after a NO GO, print the first reading that failed
wind = float(input("Wind speed, in mph? "))
temperature = float(input("Temperature, in degrees C? "))
ceiling = int(input("Cloud ceiling, in feet? "))
try:
    fuel = int(input("Fuel, in percent? "))
    if fuel < 0 or fuel > 100:
        fuel_status = "BAD READING"
    elif fuel >= 95:
        fuel_status = "OK"
    else:
        fuel_status = "LOW"
except ValueError:
    fuel_status = "BAD READING"

if wind < 30:
    print("Wind: OK")
else:
    print("Wind: TOO STRONG")

if 2 <= temperature <= 35:
    print("Temperature: OK")
else:
    print("Temperature: OUT OF RANGE")

if ceiling >= 5000:
    print("Ceiling: CLEAR")
elif ceiling >= 2000:
    print("Ceiling: MARGINAL")
else:
    print("Ceiling: TOO LOW")

print(f"Fuel: {fuel_status}")

if wind < 30 and 2 <= temperature <= 35 and ceiling >= 2000 and fuel_status == "OK":
    print("LAUNCH: GO")
else:
    print("LAUNCH: NO GO")
    if wind >= 30:
        print("HOLD: wind")
    elif temperature < 2 or temperature > 35:
        print("HOLD: temperature")
    elif ceiling < 2000:
        print("HOLD: ceiling")
    else:
        print("HOLD: fuel")
```

Each reading is judged once for its own line, and again for the verdict. With 35, 40, 1000 and 50, everything fails, but the `elif` chain names only the wind, because it comes first.

## ch05a-while#4

```python
count = 1
while count <= 10:
    print(count)
    count += 1
```

Only the condition changes. The loop now stops once `count` is past 10, not past 5. `count < 11` works too.

## ch05a-while#6

```python
count = 1
number = 1
while count <= 3:
    number *= 2
    count += 1
print(number)
```

The loop had the first two parts but not the third: nothing moved `count`, so `count <= 3` stayed `True` forever. `count += 1` in the block moves it, one each pass, until it reaches 4. It has to be indented, so that it is part of the block.

## ch05a-while#7

```python
# Say it: count down from 5 to 1, then print Liftoff!
# Split it:
# 1. start the count at 5
# 2. while it is 1 or more: print it, then take 1 away
# 3. after the loop, print Liftoff!
countdown = 5
while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Liftoff!")
```

The count moves down this time, so the condition asks whether it is still 1 or more. With `countdown >= 0`, the loop would make one pass too many and print 0. `Liftoff!` is not indented, so it runs once, after the loop.

## ch05b-for-and-range#8

```python
number = int(input("Whole number: "))
for times in range(1, 13):
    print(f"{number} x {times} = {number * times}")
```

The table goes from 1 to 12, so the stop is 13: `range()` leaves its stop out.

## ch05b-for-and-range#9

```python
# Say it: print the squares of 1 to 10, one per line.
# Split it:
# 1. loop over the numbers 1 to 10
# 2. print each one times itself
for number in range(1, 11):
    print(number * number)
```

`range(1, 11)` starts at 1, not 0, and stops just before 11, so the last square is 10 times 10, which is 100. `number ** 2` works too.

## ch05c-looping-over-text#6

```python
word = input("Word: ")
count = 0
for letter in word:
    if letter == "s":
        count += 1
print(f"s: {count}")
```

The `print()` is not indented, so it runs once, after the loop. Indented, it would print a count on every pass. A capital `S` is a different character, so `Sam` has no small `s`.

## ch05c-looping-over-text#7

```python
# Say it: print a word one letter per line, then how many vowels it has.
# Split it:
# 1. ask for the word
# 2. start the vowel count at 0
# 3. for each letter: print it; if it is a vowel, add 1
# 4. after the loop, print the count
word = input("Word: ")
vowels = 0
for letter in word:
    print(letter)
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels += 1
print(f"Vowels: {vowels}")
```

The printing and the counting share one loop: on each pass, the letter is printed, and then the `if` decides whether it counts. `rhythm` has no vowels, so the count stays at 0, and the program still says so.

## ch05d-loops-inside-loops#8

```python
# Say it: print every pair of dice that adds up to a total.
# Split it:
# 1. ask for the total, as a whole number
# 2. loop over the first die, 1 to 6
# 3.   inside it, loop over the second die, 1 to 6
# 4.     if the two add up to the total, print the pair
total = int(input("Total: "))
for first_die in range(1, 7):
    for second_die in range(1, 7):
        if first_die + second_die == total:
            print(f"{first_die} + {second_die}")
```

The inner loop tries all six faces of the second die for each face of the first, so all 36 pairs are tried, and the `if` lets through only those that add up. A die goes up to 6, so the stop is 7. With 13, no pair adds up, and nothing is printed, which is right.

## ch05e-adding-up#6

```python
coldest = int(input("Temperature: "))
for day in range(2):
    temperature = int(input("Temperature: "))
    if temperature < coldest:
        coldest = temperature
print(f"The coldest was {coldest}.")
```

It is the largest-so-far fix, turned around. Starting at 0, no temperature above 0 could ever be colder, so 0 won. Starting from the first temperature, the coldest so far is one that was really typed. The loop then reads the other two, so it is `range(2)`.

## ch05e-adding-up#7

```python
# Say it: add up the points of four rounds, and find the highest round.
# Split it:
# 1. ask for the first round's points: the total and the highest so far
# 2. for the other three rounds:
#    ask for the points, add them to the total,
#    and keep them as the highest if they beat it
# 3. after the loop, print the total, then the highest
points = int(input("Points: "))
total = points
highest = points
for round_number in range(3):
    points = int(input("Points: "))
    total += points
    if points > highest:
        highest = points
print(f"Total: {total}")
print(f"Highest: {highest}")
```

Both accumulators start from the first round, so the highest is always a score someone really got. With -3, -8, -1 and -4, the highest is -1; starting from 0, it would have said 0. The two `print()` lines are not indented, so they run once, after the loop.

## ch05f-until-a-stop-value#5

```python
name = input("Name (or stop): ")
while name != "stop":
    print(f"Hello, {name}!")
    name = input("Name (or stop): ")
```

Read, loop, read again, as in the words program. `stop` never reaches the greeting, because the condition sees it first.

## ch05f-until-a-stop-value#6

```python
month = int(input("Month (1 to 12): "))
while month < 1 or month > 12:
    print("Please type a month from 1 to 12.")
    month = int(input("Month (1 to 12): "))
print(f"Month: {month}")
```

The condition is the range check from lesson 4.4, and it keeps the loop going while the month is bad. 1 and 12 are real months, so the tests are `<` and `>`.

## ch05f-until-a-stop-value#9

```python
# Say it: add up numbers until 0, and count how many there were.
# Split it:
# 1. start the total and the count at 0
# 2. read the first number
# 3. while it is not 0: add it to the total, add 1 to the count,
#    and read the next number
# 4. after the loop, print the total, then the count
total = 0
count = 0
number = int(input("Number (0 to stop): "))
while number != 0:
    total += number
    count += 1
    number = int(input("Number (0 to stop): "))
print(f"Total: {total}")
print(f"Count: {count}")
```

The stop value is a number this time, so `int()` can go on the `input()` lines. The 0 is checked before it is counted, so it is never added or counted. With 0 first, the block never runs, and both are 0.

## ch05g-the-guessing-game#3

```python
secret = 7
guesses = 0
while True:
    guess = int(input("Guess: "))
    guesses += 1
    if guess == secret:
        break
print(f"Correct! Guesses: {guesses}")
```

The count goes up before the test, so the right guess is counted too. Nobody knows how many guesses it will take, so it is a `while` loop, and `break` ends it at the right guess.

## ch05g-the-guessing-game#4

```python
secret = 7
guesses = 0
while True:
    guess = int(input("Guess: "))
    guesses += 1
    if guess == secret:
        break
    elif guess > secret:
        print("Too high.")
    else:
        print("Too low.")
print(f"Correct! Guesses: {guesses}")
```

Three possibilities, so `if`, `elif` and `else`, as in lesson 4.2. A right guess reaches `break` first, so it never gets a hint.

## ch05g-the-guessing-game#6

```python
secret = 7
guesses = 0
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        print("Please type a whole number.")
        continue
    guesses += 1
    if guess == secret:
        break
    elif guess > secret:
        print("Too high.")
    else:
        print("Too low.")
print(f"Correct! Guesses: {guesses}")
```

`continue` skips the rest of the pass, so a word never reaches `guesses += 1`. Where that line sits is a rule of the game: after the check, a slip is free; before it, a slip would cost a guess.

## ch05g-the-guessing-game#9

```python
# Say it: a guessing game with at most 5 guesses, which says how it ended.
# Split it:
# 1. the secret, a count of guesses, and a flag for a win
# 2. while fewer than 5 guesses have been counted:
#    ask; skip a word without counting it; count the guess;
#    if it is right, set the flag and stop; otherwise, say too high or too low
# 3. after the loop: the Correct line if the flag is set,
#    otherwise the out-of-guesses line
secret = 7
guesses = 0
won = False
while guesses < 5:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        print("Please type a whole number.")
        continue
    guesses += 1
    if guess == secret:
        won = True
        break
    elif guess > secret:
        print("Too high.")
    else:
        print("Too low.")
if won:
    print(f"Correct! Guesses: {guesses}")
else:
    print(f"Out of guesses. It was {secret}.")
```

The loop can end two ways: `break` on a right guess, or the count reaching 5. `won` remembers which. `guesses < 5` lets exactly 5 guesses through: with `<=`, the player would get 6. Using `{secret}` in the last line means it stays right when the secret is random.

## ch05-practice#1

```python
for week in range(1, 9):
    print(f"Week {week}")
```

`range(1, 9)` starts at 1 and stops just before 9, so it gives the 8 week numbers.

## ch05-practice#2

```python
amount = int(input("How much do you save each week? "))
total = 0
for week in range(1, 9):
    total += amount
    print(f"Week {week}: {total}")
```

`total` is an accumulator: set up before the loop, added to on each pass, and printed as it grows. An amount of 0 gives eight lines of 0, which is right.

## ch05-practice#3

```python
amount = int(input("How much do you save each week? "))
total = 0
for week in range(1, 9):
    total += amount
    if week % 4 == 0:
        total += 10
    print(f"Week {week}: {total}")
```

`week % 4 == 0` is `True` only in weeks 4 and 8. `week % 4 == 1` would pay the bonus in weeks 1 and 5 instead, and week 1's total would already be wrong.

## ch05-practice#4

```python
saved = int(input("How much have you saved already? "))
amount = int(input("How much do you save each week? "))
weeks = 0
while saved < 240:
    saved += amount
    weeks += 1
print(f"Weeks: {weeks}")
```

The condition asks before every pass, so with 240 already, the block never runs and the count stays at 0. `saved < 240` keeps going while the goal is not yet reached, so landing on exactly 240 stops it.

## ch05-practice#5

```python
saved = 0
weeks = 0
amount = int(input("Saved this week (0 to stop)? "))
while amount != 0:
    saved += amount
    weeks += 1
    print(f"Saved: {saved}")
    amount = int(input("Saved this week (0 to stop)? "))
print(f"Weeks: {weeks}")
```

Read, loop, read again. The 0 is the stop value, not a week: the condition sees it first, so it is never added or counted. A 0 straight away gives `Weeks: 0`.

## ch05-practice#6

```python
saved = 0
week = 0
while True:
    amount = int(input("Saved this week (0 to stop)? "))
    if amount == 0:
        break
    saved += amount
    week += 1
    print(f"Saved: {saved}")
    if saved >= 240:
        break
if saved >= 240:
    print(f"Goal reached in week {week}!")
else:
    print(f"Still to save: {240 - saved}")
```

There are two ways out of the loop, a 0 or the goal, and each has a `break`. After the loop, `saved >= 240` says which one it was.

## ch05-practice#7

```python
# Say it: start from what is saved already, add a week's savings at a time,
# and say when the total reaches 240, or how much is still needed.
# Split it:
# 1. ask what is saved already
# 2. if it is 240 or more, say so, and stop there
# 3. otherwise, loop: read a week's savings; stop at a 0;
#    add it, count the week, print the total; stop at the goal
# 4. after the loop, the goal line or the still-to-save line
saved = int(input("How much have you saved already? "))
if saved >= 240:
    print("Goal reached already!")
else:
    week = 0
    while True:
        amount = int(input("Saved this week (0 to stop)? "))
        if amount == 0:
            break
        saved += amount
        week += 1
        print(f"Saved: {saved}")
        if saved >= 240:
            break
    if saved >= 240:
        print(f"Goal reached in week {week}!")
    else:
        print(f"Still to save: {240 - saved}")
```

Step 6's program moved into the `else` block, one level deeper, and `saved` now starts from what was typed instead of 0. With 240 already, the loop never starts, so nothing more is asked.

## ch06a-defining#5

```python
def draw_line():
    print("----------")


draw_line()
draw_line()
draw_line()
```

The `def` stores the line, and each of the three calls runs it. The calls are not indented: indented, they would be part of the function's block, and nothing would ever call it.

## ch06a-defining#8

```python
def show_square(number):
    print(f"{number} squared is {number * number}")


typed = int(input("Whole number: "))
show_square(typed)
```

The call hands the typed number to the function, and `number` holds it while the block runs. `number ** 2` works too. A number below 0, times itself, is above 0, so -3 gives 9.

## ch06a-defining#9

```python
# Say it: greet a person by name, or greet a stranger
# if no name was typed.
# Split it:
# 1. the function: if the name is empty, print the stranger line;
#    otherwise print the hello line
# 2. ask for a name
# 3. call the function with it
def greet(name):
    if not name:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")


typed_name = input("Your name: ")
greet(typed_name)
```

An empty string counts as `False` (lesson 4.3), so `not name` is `True` only when nothing was typed. `name == ""` works too. Without the `if`, an empty name prints `Hello, !`.

## ch06b-returning#4

```python
def average(first, second, third):
    total = first + second + third
    return round(total / 3, 1)
```

The brackets around the addition matter if you do it in one line: `round((first + second + third) / 3, 1)`. Without them, only `third` would be divided by 3 (lesson 3.2). Three zeros average to 0.0, and numbers below 0 work the same as any others.

## ch06b-returning#6

```python
def total_price(price, count):
    return price * count


cost = total_price(3, 4)
print(cost)
```

`print()` showed the answer on the screen, but handed nothing back, so `cost` got `None`. With `return`, the answer goes back to the call, `cost` keeps 12, and the `print()` below shows it.

## ch06b-returning#8

```python
def sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
```

Three outcomes, so three branches, each with its own `return`, like `ticket_price`. 0 is neither above nor below 0, so it falls through to the `else`.

## ch06b-returning#9

```python
# Say it: give back the largest of three numbers.
# Split it:
# 1. if a is at least as big as both others, it is the largest
# 2. otherwise, the largest is b or c: whichever is bigger
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


print(largest_of_three(3, 9, 5))
print(largest_of_three(-1, -5, -3))
```

The second test only compares `b` and `c`, because by then `a` has lost to one of them. When two numbers tie for largest, either one is the right answer: with 7, 7 and 2, `a >= b` is `True`, so `a` comes back, which is 7. `>` in place of `>=` works too: then `b` comes back, which is also 7.

## ch06c-scope-and-docstrings#4

```python
def add_shipping(price):
    total = price + 4
    return total


cost = add_shipping(20)
print(cost)
```

`total` is local to `add_shipping()`, so the last line could not see it: that was the `NameError`. Now the function returns the value, and the program stores it in a variable of its own. Calling that variable `total` too would also work: it would be a second, separate variable, outside the function.

## ch06c-scope-and-docstrings#6

```python
def add_bonus(score, bonus):
    return score + bonus


print(add_bonus(10, 5))
```

With `bonus` in the brackets, the function no longer reads the global variable, so the line `bonus = 5` can go. Every call now says what bonus it uses, and a change somewhere else in the program can't change the answer.

## ch06c-scope-and-docstrings#9

```python
# Say it: give back True if a number is even, False if not.
# Split it:
# 1. say what the function does, in a docstring
# 2. an even number leaves no remainder when divided by 2
# 3. return True or False
def is_even(number):
    """Give back True if the number is even, False if it is not."""
    return number % 2 == 0


print(is_even(4))
print(is_even(-3))
```

`number % 2 == 0` is already `True` or `False`, so the function can return it as it is. An `if` with `return True` and `return False` works too. 0 divided by 2 leaves no remainder, so 0 is even, and so is -2.

## ch06d-defaults-and-calls#4

```python
def repeat_text(text, times=2):
    return text * times
```

With one argument, `times` holds its default, 2. With two, the second replaces it. An empty string repeated is still empty, and any string times 0 is `""`.

## ch06d-defaults-and-calls#6

```python
def is_even(number):
    """Give back True if the number is even, False if it is not."""
    return number % 2 == 0


for number in range(1, 21):
    if is_even(number):
        print(number)
```

`is_even()` gives back `True` or `False`, so its call can be the whole condition of the `if`. `range(1, 21)` stops just before 21, so 20 is included.

## ch06d-defaults-and-calls#8

```python
# Say it: count the vowels in a word.
# Split it:
# 1. is_vowel: True for a, e, i, o or u, otherwise False
# 2. count_vowels: start a count at 0
# 3. for each letter, if is_vowel says so, add 1
# 4. after the loop, return the count
def is_vowel(letter):
    """Give back True if the letter is a vowel."""
    return letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"


def count_vowels(word):
    """Give back how many vowels the word has."""
    count = 0
    for letter in word:
        if is_vowel(letter):
            count += 1
    return count


print(is_vowel("e"))
print(is_vowel("k"))
print(count_vowels("banana"))
```

`count_vowels()` is lesson 5.3's counting loop, inside a function, and the vowel test has a name of its own. The two `is_vowel()` calls check it alone, before `count_vowels()` relies on it. With an empty string, the loop makes no passes, and the count stays 0. The `return` is not indented into the loop: there, it would end the function after the first letter.

## ch06e-splitting-into-functions#3

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

def volume(width, length, height):
    """Give back the volume of a box-shaped room."""
    return area(width, length) * height

def main():
    width = get_whole_number("Width: ")
    length = get_whole_number("Length: ")
    height = get_whole_number("Height: ")
    print(f"The room is {area(width, length)} square meters.")
    print(f"The room holds {volume(width, length, height)} cubic meters.")

main()
```

`get_whole_number()` did not change: it was checked once, and now it is used three times. `volume()` uses `area()`, though `width * length * height` works too. Only `main()`, the plan, gained a step.

## ch06e-splitting-into-functions#4

```python
# Say it: ask for a student's name and four scores, then print
# their average and letter grade.
# Split it:
# 1. ask for the name
# 2. ask for a score, again until it is a whole number
#    from 0 to 100 (four times)                  -> get_score(prompt)
# 3. add up the four scores, and divide by 4
# 4. turn the average into a letter              -> letter_grade(average)
# 5. print the average and the letter
# The whole plan, run in order:                  -> main()
```

Your steps and names can differ. What matters is that a job done four times becomes one function, used four times, and that the step that turns a number into a letter is a function of its own, which you can check without typing a single score.

## ch06e-splitting-into-functions#5

```python
def letter_grade(average):
    """Give back the letter grade for an average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


print(letter_grade(89.5))
print(letter_grade(0))
```

The highest grade is tested first. Tested last, `average >= 60` would catch 95 too, and give it a D. 89.5 is not 90 or above, so it is a B: the rule says nothing about rounding up.

## ch06e-splitting-into-functions#6

```python
def get_score(prompt):
    """Ask until a whole number from 0 to 100 is typed, and give it back."""
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Please type a whole number from 0 to 100.")
        except ValueError:
            print("Please type a whole number from 0 to 100.")


print(get_score("Score: "))
```

A number outside 0 to 100 does not reach the `return`, so the message is printed, and the loop asks again. A word never gets that far: `int()` fails, and the `except` block prints the same message. `<=` at both ends lets 0 and 100 in.

## ch06e-splitting-into-functions#7

```python
def letter_grade(average):
    """Give back the letter grade for an average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_score(prompt):
    """Ask until a whole number from 0 to 100 is typed, and give it back."""
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Please type a whole number from 0 to 100.")
        except ValueError:
            print("Please type a whole number from 0 to 100.")


def main():
    """Run the grade calculator."""
    name = input("Student name: ")
    total = 0
    for turn in range(4):
        total += get_score("Score: ")
    average = total / 4
    print(f"{name}: average {average}")
    print(f"Grade: {letter_grade(average)}")


main()
```

`main()` reads like the plan: ask for the name, add up four scores, work out the average, print it and its letter. The asking again and the grading rule are inside their own functions, already checked, so `main()` stays short.

## ch06e-splitting-into-functions#9

```python
# Say it: give back True if a number is prime, False if not;
# then print the primes below 50.
# Split it:
# 1. below 2: not prime
# 2. try each number from 2 up to one less than the number:
#    if it divides evenly, not prime
# 3. if none did, prime
# 4. loop over 0 to 49, printing each prime
def is_prime(number):
    """Give back True if the number is prime, False if it is not."""
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


for candidate in range(50):
    if is_prime(candidate):
        print(candidate)
```

`return False` inside the loop stops at the first divisor found: 9 stops at 3. `return True` is after the loop, so it runs only when no divisor was found. For 2, `range(2, 2)` is empty, the loop makes no passes, and 2 is prime, which is right. Without the first `if`, 1, 0 and -7 would also skip the loop, and come back `True`.

## ch06-practice#1

```python
def c_to_f(celsius):
    return round(celsius * 9 / 5 + 32, 1)

print(c_to_f(100))
print(c_to_f(39.2))
```

Without `round()`, 39.2 gives 102.56, and 36.6 gives `97.88000000000001`, one of those long decimals from lesson 3.2. The function rounds, so every caller gets a tidy answer.

## ch06-practice#2

```python
def f_to_c(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 1)

print(f_to_c(212))
print(f_to_c(0))
```

The brackets make the take-away happen first, before the multiplying. 0 Fahrenheit gives -17.8: a function gives back numbers below 0 as happily as any other.

## ch06-practice#3

```python
def km_to_miles(km):
    return round(km * 0.621371, 2)

print(km_to_miles(5))
```

5 km is 3.106855 miles, which rounds to 3.11.

## ch06-practice#4

```python
def cups_to_ml(cups):
    return round(cups * 236.588, 1)

print(cups_to_ml(2))
```

2 cups is 473.176 ml, which rounds to 473.2. 0 cups gives 0.0, which is right.

## ch06-practice#5

```python
def c_to_f(celsius):
    return round(celsius * 9 / 5 + 32, 1)

def oven_setting(celsius):
    fahrenheit = c_to_f(celsius)
    return round(fahrenheit / 25) * 25

print(oven_setting(180))
print(oven_setting(200))
```

356.0 holds 14.24 lots of 25. `round()` with no places gives the nearest whole number, 14, and 14 lots of 25 is 350. 200 C is 392.0 F, which is 15.68 lots, so the dial goes up to 400. The sum for Fahrenheit is written once, in `c_to_f()`, and `oven_setting()` uses it.

## ch06-practice#6

```python
def hours_in(minutes):
    return minutes // 60

print(hours_in(125))
print(hours_in(45))
```

`//` gives how many whole 60s fit. 45 minutes is 0 whole hours.

## ch06-practice#7

```python
def minutes_left(minutes):
    return minutes % 60

print(minutes_left(125))
print(minutes_left(60))
```

`%` gives what is left after the whole hours. 60 minutes is exactly 1 hour, so 0 is left.

## ch06-practice#8

```python
# Say it: ask for a temperature, a distance, some cups and a cooking time,
# and print each one converted, using the toolkit's functions.
# Split it:
# 1. ask the four questions
# 2. print the temperature line and the oven dial line
# 3. print the distance line
# 4. print the cups line
# 5. print the time line
def c_to_f(celsius):
    return round(celsius * 9 / 5 + 32, 1)

def oven_setting(celsius):
    return round(c_to_f(celsius) / 25) * 25

def km_to_miles(km):
    return round(km * 0.621371, 2)

def cups_to_ml(cups):
    return round(cups * 236.588, 1)

def hours_in(minutes):
    return minutes // 60

def minutes_left(minutes):
    return minutes % 60

def main():
    celsius = float(input("Temperature, in degrees C? "))
    km = float(input("Distance, in km? "))
    cups = float(input("How many cups? "))
    minutes = int(input("Cooking time, in minutes? "))
    print(f"{celsius} C is {c_to_f(celsius)} F")
    print(f"Oven dial: {oven_setting(celsius)}")
    print(f"{km} km is {km_to_miles(km)} miles")
    print(f"{cups} cups is {cups_to_ml(cups)} ml")
    print(f"{minutes} minutes is {hours_in(minutes)} h {minutes_left(minutes)} min")

main()
```

`main()` is the plan from Split it, as code, and each line of it uses a function you checked on its own. `float()` turns 180 into `180.0`, so the first line says `180.0 C`; that is the same temperature. (`f_to_c()` is not needed here, and that is fine: a toolkit can hold more than one program uses.)

## ch07a-lists-and-indexing#7

```python
seasons = ["spring", "summer", "fall", "winter"]
print(seasons[3])
```

The list has four items, at index 0, 1, 2 and 3, so `seasons[4]` is past the end. `winter` is the fourth item, at index 3. `seasons[-1]` works too: it is always the last item.

## ch07a-lists-and-indexing#8

```python
# Say it: print the first and the last name in the finishing order.
# Split it:
# 1. the winner is the first item, at index 0
# 2. the last finisher is the last item, at index -1
finishers = ["Mo", "Ada", "Kim", "Lee", "Bo"]
print("Winner:", finishers[0])
print("Last:", finishers[-1])
```

`finishers[4]` also finds `Bo` today. But add a sixth finisher and index 4 is no longer the last one, while `finishers[-1]` still is. That is what the awkward check in Check it shows.

## ch07b-slicing#6

```python
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(week[5:])
```

`Sat` is at index 5, and leaving out the stop goes to the end. `week[-2:]`, the last two, works as well, and so does `week[5:7]`.

## ch07b-slicing#8

```python
# Say it: give back the three scores in the middle of five.
# Split it:
# 1. the middle three of five are at index 1, 2 and 3
# 2. slice from 1, stopping just before 4
# 3. give back the slice
def middle_three(scores):
    middle = scores[1:4]
    return middle


print(middle_three([5, 6, 7, 8, 9]))
print(middle_three([]))
```

The stop is 4, one past the last index you want, as with `range()`. `scores[1:-1]` works too: from index 1, up to just before the last item. An empty list gives back `[]`, with no error, because a slice is never out of range.

## ch07c-changing-a-list#5

```python
multiples = []
for number in range(1, 6):
    multiples.append(number * 3)
print(multiples)
```

The loop runs for 1 to 5, and appends 3 times each one. `range(3, 16, 3)` gives the multiples themselves, so `multiples.append(number)` works with it too.

## ch07c-changing-a-list#6

```python
scores = [88, 92]
scores.append(79)
scores.append(95)
print(scores)
```

`append()` takes exactly one item, and the error said so: two were given. One `append()` for each score fixes it, and keeps them in order.

## ch07c-changing-a-list#9

```python
# Say it: ask for things to buy until an empty answer, then print the list.
# Split it:
# 1. start with an empty list
# 2. ask for the first item
# 3. while it is not empty: append it, then ask for the next
# 4. after the loop, print the list
shopping = []
item = input("Thing to buy (Enter to finish): ")
while item != "":
    shopping.append(item)
    item = input("Thing to buy (Enter to finish): ")
print(shopping)
```

The empty answer is the stop value, so it is checked before it is appended, and never goes into the list. When Enter is pressed straight away, the loop makes no passes, and the list stays `[]`.

## ch07d-inserting-and-removing#7

```python
def move_to_front(items, item):
    items.remove(item)
    items.insert(0, item)
    return items
```

`remove()` finds the item by its value, wherever it is, and `insert(0, item)` puts it back at the front. When it is already at the front, it is taken out and put straight back, so nothing changes.

## ch07d-inserting-and-removing#8

```python
# Say it: serve a number of people from the front of the line, then print the rest.
# Split it:
# 1. ask how many to serve
# 2. that many times: take out the person at the front, and print their name
# 3. print the line
line = ["Ada", "Bo", "Cy"]
how_many = int(input("How many to serve? "))
for turn in range(how_many):
    person = line.pop(0)
    print(f"Serving {person}")
print(line)
```

`pop(0)` takes out the person at the front and gives them back, so `person` can be printed. With 0, `range(0)` makes no passes, and the whole line is printed. With 3, the loop empties the line, and it prints `[]`.

## ch07e-asking-about-a-list#4

```python
def spread(numbers):
    if len(numbers) == 0:
        return 0
    return max(numbers) - min(numbers)
```

Without the first `if`, an empty list stops at `max()` with a `ValueError`. The `return 0` ends the function first (lesson 6.2), so `max()` never sees an empty list. A list of one number has the same largest and smallest, so its spread is 0 with no special case.

## ch07e-asking-about-a-list#5

```python
rolls = [4, 6, 1, 5, 3, 6]
print(sum(rolls))
print(max(rolls))
print(min(rolls))
```

One question about the whole list per line, each in one word. Labels, like `print("Total:", sum(rolls))`, are fine too.

## ch07e-asking-about-a-list#6

```python
# Say it: give back the average of a list of numbers, or 0 for an empty list.
# Split it:
# 1. if the list is empty, give back 0
# 2. otherwise, add up the numbers, divide by how many there are, and give that back
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(average([88, 92, 79, 95]))
print(average([]))
```

Without step 1, `average([])` divides 0 by 0, and stops with a `ZeroDivisionError`. Checking the empty list first, and returning, means the division only ever runs when there is at least one number.

## ch07f-sorting-a-list#3

```python
words = []
for turn in range(4):
    words.append(input("Word: "))
print(sorted(words))
```

The loop asks four times and appends each word, as in lesson 7.3. `sorted()` gives back the list in order. `words.sort()` on its own line, then `print(words)`, works as well.

## ch07f-sorting-a-list#5

```python
scores = [88, 92, 79]
scores.sort()
print(scores[0])
```

`scores.sort()` sorts the list and gives back `None`, so `scores = scores.sort()` threw the list away and kept `None`, and `None[0]` makes no sense. Call `sort()` on its own line. `scores = sorted(scores)` works too, because `sorted()` gives back the new list.

## ch07f-sorting-a-list#6

```python
def in_order(scores):
    return sorted(scores)

marks = [88, 92, 79]
print(in_order(marks))
print(marks)
```

`scores.sort()` sorted the caller's list itself, because `scores` and `marks` are two names for one list. `sorted(scores)` makes a new list in order, and leaves the one it was given alone. Sorting a copy, `scores[:]`, then giving that back, works too.

## ch07f-sorting-a-list#7

```python
# Say it: give back the second-largest number, or None if there are fewer than two.
# Split it:
# 1. if the list has fewer than two numbers, give back None
# 2. make a sorted copy of the list
# 3. give back its second item from the end
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    in_order = sorted(numbers)
    return in_order[-2]


print(second_largest([3, 9, 5]))
print(second_largest([]))
```

`sorted()` makes a new list, so the caller's list is left as it was; `numbers.sort()` would have sorted the caller's list too. In order, the largest is at index -1 and the second-largest at -2. Without step 1, `[7]` would stop with an `IndexError`, because a list of one item has no index -2.

## ch07g-looping-over-a-list#4

```python
def evens(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
```

The shape of `passing`: an empty list, a loop, an `if`, and `append()`. `% 2` gives 0 for every even number, 0 and the ones below 0 included. An empty list makes no passes, and gives back `[]`.

## ch07g-looping-over-a-list#5

```python
def count_above(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count
```

A count, as in lesson 5.3, kept in a loop over the list. `>` and not `>=`, because a number equal to the threshold is not above it. Building a list of the numbers above it, and giving back its `len()`, works too.

## ch07g-looping-over-a-list#9

```python
# Say it: give back every index where target appears in items.
# Split it:
# 1. start with an empty list of indexes
# 2. loop over the items, with their indexes
# 3. if an item is the target, append its index
# 4. after the loop, give back the list of indexes
def positions(items, target):
    indexes = []
    for index, item in enumerate(items):
        if item == target:
            indexes.append(index)
    return indexes


print(positions(["a", "b", "a"], "a"))
print(positions([], "a"))
```

`enumerate()` hands over each index with its item, so the index is there to append when the item matches. If nothing matches, or the list is empty, nothing is appended, and `[]` comes back, as it should. `range(len(items))` with `items[i]` works the same way.

## ch07h-lists-inside-lists#6

```python
sales = [[3, 5, 2], [4, 0, 6], [1, 1, 1]]
for row in sales:
    print(sum(row))
```

Each time round, `row` is one whole row, a list, so `sum(row)` adds it up. A loop inside the loop that keeps a total, set back to 0 at the start of each row, works too.

## ch07h-lists-inside-lists#7

```python
# Say it: change two squares of the board, then print it as three rows of three.
# Split it:
# 1. put the X in the center: row 1, index 1
# 2. put the O in the top right corner: row 0, index 2
# 3. for each row: print each square with a space after it, then end the line
board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
]
board[1][1] = "X"
board[0][2] = "O"
for row in board:
    for square in row:
        print(square, end=" ")
    print()
```

Rows and squares both count from 0, so the center is row 1, index 1, and the top right is row 0, index 2, which is also `board[0][-1]`. The bare `print()` ends each row; without it, all nine squares would be on one line.

## ch07i-the-gradebook#6

```python
def top_student(names, scores):
    if len(scores) == 0:
        return None
    best = max(scores)
    where = scores.index(best)
    return names[where]
```

The same three steps as the example: the top score, its index, and the name at that index. The `if` comes first, because `max()` of an empty list stops with a `ValueError`. With a tie, `index()` finds the first of them, so the first student with that score is the answer.

## ch07i-the-gradebook#7

```python
def count_passing(scores):
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    return count
```

`count_above()` from lesson 7.7, with `>=` in place of `>`, because 60 is a pass. An empty list makes no passes, so the count stays 0.

## ch07i-the-gradebook#9

```python
# Say it: print each student's line, then a summary of the class.
# Split it:
# 1. each student's line: name, score and letter grade
# 2. the class average
# 3. who got the top score
# 4. how many passed
# 5. print it all
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def top_student(names, scores):
    if len(scores) == 0:
        return None
    return names[scores.index(max(scores))]


def count_passing(scores):
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    return count


names = ["Ada", "Grace", "Alan", "Katherine", "Edsger"]
scores = [88, 92, 45, 95, 71]
for index, name in enumerate(names):
    score = scores[index]
    print(name, score, letter_grade(score))
print(f"Average: {round(average(scores), 1)}")
print(f"Top: {top_student(names, scores)} {max(scores)}")
print(f"Passing: {count_passing(scores)} of {len(scores)}")
```

The loop needs each index, because the same index finds a name in `names` and its score in `scores`. Every summary line is one call to a function that was checked on its own. The average here is exactly 78.2, but rounding it to 1 place keeps a class whose average is 78.2222 from printing all those digits.

## ch07-practice#1

```python
def with_song(playlist, title):
    new_playlist = playlist[:]
    new_playlist.append(title)
    return new_playlist

playlist = ["Ghost Town", "Ribbons", "Anvil"]
print(with_song(playlist, "Low Tide"))
print(with_song([], "Low Tide"))
print(playlist)
```

## ch07-practice#2

```python
def play_next(playlist, title):
    new_playlist = playlist[:]
    new_playlist.insert(1, title)
    return new_playlist

playlist = ["Ghost Town", "Ribbons", "Anvil"]
print(play_next(playlist, "Low Tide"))
print(play_next([], "Low Tide"))
print(playlist)
```

## ch07-practice#3

```python
def without_song(playlist, title):
    new_playlist = playlist[:]
    if new_playlist.count(title) > 0:
        new_playlist.remove(title)
    return new_playlist

playlist = ["Ghost Town", "Ribbons", "Anvil", "Ribbons"]
print(without_song(playlist, "Ribbons"))
print(without_song(playlist, "Low Tide"))
print(without_song([], "Low Tide"))
print(playlist)
```

## ch07-practice#4

```python
def up_next(playlist):
    return playlist[1:4]

playlist = ["Ghost Town", "Ribbons", "Anvil", "Low Tide", "Harbor"]
print(up_next(playlist))
print(up_next(["Ghost Town", "Ribbons"]))
print(up_next(["Ghost Town"]))
print(up_next([]))
print(playlist)
```

## ch07-practice#5

```python
def song_number(playlist, title):
    if playlist.count(title) == 0:
        return 0
    return playlist.index(title) + 1

playlist = ["Ghost Town", "Ribbons", "Anvil", "Ribbons"]
print(song_number(playlist, "Anvil"))
print(song_number(playlist, "Ghost Town"))
print(song_number(playlist, "Ribbons"))
print(song_number(playlist, "Low Tide"))
print(song_number([], "Anvil"))
print(playlist)
```

## ch07-practice#6

```python
def a_to_z(playlist):
    return sorted(playlist)

playlist = ["Ribbons", "Anvil", "Low Tide", "Ghost Town"]
print(a_to_z(playlist))
print(a_to_z([]))
print(playlist)
```

## ch07-practice#7

```python
def show(playlist):
    for position, title in enumerate(playlist):
        print(f"{position + 1}. {title}")

show(["Ghost Town", "Ribbons", "Anvil"])
show([])
```

## ch07-practice#8

```python
# Say it: four songs go in, to add, to play next, to take out and to find;
# the changed playlist comes out, numbered, then what is up next, the
# playlist from A to Z, and where the song to find is.
# Split it:
# 1. ask for the song to add, and keep the new playlist
# 2. the same for the song to play next, and the song to take out
# 3. ask for the song to find
# 4. show the playlist; print the up-next line and the A-to-Z line
# 5. print where the song to find is, or that it is not there
def with_song(playlist, title):
    new_playlist = playlist[:]
    new_playlist.append(title)
    return new_playlist

def play_next(playlist, title):
    new_playlist = playlist[:]
    new_playlist.insert(1, title)
    return new_playlist

def without_song(playlist, title):
    new_playlist = playlist[:]
    if new_playlist.count(title) > 0:
        new_playlist.remove(title)
    return new_playlist

def up_next(playlist):
    return playlist[1:4]

def song_number(playlist, title):
    if playlist.count(title) == 0:
        return 0
    return playlist.index(title) + 1

def a_to_z(playlist):
    return sorted(playlist)

def show(playlist):
    for position, title in enumerate(playlist):
        print(f"{position + 1}. {title}")

playlist = ["Ghost Town", "Ribbons", "Anvil"]
added = input("Song to add: ")
playlist = with_song(playlist, added)
next_song = input("Song to play next: ")
playlist = play_next(playlist, next_song)
gone = input("Song to take out: ")
playlist = without_song(playlist, gone)
wanted = input("Song to find: ")

show(playlist)
print("Up next:", up_next(playlist))
print("A to Z:", a_to_z(playlist))
number = song_number(playlist, wanted)
if number == 0:
    print(f"{wanted} is not in the playlist")
else:
    print(f"{wanted} is song {number}")
```

## ch08a-text-is-a-sequence#5

```python
def ends(word):
    if word == "":
        return ""
    return word[0] + word[-1]
```

`word[0]` is the first character and `word[-1]` the last, and `+` joins them. An empty string has no index 0, so without the first two lines `ends("")` would stop with an `IndexError`. For a word of one letter, index 0 and index -1 are the same letter, so `"a"` gives `"aa"`.

## ch08a-text-is-a-sequence#6

```python
name = "grace"
name = "G" + name[1:]
print(name)
```

A string can't change, so `name[0] = "G"` stops with a `TypeError`. `name[1:]` is `"race"`, and `"G" + name[1:]` is a new string, `"Grace"`, which `name` then names. Printing `"G" + name[1:]` straight away works too.

## ch08a-text-is-a-sequence#8

```python
# Say it: print the word, then the word turned around, then its length.
# Split it:
# 1. ask for the word
# 2. print it
# 3. print it turned around, with a slice
# 4. print its length
word = input("Word: ")
print("Forward:", word)
print("Backward:", word[::-1])
print("Length:", len(word))
```

`word[::-1]` steps backward through the whole word. `len()` counts every character, so a space counts too: `top spot` has 8. An f-string, like `print(f"Length: {len(word)}")`, works as well.

## ch08b-capital-letters#4

```python
name = input("Name: ")
print(name.upper())
```

`upper()` gives back a new string in capitals, and `print()` shows it. A name already in capitals comes back as it was. Keeping it first, as `loud_name = name.upper()`, then printing that, works too.

## ch08b-capital-letters#5

```python
message = "shout"
message = message.upper()
print(message)
```

`message.upper()` gave back `"SHOUT"`, but nothing kept it, and `message` itself can't change. `message = message.upper()` keeps the new string. `print(message.upper())` works too.

## ch08b-capital-letters#7

```python
answer = input("Do you like pizza? ")
if answer.lower() == "yes":
    print("Me too!")
else:
    print("Oh well.")
```

`answer.lower()` turns `YES` and `Yes` into `yes` before the comparison, so one test covers them all. Comparing `answer` itself with `"yes"` would say `Oh well.` to `YES`.

## ch08b-capital-letters#8

```python
def same_word(first, second):
    return first.lower() == second.lower()
```

Both sides need `lower()`. With only `first.lower() == second`, `"ADA"` and `"Ada"` would compare `"ada"` with `"Ada"`, which is `False`. An `if` that gives back `True` or `False` works too; the comparison already is `True` or `False`.

## ch08b-capital-letters#9

```python
# Say it: count how many times the letter is in the text, capital or small.
# Split it:
# 1. make the text and the letter both small letters
# 2. start a count at 0
# 3. loop over the text, and add 1 for each character that is the letter
# 4. after the loop, give back the count
def count_letter(text, letter):
    text = text.lower()
    letter = letter.lower()
    count = 0
    for character in text:
        if character == letter:
            count += 1
    return count


print(count_letter("Banana", "a"))
print(count_letter("Anna", "A"))
```

Step 1 is the comparing-safely idea: both sides in small letters, so `A` and `a` match. Without `letter = letter.lower()`, `count_letter("Anna", "A")` would look for a capital in a text of small letters, and give back 0. An empty text makes no passes, so the count stays 0.

## ch08c-tidying-text#4

```python
def is_yes(answer):
    return answer.strip().lower() == "yes"
```

`strip()` first, then `lower()`, then the comparison. The order of the two methods does not matter here: `answer.lower().strip()` gives back the same. Spaces in the middle are not at an end, so `"y e s"` keeps them, and is not `"yes"`.

## ch08c-tidying-text#6

```python
def no_spaces(text):
    return text.replace(" ", "")
```

Every space is swapped for the empty string, so every space is gone. `strip()` alone would give back `"a b c"` unchanged, because its spaces are in the middle.

## ch08c-tidying-text#7

```python
# Say it: give back the name with no spaces at its ends, a capital first, and small letters after.
# Split it:
# 1. strip the spaces from the ends
# 2. if what is left is "", give it back
# 3. join the first character, in capitals, and the rest, in small letters
# 4. give that back
def tidy_name(name):
    stripped = name.strip()
    if stripped == "":
        return ""
    return stripped[0].upper() + stripped[1:].lower()


print(tidy_name("  aDA "))
print(tidy_name("   "))
```

Strip first, so that index 0 is the first letter and not a space. Without step 2, `""` and `"   "` would stop with an `IndexError`, because an empty string has no index 0. A slice is never out of range, so `stripped[:1].upper()` in place of `stripped[0].upper()` works without step 2 as well.

## ch08d-finding-text#4

```python
def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count
```

`text.lower()` makes the capitals small before the loop, so `letter in "aeiou"` catches them too. Writing the test as `letter in "aeiouAEIOU"`, with no `lower()`, works as well.

## ch08d-finding-text#7

```python
def before_at(email):
    where = email.find("@")
    if where == -1:
        return email
    return email[:where]
```

`email[:where]` stops just before the `@`, because a slice stops before its end index (lesson 7.2). Without the -1 test, `"no-at-sign"` would give `email[:-1]`, which drops the last character. `"@home"` has its `@` at index 0, so the slice `[:0]` is `""`. `if "@" not in email:` is a fine first test too.

## ch08d-finding-text#8

```python
# Say it: True if "free" or "winner" is in the message, in any capitals.
# Split it:
# 1. make the message small letters
# 2. ask whether "free" is in it, or "winner" is
# 3. give back the answer
def is_spam(message):
    small_message = message.lower()
    return "free" in small_message or "winner" in small_message


print(is_spam("FREE pizza!"))
print(is_spam(""))
```

Each side of the `or` needs its own `in`. `"free" or "winner" in small_message` reads well in English, but Python sees `"free"` on its own, which is not empty, so it counts as true (lesson 4.3), and every message would be spam. An `if` that gives back `True`, then `False` after it, works too.

## ch08e-starts-and-ends#4

```python
def is_python_file(name):
    return name.lower().endswith(".py")
```

`lower()` first, so `GAME.PY` becomes `game.py`, then `endswith()` looks at the end only. `".py" in name.lower()` would say `True` for `game.pyc` too.

## ch08e-starts-and-ends#6

```python
sentence = input("Sentence: ")
if sentence.endswith("?"):
    print("That is a question.")
else:
    print("That is not a question.")
```

Nothing typed is `""`, which ends with no `?`, so it is not a question. `"?" in sentence` would call `Why? I see.` a question, because it looks anywhere.

## ch08e-starts-and-ends#7

```python
# Say it: give back the title without "The " at its start, or as it was.
# Split it:
# 1. if the title starts with "The ", give back the rest, from index 4 on
# 2. otherwise, give back the title as it was
def drop_the(title):
    if title.startswith("The "):
        return title[4:]
    return title


print(drop_the("The Hobbit"))
print(drop_the("Theory of Everything"))
```

`"The "` is four characters, the space included, so the rest starts at index 4. Testing `startswith("The")` without the space would turn `Theory of Everything` into `ory of Everything`. `replace("The ", "")` is not right either: it would take out every `The ` in the title, not only the one at the start.

## ch08f-letters-and-digits#4

```python
tickets = input("How many tickets? ")
while not tickets.isdigit():
    tickets = input("Please type a whole number: ")
print("Cost:", int(tickets) * 5)
```

The shape of the age example: read, loop while it is not all digits, read again. `-1` and `3.5` are not all digits, so the loop asks again. `0` is all digits, so it is accepted, and costs 0. The empty answer is not all digits either.

## ch08f-letters-and-digits#5

```python
def letters_only(text):
    letters = ""
    for character in text:
        if character.isalpha():
            letters += character
    return letters
```

An accumulator that starts as `""`, as `bar` did in lesson 5.5. Only a character that `isalpha()` says is a letter is added, so spaces, digits and signs are left out.

## ch08f-letters-and-digits#6

```python
# Say it: True if the length is 3 to 12 and every character is a letter or a digit.
# Split it:
# 1. if the length is below 3 or above 12, give back False
# 2. loop over the characters: if one is not a letter and not a digit, give back False
# 3. after the loop, give back True
def valid_username(name):
    if len(name) < 3 or len(name) > 12:
        return False
    for character in name:
        if not character.isalpha() and not character.isdigit():
            return False
    return True


print(valid_username("ada99"))
print(valid_username("ada_99"))
```

One bad character is enough to say `False`, so step 2 gives back as soon as it finds one. Only after every character has passed is the answer `True`. Watch the `and` in step 2: with `or`, every character would be bad, because no character is both a letter and a digit. `""` is caught by step 1, as too short.

## ch08g-splitting-text#4

```python
def first_word(sentence):
    words = sentence.split()
    if len(words) == 0:
        return ""
    return words[0]
```

`split()` gives back an empty list for `""` and for `"   "`, because it drops the spaces and there is nothing left. An empty list has no index 0, so the test comes first. `if words == []:` works too.

## ch08g-splitting-text#6

```python
def total_of(line):
    if line == "":
        return 0
    total = 0
    for piece in line.split(","):
        total += int(piece)
    return total
```

Each piece is a string, like `"3"`, so `int()` turns it into a number before it is added. `int("-2")` is -2, so numbers below 0 work too. Without the first test, `"".split(",")` gives back `[""]`, one empty piece, and `int("")` stops with a `ValueError`. Building a list of numbers and giving back its `sum()` works as well.

## ch08g-splitting-text#7

```python
# Say it: print how many words the sentence has.
# Split it:
# 1. ask for the sentence
# 2. split it into a list of words
# 3. print how many items the list has
sentence = input("Sentence: ")
words = sentence.split()
print("Words:", len(words))
```

`split()` with nothing in its brackets cuts at runs of spaces and drops the ends, so extra spaces make no empty words, and nothing typed gives an empty list, of length 0. `split(" ")` would cut at every single space, and count the empty pieces between them as words.

## ch08h-joining-a-list#4

```python
def dashes(sentence):
    words = sentence.split()
    return "-".join(words)
```

`split()` drops the extra spaces, so `"  hi  there "` gives two words, and `join()` puts one dash between them. An empty sentence gives an empty list, and joining an empty list gives `""`. `sentence.replace(" ", "-")` is not the same: it would put a dash for every space, the extra ones too.

## ch08h-joining-a-list#5

```python
numbers = [3, 1, 4]
texts = []
for number in numbers:
    texts.append(str(number))
print(" + ".join(texts))
```

`join()` glues strings only, so each number becomes a string first, in a new list. Writing the list as strings to begin with, `["3", "1", "4"]`, also prints the right line, but it no longer starts from the numbers.

## ch08h-joining-a-list#6

```python
def capitalize_words(sentence):
    words = sentence.split()
    capitalized = []
    for word in words:
        capitalized.append(word[0].upper() + word[1:].lower())
    return " ".join(capitalized)
```

`split()` never gives back an empty word, so `word[0]` is always there. An empty sentence makes no passes, and joining an empty list gives `""`. `title()` does the same job in one method, as the next section shows; for these sentences it gives the same answers.

## ch08h-joining-a-list#8

```python
# Say it: give back the first letter of each word, in capitals, as one string.
# Split it:
# 1. split the name into words
# 2. start a new, empty list
# 3. for each word, append its first letter, in capitals
# 4. join the list with "", and give it back
def initials(full_name):
    words = full_name.split()
    letters = []
    for word in words:
        letters.append(word[0].upper())
    return "".join(letters)


print(initials("ada lovelace"))
print(initials(""))
```

`split()` with nothing in its brackets drops extra spaces, so every word has a first letter. `split(" ")` would give empty pieces for `"  bo  "`, and `word[0]` would stop with an `IndexError`. Adding each letter to a string that starts as `""`, then giving back its `upper()`, works too.

## ch08i-character-by-character#5

```python
def hide_digits(text):
    hidden = ""
    for character in text:
        if character.isdigit():
            hidden += "#"
        else:
            hidden += character
    return hidden
```

Every character adds something: a `#` for a digit, and the character itself for anything else. Without the `else`, only the `#` marks would be left.

## ch08i-character-by-character#7

```python
# Say it: True if the text reads the same both ways, ignoring spaces and capitals.
# Split it:
# 1. make a cleaned text: the spaces taken out, and the letters made small
# 2. turn the cleaned text around
# 3. compare the two
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    backward = cleaned[::-1]
    return cleaned == backward


print(is_palindrome("Never odd or even"))
print(is_palindrome("rocket"))
print(is_palindrome(""))
```

`replace(" ", "")` takes out every space, the middle ones too, which `strip()` would not. Cleaning comes first, so that both sides of the comparison are cleaned. A loop that keeps only the letters, made small, as `letters_only()` did in lesson 8.6, works as well, and ignores signs like commas too.

## ch08j-special-characters#4

```python
print("Name:\tAda\nAge:\t13")
```

`\t` is one tab and `\n` is one new line, each written inside the string where it goes. Two `print()` calls, one for each line, print the same thing.

## ch08j-special-characters#5

```python
records = "Ada,88\nGrace,92\nAlan,45"
for line in records.split("\n"):
    parts = line.split(",")
    print(parts[0], "scored", parts[1])
```

Splitting at `"\n"` gives a list of three lines. Each line is split again, at the comma, so `parts[0]` is the name and `parts[1]` the score. An f-string, `f"{parts[0]} scored {parts[1]}"`, works too.

## ch08j-special-characters#7

```python
# Say it: give back one string, a line for each item, each starting with a dash and a space.
# Split it:
# 1. start a new, empty list of lines
# 2. for each item, append a dash, a space and the item
# 3. join the lines with "\n", and give that back
def make_list(items):
    lines = []
    for item in items:
        lines.append("- " + item)
    return "\n".join(lines)


print(make_list(["eggs", "milk"]))
print(make_list(["tea"]))
```

`join()` puts the glue only between items, so there is no new line after the last one, and an empty list gives `""`. Adding `"- " + item + "\n"` to a string in the loop would leave a new line after the last item.

## ch08k-lining-up-columns#4

```python
items = ["tea", "cake", "soup"]
prices = [2.5, 3.25, 4.0]
for i in range(len(items)):
    print(f"{items[i]:<8}{prices[i]:>6.2f}")
```

`<8` fills 8 characters with the item, at the left, and `>6.2f` fills 6 with the price, at the right, with 2 decimal places. So every price ends in the same column. `enumerate()` from lesson 7.7 works too.

## ch08k-lining-up-columns#5

```python
# Say it: print each item and its price in two columns, a dashed line, then the total.
# Split it:
# 1. loop with each index, and print the item with <12 and the price with >8.2f
# 2. print 20 - signs
# 3. work out the total of the prices
# 4. print Total and the total, with the same widths
items = ["notebook", "pens", "stickers"]
prices = [3.5, 2.25, 1.75]
for i in range(len(items)):
    print(f"{items[i]:<12}{prices[i]:>8.2f}")
print("-" * 20)
total = sum(prices)
label = "Total"
print(f"{label:<12}{total:>8.2f}")
```

Every line uses the same two widths, so the prices end in one column, the total's too. `sum()` from lesson 7.5 adds up the prices; a running total in the loop works as well. `Total` is put in a variable here so that the f-string needs no quotes inside it; `f"{'Total':<12}..."`, with single quotes inside, works too.

## ch08l-the-text-analyzer#3

```python
def letters_only(text):
    letters = ""
    for character in text:
        if character.isalpha():
            letters += character
    return letters


def word_list(text):
    words = []
    for raw_word in text.split():
        word = letters_only(raw_word).lower()
        if word != "":
            words.append(word)
    return words
```

`split()` gives the words with their signs still on, like `Ada!`; `letters_only()` keeps the letters, and `lower()` makes them small. `42` has no letters, so it becomes `""`, and the `if` leaves it out. Without the `if`, `"Hi, Ada! 42"` would give `["hi", "ada", ""]`.

## ch08l-the-text-analyzer#4

```python
def count_sentences(text):
    count = 0
    for character in text:
        if character in ".!?":
            count += 1
    return count
```

One `in` asks about all three signs, as `in "aeiou"` did for vowels. Adding `text.count(".")`, `text.count("!")` and `text.count("?")` works too.

## ch08l-the-text-analyzer#5

```python
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
```

Starting from `""` means an empty list gives back `""` with no extra test, and any real word is longer. `>` and not `>=`: a word as long as the longest so far does not replace it, so a tie keeps the first.

## ch08l-the-text-analyzer#6

```python
def average_length(words):
    if len(words) == 0:
        return 0.0
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)
```

The total of the lengths, divided by how many words there are, as `average()` did in lesson 7.5. Without the first test, an empty list would divide by 0 and stop with a `ZeroDivisionError`.

## ch08l-the-text-analyzer#7

```python
# Say it: print a report on a passage of text.
# Split it:
# 1. the characters: len() of the text, then of the text with its spaces taken out
# 2. the words: word_list(text), then len() of it
# 3. the sentences: count_sentences(text)
# 4. the vowels: count_vowels() from lesson 8.4
# 5. the longest word: longest_word(words)
# 6. the average word length: average_length(words), rounded to 1 place
# 7. print each one with report_line()
def letters_only(text):
    letters = ""
    for character in text:
        if character.isalpha():
            letters += character
    return letters

def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

sample = "The quick brown fox jumps over the lazy dog. Programming is the art of telling a computer what to do! Is that not remarkable?"

def report_line(label, value):
    """Print one line of the report: the label at the left, the value at the right."""
    print(f"{label:<24}{value:>12}")

def word_list(text):
    words = []
    for raw_word in text.split():
        word = letters_only(raw_word).lower()
        if word != "":
            words.append(word)
    return words

def count_sentences(text):
    count = 0
    for character in text:
        if character in ".!?":
            count += 1
    return count

def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def average_length(words):
    if len(words) == 0:
        return 0.0
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)

words = word_list(sample)
print("=" * 36)
report_line("Characters:", len(sample))
report_line("Characters (no spaces):", len(sample.replace(" ", "")))
report_line("Words:", len(words))
report_line("Sentences:", count_sentences(sample))
report_line("Vowels:", count_vowels(sample))
report_line("Longest word:", longest_word(words))
report_line("Average word length:", round(average_length(words), 1))
print("=" * 36)
```

Each line is one step of the plan, and each step is a function you checked on its own. The words are worked out once, in `words`, and used three times. `round(..., 1)` gives 4.1, which `report_line()` puts at the right like any other value; `:>12.1f` in an f-string of your own does the same.

## ch08-practice#1

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, shift):
    position = alphabet.find(letter)
    return alphabet[position + shift]


print(shift_letter("a", 3))
```

## ch08-practice#2

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, shift):
    position = alphabet.find(letter)
    new_position = (position + shift) % 26
    return alphabet[new_position]


print(shift_letter("x", 3))
```

## ch08-practice#3

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, shift):
    position = alphabet.find(letter)
    if position == -1:
        return letter
    new_position = (position + shift) % 26
    return alphabet[new_position]


print(shift_letter("!", 3))
```

## ch08-practice#4

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
capitals = alphabet.upper()


def shift_letter(letter, shift):
    if alphabet.find(letter) != -1:
        position = alphabet.find(letter)
        return alphabet[(position + shift) % 26]
    if capitals.find(letter) != -1:
        position = capitals.find(letter)
        return capitals[(position + shift) % 26]
    return letter


print(shift_letter("A", 3))
```

## ch08-practice#5

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
capitals = alphabet.upper()


def shift_letter(letter, shift):
    if alphabet.find(letter) != -1:
        position = alphabet.find(letter)
        return alphabet[(position + shift) % 26]
    if capitals.find(letter) != -1:
        position = capitals.find(letter)
        return capitals[(position + shift) % 26]
    return letter


def encode(text, shift):
    result = ""
    for character in text:
        result += shift_letter(character, shift)
    return result


print(encode("Hello, World!", 3))
```

## ch08-practice#6

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
capitals = alphabet.upper()


def shift_letter(letter, shift):
    if alphabet.find(letter) != -1:
        position = alphabet.find(letter)
        return alphabet[(position + shift) % 26]
    if capitals.find(letter) != -1:
        position = capitals.find(letter)
        return capitals[(position + shift) % 26]
    return letter


def encode(text, shift):
    result = ""
    for character in text:
        result += shift_letter(character, shift)
    return result


def decode(text, shift):
    return encode(text, -shift)


print(decode("Khoor, Zruog!", 3))
```

## ch08-practice#7

```python
# Say it: a choice, a message and a shift go in; the message comes out in
# code, or out of code, or a reminder of the two choices.
# Split it:
# 1. ask encode or decode, and tidy the answer
# 2. if encode: ask the message and the shift, print the encoded result
# 3. if decode: the same, with the decoded result
# 4. otherwise: print the reminder, and ask nothing more
alphabet = "abcdefghijklmnopqrstuvwxyz"
capitals = alphabet.upper()


def shift_letter(letter, shift):
    if alphabet.find(letter) != -1:
        position = alphabet.find(letter)
        return alphabet[(position + shift) % 26]
    if capitals.find(letter) != -1:
        position = capitals.find(letter)
        return capitals[(position + shift) % 26]
    return letter


def encode(text, shift):
    result = ""
    for character in text:
        result += shift_letter(character, shift)
    return result


def decode(text, shift):
    return encode(text, -shift)


choice = input("Encode or decode? ").strip().lower()
if choice == "encode":
    message = input("Message: ")
    shift = int(input("Shift: "))
    print("Result:", encode(message, shift))
elif choice == "decode":
    message = input("Message: ")
    shift = int(input("Shift: "))
    print("Result:", decode(message, shift))
else:
    print("Please type encode or decode.")
```

## ch09a-dictionaries#5

```python
prices = {"apple": 0.5, "pear": 0.75}
print(prices["apple"])
```

The last line of the error is `KeyError: 'Apple'`: the dictionary has no key `"Apple"`, with a capital A. Its key is `"apple"`, so that is what goes in the square brackets.

## ch09a-dictionaries#9

```python
# Say it: change the phone book in two ways, then print one number and how many there are.
# Split it:
# 1. store Lee's number
# 2. store Ada's new number
# 3. print Ada's number
# 4. print how many entries the book has
phone_book = {"Ada": "555-0100", "Grace": "555-0142"}
phone_book["Lee"] = "555-0199"
phone_book["Ada"] = "555-0111"
print("Ada:", phone_book["Ada"])
print("Numbers:", len(phone_book))
```

Storing a value under `"Lee"`, a new key, adds an entry; storing one under `"Ada"`, a key that is there, changes its value. So the book ends with three entries. Under `"ada"`, with a small a, the second line would add a fourth entry instead, and Ada's number would stay `555-0100`.

## ch09b-missing-keys#4

```python
def price_of(prices, item):
    if item in prices:
        return prices[item]
    return 0
```

The lookup in square brackets runs only when `item` is a key, so a missing item never meets a `KeyError`. An `else:` before the last line works the same. After the next section, `return prices.get(item, 0)` does it in one line.

## ch09b-missing-keys#6

```python
def nickname(nicknames, name):
    return nicknames.get(name, name)
```

The first `name` is the key to look up; the second is the default, given back when that key is missing. An `if name in nicknames:` with an `else:` works too.

## ch09b-missing-keys#8

```python
def take_one(stock, item):
    if item not in stock:
        return stock
    if stock[item] == 1:
        del stock[item]
    else:
        stock[item] = stock[item] - 1
    return stock
```

The first test comes first, because `stock[item]` would be a `KeyError` for an item that is not there. Storing `stock[item] - 1` when there is 1 left would leave the item in with 0, and the exercise says an item held 0 times is not held.

## ch09b-missing-keys#9

```python
# Say it: print the number for the name typed in, or a message if the book does not have it.
# Split it:
# 1. ask for the name
# 2. if it is a key of the book, print it and its number
# 3. otherwise, print the message
phone_book = {"Ada": "555-0100", "Grace": "555-0142", "Lee": "555-0199"}
name = input("Name: ")
if name in phone_book:
    print(name + ":", phone_book[name])
else:
    print("No number for " + name + ".")
```

`in` asks about the keys, so the lookup in square brackets runs only for a name the book has. `get()` with a default works too: look the name up once, then test what came back.

## ch09c-looping-over-a-dictionary#4

```python
def names_over(scores, limit):
    names = []
    for name in scores:
        if scores[name] > limit:
            names.append(name)
    return names
```

The loop gives each name in turn, and `scores[name]` is that name's score. The names go into the new list in the dictionary's order, because that is the order the loop gives them in.

## ch09c-looping-over-a-dictionary#6

```python
def average_score(scores):
    if len(scores) == 0:
        return 0
    return sum(scores.values()) / len(scores)
```

The test comes first, because dividing by `len({})`, which is 0, stops with a `ZeroDivisionError`. `if scores == {}:` works as the test too.

## ch09c-looping-over-a-dictionary#7

```python
# Say it: print each item in the cart with its price, then the total.
# Split it:
# 1. loop over the cart: print each item and its price, to 2 places
# 2. print the total of the prices, to 2 places
cart = {"bread": 2.5, "milk": 1.25, "eggs": 3.0}
for item in cart:
    print(f"{item}: {cart[item]:.2f}")
print(f"Total: {sum(cart.values()):.2f}")
```

`:.2f` (lesson 3.3) shows 2.5 as `2.50`. The total can also be added up inside the loop, starting from 0, as in lesson 5.5.

## ch09d-counting#7

```python
def count_words(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

`"".split()` gives back `[]`, so for an empty text the loop never runs, and the empty dictionary comes back. The `if word in counts:` version of the counting pattern works the same.

## ch09d-counting#8

```python
def repeated(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    result = []
    for word, count in counts.items():
        if count > 1:
            result.append(word)
    return result
```

Counting first means each word is a key once, so it goes into the list once, however many times it repeats. The keys are in the order the words first turned up, so the list is too.

## ch09d-counting#9

```python
# Say it: count each letter in the text, with capitals made small and anything else left out.
# Split it:
# 1. start an empty dictionary
# 2. loop over the text, made small, one character at a time
# 3. if the character is a letter, count it
# 4. give the dictionary back
def letter_counts(text):
    counts = {}
    for character in text.lower():
        if character.isalpha():
            counts[character] = counts.get(character, 0) + 1
    return counts
```

`lower()` (lesson 8.2) makes `"A"` and `"a"` the same key, and `isalpha()` (lesson 8.6) skips the spaces, digits and punctuation. Making each character small inside the loop works too.

## ch09e-the-most#5

```python
def top_scorer(scores):
    if len(scores) == 0:
        return None
    return max(scores, key=scores.get)
```

`max()` of an empty dictionary stops with a `ValueError`, as it does for an empty list (lesson 7.5), so the test comes first. On a tie, `max()` gives back the first of the keys, which is what the exercise asks.

## ch09e-the-most#7

```python
def top_three(counts):
    ranked = sorted(counts, key=counts.get, reverse=True)
    return ranked[:3]
```

A slice never runs past the end of a list, so `[:3]` of a list with fewer than three keys gives back all of them, and of `[]` gives back `[]`. No test is needed.

## ch09e-the-most#8

```python
# Say it: give back the character the text has the most of, not counting spaces, or None.
# Split it:
# 1. count the characters that are not spaces
# 2. if nothing was counted, give back None
# 3. give back the key with the biggest count
def most_common(text):
    counts = {}
    for character in text:
        if character != " ":
            counts[character] = counts.get(character, 0) + 1
    if len(counts) == 0:
        return None
    return max(counts, key=counts.get)
```

The keys go into `counts` in the order the characters first appear, so on a tie `max()` gives back the one that appears first. For `""` and `"   "` nothing is counted, and `max()` of an empty dictionary would stop with a `ValueError`: that is why step 2 comes before step 3.

## ch09f-nested#6

```python
students = {
    "Ada": {"grade": 7, "subject": "math"},
    "Grace": {"grade": 8, "subject": "science"},
    "Alan": {"grade": 7, "subject": "art"},
}
for name, details in students.items():
    print(f"{name}: grade {details['grade']}, likes {details['subject']}")
```

`details` is one student's own dictionary, so `details['grade']` is one level down from `students`. `students[name]['grade']` in a loop over the names works too.

## ch09f-nested#7

```python
def class_average(students):
    if len(students) == 0:
        return 0
    total = 0
    for name, details in students.items():
        total += details["score"]
    return total / len(students)
```

Each student's score is one level down, in their own dictionary, so the loop adds up `details["score"]`. `len(students)` counts the students. The test comes first, because dividing by 0 stops with a `ZeroDivisionError`.

## ch09f-nested#8

```python
# Say it: print where and when the club typed in meets, or a message if there is no such club.
# Split it:
# 1. ask for the club's name
# 2. if it is a key of clubs, print the sentence from that club's dictionary
# 3. otherwise, print the message
clubs = {
    "chess": {"room": "B12", "day": "Monday"},
    "drama": {"room": "Hall", "day": "Wednesday"},
    "robots": {"room": "Lab 2", "day": "Friday"},
}
name = input("Club: ")
if name in clubs:
    room = clubs[name]["room"]
    day = clubs[name]["day"]
    print(name, "meets in", room, "on " + day + ".")
else:
    print("No club called " + name + ".")
```

`clubs[name]` is the club's own dictionary, and `["room"]` picks the room out of it: two levels down, one at a time. The `in` test comes first, so a name that is not a key never reaches the lookup.

## ch09h-sets#4

```python
def distinct_count(items):
    return len(set(items))
```

`set()` drops the repeats, so its length is the number of different items. `set([])` is an empty set, of length 0.

## ch09h-sets#8

```python
# Say it: print how many different words the sentence has, with capitals ignored.
# Split it:
# 1. ask for the sentence
# 2. make it small, and split it into words
# 3. make a set of the words
# 4. print how many items the set holds
sentence = input("Sentence: ")
words = sentence.lower().split()
different = set(words)
print("Different words:", len(different))
```

`lower()` comes before the set is made, so `Go` and `go` are the same item. `split()` with nothing in its brackets gives `[]` for an empty sentence, and the set of that holds 0 items.

## ch09i-set-operations#4

```python
def in_both(left, right):
    both = set(left) & set(right)
    return sorted(both)
```

`&` keeps only the names in both sets, and a set holds each name once, so the repeats drop out. `sorted()` gives the names back as a list, in order.

## ch09i-set-operations#5

```python
def only_first(left, right):
    return sorted(set(left) - set(right))
```

`-` keeps the names in the first set that are not in the second, so `left` goes first. `set(right) - set(left)` would give the names only in `right`.

## ch09i-set-operations#9

```python
# Say it: three sorted lists of names, each printed on one line with a label.
# Split it:
# 1. make a set of each list
# 2. the names in both, sorted and joined
# 3. the names only in the first, the same way
# 4. everyone, the same way
first = ["Ada", "Grace", "Alan", "Katherine", "Grace", "Edsger"]
second = ["Grace", "Alan", "Margaret", "Barbara"]
first_set = set(first)
second_set = set(second)
print("Both:", ", ".join(sorted(first_set & second_set)))
print("Only first:", ", ".join(sorted(first_set - second_set)))
print("Everyone:", ", ".join(sorted(first_set | second_set)))
```

`sorted()` turns each set into a list in alphabetical order, and `join()` (lesson 8.8) puts `", "` between the names. The sets drop Grace's repeat, so each line names her once.

## ch09j-the-poll#4

```python
def tally(votes):
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts
```

The counting pattern from lesson 9.4. For `[]`, the loop never runs, and the empty dictionary comes back.

## ch09j-the-poll#5

```python
def winners(counts):
    if len(counts) == 0:
        return []
    best = max(counts.values())
    leaders = []
    for option, count in counts.items():
        if count == best:
            leaders.append(option)
    return leaders
```

`max()` of the values finds the most votes; the loop keeps every option with that many, so a tie keeps them all, in the dictionary's order. `max()` of an empty dictionary's values stops with a `ValueError`, so the test comes first.

## ch09j-the-poll#6

```python
def winner_line(leaders):
    if len(leaders) == 0:
        return "No votes"
    elif len(leaders) == 1:
        return "Winner: " + leaders[0]
    else:
        return "Tied: " + ", ".join(sorted(leaders))
```

`sorted()` gives a new list in alphabetical order, and `join()` (lesson 8.8) puts `", "` between the names. `leaders[0]` is the only leader when there is one.

## ch09j-the-poll#7

```python
# Say it: count the votes, and print a report on them.
# Split it:
# 1. count the votes: tally(votes)
# 2. rank the options, most votes first
# 3. print a line for each option, with report_line()
# 4. print the total, and how many different options got votes
# 5. find every option with the most votes: winners(counts)
# 6. print the winner, or the options that tied: winner_line(leaders)
def report_line(option, count, total):
    """Print one option's line: its votes, its share of all the votes, and a bar."""
    share = count / total * 100
    bar = "#" * round(share / 4)
    print(f"{option:<10}{count:>4}{share:>7.1f}%  {bar}")


votes = [
    "tacos", "pizza", "pizza", "sushi", "pizza",
    "tacos", "salad", "sushi", "pizza", "tacos",
    "sushi", "pizza", "tacos", "pizza", "sushi",
]


def tally(votes):
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts


def winners(counts):
    if len(counts) == 0:
        return []
    best = max(counts.values())
    leaders = []
    for option, count in counts.items():
        if count == best:
            leaders.append(option)
    return leaders


def winner_line(leaders):
    if len(leaders) == 0:
        return "No votes"
    elif len(leaders) == 1:
        return "Winner: " + leaders[0]
    else:
        return "Tied: " + ", ".join(sorted(leaders))


counts = tally(votes)
ranked = sorted(counts, key=counts.get, reverse=True)
for option in ranked:
    report_line(option, counts[option], len(votes))
print("Total votes:", len(votes))
print("Options:", len(set(votes)))
leaders = winners(counts)
print(winner_line(leaders))
```

Tacos and sushi both have 4 votes, and `sorted()` keeps tied keys in the dictionary's order: tacos turned up first. `len(set(votes))` counts the different options, which is the set doing the job it is for. `len(counts)` gives the same number.

## ch09-practice#1

```python
def kind_of(register, ticket):
    if ticket in register:
        return register[ticket]["kind"]
    return None
```

## ch09-practice#2

```python
def with_item(register, ticket, kind, place):
    new_register = register.copy()
    new_register[ticket] = {"kind": kind, "place": place}
    return new_register


register = {"A1": {"kind": "umbrella", "place": "platform 2"}}
bigger = with_item(register, "A2", "phone", "ticket hall")
print(bigger["A2"]["kind"], "found at", bigger["A2"]["place"])
print(len(bigger), "items")
first = with_item({}, "A1", "scarf", "cafe")
print(first["A1"]["kind"], "found at", first["A1"]["place"])
print(register)
```

## ch09-practice#3

```python
def claimed(register, ticket):
    new_register = register.copy()
    if ticket in new_register:
        del new_register[ticket]
    return new_register


register = {
    "A1": {"kind": "umbrella", "place": "platform 2"},
    "A2": {"kind": "phone", "place": "ticket hall"},
}
print(sorted(claimed(register, "A1")))
print(sorted(claimed(register, "A9")))
print(sorted(claimed({}, "A1")))
print(sorted(register))
```

## ch09-practice#4

```python
def count_kinds(register):
    counts = {}
    for details in register.values():
        kind = details["kind"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts
```

## ch09-practice#5

```python
def places(register):
    found_at = []
    for details in register.values():
        found_at.append(details["place"])
    return sorted(set(found_at))
```

## ch09-practice#6

```python
# Say it: a new item and a ticket go in; the claim, or a message that
# there is no such ticket, comes out, then what is still held.
# Split it:
# 1. ask the kind and the place, and add the item under A5
# 2. ask for the ticket
# 3. if it is there: print the claim line, and take the item out
# 4. otherwise: print the no-item line
# 5. count the kinds, and print a line for each
# 6. print the places, joined
def kind_of(register, ticket):
    if ticket in register:
        return register[ticket]["kind"]
    return None


def with_item(register, ticket, kind, place):
    new_register = register.copy()
    new_register[ticket] = {"kind": kind, "place": place}
    return new_register


def claimed(register, ticket):
    new_register = register.copy()
    if ticket in new_register:
        del new_register[ticket]
    return new_register


def count_kinds(register):
    counts = {}
    for details in register.values():
        kind = details["kind"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def places(register):
    found_at = []
    for details in register.values():
        found_at.append(details["place"])
    return sorted(set(found_at))


register = {
    "A1": {"kind": "umbrella", "place": "platform 2"},
    "A2": {"kind": "phone", "place": "ticket hall"},
    "A3": {"kind": "umbrella", "place": "cafe"},
    "A4": {"kind": "scarf", "place": "platform 2"},
}
kind = input("What kind of thing is it? ")
place = input("Where was it found? ")
register = with_item(register, "A5", kind, place)

ticket = input("Ticket? ")
if ticket in register:
    print(f"Claimed: {kind_of(register, ticket)}, found at {register[ticket]['place']}")
    register = claimed(register, ticket)
else:
    print("No item with ticket", ticket)

for kind, count in count_kinds(register).items():
    print(f"{kind}: {count}")
print("Places:", ", ".join(places(register)))
```

## ch09g-copies#4

```python
def add_item(register, item):
    new_register = register.copy()
    new_register[item] = new_register.get(item, 0) + 1
    return new_register


register = {"umbrella": 3, "phone": 1}
print(add_item(register, "phone"))
print(add_item(register, "hat"))
print(register)
```

Without the copy, the first call would change `register` itself, and the second and last lines would show 2 phones. `new_register` is a new dictionary, so the change goes there only.

## ch09g-copies#6

```python
ages = {"Mo": 12, "Kim": 15, "Lee": 11, "Ada": 14, "Bo": 13}
for name in ages.copy():
    if ages[name] < 13:
        del ages[name]
print(ages)
```

The loop goes over a copy, which never changes, and the entries come out of `ages`. Building a new dictionary of the people who are 13 or over works too.

## ch09g-copies#7

```python
def invert(original):
    swapped = {}
    for key, value in original.items():
        swapped[value] = key
    return swapped
```

It has the shape of the `by_capital` example: start empty, and store something worked out from each entry. Here the new key is the old value, and the new value is the old key.

## ch09g-copies#9

```python
# Say it: give back a new register with one fewer of the item, leaving the old one as it was.
# Split it:
# 1. make a copy of the register
# 2. if the item is not in the copy, give the copy back
# 3. if the copy holds exactly 1, take the entry out; otherwise, store one less
# 4. give back the copy
def remove_item(register, item):
    new_register = register.copy()
    if item not in new_register:
        return new_register
    if new_register[item] == 1:
        del new_register[item]
    else:
        new_register[item] = new_register[item] - 1
    return new_register


register = {"umbrella": 3, "phone": 1}
print(remove_item(register, "umbrella"))
print(remove_item(register, "phone"))
print(remove_item(register, "hat"))
print(remove_item({}, "hat"))
print(register)
```

Every change goes to the copy, so the last line still shows the register as it started. It is `take_one()` from lesson 9.2, working on a copy instead of on the dictionary it was handed.

## ch10a-tuples-and-unpacking#4

```python
point = (3, 4)
point = (point[0] + 5, point[1])
print(point)
```

A tuple cannot change, so the fix makes a new one, from the old x plus 5 and the old y, and stores it under the same name.

## ch10a-tuples-and-unpacking#8

```python
full_name = input("Full name: ")
first, last = full_name.split()
print(last + ", " + first)
```

`split()` gives back a list of two words, and unpacking gives the first to `first` and the second to `last`. An f-string, `f"{last}, {first}"`, prints the same.

## ch10a-tuples-and-unpacking#9

```python
# Say it: two numbers go in; they come out on one line, the smaller first.
# Split it:
# 1. ask for the two numbers
# 2. if the first is bigger, swap them
# 3. print them both
first = int(input("First number: "))
second = int(input("Second number: "))
if first > second:
    first, second = second, first
print(first, second)
```

On the swap line, Python works out the right side first: a tuple of the two values, the second first. Only then does it unpack that tuple into `first` and `second`, so neither value is lost. Without unpacking, a swap needs a third name to hold one value while the other moves. When the two numbers are the same, no swap happens, and none is needed.

## ch10c-tuples-in-lists-and-keys#4

```python
cities = [
    ("Paris", 48.9, 2.4),
    ("Tokyo", 35.7, 139.7),
    ("Lima", -12.0, -77.0),
    ("Cairo", 30.0, 31.2),
    ("Oslo", 59.9, 10.8),
]
for name, latitude, longitude in cities:
    print(f"{name} is at {latitude}, {longitude}")
```

The `for` line unpacks each city's tuple into three names, in the order the tuple holds them.

## ch10c-tuples-in-lists-and-keys#5

```python
def destinations(services):
    places = []
    for route, minute, place in services:
        places.append(place)
    return places


services = [("47", 415, "Harbour"), ("12", 380, "Museum"), ("9", 1000, "Airport")]
print(destinations(services))
print(destinations([]))
```

The loop needs a name for every part of the tuple, even the parts it does not use. A list comprehension (lesson 7.9) does the same in one line: `[place for route, minute, place in services]`.

## ch10c-tuples-in-lists-and-keys#8

```python
# Say it: the board goes in; three lines of three squares come out, a mark or a . for each.
# Split it:
# 1. loop over the rows
# 2. build the row's line, one column at a time
# 3. print the line
board = {(0, 0): "X", (1, 1): "O", (2, 2): "X", (0, 2): "O"}
for row in range(3):
    line = ""
    for column in range(3):
        line += board.get((row, column), ".")
    print(line)
```

The example's loop over the columns goes inside a loop over the rows, so `row` takes 0, 1 and 2 in turn. `line` starts empty for each row; if it started once, above both loops, the rows would run together into one long line.

## ch10d-records#4

```python
books = [
    {"title": "Dune", "year": 1965},
    {"title": "Holes", "year": 1998},
]
for book in books:
    print(book["title"])
```

The last line of the error says `KeyError: 'Title'`. The field is `"title"`, with a small t, and capitals matter in a key.

## ch10d-records#6

```python
def average_score(students):
    if students == []:
        return 0
    scores = [student["score"] for student in students]
    return sum(scores) / len(scores)
```

Dividing by `len([])`, which is 0, would stop with a `ZeroDivisionError`, so the empty list is answered first.

## ch10d-records#7

```python
def find_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
    return None
```

If two books have the same title, the first one found comes back, because `return` stops the loop there.

## ch10d-records#9

```python
# Say it: a list of people and an age go in; the names of everyone older than that age come out.
# Split it:
# 1. start an empty list
# 2. loop over the people
# 3. if a person's age is more than age, add their name
# 4. give the list back
def older_than(people, age):
    names = []
    for person in people:
        if person["age"] > age:
            names.append(person["name"])
    return names
```

`>` leaves out someone whose age is exactly `age`: "more than" means strictly more. For an empty list, the loop never runs, and the empty list comes back.

## ch10e-sorting-records#7

```python
def by_year(books):
    return sorted(books, key=lambda book: book["year"])
```

`sorted()` gives back a new list and leaves `books` as it was. Books from the same year keep the order they had, as ties did in lesson 9.5.

## ch10e-sorting-records#8

```python
# Say it: a list of book records goes in; the record of the oldest book comes out, or None.
# Split it:
# 1. if the list is empty, give back None
# 2. otherwise, give back the book with the smallest year
def oldest(books):
    if books == []:
        return None
    return min(books, key=lambda book: book["year"])
```

`min()` of an empty list stops with a `ValueError`, so step 1 comes first. On a tie, `min()` gives back the first of the books it tied on. The whole record comes back, so the caller can read its title, its year, or any other field.

## ch10f-grouping#4

```python
def by_first_letter(words):
    groups = {}
    for word in words:
        letter = word[0]
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(word)
    return groups
```

It is the `by_grade` loop, with the first letter in place of the grade and the word in place of the name. A word that turns up twice goes into its list twice.

## ch10f-grouping#7

```python
def count_routes(routes):
    counts = {}
    for route in routes:
        counts.setdefault(route, 0)
        counts[route] += 1
    return counts
```

`setdefault(route, 0)` stores 0 the first time a route turns up, and does nothing after that, so `+= 1` always has a count to add to. `get(route, 0) + 1`, from lesson 9.4, gives the same dictionary.

## ch10f-grouping#8

```python
# Say it: a list of book records goes in; a dictionary from each author to their titles comes out.
# Split it:
# 1. start an empty dictionary
# 2. loop over the books
# 3. add each book's title to its author's list
# 4. give the dictionary back
def titles_by_author(books):
    groups = {}
    for book in books:
        groups.setdefault(book["author"], []).append(book["title"])
    return groups
```

`setdefault()` gives back the author's list, making an empty one the first time the author turns up, and `append()` adds the title to it. The titles go in the order the books are in, because the loop goes through them in that order.

## ch10g-the-inventory#4

```python
def stock_label(quantity):
    return "OUT OF STOCK" if quantity == 0 else f"{quantity} left"
```

The four-line `if` and `else`, each with its own `return`, gives back the same values.

## ch10g-the-inventory#6

```python
def total_value(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total
```

For an empty list, the loop never runs, and the total stays 0.

## ch10g-the-inventory#7

```python
def low_stock(items, limit):
    low = [item for item in items if item["quantity"] <= limit]
    return sorted(low, key=lambda item: item["quantity"])
```

`<=` keeps an item with exactly `limit` left, as "at or below" says. `sorted()` keeps the order of records whose quantities tie.

## ch10g-the-inventory#8

```python
def by_category(items):
    groups = {}
    for item in items:
        groups.setdefault(item["category"], []).append(item)
    return groups
```

Each list holds whole records, not names, so the report can work out how many items a category has, and what they are worth, with `len()` and `total_value()`.

## ch10g-the-inventory#9

```python
# Say it: print a report on the shop's stock.
# Split it:
# 1. a line for each item, in order of name
# 2. the total value of all the stock
# 3. a line for each item at or below LOW_STOCK, fewest first, with its label
# 4. a line for each category, in order, with its number of items and their value
def item_line(item):
    """Print one item's line: name, category, price, quantity and value."""
    value = item["price"] * item["quantity"]
    words = f"{item['name']:<12}{item['category']:<10}"
    numbers = f"{item['price']:>7.2f}{item['quantity']:>5}{value:>9.2f}"
    print(words + numbers)


LOW_STOCK = 10

inventory = [
    {"name": "Notebook", "category": "paper", "price": 3.50, "quantity": 42},
    {"name": "Pens", "category": "writing", "price": 2.25, "quantity": 10},
    {"name": "Stickers", "category": "paper", "price": 1.75, "quantity": 120},
    {"name": "Backpack", "category": "bags", "price": 34.99, "quantity": 5},
    {"name": "Pencils", "category": "writing", "price": 1.20, "quantity": 3},
    {"name": "Lunch box", "category": "bags", "price": 12.00, "quantity": 0},
    {"name": "Ruler", "category": "writing", "price": 0.85, "quantity": 15},
]


def stock_label(quantity):
    return "OUT OF STOCK" if quantity == 0 else f"{quantity} left"


def total_value(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def low_stock(items, limit):
    low = [item for item in items if item["quantity"] <= limit]
    return sorted(low, key=lambda item: item["quantity"])


def by_category(items):
    groups = {}
    for item in items:
        groups.setdefault(item["category"], []).append(item)
    return groups


for item in sorted(inventory, key=lambda item: item["name"]):
    item_line(item)
print(f"Total value: {total_value(inventory):.2f}")
print(f"Low stock, at or below {LOW_STOCK}:")
for item in low_stock(inventory, LOW_STOCK):
    print(f"{item['name']:<12}{stock_label(item['quantity'])}")
print("By category:")
groups = by_category(inventory)
for category in sorted(groups):
    members = groups[category]
    print(f"{category:<12}{len(members)} items{total_value(members):>9.2f}")
```

`total_value()` is used twice: once on the whole stock, and once on each category's list of records. That is why it takes a list, not one item. If `LOW_STOCK` changes, the low-stock lines and their heading both follow, because the heading prints the constant too.

## ch10-practice#1

```python
def clock_parts(minute):
    hour = minute // 60
    past = minute % 60
    return hour, past


hour, past = clock_parts(415)
print(hour, past)
print(clock_parts(1000))
print(clock_parts(0))
```

`return hour, past` gives back one tuple of two values, and the first line of the calling code unpacks it into two names.

## ch10-practice#2

```python
def clock_parts(minute):
    hour = minute // 60
    past = minute % 60
    return hour, past


def clock(minute):
    hour, past = clock_parts(minute)
    tens = "0" if past < 10 else ""
    return f"{hour}:{tens}{past}"
```

Only the minutes need two digits: the hour is printed as it is, so midnight is `0:00`.

## ch10-practice#3

```python
def clock_parts(minute):
    hour = minute // 60
    past = minute % 60
    return hour, past


def clock(minute):
    hour, past = clock_parts(minute)
    if past < 10:
        return f"{hour}:0{past}"
    return f"{hour}:{past}"


def describe(service):
    route, minute, place = service
    return f"{route} at {clock(minute)} to {place}"


print(describe(("47", 415, "Harbor")))
print(describe(("12", 605, "Museum")))
print(describe(("N1", 0, "Depot")))
```

Unpacking names each part of the service, so the f-string reads as the line it makes.

## ch10-practice#4

```python
def by_time(services):
    return sorted(services, key=lambda service: service[1])


services = [("47", 500, "Harbor"), ("12", 380, "Museum"), ("9", 300, "Airport"), ("47", 415, "Harbor")]
print(by_time(services))
print(by_time([]))
print(services)
```

`sorted()` gives back a new list, so `services` keeps its order. The key is the minute, `service[1]`: with no key, `sorted()` would put route `"12"` before route `"9"`, since it would compare the routes first, as text.

## ch10-practice#5

```python
def clock_parts(minute):
    hour = minute // 60
    past = minute % 60
    return hour, past


def clock(minute):
    hour, past = clock_parts(minute)
    if past < 10:
        return f"{hour}:0{past}"
    return f"{hour}:{past}"


def by_route(services):
    groups = {}
    for route, minute, place in services:
        groups.setdefault(route, []).append(clock(minute))
    return groups
```

`setdefault()` makes each route's empty list the first time the route turns up, as in lesson 10.6.

## ch10-practice#6

```python
# Say it: the services are there already, and a route goes in; the
# timetable in time order comes out, then that route's times, or a
# message that no bus runs on it.
# Split it:
# 1. put the services in time order
# 2. print a line for each one
# 3. group the services in time order by route
# 4. ask for the route
# 5. if it has a group: print its times, joined
# 6. otherwise: print the no-buses line
def clock_parts(minute):
    hour = minute // 60
    past = minute % 60
    return hour, past


def clock(minute):
    hour, past = clock_parts(minute)
    if past < 10:
        return f"{hour}:0{past}"
    return f"{hour}:{past}"


def describe(service):
    route, minute, place = service
    return f"{route} at {clock(minute)} to {place}"


def by_time(services):
    return sorted(services, key=lambda service: service[1])


def by_route(services):
    groups = {}
    for route, minute, place in services:
        groups.setdefault(route, []).append(clock(minute))
    return groups


services = [
    ("47", 500, "Harbor"),
    ("12", 380, "Museum"),
    ("9", 1000, "Airport"),
    ("47", 415, "Harbor"),
    ("12", 605, "Museum"),
]
in_order = by_time(services)
for service in in_order:
    print(describe(service))

groups = by_route(in_order)
route = input("Which route? ")
if route in groups:
    print(f"Route {route}: {', '.join(groups[route])}")
else:
    print("No buses on route", route)
```

The services are grouped after they are put in time order, so each route's times come out in the order they leave. Grouping the list as it started would give route 12's times as `10:05, 6:20`.

## ch10b-two-values#5

```python
def split_price(total_cents):
    dollars = total_cents // 100
    cents = total_cents % 100
    return dollars, cents


dollars, cents = split_price(1250)
print(dollars, cents)
print(split_price(99))
print(split_price(0))
```

It is `split_time()` with 100 in place of 60. The second and third lines print the tuple itself, brackets and all, because nothing unpacks it.

## ch10b-two-values#8

```python
def midpoint(start, end):
    x1, y1 = start
    x2, y2 = end
    return (x1 + x2) / 2, (y1 + y2) / 2


print(midpoint((0, 0), (4, 6)))
print(midpoint((1, 1), (2, 2)))
print(midpoint((3, 5), (3, 5)))
print(midpoint((-4, 2), (4, -2)))
```

`/` always gives back a float, so 2 shows as `2.0`. With `//`, (1, 1) and (2, 2) would give (1, 1), not halfway.

## ch10b-two-values#9

```python
# Say it: two points go in; the length of the straight line between them comes out.
# Split it:
# 1. unpack each point into its x and y
# 2. work out how far across and how far up
# 3. give back the square root of across squared plus up squared
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    across = x2 - x1
    up = y2 - y1
    return (across ** 2 + up ** 2) ** 0.5


print(distance((0, 0), (3, 4)))
print(distance((1, 2), (7, 10)))
print(distance((2, 3), (2, 3)))
print(distance((5, 5), (-7, 0)))
print(round(distance((0, 0), (1, 1)), 3))
```

It does not matter which point comes first: going the other way makes across and up negative, and a negative number squared is positive, so the distance is the same. The square root of 2 has no end to its digits, which is why the last line rounds it.

## ch11a-linear-search#5

```python
def any_over(numbers, limit):
    for number in numbers:
        if number > limit:
            return True
    return False
```

`return False` is below the loop, so it runs only once every number has been looked at. Inside the loop, in an `else`, it would give up after the first number.

## ch11a-linear-search#8

```python
def all_positions(items, target):
    positions = []
    for position in range(len(items)):
        if items[position] == target:
            positions.append(position)
    return positions
```

There is no `break` and no `return` inside the loop: this search keeps going to the end, because every match counts.

## ch11a-linear-search#9

```python
# Say it: a list and a target go in; the position of the first match comes out, or -1.
# Split it:
# 1. loop over the positions
# 2. if the item at a position is the target, give back that position
# 3. below the loop, give back -1
def find_position(items, target):
    for position in range(len(items)):
        if items[position] == target:
            return position
    return -1
```

`return position` ends the search at the first match, so a later match is never reached. For an empty list, `range(0)` gives no positions, the loop never runs, and the function gives back -1. A match at position 0 gives back 0, which is a real position: that is why "not found" is -1, and not 0.

## ch11b-binary-search#4

```python
numbers = [4, 8, 9, 15, 17, 23, 42]
target = 17
low = 0
high = len(numbers) - 1
where = -1
while low <= high:
    middle = (low + high) // 2
    if numbers[middle] == target:
        where = middle
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
print(where)
```

`/` always gives back a float: `(0 + 6) / 2` is `3.0`, and a list cannot be indexed with a float, even one with nothing after the point. `//` gives back the whole number 3.

## ch11b-binary-search#9

```python
# Say it: a sorted list and a target go in; the position of the target comes out, or -1, found by halving.
# Split it:
# 1. low is the first position, high the last
# 2. while low <= high, work out the middle
# 3. if the middle item is the target, give back the middle
# 4. if it is smaller, move low past the middle; otherwise move high before it
# 5. below the loop, give back -1
def binary_search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
```

`return middle` does the job of the example's `break`. For an empty list, `high` starts at -1, so `0 <= -1` is `False`: the loop never runs, and the function gives back -1 without looking at anything. For `[7]`, `low` and `high` are both 0, and `<=` lets that one item be looked at.

## ch11c-counting-the-work#5

```python
def linear_count(items, target):
    comparisons = 0
    for item in items:
        comparisons += 1
        if item == target:
            break
    return comparisons


def binary_count(items, target):
    comparisons = 0
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if items[middle] == target:
            break
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return comparisons


for size in [10, 100, 1000]:
    numbers = [number for number in range(size)]
    print(size, linear_count(numbers, size), binary_count(numbers, size))
```

Ten times the items is ten times the work for a linear search. For a binary search it is about three more passes, because ten is between 8 and 16: three or four doublings.

## ch11c-counting-the-work#8

```python
# Say it: a list's size goes in; the most passes a binary search can make on a list that long comes out.
# Split it:
# 1. start a count at 0
# 2. while the size is more than 0, halve it with // 2 and add one to the count
# 3. give back the count
def halvings(size):
    count = 0
    while size > 0:
        size = size // 2
        count += 1
    return count
```

Each pass of a binary search leaves at most half of what was in play, so the number of halvings is the most passes it can make. `halvings(1000)` gives 10, as in the table, and `halvings(1048576)` gives 21. For 0, the loop never runs: an empty list needs no comparisons.

## ch11d-selection-sort#6

```python
def largest_first(items):
    result = items.copy()
    for start in range(len(result)):
        biggest = start
        for position in range(start + 1, len(result)):
            if result[position] > result[biggest]:
                biggest = position
        result[start], result[biggest] = result[biggest], result[start]
    return result


scores = [60, 95, 82, 95, 70]
print(largest_first(scores))
print(scores)
print(largest_first([]))
print(largest_first([5]))
```

Two changes from the example: `>` instead of `<`, and a name that says what it holds now, `biggest`. Without `copy()`, the function would sort the caller's list itself, and the second line would print it sorted.

## ch11d-selection-sort#8

```python
# Say it: a list goes in; the number of times a selection sort compares two items, sorting it, comes out.
# Split it:
# 1. start a count at 0
# 2. do the selection sort, on a copy
# 3. add one to the count each time two items are compared, just before the if
# 4. give back the count, not the list
def selection_count(items):
    comparisons = 0
    result = items.copy()
    for start in range(len(result)):
        smallest = start
        for position in range(start + 1, len(result)):
            comparisons += 1
            if result[position] < result[smallest]:
                smallest = position
        result[start], result[smallest] = result[smallest], result[start]
    return comparisons
```

The count goes up once each time the inner loop runs, because each pass of it makes one comparison. For 5 items that is 4 + 3 + 2 + 1 + 0. The order of the items never changes the count: a selection sort does the same comparisons on a sorted list as on a jumbled one.

## ch11e-bubble-sort#7

```python
def bubble_swaps(items):
    swaps = 0
    result = items.copy()
    for done in range(len(result)):
        for position in range(len(result) - 1 - done):
            if result[position] > result[position + 1]:
                result[position], result[position + 1] = result[position + 1], result[position]
                swaps += 1
    return swaps
```

The count goes up inside the `if`, next to the swap, so only real swaps count. Stopping early would give the same count: a pass that swaps nothing adds nothing. Two equal neighbors are never swapped, because `>` asks whether the left one is bigger.

## ch11e-bubble-sort#8

```python
# Say it: a list goes in; True comes out if it is in order, smallest first, and False if any neighbor pair is the wrong way round.
# Split it:
# 1. walk along the neighbor pairs, as one pass of a bubble sort does
# 2. as soon as a left item is bigger than its right neighbor, give back False
# 3. below the loop, give back True
def is_sorted(items):
    for position in range(len(items) - 1):
        if items[position] > items[position + 1]:
            return False
    return True
```

One pass, with no swaps: the first pair the wrong way round settles it. Equal neighbors are fine, because `>` asks whether the left one is bigger. For `[]` and `[7]`, `range(len(items) - 1)` gives no positions, the loop never runs, and the answer is `True`.

## ch11f-ties-and-keys#7

```python
# Say it: a list of race records goes in; a new list comes out, fastest first, with ties in alphabetical order of name.
# Split it:
# 1. give back sorted() of the results
# 2. as the key, a lambda that gives back a tuple: the seconds, then the name
def ranked(results):
    return sorted(results, key=lambda record: (record["seconds"], record["name"]))
```

The tuple's first item, the time, decides. Only when two times are equal does the name get a say. A key of the time alone would keep tied runners in the order they were listed, which is not the rule asked for.

## ch11g-insertion-sort#5

```python
def place_after(times, new_time):
    for position in range(len(times)):
        if times[position] > new_time:
            return position
    return len(times)
```

One character changes: `>` walks past every time equal to the new one, so the new time goes after them all.

## ch11g-insertion-sort#6

```python
# Say it: a list goes in; a new sorted list comes out, built by putting each item in at its place.
# Split it:
# 1. copy place_for() in above it
# 2. start an empty list
# 3. for each item, find its place in the new list with place_for(), and insert() it there
# 4. give back the new list
def place_for(times, new_time):
    for position in range(len(times)):
        if times[position] >= new_time:
            return position
    return len(times)


def insertion_sort(items):
    in_order = []
    for item in items:
        in_order.insert(place_for(in_order, item), item)
    return in_order
```

The new list is sorted all the time: it starts empty, which is sorted, and each item goes in at the place that keeps it sorted. The list given to the function is only read, never changed. For `[]`, the loop never runs, and the empty list comes back.

## ch11h-measuring#3

```python
def bubble_count(items):
    comparisons = 0
    result = items.copy()
    for done in range(len(result)):
        swapped = False
        for position in range(len(result) - 1 - done):
            comparisons += 1
            if result[position] > result[position + 1]:
                result[position], result[position + 1] = result[position + 1], result[position]
                swapped = True
        if not swapped:
            break
    return comparisons
```

The count goes up for every comparison, swap or not, so it sits before the `if`. On `[1, 2, 3, 4]`, the first pass makes 3 comparisons and no swaps, and the sort stops: 3. On `[4, 3, 2, 1]`, every pass swaps, and the count is 3 + 2 + 1, as for a selection sort.

## ch11h-measuring#7

```python
# Say it: print how many comparisons each search and sort makes, for lists of 4, 8, 16 and 32 numbers.
# Split it:
# 1. the heading line: row() with the five column names
# 2. for each size, a sorted list of that many numbers, and a copy with its first two numbers swapped
# 3. the searches' counts on the sorted list, for the target size: linear_count(), binary_count()
# 4. the sorts' counts on the nearly sorted list: selection_count(), bubble_count()
# 5. the line for that size: row()
def row(size, linear, binary, selection, bubble):
    """Print one line of the table, each value at the right of a column 10 wide."""
    print(f"{size:>10}{linear:>10}{binary:>10}{selection:>10}{bubble:>10}")


def linear_count(items, target):
    comparisons = 0
    for item in items:
        comparisons += 1
        if item == target:
            break
    return comparisons


def binary_count(items, target):
    comparisons = 0
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if items[middle] == target:
            break
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return comparisons


def selection_count(items):
    comparisons = 0
    result = items.copy()
    for start in range(len(result)):
        smallest = start
        for position in range(start + 1, len(result)):
            comparisons += 1
            if result[position] < result[smallest]:
                smallest = position
        result[start], result[smallest] = result[smallest], result[start]
    return comparisons


def bubble_count(items):
    comparisons = 0
    result = items.copy()
    for done in range(len(result)):
        swapped = False
        for position in range(len(result) - 1 - done):
            comparisons += 1
            if result[position] > result[position + 1]:
                result[position], result[position + 1] = result[position + 1], result[position]
                swapped = True
        if not swapped:
            break
    return comparisons


row("size", "linear", "binary", "selection", "bubble")
for size in [4, 8, 16, 32]:
    numbers = [number for number in range(size)]
    nearly = numbers.copy()
    nearly[0], nearly[1] = nearly[1], nearly[0]
    linear = linear_count(numbers, size)
    binary = binary_count(numbers, size)
    selection = selection_count(nearly)
    bubble = bubble_count(nearly)
    row(size, linear, binary, selection, bubble)
```

Each function was checked on its own before the loop puts them together. Read the columns: doubling the size doubles the linear search's count and adds one to the binary search's. The selection sort's count goes up about four times, whatever order the list is in, while the bubble sort, on a list that is nearly in order, makes two passes and stops.

## ch12a-the-two-parts#7

```python
def stars_down(n):
    if n == 0:
        print("Done.")
    else:
        print("*" * n)
        stars_down(n - 1)


stars_down(3)
stars_down(0)
```

The base case is `n == 0`: print `Done.`, with no more calls. The recursive case prints a row of `n` stars, then calls `stars_down()` with one fewer. `stars_down(0)` goes straight to the base case.

## ch12a-the-two-parts#8

```python
# Say it: print n, then the numbers going down by step, then Liftoff! once the number is 0 or below.
# Split it:
# 1. the base case: if n is 0 or below, print Liftoff!
# 2. the recursive case: otherwise print n, then count down from n - step, by the same step
def count_down_by(n, step):
    if n <= 0:
        print("Liftoff!")
    else:
        print(n)
        count_down_by(n - step, step)


count_down_by(10, 3)
count_down_by(6, 2)
count_down_by(0, 5)
```

`step` is handed on unchanged to every call, as `word` is in `cheer()`, and only `n` gets smaller. The base case is `n <= 0` because 10, 7, 4, 1 jumps from 1 to -2: with `n == 0`, that call would not stop, and nor would any after it. Writing the base case as "not above 0", `if n > 0:` with the two parts the other way round, works the same.

## ch12b-the-way-back#7

```python
def power_of_three(n):
    if n == 0:
        return 1
    else:
        return 3 * power_of_three(n - 1)
```

3 to the power 0 is 1, the base case. Every other call multiplies the smaller call's answer by 3 on the way back: `power_of_three(2)` is 3 * 3 * 1, which is 9.

## ch12b-the-way-back#8

```python
# Say it: a whole number goes in; the sum of 1 up to that number comes out, worked out from a smaller sum.
# Split it:
# 1. the base case: if n is 0, give back 0
# 2. the recursive case: give back n plus the sum up to n - 1
def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)
```

The call table for `sum_to(3)`: it waits for `sum_to(2)`, which waits for `sum_to(1)`, which waits for `sum_to(0)`. The base case gives back 0, and on the way back up the answers are 1 + 0 = 1, then 2 + 1 = 3, then 3 + 3 = 6. A loop that adds up 1 to `n` gives the same answers; here the sum is built from a smaller sum instead.

## ch12c-more-examples#4

```python
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
```

Only `exponent` gets smaller; `base` is handed on unchanged. Anything to the power 0 is 1, which is also the answer that changes nothing when the answers are multiplied on the way back.

## ch12c-more-examples#6

```python
def double_letters(text):
    if text == "":
        return ""
    else:
        return text[0] + text[0] + double_letters(text[1:])
```

`text[0] * 2` works too. Here the first character goes in front of the rest, so the order stays the same; in `reverse()` it went at the end.

## ch12c-more-examples#8

```python
def product(numbers):
    if numbers == []:
        return 1
    else:
        return numbers[0] * product(numbers[1:])
```

The base case gives back 1, as `factorial(0)` does: the answers are multiplied on the way back, and 0 at the bottom would make every product 0.

## ch12c-more-examples#9

```python
# Say it: a list and a target go in; how many times the target is in the list comes out.
# Split it:
# 1. the base case: an empty list holds the target 0 times
# 2. count the first item: 1 if it is the target, 0 if not
# 3. add that to count_item() of the rest of the list, and give it back
def count_item(items, target):
    if items == []:
        return 0
    first_counts = 1 if items[0] == target else 0
    return first_counts + count_item(items[1:], target)
```

It is `total()`, adding a 1 or a 0 for each item instead of the item itself. The conditional expression is lesson 10.7's; an `if` and an `else`, each with its own `return`, work the same.

## ch12d-when-it-goes-wrong#3

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))
print(factorial(0))
```

`factorial(n)` called itself with the same `n`, so the calls never got any smaller and never reached `n == 0`. Handing on `n - 1` moves every call one closer to the base case.

## ch12d-when-it-goes-wrong#7

```python
def sum_to(n):
    if n <= 0:
        return 0
    else:
        return n + sum_to(n - 1)


print(sum_to(3))
```

`sum_to(1)` worked out 1 + 0 and dropped it, so it gave back `None`. Then `sum_to(2)` tried `2 + None`, which is the `TypeError`. With `return` in front, every call gives its answer back to the one waiting above it.

## ch12d-when-it-goes-wrong#8

```python
# Say it: two whole numbers go in; the biggest number that divides both comes out, by Euclid's rule.
# Split it:
# 1. the base case: if b is 0, give back a
# 2. the recursive case: give back the GCD of b and a % b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

The rule turns straight into the two parts. For 12 and 18 the calls are `gcd(12, 18)`, `gcd(18, 12)`, `gcd(12, 6)` and `gcd(6, 0)`, which gives back 6, and every call above it gives that same 6 back up. The second number always shrinks, because a remainder is smaller than what you divide by, so the base case is always reached.

## ch12e-repeated-work#8

```python
# Say it: a number of stairs and a dictionary of answers go in; the number of ways to climb them comes out.
# Split it:
# 1. the base case: 0 or 1 stairs have 1 way
# 2. if n is in known, give back its answer
# 3. otherwise add the ways for n - 1 and n - 2, handing on known
# 4. store the answer in known, then give it back
def ways(n, known):
    if n <= 1:
        return 1
    if n in known:
        return known[n]
    answer = ways(n - 1, known) + ways(n - 2, known)
    known[n] = answer
    return answer
```

It is `fast_fib()` with a different base case: 0 and 1 stairs both give 1, where `fib` gave 0 and 1. So the answers run 1, 1, 2, 3, 5, 8: the Fibonacci numbers again, one place along. Without `known`, `ways(40, {})` would make hundreds of millions of calls; with it, each number of stairs is worked out once.

## ch12f-loop-or-recursion#9

```python
# Say it: a text goes in; True comes out if it reads the same both ways, and False if not.
# Split it:
# 1. the first base case: 0 or 1 letters is always a palindrome
# 2. the second: if the first and last letters differ, it is not
# 3. the recursive case: it is a palindrome if the middle is
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[len(text) - 1]:
        return False
    return is_palindrome(text[1:len(text) - 1])
```

Like `search()`, it has two base cases: one gives the answer `True` when there is nothing left to check, and one gives `False` as soon as two letters differ. Each call checks a text two letters shorter, so the calls always reach one of them. `text[-1]` for the last letter, and `text[1:-1]` for the middle, work the same.

## ch12g-the-capstone#4

```python
def numbered(names):
    lines = []
    for number, name in enumerate(names, start=1):
        lines.append(f"{number}. {name}")
    return lines
```

`start=1` makes the first number 1, so there is no `+ 1` to remember. An empty list never goes round the loop, and `[]` comes back.

## ch12g-the-capstone#5

```python
def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


def ranked(records):
    return sorted(records, key=lambda record: average(record["scores"]), reverse=True)
```

The `lambda` gives back each record's average, so `sorted()` compares averages, and `reverse=True` puts the highest first. `sorted()` keeps records with the same average in the order they were in (lesson 9.5), and gives back a new list, leaving the caller's alone.

## ch12g-the-capstone#6

```python
def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def roster_line(rank, record):
    mean = average(record["scores"])
    return f"{rank:<6}{record['id']:<7}{record['name']:<20}{record['grade']:<4}{mean:>7.1f}{letter_grade(mean):>7}"


print(roster_line(1, {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]}))
print(roster_line(12, {"id": 1010, "name": "New Student", "grade": 9, "scores": []}))
```

The average is worked out once, as `mean`, and used twice: printed with 1 decimal place, and handed to `letter_grade()`. Inside the f-string, the field names are in single quotes, because the f-string itself is in double quotes, as in `item_line()` in lesson 10.7.

## ch12g-the-capstone#7

```python
# Say it: a heading, the students' lines, best average first and numbered from 1, then a closing line.
# Split it:
# 1. print the heading line, and 51 dashes
# 2. loop over the ranked records, numbered from 1, printing each roster_line()
# 3. print 51 dashes again
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


students = [
    {"id": 1001, "name": "Grace Hopper", "grade": 10, "scores": [95, 91, 98]},
    {"id": 1004, "name": "Ada Lovelace", "grade": 9, "scores": [88, 92, 85]},
    {"id": 1007, "name": "Alan Turing", "grade": 9, "scores": [45, 62, 58]},
    {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]},
    {"id": 1009, "name": "Edsger Dijkstra", "grade": 10, "scores": [71, 68, 75]},
]


def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


def ranked(records):
    return sorted(records, key=lambda record: average(record["scores"]), reverse=True)


def roster_line(rank, record):
    mean = average(record["scores"])
    return f"{rank:<6}{record['id']:<7}{record['name']:<20}{record['grade']:<4}{mean:>7.1f}{letter_grade(mean):>7}"


def print_roster(records):
    print(f"{'Rank':<6}{'ID':<7}{'Name':<20}{'Gr':<4}{'Avg':>7}{'Grade':>7}")
    print("-" * 51)
    for rank, record in enumerate(ranked(records), start=1):
        print(roster_line(rank, record))
    print("-" * 51)


print_roster(students)
```

`print_roster()` is short, because each step it needs was built and checked on its own first. The heading lines up with the students' lines because it uses the same column widths, with `<` for the words and `>` for the two columns of numbers. `enumerate(..., start=1)` gives each line its rank.

## ch12h-the-records-system#3

```python
def group_by_grade(records):
    groups = {}
    for record in records:
        groups.setdefault(record["grade"], []).append(record)
    return groups


students = [
    {"id": 1001, "name": "Grace Hopper", "grade": 10, "scores": [95, 91, 98]},
    {"id": 1004, "name": "Ada Lovelace", "grade": 9, "scores": [88, 92, 85]},
    {"id": 1007, "name": "Alan Turing", "grade": 9, "scores": [45, 62, 58]},
    {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]},
    {"id": 1009, "name": "Edsger Dijkstra", "grade": 10, "scores": [71, 68, 75]},
]

groups = group_by_grade(students)
for grade in sorted(groups):
    print(grade, [record["name"] for record in groups[grade]])
print(group_by_grade([]))
```

`setdefault()` gives the grade level an empty list the first time it is seen, and the record is added to that list. The records are added in the order they come, so Ada Lovelace is before Alan Turing.

## ch12h-the-records-system#4

```python
def students_word(count):
    return f"{count} student" if count == 1 else f"{count} students"
```

Only 1 takes the word without an s: 0 students, 2 students, 11 students.

## ch12h-the-records-system#5

```python
def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


def passing_count(records):
    passing = [record for record in records if average(record["scores"]) >= 60]
    return len(passing)
```

`>= 60` makes 60 itself a pass. A record with no scores has an average of 0, so it does not pass, and an empty list gives 0.

## ch12h-the-records-system#7

```python
def search_by_name(records, text):
    return [record for record in records if text.lower() in record["name"].lower()]
```

Both sides are lowered, so `"ER"` finds `"Grace Hopper"`. `""` is in every text, so searching for it keeps every record.

## ch12h-the-records-system#8

```python
def find_by_id(records, student_id):
    """Give back the record with this id, or None. records must be sorted by id."""
    low = 0
    high = len(records) - 1
    while low <= high:
        middle = (low + high) // 2
        if records[middle]["id"] == student_id:
            return records[middle]
        elif records[middle]["id"] < student_id:
            low = middle + 1
        else:
            high = middle - 1
    return None
```

It is lesson 11.2's binary search, comparing ids, and giving back the whole record instead of its position. For an empty list, `high` starts at -1, the loop never runs, and the answer is `None`.

## ch12h-the-records-system#10

```python
# Say it: the roster, the grade levels, the top student and the passing count, a search by name, and two look-ups by id.
# Split it:
# 1. print_roster()
# 2. By grade level:, then a line for each grade level in order
# 3. the top student, with max()
# 4. the passing count
# 5. the names with er
# 6. a copy sorted by id, and a look-up of 1002 and of 9999 in it
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


students = [
    {"id": 1001, "name": "Grace Hopper", "grade": 10, "scores": [95, 91, 98]},
    {"id": 1004, "name": "Ada Lovelace", "grade": 9, "scores": [88, 92, 85]},
    {"id": 1007, "name": "Alan Turing", "grade": 9, "scores": [45, 62, 58]},
    {"id": 1002, "name": "Katherine Johnson", "grade": 11, "scores": [99, 97, 94]},
    {"id": 1009, "name": "Edsger Dijkstra", "grade": 10, "scores": [71, 68, 75]},
]


def average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


def ranked(records):
    return sorted(records, key=lambda record: average(record["scores"]), reverse=True)


def roster_line(rank, record):
    mean = average(record["scores"])
    return f"{rank:<6}{record['id']:<7}{record['name']:<20}{record['grade']:<4}{mean:>7.1f}{letter_grade(mean):>7}"


def print_roster(records):
    print(f"{'Rank':<6}{'ID':<7}{'Name':<20}{'Gr':<4}{'Avg':>7}{'Grade':>7}")
    print("-" * 51)
    for rank, record in enumerate(ranked(records), start=1):
        print(roster_line(rank, record))
    print("-" * 51)


def group_by_grade(records):
    groups = {}
    for record in records:
        groups.setdefault(record["grade"], []).append(record)
    return groups


def students_word(count):
    return f"{count} student" if count == 1 else f"{count} students"


def passing_count(records):
    passing = [record for record in records if average(record["scores"]) >= 60]
    return len(passing)


def search_by_name(records, text):
    return [record for record in records if text.lower() in record["name"].lower()]


def find_by_id(records, student_id):
    """Give back the record with this id, or None. records must be sorted by id."""
    low = 0
    high = len(records) - 1
    while low <= high:
        middle = (low + high) // 2
        if records[middle]["id"] == student_id:
            return records[middle]
        elif records[middle]["id"] < student_id:
            low = middle + 1
        else:
            high = middle - 1
    return None


print_roster(students)

print("By grade level:")
groups = group_by_grade(students)
for grade in sorted(groups):
    members = groups[grade]
    averages = [average(record["scores"]) for record in members]
    print(f"Grade {grade}: {students_word(len(members))}, average {average(averages):.1f}")

best = max(students, key=lambda record: average(record["scores"]))
print(f"Top student: {best['name']} ({average(best['scores']):.1f})")
print(f"Passing: {passing_count(students)} of {len(students)}")

found = search_by_name(students, "er")
names = [record["name"] for record in found]
print("Names with er: " + ", ".join(names))

by_id = sorted(students, key=lambda record: record["id"])
for student_id in [1002, 9999]:
    record = find_by_id(by_id, student_id)
    if record == None:
        print(f"Lookup {student_id}: not found")
    else:
        print(f"Lookup {student_id}: {record['name']}")
```

Every function was built and checked on its own first, so this last step only puts them in order. Each grade level's line needs the average of its students' averages, so `average()` is used twice: once for each student, then once on the list of their averages. `students` is never changed: `ranked()` and the copy sorted by id are new lists, which is why the look-ups can sort one without spoiling the roster.
