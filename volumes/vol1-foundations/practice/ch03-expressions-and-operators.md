## Practice: a pizza party splitter

Games night, and somebody has to work out how many pizzas to order and what
everyone owes. It is the same argument every month. You are going to settle it
with a program.

The shop sells one size: **8 slices, 13.50 a pizza**, whole pizzas only.

Everything here uses Chapters 1 to 3: variables, `input()`, arithmetic,
`//` and `%`, `**`, f-strings, `round()`, and the comparison operators. There
is still no `if` — that is Chapter 4 — so where this asks a yes-or-no question,
print the comparison itself and let it show `True` or `False`.

One trick you will need in step 2. Ordering whole pizzas means rounding *up*,
and `//` always rounds down. Adding 7 before dividing by 8 fixes that: 15
slices becomes `22 // 8`, which is 2. Any number of slices that is already a
multiple of 8 is unaffected.

### Steps

1. Ask how many people are coming and how many slices each one eats, then print the total number of slices needed. Both answers are whole numbers.
2. Print how many whole pizzas to order, rounding up as described above.
3. Print how many slices will be left in the boxes afterwards — that is, the slices ordered minus the slices eaten.
4. Print what the order costs at 13.50 a pizza, to two decimal places. An f-string with `:.2f` does the formatting.
5. Print what each person owes, split evenly and rounded to the nearest penny.
6. Print whether a single pizza would have been enough, as a comparison that shows `True` or `False`.
7. The shop adds 15% for delivery. Print the new total and the new share each, both to two decimal places.
8. Put it together: ask for the two numbers, then print the slices needed, the pizzas to order, the slices left over, the cost, the delivery total, and what each person owes with delivery included.
