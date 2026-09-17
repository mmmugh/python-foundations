"""Chapter 6 - Functions

Every worked example from the chapter.
"""

# --- Defining and calling --------------------------------------------------


def greet_plain():
    print("Hello!")
    print("Welcome to the program.")


greet_plain()
greet_plain()


# --- Parameters ------------------------------------------------------------


def greet(name):
    print(f"Hello, {name}!")


greet("Ada")
greet("Grace")


def describe_rectangle(width, height):
    print(f"A {width} by {height} rectangle has area {width * height}.")


describe_rectangle(7, 4)
describe_rectangle(4, 7)


def greet_with(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet_with("Ada")
greet_with("Ada", "Good morning")


# --- Return values ---------------------------------------------------------


def area(width, height):
    return width * height


room = area(12, 10)
print(f"The room is {room} square feet.")
print(f"Two rooms would be {area(12, 10) * 2} square feet.")


def double_print(n):
    print(n * 2)


def double_return(n):
    return n * 2


a = double_print(5)
b = double_return(5)

print("a is", a)
print("b is", b)


def safe_divide(a, b):
    if b == 0:
        return None
    return a / b


print(safe_divide(10, 2))
print(safe_divide(10, 0))


def split_time(total_seconds):
    return total_seconds // 60, total_seconds % 60


minutes, seconds = split_time(500)
print(f"{minutes} minutes and {seconds} seconds")


# --- Scope -----------------------------------------------------------------


def calculate():
    result = 42
    return result


print(calculate())

# The next line would raise NameError, because `result` lived only inside
# the function. Uncomment it to see the error for yourself.
# print(result)


# --- Docstrings ------------------------------------------------------------


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit.__doc__)


# --- Decomposition: Chapter 4's kiosk, rewritten ---------------------------


def base_price(age):
    """Return the ticket price in dollars for a customer of the given age."""
    if age < 5:
        return 0
    elif age <= 12:
        return 8
    elif age <= 64:
        return 14
    else:
        return 10


def apply_discount(price, day):
    """Return the price after any day-of-week discount."""
    if day == "tuesday" and price > 0:
        return price - 3
    return price


def ticket_price(age, day):
    """Return the final ticket price for an age and day."""
    return apply_discount(base_price(age), day)


print(ticket_price(70, "tuesday"))
print(ticket_price(3, "tuesday"))
print(ticket_price(30, "friday"))


# --- Try It #6: what does this print, and why? -----------------------------


def add_ten(n):
    n = n + 10


x = 5
add_ten(x)
print(x)
