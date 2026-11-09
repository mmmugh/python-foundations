<!-- part: Unit 2 — Variables and types -->
## Lesson 2.4 — Putting it together

This lesson has no new Python in it. Instead you use everything from this unit, and the whole routine, to build one program yourself, a step at a time.

### Warm-up

1. Predict what this prints, then press Check.

```python
price = 3.5
print(price * 2)
```

2. What kind of value does `input()` give back?

### The problem

Unit 1's receipt typed every price twice: once to show it, and once in the total. Change one and forget the other, and the receipt lies.

Here is the problem: "Write a receipt program for the Corner Store. It asks for the customer's name, stores each price once in a variable with a clear name, and works out the total from those variables."

You will write every line of it. First, **Say it** and **Split it**:

```python
# Say it: ask who the customer is, then print a receipt whose total
# is worked out from the prices, each stored once.
# Split it:
# 1. ask for the customer's name and print it
# 2. store each price in a variable
# 3. print a line for each item
# 4. work out the total from the variables and print it
```

Then **Name it**. This receipt needs a name for the customer, one for each price, and one for the total: `customer`, `notebook_price`, `pens_price`, `stickers_price` and `total`. Each says what it holds, so the finished program will explain itself.

The practices below are the routine's **Build it** step: one or two comments at a time, run after each.

### Practice

1. Step 1: under the plan, ask for the customer's name and print "Customer:" followed by it. Run it.

```python
# Say it: ask who the customer is, then print a receipt whose total
# is worked out from the prices, each stored once.
# Split it:
# 1. ask for the customer's name and print it
# 2. store each price in a variable
# 3. print a line for each item
# 4. work out the total from the variables and print it
```

2. Steps 2 and 3: store the three prices in variables (notebook 3.50, pens 2.25, stickers 1.75) and print a line for each item. Copy your step 1 into this box first.
3. Step 4: work out the total from the three variables, and print it. Copy your program so far into this box first.

### Check it

Run your receipt with an ordinary name. Then run it again with an awkward one: just press Enter without typing anything. Does the receipt still make sense?

Now change one price and run it again. The item's line and the total change together, because both read the same variable. That is the point of storing each fact in one place: the receipt cannot lie about its own total.

### Practice

1. You change `pens_price` to 3.00 and run it again. What happens to the total?

### Try It

1. The store starts selling rulers at 1.25. Add a ruler to your receipt, so its line and the total are both right. Copy your receipt from exercise 5 into this box first.

> Say it: what has to change on the receipt? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: add a comment for each new step, where it belongs in the plan.
> Name it: what will you call the ruler's price?
> Check it: is the new total 8.75? Then change the ruler's price. Does the total follow?

### What you can do now

- Turn a problem sentence into a plan made of comments.
- Build it a step at a time, running as you go.
- Check it with an awkward input and a changed value.

Key words: **Say it**, **Split it**, **Name it**, **Build it**, **Check it**.

That is the end of unit 2. Its quiz is below: fill it in, then show or print it.
