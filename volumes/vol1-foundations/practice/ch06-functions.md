## Practice: a unit converter toolkit

Every recipe in the box is American, the oven dial is in Fahrenheit, and the
running app is in kilometres. You keep doing the same conversions by hand. This
time you are going to write them down once, as functions, and then use them.

Everything here uses Chapters 1 to 6. There are no lists yet, so a function
that has two things to report returns them as a tuple.

The conversions:

| From | To | Multiply by |
| --- | --- | --- |
| Celsius | Fahrenheit | 9/5, then add 32 |
| Kilometres | Miles | 0.621371 |
| Cups | Millilitres | 236.588 |

Each step names the function and its parameters exactly. That name is the
contract the check calls, so spell it as written; everything inside is up to
you.

### Steps

1. Write `c_to_f(celsius)`, returning the temperature in Fahrenheit rounded to one decimal place. Check it against the two you know: 100 is 212, and 0 is 32.
2. Write `f_to_c(fahrenheit)` going the other way, also rounded to one decimal place. There is exactly one temperature where both functions agree; if you are curious, look for it.
3. Write `km_to_miles(km)`, rounded to two decimal places.
4. Write `cups_to_ml(cups)`, rounded to one decimal place.
5. Oven dials only go in 25s. Write `oven_setting(celsius)` that converts to Fahrenheit and rounds to the nearest 25 — so 180 becomes 350. Call `c_to_f()` rather than repeating its arithmetic.
6. Write `minutes_to_h_m(total)` that returns **two** values, hours and minutes, as a tuple, then print the result for 90, 45 and 125 minutes on three lines.
7. Write `scale_recipe(amount, factor)` — two parameters this time — returning the amount multiplied by the factor, rounded to two decimal places, so half a recipe or a triple one is a single call.
8. Put three of them in one program and print a small table: 180 C in Fahrenheit, 5 km in miles, and 2 cups in millilitres, each on its own line reading like `180 C is 356.0 F`.
