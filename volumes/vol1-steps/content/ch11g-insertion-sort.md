<!-- part: Unit 11 — Searching and sorting -->
## Lesson 11.7 — Where a new item goes, and insertion sort

Race times arrive one at a time, and the list of them should stay sorted as they do. In this lesson you find where a new item goes in a sorted list, decide where a tie goes, and then sort a whole list that way.

### Warm-up

1. Predict what this prints, then press Check.

```python
names = ["bo", "Al", "cy"]
print(sorted(names, key=str.lower))
print((1, "b") < (1, "a"))
print(sorted([(2, "b"), (1, "z"), (2, "a")]))
```

2. `sorted()` is given two records that tie on its key. Which comes first?

### Where a new item goes

A new time has to go into a sorted list of times, and keep it sorted. A linear search finds its place: the position of the first time that is not smaller than it. If there is none, it goes at the end:

```python
def place_for(times, new_time):
    for position in range(len(times)):
        if times[position] >= new_time:
            return position
    return len(times)


times = [57.4, 58.2, 61.0]
print(place_for(times, 59.0))
print(place_for(times, 58.2))
print(place_for(times, 70.0))
times.insert(place_for(times, 59.0), 59.0)
print(times)
```

Output:

```
2
1
3
[57.4, 58.2, 59.0, 61.0]
```

The tie rule is in the `>=`. A new time equal to one already there stops the search at that one, so it goes before it: 58.2 goes in at position 1, ahead of the 58.2 already there. With `>`, it would go after. Either rule can be right, but a program has to pick one, and say which.

### Practice

3. Predict what this prints, then press Check.

```python
def place_for(times, new_time):
    for position in range(len(times)):
        if times[position] >= new_time:
            return position
    return len(times)


times = [10, 20, 20, 30]
print(place_for(times, 20))
print(place_for(times, 5))
print(place_for(times, 35))
print(place_for([], 7))
```

4. In `place_for()`, `>=` is changed to `>`. Where does a new time of 20 go in `[10, 20, 20, 30]` now?

5. Write a function `place_after(times, new_time)` that gives back the position where `new_time` goes in the sorted list `times`, with the other tie rule: a new time equal to one already there goes after it. So `place_after([10, 20, 30], 20)` gives 2.

> Split it: `place_for()` with one change: stop at the first time that is bigger than the new one.
> Check it: try `[10, 20, 20, 30]` with 20, which gives 3, after both 20s. Then the awkward ones: `[]` with 7, which gives 0, and a time bigger than all of them, which gives the length of the list.

### Putting each item in its place

`place_for()` and `insert()` keep a sorted list sorted as items arrive. Start with an empty list, which is sorted, and put the items in one at a time, each at its place: the list is sorted after every step, so it is sorted at the end. Sorting this way is called **insertion sort**. It is how many people sort a hand of cards as they are dealt.

### Try It

6. Write a function `insertion_sort(items)` that gives back a new sorted list of the items. Start with an empty list, and put each item into it at its place, found with `place_for()`.

> Say it: a list goes in; a new sorted list comes out, built by putting each item in at its place. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: 1. copy `place_for()` in above it. 2. start an empty list. 3. for each item, find its place in the new list with `place_for()`, and `insert()` it there. 4. give back the new list.
> Name it: the function and its parameter are named for you. What would you call the new list?
> Check it: try `[5, 2, 9, 1]`, which gives `[1, 2, 5, 9]`, and `[2, 1, 2]`, which gives `[1, 2, 2]`. Then the awkward ones: `[]`, which gives `[]`, and `[3]`.
> Did it sort by insertion? While you try it, put `print(in_order)` (or whatever you named the new list) after each `insert()`: it grows by one item at a time, in order every time. Take the print out before you press Check.

### What you can do now

- Find where a new item goes in a sorted list, with `place_for()`.
- Say where a tie goes, and change the rule.
- Sort by insertion, keeping a list sorted as items arrive.

Key words: **insertion sort**.
