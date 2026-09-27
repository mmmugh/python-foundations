"""Two correct answers in different styles, plus a realistic mistake, for each
stdin-checked exercise. Used only to validate content/_checks.json."""

A = {
"ch02-variables-and-types#2": (
 "a = int(input('a: '))\nb = int(input('b: '))\nprint(a + b)\nprint(a - b)\nprint(a * b)",
 "x = int(input())\ny = int(input())\nprint(f'sum {x+y}, difference {x-y}, product {x*y}')",
 "a = input('a: ')\nb = input('b: ')\nprint(a + b)"),                    # forgot int()
"ch02-variables-and-types#5": (
 "height = int(input('Height in inches: '))\nprint('That is', height / 12, 'feet')",
 "h = float(input())\nprint(f'{h/12} feet')",
 "height = input('Height: ')\nprint('That is', height / 12, 'feet')"),   # unfixed
"ch03-expressions-and-operators#1": (
 "m = int(input())\nprint(m // 60, 'hours', m % 60, 'minutes')",
 "mins = int(input('Minutes: '))\nprint(f'{mins//60}h {mins%60}m')",
 "m = int(input())\nprint(m / 60, 'hours')"),                            # used /
"ch03-expressions-and-operators#2": (
 "p = float(input())\nr = float(input())\ntax = p*r/100\nprint(f'{tax:.2f}')\nprint(f'{p+tax:.2f}')",
 "price = float(input())\nrate = float(input())\nt = price*rate/100\nprint(f'Tax {t:.2f}, total {price+t:.2f}')",
 "p = float(input())\nr = float(input())\nt = p*r/100\nprint(f'{t:.2f}')\nprint(f'{p:.2f}')"),  # forgot to add
"ch03-expressions-and-operators#5": (
 "a=int(input());b=int(input());c=int(input())\nprint(f'{(a+b+c)/3:.1f}')",
 "total = 0\nfor i in range(3):\n    total += int(input())\nprint(round(total/3, 1))",
 "a=int(input());b=int(input());c=int(input())\nprint(a+b+c)"),          # never divided
"ch04-making-decisions#1": (
 "n = int(input())\nif n > 0:\n    print('positive')\nelif n < 0:\n    print('negative')\nelse:\n    print('zero')",
 "n = float(input())\nprint('zero' if n == 0 else 'positive' if n > 0 else 'negative')",
 "n = int(input())\nif n > 0:\n    print('positive')\nelse:\n    print('negative')"),  # no zero case
"ch04-making-decisions#4": (
 "m = int(input())\nif m == 2:\n    print(28)\nelif m in (4,6,9,11):\n    print(30)\nelse:\n    print(31)",
 "days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}\nprint(days[int(input())])",
 "m = int(input())\nprint(31)"),                                         # always 31
"ch05-repetition#2": (
 "num = int(input())\nfor n in range(1, 13):\n    print(num * n)",
 "num = int(input('n: '))\nn = 1\nwhile n <= 12:\n    print(f'{num} x {n} = {num*n}')\n    n += 1",
 "num = input('please enter a number')\nfor n in range(1,13):\n    print(num * n)"),  # the screenshot
"ch05-repetition#3": (
 "total = 0\nwhile True:\n    n = int(input())\n    if n == 0:\n        break\n    total += n\nprint(total)",
 "total = 0\nn = int(input())\nwhile n != 0:\n    total += n\n    n = int(input())\nprint('Total:', total)",
 "total = 0\nwhile True:\n    n = int(input())\n    if n == 0:\n        break\nprint(total)"),  # never adds
"ch05-repetition#5": (
 "word = input()\ncount = 0\nfor c in word:\n    if c in 'aeiou':\n        count += 1\nprint(count)",
 "w = input('Word: ')\nprint(sum(1 for c in w.lower() if c in 'aeiou'))",
 "word = input()\nprint(sum(1 for c in word if c in 'aeio'))"),          # dropped u
"ch07-lists#2": (
 "words = [input() for _ in range(5)]\nfor w in sorted(words):\n    print(w)",
 "ws = []\nfor i in range(5):\n    ws.append(input('Word: '))\nws.sort()\nprint(', '.join(ws))",
 "words = [input() for _ in range(5)]\nfor w in words:\n    print(w)"),  # never sorted
"ch08-strings-as-data#1": (
 "w = input()\nprint(w)\nprint(w[::-1])\nprint(w.upper())\nprint(len(w))",
 "word = input('Word: ')\nprint(f'{word}\\n{word[::-1]}\\n{word.upper()}\\n{len(word)}')",
 "w = input()\nprint(w)\nprint(w.upper())\nprint(len(w))"),              # no backwards
"ch08-strings-as-data#5": (
 "s = input()\nprint(len(s.split()))",
 "sentence = input('Sentence: ')\nprint(f'{len(sentence.split(\" \"))} words')",
 "s = input()\nprint(len(s))"),                                          # counted characters
}

