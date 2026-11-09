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
