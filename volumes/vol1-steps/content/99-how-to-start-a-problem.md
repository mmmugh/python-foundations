## How to start a problem

Sometimes you read a problem and have no idea where to begin. These five steps give you somewhere to begin, every time. Each one is small. You do them in order, and you can go back to an earlier one whenever you get stuck.

The example on this page is: "A bag holds 6 apples. How many apples are in 5 bags?"

### Say it

Write the problem in your own words, as a comment at the top of your program. If you can say it, you understand it. If you can't, read the problem again before writing any code.

```python
# Say it: work out how many apples are in 5 bags of 6.
```

### Split it

Break the problem into small steps, one comment line each. Each step should be small enough that you can see how to do it. If a step still looks hard, split it again.

```python
# Say it: work out how many apples are in 5 bags of 6.
# Split it:
# 1. store how many apples a bag holds
# 2. store how many bags
# 3. multiply, and print the answer
```

### Name it

Choose names that say what each value means. `apples_per_bag` tells a reader what 6 is; `a` tells them nothing. A good name is one a friend would understand without asking you.

### Build it

Turn one comment into code, and run it. Then the next. Running after each step means that when something goes wrong, you know it was the line you just wrote.

```python
# Say it: work out how many apples are in 5 bags of 6.
# Split it:
# 1. store how many apples a bag holds
# 2. store how many bags
# 3. multiply, and print the answer
apples_per_bag = 6
bags = 5
print(apples_per_bag * bags)
```

The comments stay. They are your plan, and now they explain the program to anyone who reads it.

### Check it

Try an ordinary input, then an awkward one. Here, change the second line to `bags = 0`, then to `bags = 1000`. Does each answer still make sense? Awkward inputs are where programs break, so it is better that you find the break than someone using your program.

When a program asks the user for something, the awkward inputs are things like 0, a negative number, a decimal, a word where a number should be, or just pressing Enter.
