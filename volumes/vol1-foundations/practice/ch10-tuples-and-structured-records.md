## Practice: a bus timetable

A timetable is a pile of records, each one the same shape:

```python
("47", 415, "Harbour")
```

Route, departure, destination. The departure is stored as minutes since
midnight — 415 is 06:55 — because minutes are easy to compare and sort, and
`06:55` is neither. Turning them back into a clock face is a job for the
display, and one of these steps.

Everything here uses Chapters 1 to 10: records, unpacking, `sorted()` with a
key, `setdefault()`, and the conditional expression.

The services to test with:

| Route | Departs | To |
| --- | --- | --- |
| 12 | 380 (06:20) | Museum |
| 47 | 415 (06:55) | Harbour |
| 47 | 500 (08:20) | Harbour |
| 9 | 1000 (16:40) | Airport |

Peak hours are 07:00 to 09:20 and 16:00 to 19:00 — in minutes, 420 up to but
not including 560, and 960 up to but not including 1140.

### Steps

1. Write `route_of(service)` returning the route from one record. Unpack the record into three names rather than reaching in by number, so the next reader can see what the fields are.
2. Write `clock(minutes)` turning minutes since midnight into a `HH:MM` string. Both halves are padded to two digits, so 380 is `06:20` and midnight is `00:00`.
3. Write `destinations(services)` returning every destination served, in alphabetical order, with no repeats.
4. Write `next_after(services, minute)` returning the record of the first bus leaving *strictly after* that minute, or `None` when the day is done. A bus leaving at exactly that minute has gone.
5. Write `by_time(services)` returning the services ordered by departure. `sorted()` takes a `key`.
6. Write `count_by_route(services)` returning a dictionary of route to how many services it runs, built with `setdefault()`.
7. Write `label(minute)` returning `"peak"` or `"off-peak"` for a departure time, as a single conditional expression rather than an `if` block.
8. Write `timetable_lines(services)` returning the printable timetable: one string per service reading `47 06:55 Harbour`, in departure order. Use the functions you already have.
