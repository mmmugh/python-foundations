"""Chapter 11 - Searching and Sorting

Every worked example from the chapter.
"""

# --- Linear search ---------------------------------------------------------


def linear_search(items, target):
    """Return the index of target in items, or -1 if it is absent."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


numbers = [17, 4, 23, 8, 42, 15, 9]

print(linear_search(numbers, 42))
print(linear_search(numbers, 99))


# --- Binary search ---------------------------------------------------------


def binary_search(items, target):
    """Return the index of target in a SORTED list, or -1 if it is absent."""
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


numbers = [4, 8, 9, 15, 17, 23, 42]

print(binary_search(numbers, 42))
print(binary_search(numbers, 4))
print(binary_search(numbers, 99))


def binary_search_verbose(items, target):
    """Binary search that prints each step."""
    low = 0
    high = len(items) - 1
    step = 0

    while low <= high:
        step += 1
        middle = (low + high) // 2
        print(f"Step {step}: checking index {middle} (value {items[middle]}), "
              f"{high - low + 1} items still in range")

        if items[middle] == target:
            return middle
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


numbers = list(range(0, 100, 2))
result = binary_search_verbose(numbers, 74)
print(f"Found at index {result}")


# --- Selection sort --------------------------------------------------------


def selection_sort(items):
    """Return a new sorted list, using selection sort."""
    result = items.copy()

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]

    return result


print(selection_sort([64, 25, 12, 22, 11]))


def selection_sort_verbose(items):
    """Selection sort that shows the list after each pass."""
    result = items.copy()

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
        sorted_part = " ".join(str(v) for v in result[:i + 1])
        rest = " ".join(str(v) for v in result[i + 1:])
        print(f"Pass {i + 1}: [{sorted_part}] {rest}")

    return result


selection_sort_verbose([64, 25, 12, 22, 11])


# --- Bubble sort -----------------------------------------------------------


def bubble_sort(items):
    """Return a new sorted list, using bubble sort with early exit."""
    result = items.copy()
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


print(bubble_sort([64, 25, 12, 22, 11]))
print(bubble_sort([1, 2, 3, 4, 5]))


# --- What Python actually does ---------------------------------------------

numbers = [64, 25, 12, 22, 11]

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(["banana", "Apple", "cherry"], key=str.lower))
