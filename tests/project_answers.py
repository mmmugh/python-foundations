"""A second correct solution and a realistic bug for each checked project."""

ALT = {
"ch02-variables-and-types#11": '''customer = input("Customer name: ")
notebook = 3.50
pens = 2.25
stickers = 1.75
total = notebook + pens + stickers
print(f"===== CORNER STORE =====")
print(f"Customer: {customer}")
print(f"Notebook {notebook}")
print(f"Pens {pens}")
print(f"Stickers {stickers}")
print(f"Total {total}")''',

"ch03-expressions-and-operators#13": '''cents = int(input("Amount: "))
quarters, cents = divmod(cents, 25)
dimes, cents = divmod(cents, 10)
nickels, pennies = divmod(cents, 5)
print(f"Quarters {quarters}")
print(f"Dimes {dimes}")
print(f"Nickels {nickels}")
print(f"Pennies {pennies}")''',

"ch04-making-decisions#12": '''age = int(input("Age: "))
day = input("Day: ").strip().lower()
if age < 5:
    category, price = "Infant", 0
elif age <= 12:
    category, price = "Child", 8
elif age <= 64:
    category, price = "Adult", 14
else:
    category, price = "Senior", 10
if day == "tuesday" and price > 0:
    price -= 3
print(f"{category} pays {price}")''',

"ch06-functions#13": '''def ask(prompt):
    while True:
        raw = input(prompt)
        if raw.isdigit() and 0 <= int(raw) <= 100:
            return int(raw)
        print("Please enter a whole number from 0 to 100.")

def grade_of(avg):
    for cut, letter in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if avg >= cut:
            return letter
    return "F"

name = input("Student name: ")
scores = [ask(f"Score {i} of 4: ") for i in range(1, 5)]
average = sum(scores) / len(scores)
print(f"Student: {name}")
print(f"Average: {average}")
print(f"Grade: {grade_of(average)}")''',
}

BUG = {
# adds the prices up wrong, so the total no longer follows from the parts
"ch02-variables-and-types#11": '''customer = input("Customer name: ")
notebook = 3.50
pens = 2.25
stickers = 1.75
print("===== CORNER STORE =====")
print(f"Customer: {customer}")
print("Notebook", notebook)
print("Pens", pens)
print("Stickers", stickers)
print("Total", 7.0)''',

# greedy, but starting from dimes instead of quarters
"ch03-expressions-and-operators#13": '''cents = int(input("Amount: "))
dimes = cents // 10
cents = cents % 10
quarters = cents // 25
cents = cents % 25
nickels = cents // 5
pennies = cents % 5
print(f"Quarters {quarters}")
print(f"Dimes {dimes}")
print(f"Nickels {nickels}")
print(f"Pennies {pennies}")''',

# forgets the Tuesday discount
"ch04-making-decisions#12": '''age = int(input("Age: "))
day = input("Day: ").strip().lower()
if age < 5:
    category, price = "Infant", 0
elif age <= 12:
    category, price = "Child", 8
elif age <= 64:
    category, price = "Adult", 14
else:
    category, price = "Senior", 10
print(f"{category} pays {price}")''',

# never validates, so 105 is accepted as a score
"ch06-functions#13": '''name = input("Student name: ")
scores = [int(input(f"Score {i} of 4: ")) for i in range(1, 5)]
average = sum(scores) / len(scores)
print(f"Student: {name}")
print(f"Average: {average}")''',
}
