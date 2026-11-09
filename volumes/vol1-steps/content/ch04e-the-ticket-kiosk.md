<!-- part: Unit 4 — Making decisions -->
## Lesson 4.5 — The ticket kiosk

This lesson has no new Python in it. You use everything from this unit to build one program yourself, a step at a time, with one more decision in each step.

### Warm-up

1. Predict what this prints, then press Check.

```python
answer = "twelve"
try:
    age = int(answer)
    print("Age:", age)
except ValueError:
    print("Not a whole number.")
```

2. Which test is `True` for a realistic age, from 0 to 120?

### The problem

A cinema wants a kiosk that works out the price of a ticket. These are its rules:

| Age | Price |
| --- | --- |
| under 5 | free |
| 5 to 12 | $8 |
| 13 to 64 | $14 |
| 65 and over | $10 |

On Tuesdays, every paying customer gets $3 off.

You will build it in three steps, running after each one. Step 1 sorts the ages. Step 2 adds the Tuesday discount. Step 3 checks the age before anything else uses it.

### Practice

3. Step 1: ask for the customer's age, as a whole number, and print the price exactly like this: `Price: $8`.

```python
# Say it: work out the price of a cinema ticket from the
# customer's age and the day of the week.
```

> Split it: four prices, so four branches: `if`, two `elif`s and an `else`. The tests overlap, so the narrowest goes first: under 5, then 12 or under, then 64 or under, then everyone else.
> Check it: try an age from each row, then the edges between the rows: 4 and 5, 12 and 13, 64 and 65.

4. Step 2: after the age, ask for the day of the week. On a Tuesday, take $3 off, but only for a paying customer: a free ticket stays free. Print the price as in step 1, like `Price: $11`. Type the day with a capital, `Tuesday`, because capitals matter (lesson 3.5). Copy your step 1 into this box first.

> Split it: work out the price as in step 1, and keep it in a variable; ask for the day; then one more `if`: is it Tuesday, and is the price more than 0? If both are true, take 3 off. Print the price last.
> Check it: try 70 on a Tuesday, which is $7, and 30 on a Monday. Then the awkward one: 3 on a Tuesday. Without the check on the price, a free ticket would cost $-3.

### Edge cases

A free ticket on a Tuesday is an **edge case**: an unusual input, at the edge of the rules, where a program is most likely to go wrong. Edge cases rarely announce themselves. Finding them is what Check it is for.

### Try It

5. Step 3: check the age first. If it is not a whole number, print `Age must be a whole number.` If it is below 0 or above 120, print `Please enter a realistic age.` Only a good age goes on to the day and the price. Copy your program so far into this box first.

> Say it: in your own words, what should the kiosk do with an age it can't use? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: put the whole program in a `try` block, and print the whole-number message in the `except` block. Inside the `try` block, after asking for the age: if it is outside 0 to 120, print the realistic-age message; otherwise, the rest of step 2 goes in the `else` block, one level deeper.
> Name it: the names from steps 1 and 2 still fit: the age, the day and the price. Does each one still say what it holds?
> Check it: try 70 on a Tuesday: $7. Then the awkward ones: banana, -1 and 121; the ends, 0 and 120; and 3 on a Tuesday, which must stay free.

### What you can do now

- Build a program with several decisions, one decision at a time.
- Validate input before the program uses it.
- Find and guard an edge case, like a free ticket on a Tuesday.

Key words: **edge case**.

That is the end of unit 4. Its quiz is below: fill it in, then show or print it.
