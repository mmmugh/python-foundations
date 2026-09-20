# Breaks an amount of cents into the fewest US coins, largest first.

cents = int(input("Amount in cents: "))
original = cents

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
pennies = cents % 5

print(f"\n{original} cents = ${original / 100:.2f}")
print(f"Quarters: {quarters}")
print(f"Dimes:    {dimes}")
print(f"Nickels:  {nickels}")
print(f"Pennies:  {pennies}")
print(f"Total coins: {quarters + dimes + nickels + pennies}")
