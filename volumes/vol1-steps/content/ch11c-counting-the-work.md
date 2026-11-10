<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.3 — Counting the work

In lesson 11.2, a binary search found 23 in two passes, where a linear search would have looked at six items. Is that a small saving, or a big one? In this lesson you count the work each search does, and build a table of counts that answers it.

### Warm-up

1. Predict what this prints, then press Check.

```python
numbers = [3, 6, 9, 12, 15]
target = 12
low = 0
high = len(numbers) - 1
while low <= high:
    middle = (low + high) // 2
    print(middle)
    if numbers[middle] == target:
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
```

2. A binary search is given the list `[9, 3, 7]`, which is not sorted. What can happen?

### Counting comparisons

Each time a search checks one item against the target, that is one **comparison**. To count them, add a counter that goes up by one each time round the loop:

```python
def linear_count(items, target):
    comparisons = 0
    for item in items:
        comparisons += 1
        if item == target:
            break
    return comparisons


numbers = [17, 4, 23, 8, 42, 15, 9]
print(linear_count(numbers, 17))
print(linear_count(numbers, 42))
print(linear_count(numbers, 99))
```

Output:

```
1
5
7
```

The function gives back the count, not the position, so `break` ends the loop and the count is given back below it. When the target is the first item, one comparison does it: the **best case**. When the target is not there, every item gets a comparison, 7 here: the **worst case**. The worst case is the number you can promise, because it is never more: a linear search makes at most one comparison per item.

### Practice

3. Predict what this prints, then press Check.

```python
def linear_count(items, target):
    comparisons = 0
    for item in items:
        comparisons += 1
        if item == target:
            break
    return comparisons


print(linear_count([5, 1, 5], 5))
print(linear_count([5, 1, 5], 1))
print(linear_count([2, 4, 6, 8, 10, 12], 7))
print(linear_count([], 7))
```

4. When does a linear search make the fewest comparisons?

### Counting a binary search

A binary search looks at one item on each pass, the middle one. It may ask two questions about it, `==` and then `<`, but it is one item looked at, so count one comparison per pass:

```python
def binary_count(items, target):
    comparisons = 0
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if items[middle] == target:
            break
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return comparisons


numbers = [4, 8, 9, 15, 17, 23, 42]
print(binary_count(numbers, 15))
print(binary_count(numbers, 23))
print(binary_count(numbers, 99))
```

Output:

```
1
2
3
```

### A table of counts

Now count both searches on bigger and bigger sorted lists. `[number for number in range(size)]` makes a sorted list of `size` numbers, from 0 up, and the target `size` is bigger than all of them, so it is not there: the worst case for both. The two functions are the ones above:

```python
def linear_count(items, target):
    comparisons = 0
    for item in items:
        comparisons += 1
        if item == target:
            break
    return comparisons


def binary_count(items, target):
    comparisons = 0
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if items[middle] == target:
            break
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return comparisons


for size in [8, 16, 32, 64]:
    numbers = [number for number in range(size)]
    print(size, linear_count(numbers, size), binary_count(numbers, size))
```

Output:

```
8 8 4
16 16 5
32 32 6
64 64 7
```

Read down the columns. Each time the list doubles, the linear search's count doubles too. The binary search's count goes up by only one: one more pass cuts the extra half away. That is because each pass leaves at most half of what was in play: from 7 items, at most 3 are left once the middle is out, then 1, then none. Keep doubling up to 1,048,576 items, about a million, and a linear search makes 1,048,576 comparisons. A binary search makes 21.

A dictionary does better still. It does not look through its keys one at a time at all: it goes straight to the key. So a lookup takes about the same time however many keys there are. That is why a dictionary was the container for looking things up by name in unit 9.

### Practice

5. Under the two functions, add a loop that prints a row for each of the sizes 10, 100 and 1000: the size, the linear search's count and the binary search's count, each for the target `size`, as in the table above. The first row is `10 10 4`.

```python
def linear_count(items, target):
    comparisons = 0
    for item in items:
        comparisons += 1
        if item == target:
            break
    return comparisons


def binary_count(items, target):
    comparisons = 0
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if items[middle] == target:
            break
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return comparisons
```

> Split it: the example's loop, with the three sizes in its list.

6. A binary search of a sorted list of 64 items makes at most 7 comparisons. At most how many does it make for a sorted list of 128 items?

7. Why does looking up a key in a dictionary stay quick, however many keys it holds?

### Try It

8. Write a function `halvings(size)` that gives back the most comparisons a binary search can make on a sorted list of `size` items. That is how many times you can halve `size` with `// 2` before nothing is left: 7, then 3, then 1, then 0 is 3 halvings, so `halvings(7)` gives 3.

> Say it: a list's size goes in; the most passes a binary search can make on a list that long comes out. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. start a count at 0. 2. while the size is more than 0, halve it with `// 2` and add one to the count. 3. give back the count.
> Name it: the function and its parameter are named for you. What would you call the count?
> Check it: try 7, which gives 3, and 8, which gives 4, as in the table. Then the awkward ones: 0, an empty list, which gives 0, and 1, which gives 1.

### What you can do now

- Count the comparisons a search makes, with a counter in its loop.
- Tell the best case from the worst case, and say which one you can promise.
- Read a table of counts: doubling the list doubles a linear search's work, and adds one pass to a binary search.

Key words: **comparison**, **best case**, **worst case**.