# Practice page: the launch console, one reading at a time.
A.update({
"ch04-making-decisions-practice#1": (
 'wind = float(input("Wind speed in mph? "))\nprint(f"Wind: {wind:.1f} mph")',
 'w = float(input())\nprint("Wind:", f"{w:.1f}", "mph")',
 'wind = int(input("Wind? "))\nprint(f"Wind: {wind} mph")'),
"ch04-making-decisions-practice#2": (
 'wind = float(input())\nif wind < 30:\n    print("Wind: OK")\nelse:\n    print("Wind: TOO STRONG")',
 'w = float(input())\nprint("Wind: OK" if w < 30 else "Wind: TOO STRONG")',
 'w = float(input())\nif w <= 30:\n    print("Wind: OK")\nelse:\n    print("Wind: TOO STRONG")'),
"ch04-making-decisions-practice#3": (
 't = float(input())\nif t >= 2 and t <= 35:\n    print("Temperature: OK")\nelse:\n    print("Temperature: OUT OF RANGE")',
 't = float(input())\nprint("Temperature: OK" if 2 <= t <= 35 else "Temperature: OUT OF RANGE")',
 't = float(input())\nif t > 2 and t <= 35:\n    print("Temperature: OK")\nelse:\n    print("Temperature: OUT OF RANGE")'),
"ch04-making-decisions-practice#4": (
 'c = float(input())\nif c >= 5000:\n    print("Ceiling: CLEAR")\nelif c >= 2000:\n    print("Ceiling: MARGINAL")\nelse:\n    print("Ceiling: TOO LOW")',
 'c = float(input())\nif c < 2000:\n    print("Ceiling: TOO LOW")\nelif c < 5000:\n    print("Ceiling: MARGINAL")\nelse:\n    print("Ceiling: CLEAR")',
 'c = float(input())\nif c >= 2000:\n    print("Ceiling: MARGINAL")\nelif c >= 5000:\n    print("Ceiling: CLEAR")\nelse:\n    print("Ceiling: TOO LOW")'),
"ch04-making-decisions-practice#5": (
 'typed = input()\nif typed.isdigit():\n    print(f"Fuel: {int(typed)}%")\nelse:\n    print("Fuel: NOT A NUMBER")',
 'typed = input()\ntry:\n    print("Fuel: " + str(int(typed)) + "%")\nexcept ValueError:\n    print("Fuel: NOT A NUMBER")',
 'typed = input()\nprint(f"Fuel: {int(typed)}%")'),
"ch04-making-decisions-practice#6": (
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nif ok_w and ok_t and ok_c and ok_f:\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")',
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\ngo = w < 30 and 2 <= t <= 35 and c >= 2000 and f.isdigit() and int(f) >= 95\nprint("LAUNCH: GO" if go else "LAUNCH: NO GO")',
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nif ok_w and ok_t and ok_c:\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")'),
"ch04-making-decisions-practice#7": (
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nif ok_w and ok_t and ok_c and ok_f:\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")\n    if not ok_w:\n        print("HOLD: wind")\n    elif not ok_t:\n        print("HOLD: temperature")\n    elif not ok_c:\n        print("HOLD: ceiling")\n    else:\n        print("HOLD: fuel")',
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nreason = ""\nif not ok_w:\n    reason = "wind"\nelif not ok_t:\n    reason = "temperature"\nelif not ok_c:\n    reason = "ceiling"\nelif not ok_f:\n    reason = "fuel"\nif reason == "":\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")\n    print("HOLD: " + reason)',
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nif ok_w and ok_t and ok_c and ok_f:\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")\n    if not ok_c:\n        print("HOLD: ceiling")\n    elif not ok_w:\n        print("HOLD: wind")\n    elif not ok_t:\n        print("HOLD: temperature")\n    else:\n        print("HOLD: fuel")'),
"ch04-making-decisions-practice#8": (
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nprint("Wind: OK" if ok_w else "Wind: TOO STRONG")\nprint("Temperature: OK" if ok_t else "Temperature: OUT OF RANGE")\nif c >= 5000:\n    print("Ceiling: CLEAR")\nelif c >= 2000:\n    print("Ceiling: MARGINAL")\nelse:\n    print("Ceiling: TOO LOW")\nif f.isdigit():\n    print(f"Fuel: {int(f)}%")\nelse:\n    print("Fuel: NOT A NUMBER")\nif ok_w and ok_t and ok_c and ok_f:\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")\n    if not ok_w:\n        print("HOLD: wind")\n    elif not ok_t:\n        print("HOLD: temperature")\n    elif not ok_c:\n        print("HOLD: ceiling")\n    else:\n        print("HOLD: fuel")',
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nif ok_w:\n    print("Wind: OK")\nelse:\n    print("Wind: TOO STRONG")\nprint("Temperature: OK" if ok_t else "Temperature: OUT OF RANGE")\nif c >= 5000:\n    print("Ceiling: CLEAR")\nelif c >= 2000:\n    print("Ceiling: MARGINAL")\nelse:\n    print("Ceiling: TOO LOW")\nif f.isdigit():\n    print(f"Fuel: {int(f)}%")\nelse:\n    print("Fuel: NOT A NUMBER")\nif ok_w and ok_t and ok_c and ok_f:\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")\n    if not ok_w:\n        print("HOLD: wind")\n    elif not ok_t:\n        print("HOLD: temperature")\n    elif not ok_c:\n        print("HOLD: ceiling")\n    else:\n        print("HOLD: fuel")',
 'w = float(input())\nt = float(input())\nc = float(input())\nf = input()\nok_w = w < 30\nok_t = 2 <= t <= 35\nok_c = c >= 2000\nok_f = f.isdigit() and int(f) >= 95\nprint("Wind: OK" if ok_w else "Wind: TOO STRONG")\nif c >= 5000:\n    print("Ceiling: CLEAR")\nelif c >= 2000:\n    print("Ceiling: MARGINAL")\nelse:\n    print("Ceiling: TOO LOW")\nif f.isdigit():\n    print(f"Fuel: {int(f)}%")\nelse:\n    print("Fuel: NOT A NUMBER")\nif ok_w and ok_t and ok_c and ok_f:\n    print("LAUNCH: GO")\nelse:\n    print("LAUNCH: NO GO")\n    if not ok_w:\n        print("HOLD: wind")\n    elif not ok_t:\n        print("HOLD: temperature")\n    elif not ok_c:\n        print("HOLD: ceiling")\n    else:\n        print("HOLD: fuel")')})

# Practice pages, chapters 2, 3 and 5: programs that ask for input.
A.update({
"ch02-variables-and-types-practice#2": (
 'distance_km = 12.4\npace = float(input("Pace in minutes per km? "))\nminutes = distance_km * pace\nprint("That takes", minutes, "minutes")',
 'd = 12.4\np = float(input())\nprint("Minutes:", d * p)',
 'distance_km = 12.4\npace = input("Pace? ")\nprint("That takes", distance_km * pace, "minutes")'),
"ch02-variables-and-types-practice#3": (
 'distance_km = 12.4\npace = float(input("Pace in minutes per km? "))\nminutes = distance_km * pace\nhours = minutes / 60\nprint("That takes", minutes, "minutes, which is", hours, "hours")',
 'd = 12.4\np = float(input())\nmins = d * p\nprint(mins, "minutes =", mins / 60, "hours")',
 'distance_km = 12.4\npace = float(input("Pace in minutes per km? "))\nminutes = distance_km * pace\nhours = minutes / 100\nprint(minutes, "minutes, which is", hours, "hours")'),
"ch02-variables-and-types-practice#4": (
 'distance_km = 12.4\npace = float(input("Pace in minutes per km? "))\nminutes = distance_km * pace\nhours = minutes / 60\nwater = hours * 0.75\nprint("Water per person:", water, "liters")',
 'd = 12.4\np = float(input())\nh = d * p / 60\nprint("Liters each:", h * 0.75)',
 'distance_km = 12.4\npace = float(input("Pace in minutes per km? "))\nminutes = distance_km * pace\nwater = minutes * 0.75\nprint("Water per person:", water, "liters")'),
"ch02-variables-and-types-practice#5": (
 'distance_km = 12.4\npace = float(input("Pace in minutes per km? "))\nminutes = distance_km * pace\nhours = minutes / 60\nwater = hours * 0.75\npeople = int(input("How many people? "))\nprint("Water for the group:", water * people, "liters")',
 'd = 12.4\np = float(input())\nn = int(input())\nprint("Group liters:", d * p / 60 * 0.75 * n)',
 'distance_km = 12.4\npace = float(input("Pace in minutes per km? "))\nminutes = distance_km * pace\nhours = minutes / 60\nwater = hours * 0.75\npeople = int(input("How many people? "))\nprint("Water for the group:", water, "liters")'),
"ch02-variables-and-types-practice#6": (
 'people = int(input("How many people? "))\nprint("Permits:", 4.50 * people)',
 'n = int(input())\ncost = n * 4.5\nprint("Permit total:", cost)',
 'people = input("How many people? ")\nprint("Permits:", 4.50 * people)'),
"ch02-variables-and-types-practice#7": (
 'distance_km = float(input("Trail length in km? "))\npace = float(input("Pace in minutes per km? "))\npeople = int(input("How many people? "))\n\nminutes = distance_km * pace\nhours = minutes / 60\nwater = hours * 0.75\n\nprint("Length:", distance_km, "km")\nprint("Time:", minutes, "minutes")\nprint("Time:", hours, "hours")\nprint("Water each:", water, "liters")\nprint("Water total:", water * people, "liters")\nprint("Permits:", 4.50 * people)',
 'd = float(input())\np = float(input())\nn = int(input())\nm = d * p\nh = m / 60\nw = h * 0.75\nprint(d, "km")\nprint(m, "minutes")\nprint(h, "hours")\nprint(w, "liters each")\nprint(w * n, "liters total")\nprint(4.5 * n, "for permits")',
 'd = float(input())\np = float(input())\nn = int(input())\nm = d * p\nh = m / 60\nw = h * 0.75\nprint(d, "km")\nprint(m, "minutes")\nprint(h, "hours")\nprint(w, "liters each")\nprint(4.5 * n, "for permits")'),
"ch03-expressions-and-operators-practice#1": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\nprint(f"You need {slices} slices")',
 'p = int(input())\ne = int(input())\nprint("Slices needed:", p * e)',
 'people = input("How many people? ")\neach = int(input("Slices each? "))\nprint(f"You need {people * each} slices")'),
"ch03-expressions-and-operators-practice#2": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\nprint(f"Order {pizzas} pizzas")',
 'n = int(input()) * int(input())\nprint("Pizzas:", (n + 7) // 8)',
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = slices // 8\nprint(f"Order {pizzas} pizzas")'),
"ch03-expressions-and-operators-practice#3": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\nprint(f"{pizzas * 8 - slices} slices left over")',
 'n = int(input()) * int(input())\nordered = ((n + 7) // 8) * 8\nprint("Left over:", ordered - n)',
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\nprint(f"{slices % 8} slices left over")'),
"ch03-expressions-and-operators-practice#4": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\ncost = pizzas * 13.50\nprint(f"That comes to {cost:.2f}")',
 'n = int(input()) * int(input())\nprint(f"Cost: {((n + 7) // 8) * 13.5:.2f}")',
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\ncost = (slices // 8) * 13.50\nprint(f"That comes to {cost:.2f}")'),
"ch03-expressions-and-operators-practice#5": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\ncost = pizzas * 13.50\nprint(f"Each of you owes {round(cost / people, 2):.2f}")',
 'p = int(input())\ne = int(input())\nc = ((p * e + 7) // 8) * 13.5\nprint(f"{c / p:.2f} each")',
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\ncost = pizzas * 13.50\nprint(f"Each of you owes {round(cost / slices, 2):.2f}")'),
"ch03-expressions-and-operators-practice#6": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\nprint(f"Would one pizza have done? {slices <= 8}")',
 'n = int(input()) * int(input())\nprint("One pizza enough:", n <= 8)',
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\nprint(f"Would one pizza have done? {slices >= 8}")'),
"ch03-expressions-and-operators-practice#7": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\ncost = pizzas * 13.50\ndelivered = cost * 1.15\nprint(f"With delivery: {delivered:.2f}")\nprint(f"Each: {delivered / people:.2f}")',
 'p = int(input())\ne = int(input())\nc = ((p * e + 7) // 8) * 13.5\nd = c + c * 0.15\nprint(f"{d:.2f} delivered, {d / p:.2f} each")',
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\ncost = pizzas * 13.50\ndelivered = cost * 0.15\nprint(f"With delivery: {delivered:.2f}")\nprint(f"Each: {delivered / people:.2f}")'),
"ch03-expressions-and-operators-practice#8": (
 'people = int(input("How many people? "))\neach = int(input("Slices each? "))\nslices = people * each\npizzas = (slices + 7) // 8\ncost = pizzas * 13.50\ndelivered = cost * 1.15\n\nprint(f"Slices needed:  {slices}")\nprint(f"Pizzas to order: {pizzas}")\nprint(f"Slices left:    {pizzas * 8 - slices}")\nprint(f"Cost:           {cost:.2f}")\nprint(f"With delivery:  {delivered:.2f}")\nprint(f"Each of you:    {delivered / people:.2f}")',
 'p = int(input())\ne = int(input())\nn = p * e\nz = (n + 7) // 8\nc = z * 13.5\nd = c * 1.15\nprint(n, "slices")\nprint(z, "pizzas")\nprint(z * 8 - n, "left")\nprint(f"{c:.2f}")\nprint(f"{d:.2f}")\nprint(f"{d / p:.2f}")',
 'p = int(input())\ne = int(input())\nn = p * e\nz = (n + 7) // 8\nc = z * 13.5\nprint(n, "slices")\nprint(z, "pizzas")\nprint(z * 8 - n, "left")\nprint(f"{c:.2f}")'),
"ch05-repetition-practice#2": (
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 9):\n    total += weekly\n    print(f"Week {week}: {total}")',
 'w = float(input())\nt = 0\nfor i in range(8):\n    t = t + w\n    print(t)',
 'weekly = float(input("Saving how much a week? "))\nfor week in range(1, 9):\n    print(f"Week {week}: {weekly * 8}")'),
"ch05-repetition-practice#3": (
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nweeks = 0\nwhile total < 240:\n    total += weekly\n    weeks += 1\nprint("Weeks needed:", weeks)',
 'w = float(input())\nt = 0\nn = 0\nwhile t < 240:\n    t += w\n    n += 1\nprint(n)',
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nweeks = 0\nwhile total <= 240:\n    total += weekly\n    weeks += 1\nprint("Weeks needed:", weeks)'),
"ch05-repetition-practice#4": (
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nweek = 0\nfor week in range(1, 53):\n    total += weekly\n    if total >= 240:\n        break\n\nif total >= 240:\n    print("Reached in week", week)\nelse:\n    print("Not this year")',
 'w = float(input())\nt = 0\nfound = 0\nfor n in range(1, 53):\n    t += w\n    if t >= 240:\n        found = n\n        break\nif found:\n    print("Reached in week", found)\nelse:\n    print("Not this year")',
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nweek = 0\nfor week in range(1, 53):\n    total += weekly\nif total >= 240:\n    print("Reached in week", week)\nelse:\n    print("Not this year")'),
"ch05-repetition-practice#5": (
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 200):\n    if week % 5 == 0:\n        continue\n    total += weekly\n    if total >= 240:\n        print("Reached in week", week)\n        break',
 'w = float(input())\nt = 0\nn = 0\nwhile t < 240:\n    n += 1\n    if n % 5 == 0:\n        continue\n    t += w\nprint("Reached in week", n)',
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 200):\n    if week % 5 == 0:\n        break\n    total += weekly\n    if total >= 240:\n        print("Reached in week", week)\n        break'),
"ch05-repetition-practice#6": (
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 200):\n    total += weekly\n    if week % 4 == 0:\n        total += 10\n    if total >= 240:\n        print("Reached in week", week)\n        break',
 'w = float(input())\nt = 0\nn = 0\nwhile t < 240:\n    n += 1\n    t += w\n    if n % 4 == 0:\n        t += 10\nprint("Reached in week", n)',
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 200):\n    total += weekly\n    if week % 4 == 1:\n        total += 10\n    if total >= 240:\n        print("Reached in week", week)\n        break'),
"ch05-repetition-practice#7": (
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 200):\n    total += weekly\n    total = total * 1.01\n    if total >= 240:\n        print("Reached in week", week)\n        break',
 'w = float(input())\nt = 0\nn = 0\nwhile t < 240:\n    n += 1\n    t = (t + w) * 1.01\nprint("Reached in week", n)',
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 200):\n    total = total * 1.01\n    total += weekly\n    if total >= 240:\n        print("Reached in week", week)\n        break'),
"ch05-repetition-practice#8": (
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 9):\n    total += weekly\n    print(f"Week {week}: {total}")\n\ntotal = 0\nfor week in range(1, 200):\n    if week % 5 == 0:\n        continue\n    total += weekly\n    if week % 4 == 0:\n        total += 10\n    if total >= 240:\n        print("Goal reached in week", week)\n        break',
 'w = float(input())\nt = 0\nfor n in range(1, 9):\n    t += w\n    print(n, t)\nt = 0\nn = 0\nwhile t < 240:\n    n += 1\n    if n % 5 == 0:\n        continue\n    t += w\n    if n % 4 == 0:\n        t += 10\nprint("Goal reached in week", n)',
 'weekly = float(input("Saving how much a week? "))\ntotal = 0\nfor week in range(1, 9):\n    total += weekly\n    print(f"Week {week}: {total}")\n\ntotal = 0\nfor week in range(1, 200):\n    total += weekly\n    if week % 4 == 0:\n        total += 10\n    if total >= 240:\n        print("Goal reached in week", week)\n        break')})
