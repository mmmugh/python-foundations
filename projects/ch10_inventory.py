# An inventory of items stored as records, with reports.

inventory = [
    {"name": "Notebook", "category": "paper", "price": 3.50, "quantity": 42},
    {"name": "Pens", "category": "writing", "price": 2.25, "quantity": 8},
    {"name": "Stickers", "category": "paper", "price": 1.75, "quantity": 120},
    {"name": "Backpack", "category": "bags", "price": 34.99, "quantity": 5},
    {"name": "Pencils", "category": "writing", "price": 1.20, "quantity": 3},
    {"name": "Lunch box", "category": "bags", "price": 12.00, "quantity": 0},
]

LOW_STOCK = 10


def item_value(item):
    """Return the total value of one item's stock."""
    return item["price"] * item["quantity"]


def total_value(items):
    """Return the total value of all stock."""
    total = 0.0
    for item in items:
        total += item_value(item)
    return total


def low_stock(items, threshold):
    """Return the items at or below a stock threshold, fewest first."""
    low = [i for i in items if i["quantity"] <= threshold]
    return sorted(low, key=lambda i: i["quantity"])


def by_category(items):
    """Return a dictionary mapping each category to its items."""
    groups = {}
    for item in items:
        groups.setdefault(item["category"], []).append(item)
    return groups


def print_inventory(items):
    """Print the full inventory table."""
    print(f"{'Item':<12}{'Category':<10}{'Price':>8}{'Qty':>6}{'Value':>10}")
    print("-" * 46)
    for item in sorted(items, key=lambda i: i["name"]):
        print(
            f"{item['name']:<12}{item['category']:<10}"
            f"${item['price']:>7.2f}{item['quantity']:>6}"
            f"${item_value(item):>9.2f}"
        )
    print("-" * 46)
    print(f"{'TOTAL':<36}${total_value(items):>9.2f}")


def print_alerts(items):
    """Print low-stock and out-of-stock warnings."""
    print(f"\nLow stock (at or below {LOW_STOCK}):")
    for item in low_stock(items, LOW_STOCK):
        state = "OUT OF STOCK" if item["quantity"] == 0 else f"{item['quantity']} left"
        print(f"  {item['name']:<12}{state}")


def print_categories(items):
    """Print a summary of each category."""
    print("\nBy category:")
    groups = by_category(items)
    for category in sorted(groups):
        members = groups[category]
        value = total_value(members)
        print(f"  {category:<10}{len(members)} items{value:>10.2f}")


print_inventory(inventory)
print_alerts(inventory)
print_categories(inventory)
