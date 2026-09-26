## Practice: a hiking trip planner

The Kettle Ridge trail is 12.4 km, and every time somebody plans a day on it
they do the same sums on the back of an envelope: how long it takes, how much
water to carry, what the permits come to. You are going to write the planner.

Everything here uses only Chapters 1 and 2: variables, `input()`, `int()` and
`float()`, and arithmetic. No f-strings and no `if` — those are Chapters 3 and
4, so every line you print is built from `print()` with commas.

The numbers the planner works from:

| Quantity | Value |
| --- | --- |
| Trail length | 12.4 km |
| Water | 0.75 litres per hour of walking |
| Permit | 4.50 per person |

Walking pace varies by person, so that one is always asked for, in minutes per
kilometre. A steady walker does about 11.

### Steps

1. Put the trail name `Kettle Ridge` and its length `12.4` into two variables, then print `Kettle Ridge is 12.4 km` from them. Pass the pieces to `print()` separated by commas and let it supply the spaces.
2. Ask for a walking pace in minutes per kilometre and print how many minutes the trail takes. Remember that `input()` hands back a string: multiply 12.4 by that string and Python will complain, so convert it first.
3. Minutes are hard to picture. Print the time in hours as well as minutes, by dividing.
4. Work out the water. At 0.75 litres for every hour walked, print how many litres one person needs — and note that it is litres per *hour*, not per minute.
5. Ask how many people are going, and print the water the group needs altogether.
6. Print what the permits cost, at 4.50 each.
7. Put the planner together: ask for the trail length, the pace, and the group size, then print the length, the time in minutes, the time in hours, the water for one person, the water for the group, and the permit total.
