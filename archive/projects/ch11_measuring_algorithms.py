# Counts the comparisons each algorithm performs at several list sizes.

import random


def linear_search_counted(items, target):
    """Return (index, comparisons) for a linear search."""
    comparisons = 0
    for i in range(len(items)):
        comparisons += 1
        if items[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search_counted(items, target):
    """Return (index, comparisons) for a binary search on a sorted list."""
    low = 0
    high = len(items) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        middle = (low + high) // 2
        if items[middle] == target:
            return middle, comparisons
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1, comparisons


def selection_sort_counted(items):
    """Return (sorted list, comparisons) for a selection sort."""
    result = items.copy()
    comparisons = 0

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            comparisons += 1
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]

    return result, comparisons


def compare_searches(sizes):
    """Print worst-case comparison counts for both searches."""
    print("SEARCHING for a value that is not present (worst case)")
    print(f"{'Size':>10}{'Linear':>10}{'Binary':>10}{'Ratio':>10}")
    print("-" * 40)

    for size in sizes:
        data = list(range(size))
        missing = size + 1
        _, linear = linear_search_counted(data, missing)
        _, binary = binary_search_counted(data, missing)
        print(f"{size:>10}{linear:>10}{binary:>10}{linear / binary:>9.0f}x")


def compare_sorts(sizes):
    """Print comparison counts for selection sort at several sizes."""
    print("\nSORTING a shuffled list")
    print(f"{'Size':>10}{'Comparisons':>14}{'Size squared':>14}")
    print("-" * 38)

    for size in sizes:
        data = list(range(size))
        random.shuffle(data)
        _, comparisons = selection_sort_counted(data)
        print(f"{size:>10}{comparisons:>14}{size * size:>14}")


compare_searches([10, 100, 1000, 10000])
compare_sorts([10, 50, 100, 200])
