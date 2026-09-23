## Practice: a launch console

The model rocket club will not fly unless four readings are within limits, and
at the moment somebody checks them on a clipboard. You are going to build the
console that does it, one reading at a time, ending with a program that reads
all four and gives a verdict.

The limits are:

| Reading | Safe |
| --- | --- |
| Wind | under 30 mph |
| Temperature | 2 to 35 °C, ends included |
| Cloud ceiling | 2000 feet or more |
| Fuel | 95 percent or more |

Everything here uses Chapters 1 to 4: variables, `input()`, arithmetic,
comparisons, `and` / `or` / `not`, f-strings, and `if` / `elif` / `else`. No
loops — so each program asks for each reading exactly once, in the order
**wind, temperature, ceiling, fuel**.

Each step names the exact line it must print. The wording around it is yours.

### Steps

1. Ask for the wind speed in mph and print it back to one decimal place, as `Wind: 12.5 mph`. Remember that `input()` hands you a string.
2. Now judge it. Print `Wind: OK` when the speed is under 30, and `Wind: TOO STRONG` otherwise. 30 exactly is too strong.
3. Ask for the temperature in °C and print `Temperature: OK` when it is from 2 to 35 with both ends allowed, and `Temperature: OUT OF RANGE` otherwise. One `if`, with `and`.
4. Ask for the cloud ceiling in feet and sort it into three bands with an `elif` chain: `Ceiling: CLEAR` at 5000 or above, `Ceiling: MARGINAL` from 2000 to 4999, and `Ceiling: TOO LOW` below 2000. Put the narrow band before the broad one, or one branch will never run.
5. Ask for the fuel as a whole-number percentage, but do not trust it: if what was typed is all digits, print `Fuel: 97%` with the number that was typed; otherwise print `Fuel: NOT A NUMBER` and do not convert it.
6. Put all four together. Ask for all four readings in order, then print one verdict line: `LAUNCH: GO` when every reading is safe, `LAUNCH: NO GO` when any of them is not. Fuel that is not a number counts as not safe.
7. A bare refusal is no use to anyone. After a `LAUNCH: NO GO`, print the first thing that failed, checked in the order wind, temperature, ceiling, fuel, as `HOLD: wind`, `HOLD: temperature`, `HOLD: ceiling` or `HOLD: fuel`. Print nothing extra when the verdict is `LAUNCH: GO`.
8. Finish the console: ask for the four readings, print the four status lines from steps 2 to 5, then the verdict, then the `HOLD:` line if there is one.
