"""Chapter 12 - Recursion and Problem Solving

Every worked example from the chapter.
"""

# --- Factorial, two ways ---------------------------------------------------


def factorial_loop(n):
    """Return n! using a loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial(n):
    """Return n! using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial_loop(5))
print(factorial(5))


# --- Following the calls ---------------------------------------------------


def factorial_traced(n, depth=0):
    """Factorial that shows each call and each return."""
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")

    if n <= 1:
        print(f"{indent}base case, returning 1")
        return 1

    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{indent}returning {n} * factorial({n - 1}) = {result}")
    return result


factorial_traced(4)


# --- More examples ---------------------------------------------------------


def total(numbers):
    """Return the sum of a list, recursively."""
    if not numbers:
        return 0
    return numbers[0] + total(numbers[1:])


print(total([1, 2, 3, 4, 5]))


def reverse(text):
    """Return the text reversed, recursively."""
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


print(reverse("recursion"))


def countdown(n):
    """Print a countdown from n to 1, then Liftoff."""
    if n <= 0:
        print("Liftoff.")
        return
    print(n)
    countdown(n - 1)


countdown(3)


# --- When recursion goes wrong: Fibonacci ----------------------------------


def fib(n):
    """Return the nth Fibonacci number. Correct, but very slow."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(fib(i), end=" ")
print()


def fib_fast(n, memo=None):
    """Return the nth Fibonacci number, remembering previous results."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_fast(n - 1, memo) + fib_fast(n - 2, memo)
    return memo[n]


print(fib_fast(50))
print(fib_fast(90))


def fib_loop(n):
    """Return the nth Fibonacci number, using a loop."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib_loop(50))


# --- Binary search, recursively --------------------------------------------


def binary_search(items, target, low=0, high=None):
    """Return the index of target in a sorted list, or -1 if absent."""
    if high is None:
        high = len(items) - 1

    if low > high:
        return -1

    middle = (low + high) // 2

    if items[middle] == target:
        return middle
    elif items[middle] < target:
        return binary_search(items, target, middle + 1, high)
    else:
        return binary_search(items, target, low, middle - 1)


numbers = [4, 8, 9, 15, 17, 23, 42]
print(binary_search(numbers, 23))
print(binary_search(numbers, 5))
