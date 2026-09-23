## Practice: a film club flyer

The Riverside Film Club needs a flyer for Friday's showing, and the person who
used to make them has left. You are going to print one, a piece at a time,
until the whole thing comes out in one go.

Everything here uses only what Chapter 1 covered: `print()`, text in quotes,
arithmetic, and a comment. No variables — those arrive in Chapter 2.

This is what you are working towards:

```
======================================
         RIVERSIDE FILM CLUB
======================================

Feature:  The Quiet Harbour  (1998)
When:     Friday, 7:30 pm
Where:    Room 14

Seats available: 96
Snack bar total: 17.25

======================================
```

Two of those numbers are not typed in. The club has **8 rows of 12 seats**, and
Friday's snack order is **3 boxes of popcorn at 3.75 each and 2 drinks at 3.00
each**. Let Python do that arithmetic — if the price changes, you want to edit
one number, not recount.

### Steps

1. Start with the banner. Print the rule, the club name, and the rule again — three lines, exactly as they appear above. The rule is 38 equals signs, and the club name is indented by nine spaces.
2. Print the feature line: `Feature:  The Quiet Harbour  (1998)`. Use a single `print()` with one string.
3. Now the same line again, but let `print()` do the spacing: pass `Feature:` and `The Quiet Harbour  (1998)` as **two arguments** separated by a comma, and notice that you get one space between them rather than two.
4. Print the two booking lines together, `When:` and `Where:`, as two separate `print()` calls, lining the values up under each other exactly as in the flyer.
5. Print the seat count as `Seats available: 96` — but work out the 96 with a calculation from 8 rows of 12 seats, not by typing it.
6. Print the snack total as `Snack bar total: 17.25`, again calculated: 3 boxes of popcorn at 3.75, plus 2 drinks at 3.00.
7. Put the whole flyer together in one program, blank lines and all, with a comment on the first line saying what it prints. Every line of the target output, in order.
