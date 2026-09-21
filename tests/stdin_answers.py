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
