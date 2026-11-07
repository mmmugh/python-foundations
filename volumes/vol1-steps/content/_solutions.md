<!-- Worked solutions for vol1-steps, one "## <page>#<n>" heading each. Never published. -->

## ch01z-welcome-back#2

```python
print("cats", "dogs")
```

## ch01z-welcome-back#3

```python
# minutes in a week
print(7 * 24 * 60)
```

## ch01z-welcome-back#5

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the pencils line
# 2. print the eraser line
# 3. print the total, worked out by Python
print("2 pencils at 1 dollar each")
print("1 eraser at 3 dollars")
print("Total:", 2 * 1 + 3)
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
