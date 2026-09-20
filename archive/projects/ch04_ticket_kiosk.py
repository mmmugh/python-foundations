# Calculates a movie ticket price from age and day of the week.

age_input = input("Customer age: ")

if not age_input.isdigit():
    print("Age must be a whole number.")
else:
    age = int(age_input)

    if age > 120:
        print("Please enter a realistic age.")
    else:
        day = input("Day of the week: ").strip().lower()

        if age < 5:
            price = 0
            category = "Infant"
        elif age <= 12:
            price = 8
            category = "Child"
        elif age <= 64:
            price = 14
            category = "Adult"
        else:
            price = 10
            category = "Senior"

        discount = 0
        if day == "tuesday" and price > 0:
            discount = 3
            price -= discount

        print(f"\nCategory: {category}")
        if discount > 0:
            print(f"Tuesday discount: -${discount}")
        print(f"Price: ${price}")
