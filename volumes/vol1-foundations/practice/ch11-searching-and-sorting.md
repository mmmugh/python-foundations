## Practice: a race leaderboard

The parkrun finishes and somebody has a clipboard of names and times in the
order people crossed the line, which is very nearly the order you want but not
quite — the timekeeper writes them down as they are handed in. A result is a
record:

```python
("Priya", 57.4)
```

Name, and seconds. You are going to build the leaderboard.

Everything here uses Chapters 1 to 11: lists, records, `sorted()` with a key,
and the searching and sorting from this chapter.

The results to test with, in the order they were handed in:

| Name | Seconds |
| --- | --- |
| Nadia | 58.2 |
| Omar | 61.0 |
| Priya | 57.4 |
| Quinn | 63.5 |

Nothing here may assume the results arrive in order, because they do not.

### Steps

1. Write `fastest_name(results)` returning the name of the winner. The fastest time is the smallest number.
2. Write `ranked(results)` returning the results ordered fastest first.
3. Write `place_of(results, name)` returning what place somebody finished in, counting from 1, or `None` for a name that did not run.
4. Write `result_for(results, name)` returning that runner's whole record, or `None`. This is a linear search: the results are not sorted by name, so there is nothing cleverer available.
5. A separate screen keeps the finishing times in a sorted list and needs to slot new ones in. Write `insertion_point(times, target)` returning the index where the target belongs to keep the list sorted, using a binary search rather than scanning. A time equal to one already there goes *before* it.
6. Write `podium(results)` returning the first three names, fastest first. A race with fewer than three finishers returns as many as there were.
7. Write `sort_times(times)` returning the times in order, sorted by hand with the algorithm from the chapter rather than by calling `sorted()`. Leave the list you were given alone.
8. Write `leaderboard_lines(results)` returning the printable leaderboard, one string per runner reading `1. Priya 57.4`, in finishing order.
