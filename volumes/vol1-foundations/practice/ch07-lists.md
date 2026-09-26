## Practice: a playlist manager

A playlist is two lists that travel together: the titles, and how long each one
runs in seconds. Same length, same order, so `titles[2]` and `seconds[2]` are
the same song. You are going to write the handful of functions a playlist app
actually needs.

Everything here uses Chapters 1 to 7: lists, indexing, slicing, `len()`,
`sum()`, `in`, `append()`, `sort()`, `enumerate()` and list comprehensions.

The test playlist:

| Title | Seconds |
| --- | --- |
| Ghost Town | 210 |
| Ribbons | 185 |
| Anvil | 240 |

None of these functions should change the list they are given. A function that
quietly rearranges its caller's playlist is a bug that shows up three screens
later, so where something needs to grow or be reordered, build a new list.

### Steps

1. Write `total_seconds(seconds)` returning the total running time. An empty playlist totals 0, and you should not need a loop.
2. Write `average_seconds(seconds)` returning the mean length, rounded to one decimal place.
3. Write `longest_title(titles)` returning the title with the most characters — the longest *name*, not the longest song.
4. Write `playlist_with(titles, title)` returning a new list with the title added at the end, leaving the original list untouched. `copy()` then `append()`.
5. Write `first_three(titles)` returning the first three titles. A playlist with fewer than three songs should come back whole rather than raising.
6. Write `has_song(titles, title)` returning `True` or `False`.
7. Write `positions(titles, title)` returning a list of every index where that title appears, since a playlist may well repeat a song. An absent title gives an empty list.
8. Write `by_length(titles, seconds)` returning the titles ordered shortest song first. There is no sorting by a key yet, so pair each length with its title in a small list, sort that, and pull the titles back out — a list of pairs sorts by the first item.
