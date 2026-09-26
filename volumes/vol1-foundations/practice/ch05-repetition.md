## Practice: a savings goal tracker

The bike costs **240**. You put something aside each week, and you want to know
when you will have it — not roughly, but which week.

Everything here uses Chapters 1 to 5: variables, `input()`, arithmetic,
f-strings, `if`, and now `while`, `for`, `range()`, `break` and `continue`.
There are no lists yet, so the running total lives in a single variable that
you add to as you go — the accumulator pattern from the chapter.

Each step is the same question with one thing changed, so the answer moves:

| Saving 15 a week | Weeks to reach 240 |
| --- | --- |
| Straightforwardly | 16 |
| Skipping every 5th week | 19 |
| With a 10 bonus every 4th week | 14 |
| With 1% interest added weekly | 15 |

### Steps

1. Print `Week 1` through `Week 8`, one per line, with a `for` loop and `range()`. Eight lines, and no eight in your code.
2. Ask how much goes in each week, then print the running total at the end of each of the first 8 weeks. Keep one variable and add to it — do not recalculate from scratch each time.
3. Ask the weekly amount again and use a `while` loop to find how many weeks it takes to reach 240. Print the number of weeks. Reaching exactly 240 counts.
4. A `while` loop that never reaches its goal runs forever. Do the same thing with a `for` loop over 52 weeks and a `break` when the goal is met. Report *after* the loop rather than inside it: print `Reached in week N`, or `Not this year` if the 52 weeks run out. Reporting from inside the loop is the bug this step is about — without the `break` it announces success every week from the 16th on.
5. Every 5th week the money goes on something else. Using `continue`, skip weeks 5, 10, 15 and so on — nothing saved, nothing lost — and print which week the goal is reached.
6. Instead, a 10 bonus lands every 4th week — weeks 4, 8, 12 — on top of the usual amount. Print which week the goal is reached now. Be careful which weeks you mean: paying it on weeks 1, 5 and 9 instead gives the same answer for a lot of weekly amounts, and a different one for the rest.
7. The account pays 1% a week, added after your deposit goes in. Print which week the goal is reached.
8. Put the tracker together: ask for the weekly amount, then print the balance at the end of each of the first 8 weeks, and then the week the goal is reached, counting the bonus every 4th week and skipping every 5th.
