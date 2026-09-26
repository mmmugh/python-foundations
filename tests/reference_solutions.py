"""Reference solutions and deliberate mutants, used only to validate the test
cases in content/_checks.json. NOT part of the site."""

GOOD = {
"is_even": "def is_even(n):\n    return n % 2 == 0",
"bmi": "def bmi(weight_kg, height_m):\n    return round(weight_kg / height_m ** 2, 1)",
"largest_of_three": "def largest_of_three(a, b, c):\n    biggest = a\n    if b > biggest:\n        biggest = b\n    if c > biggest:\n        biggest = c\n    return biggest",
"count_vowels": "def count_vowels(word):\n    total = 0\n    for letter in word:\n        if letter in 'aeiou':\n            total += 1\n    return total",
"is_prime": "def is_prime(n):\n    if n < 2:\n        return False\n    for d in range(2, int(n ** 0.5) + 1):\n        if n % d == 0:\n            return False\n    return True",
"count_above": "def count_above(numbers, threshold):\n    return sum(1 for n in numbers if n > threshold)",
"second_largest": "def second_largest(numbers):\n    return sorted(set(numbers))[-2]",
"count_letter": "def count_letter(text, letter):\n    return text.lower().count(letter.lower())",
"title_case": "def title_case(sentence):\n    return ' '.join(w[0].upper() + w[1:] for w in sentence.split(' '))",
"caesar_shift": "def caesar_shift(text, n):\n    out = ''\n    for ch in text:\n        out += chr((ord(ch) - 97 + n) % 26 + 97)\n    return out",
"invert": "def invert(d):\n    return {v: k for k, v in d.items()}",
"distance": "def distance(p1, p2):\n    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5",
"linear_search": "def linear_search(items, target):\n    return [i for i, x in enumerate(items) if x == target]",
"binary_search": "def binary_search(items, target):\n    lo, hi = 0, len(items)\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if items[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid\n    return lo",
"is_sorted": "def is_sorted(items):\n    for i in range(len(items) - 1):\n        if items[i] > items[i+1]:\n            return False\n    return True",
"power": "def power(base, exponent):\n    if exponent == 0:\n        return 1\n    return base * power(base, exponent - 1)",
"digit_sum": "def digit_sum(n):\n    if n < 10:\n        return n\n    return n % 10 + digit_sum(n // 10)",
"is_palindrome": "def is_palindrome(text):\n    if len(text) < 2:\n        return True\n    if text[0] != text[-1]:\n        return False\n    return is_palindrome(text[1:-1])",
"count_item": "def count_item(items, target):\n    if not items:\n        return 0\n    return (items[0] == target) + count_item(items[1:], target)",
"gcd": "def gcd(a, b):\n    if b == 0:\n        return a\n    return gcd(b, a % b)",
}

# Each is a mistake a real beginner makes. The test cases must catch every one.
MUTANT = {
"is_even": "def is_even(n):\n    return n % 2 == 1",
"bmi": "def bmi(weight_kg, height_m):\n    return weight_kg / height_m ** 2",
"largest_of_three": "def largest_of_three(a, b, c):\n    return a if a > b else b",
"count_vowels": "def count_vowels(word):\n    return sum(1 for c in word if c in 'aeio')",
"is_prime": "def is_prime(n):\n    for d in range(2, n):\n        if n % d == 0:\n            return False\n    return True",
"count_above": "def count_above(numbers, threshold):\n    return sum(1 for n in numbers if n >= threshold)",
"second_largest": "def second_largest(numbers):\n    return max(numbers)",
"count_letter": "def count_letter(text, letter):\n    return text.count(letter)",
"title_case": "def title_case(sentence):\n    return sentence[0].upper() + sentence[1:]",
"caesar_shift": "def caesar_shift(text, n):\n    return ''.join(chr(ord(c) + n) for c in text)",
"invert": "def invert(d):\n    return d",
"distance": "def distance(p1, p2):\n    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2",
"linear_search": "def linear_search(items, target):\n    for i, x in enumerate(items):\n        if x == target:\n            return [i]\n    return []",
"binary_search": "def binary_search(items, target):\n    lo, hi = 0, len(items) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if items[mid] == target:\n            return mid\n        if items[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1",
"is_sorted": "def is_sorted(items):\n    return True",
"power": "def power(base, exponent):\n    return base * exponent",
"digit_sum": "def digit_sum(n):\n    return n",
"is_palindrome": "def is_palindrome(text):\n    return len(text) % 2 == 1",
"count_item": "def count_item(items, target):\n    return 1 if target in items else 0",
"gcd": "def gcd(a, b):\n    return min(a, b)",
}

OUTPUT_GOOD = {
"ch03-expressions-and-operators#3": "for row in range(5):\n    print('#' * 20)",
"ch05-repetition#1": "for n in range(1, 21):\n    print(n * n)",
}
OUTPUT_MUTANT = {
"ch03-expressions-and-operators#3": "for row in range(4):\n    print('#' * 20)",
"ch05-repetition#1": "for n in range(1, 21):\n    print(n)",
}

# Practice pages. The flyer is pinned line for line, so these are
# checked by exact output rather than by calling anything.
OUTPUT_GOOD.update({
 "ch01-your-first-programs-practice#1": "print(\"======================================\")\nprint(\"         RIVERSIDE FILM CLUB\")\nprint(\"======================================\")",
 "ch01-your-first-programs-practice#2": "print(\"Feature:  The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#3": "print(\"Feature:\", \"The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#4": "print(\"When:     Friday, 7:30 pm\")\nprint(\"Where:    Room 14\")",
 "ch01-your-first-programs-practice#5": "print(\"Seats available:\", 8 * 12)",
 "ch01-your-first-programs-practice#6": "print(\"Snack bar total:\", 3 * 3.75 + 2 * 3.00)",
 "ch01-your-first-programs-practice#7": "# Prints the flyer for Friday's Riverside Film Club showing.\n\nprint(\"======================================\")\nprint(\"         RIVERSIDE FILM CLUB\")\nprint(\"======================================\")\nprint()\nprint(\"Feature:  The Quiet Harbour  (1998)\")\nprint(\"When:     Friday, 7:30 pm\")\nprint(\"Where:    Room 14\")\nprint()\nprint(\"Seats available:\", 8 * 12)\nprint(\"Snack bar total:\", 3 * 3.75 + 2 * 3.00)\nprint()\nprint(\"======================================\")"
})

OUTPUT_MUTANT.update({
 "ch01-your-first-programs-practice#1": "print(\"======================================\")\nprint(\"RIVERSIDE FILM CLUB\")\nprint(\"======================================\")",
 "ch01-your-first-programs-practice#2": "print(\"Feature: The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#3": "print(\"Feature:  The Quiet Harbour  (1998)\")",
 "ch01-your-first-programs-practice#4": "print(\"When: Friday, 7:30 pm\")\nprint(\"Where: Room 14\")",
 "ch01-your-first-programs-practice#5": "print(\"Seats available:\", 8 * 11)",
 "ch01-your-first-programs-practice#6": "print(\"Snack bar total:\", 3 * 3.75 + 2 * 3.50)",
 "ch01-your-first-programs-practice#7": "# Prints the flyer for Friday's Riverside Film Club showing.\n\nprint(\"======================================\")\nprint(\"         RIVERSIDE FILM CLUB\")\nprint(\"======================================\")\nprint()\nprint(\"Feature:  The Quiet Harbour  (1998)\")\nprint(\"When:     Friday, 7:30 pm\")\nprint(\"Where:    Room 14\")\nprint(\"Seats available:\", 8 * 12)\nprint(\"Snack bar total:\", 3 * 3.75 + 2 * 3.00)\nprint()\nprint(\"======================================\")"
})

# Practice pages, chapters 6 to 12: one function per step.
GOOD.update({
"add_item": 'def add_item(register, item):\n    new = register.copy()\n    new[item] = new.get(item, 0) + 1\n    return new',
"all_sizes": 'def all_sizes(folder):\n    sizes = list(folder["files"])\n    for inner in folder["folders"]:\n        sizes += all_sizes(inner)\n    return sizes',
"average_seconds": 'def average_seconds(seconds):\n    return round(sum(seconds) / len(seconds), 1)',
"busiest": 'def busiest(register):\n    return max(register, key=lambda item: register[item])',
"by_length": 'def by_length(titles, seconds):\n    pairs = []\n    for i in range(len(titles)):\n        pairs.append([seconds[i], titles[i]])\n    pairs.sort()\n    return [pair[1] for pair in pairs]',
"by_time": 'def by_time(services):\n    return sorted(services, key=lambda service: service[1])',
"c_to_f": 'def c_to_f(celsius):\n    return round(celsius * 9 / 5 + 32, 1)',
"clock": 'def clock(minutes):\n    return f"{minutes // 60:02d}:{minutes % 60:02d}"',
"count_by_route": 'def count_by_route(services):\n    counts = {}\n    for service in services:\n        counts.setdefault(service[0], 0)\n        counts[service[0]] += 1\n    return counts',
"count_of": 'def count_of(register, item):\n    return register.get(item, 0)',
"cups_to_ml": 'def cups_to_ml(cups):\n    return round(cups * 236.588, 1)',
"depth": 'def depth(folder):\n    deepest = 0\n    for inner in folder["folders"]:\n        if depth(inner) > deepest:\n            deepest = depth(inner)\n    return 1 + deepest',
"destinations": 'def destinations(services):\n    return sorted(set(service[2] for service in services))',
"f_to_c": 'def f_to_c(fahrenheit):\n    return round((fahrenheit - 32) * 5 / 9, 1)',
"fastest_name": 'def fastest_name(results):\n    best = results[0]\n    for result in results:\n        if result[1] < best[1]:\n            best = result\n    return best[0]',
"file_count": 'def file_count(folder):\n    count = len(folder["files"])\n    for inner in folder["folders"]:\n        count += file_count(inner)\n    return count',
"find_folder": 'def find_folder(folder, name):\n    if folder["name"] == name:\n        return folder\n    for inner in folder["folders"]:\n        found = find_folder(inner, name)\n        if found is not None:\n            return found\n    return None',
"first_three": 'def first_three(titles):\n    return titles[:3]',
"folder_names": 'def folder_names(folder):\n    names = [folder["name"]]\n    for inner in folder["folders"]:\n        names += folder_names(inner)\n    return names',
"has_song": 'def has_song(titles, title):\n    return title in titles',
"in_both": 'def in_both(left, right):\n    return sorted(set(left) & set(right))',
"insertion_point": 'def insertion_point(times, target):\n    low = 0\n    high = len(times)\n    while low < high:\n        middle = (low + high) // 2\n        if times[middle] < target:\n            low = middle + 1\n        else:\n            high = middle\n    return low',
"is_warning": 'def is_warning(line):\n    return line.split("|")[0].upper() == "WARN"',
"km_to_miles": 'def km_to_miles(km):\n    return round(km * 0.621371, 2)',
"label": 'def label(minute):\n    return "peak" if 420 <= minute < 560 or 960 <= minute < 1140 else "off-peak"',
"largest_file": 'def largest_file(folder):\n    biggest = None\n    for size in folder["files"]:\n        if biggest is None or size > biggest:\n            biggest = size\n    for inner in folder["folders"]:\n        inner_biggest = largest_file(inner)\n        if inner_biggest is not None:\n            if biggest is None or inner_biggest > biggest:\n                biggest = inner_biggest\n    return biggest',
"leaderboard_lines": 'def ranked(results):\n    return sorted(results, key=lambda result: result[1])\n\ndef leaderboard_lines(results):\n    lines = []\n    for place, result in enumerate(ranked(results), 1):\n        lines.append(f"{place}. {result[0]} {result[1]}")\n    return lines',
"level_of": 'def level_of(line):\n    return line.split("|")[0]',
"longest_title": 'def longest_title(titles):\n    best = titles[0]\n    for title in titles:\n        if len(title) > len(best):\n            best = title\n    return best',
"message_of": 'def message_of(line):\n    return line.split("|")[2]',
"next_after": 'def by_time(services):\n    return sorted(services, key=lambda service: service[1])\n\ndef next_after(services, minute):\n    for service in by_time(services):\n        if service[1] > minute:\n            return service\n    return None',
"oven_setting": 'def c_to_f(celsius):\n    return round(celsius * 9 / 5 + 32, 1)\n\n\ndef oven_setting(celsius):\n    return round(c_to_f(celsius) / 25) * 25',
"place_of": 'def ranked(results):\n    return sorted(results, key=lambda result: result[1])\n\ndef place_of(results, name):\n    for place, result in enumerate(ranked(results), 1):\n        if result[0] == name:\n            return place\n    return None',
"playlist_with": 'def playlist_with(titles, title):\n    new = titles.copy()\n    new.append(title)\n    return new',
"podium": 'def ranked(results):\n    return sorted(results, key=lambda result: result[1])\n\ndef podium(results):\n    return [r[0] for r in ranked(results)[:3]]',
"positions": 'def positions(titles, title):\n    return [i for i, t in enumerate(titles) if t == title]',
"ranked": 'def ranked(results):\n    return sorted(results, key=lambda result: result[1])',
"redact": 'def redact(line, word):\n    return line.replace(word, "****")',
"register_from": 'def register_from(found):\n    register = {}\n    for item in found:\n        register[item] = register.get(item, 0) + 1\n    return register',
"remove_item": 'def remove_item(register, item):\n    new = register.copy()\n    if item not in new:\n        return new\n    new[item] = new[item] - 1\n    if new[item] == 0:\n        del new[item]\n    return new',
"result_for": 'def result_for(results, name):\n    for result in results:\n        if result[0] == name:\n            return result\n    return None',
"route_of": 'def route_of(service):\n    route, departs, destination = service\n    return route',
"scale_recipe": 'def scale_recipe(amount, factor):\n    return round(amount * factor, 2)',
"size_report": 'def total_size(folder):\n    size = sum(folder["files"])\n    for inner in folder["folders"]:\n        size += total_size(inner)\n    return size\n\ndef size_report(folder):\n    lines = [f"{folder[\'name\']}: {total_size(folder)}"]\n    for inner in folder["folders"]:\n        lines += size_report(inner)\n    return lines',
"sort_times": 'def sort_times(times):\n    out = times.copy()\n    for i in range(1, len(out)):\n        current = out[i]\n        j = i - 1\n        while j >= 0 and out[j] > current:\n            out[j + 1] = out[j]\n            j -= 1\n        out[j + 1] = current\n    return out',
"sorted_items": 'def sorted_items(register):\n    return sorted(register)',
"tidy": 'def tidy(line):\n    level, time, message = line.split("|")\n    return "|".join([level.upper(), time, message.strip()])',
"time_of": 'def time_of(line):\n    return line.split("|")[1]',
"timetable_lines": 'def clock(minutes):\n    return f"{minutes // 60:02d}:{minutes % 60:02d}"\ndef by_time(services):\n    return sorted(services, key=lambda service: service[1])\n\ndef timetable_lines(services):\n    lines = []\n    for route, departs, destination in by_time(services):\n        lines.append(f"{route} {clock(departs)} {destination}")\n    return lines',
"total_items": 'def total_items(register):\n    return sum(register.values())',
"total_seconds": 'def total_seconds(seconds):\n    return sum(seconds)',
"total_size": 'def total_size(folder):\n    size = sum(folder["files"])\n    for inner in folder["folders"]:\n        size += total_size(inner)\n    return size',
"warning_messages": 'def warning_messages(lines):\n    out = []\n    for line in lines:\n        if line.split("|")[0].upper() == "WARN":\n            out.append(line.split("|")[2].strip())\n    return out',
"words_in": 'def words_in(message):\n    return [word for word in message.split() if word.isalpha()]'})


# The matching mistakes, each one a thing a beginner really does.
MUTANT.update({
"add_item": 'def add_item(register, item):\n    new = register.copy()\n    new[item] = 1\n    return new',
"all_sizes": 'def all_sizes(folder):\n    return folder["files"]',
"average_seconds": 'def average_seconds(seconds):\n    return round(sum(seconds) / 3, 1)',
"busiest": 'def busiest(register):\n    return max(register)',
"by_length": 'def by_length(titles, seconds):\n    return sorted(titles)',
"by_time": 'def by_time(services):\n    return sorted(services)',
"c_to_f": 'def c_to_f(celsius):\n    return round((celsius + 32) * 9 / 5, 1)',
"clock": 'def clock(minutes):\n    return f"{minutes // 60}:{minutes % 60}"',
"count_by_route": 'def count_by_route(services):\n    counts = {}\n    for service in services:\n        counts[service[0]] = 1\n    return counts',
"count_of": 'def count_of(register, item):\n    return register[item]',
"cups_to_ml": 'def cups_to_ml(cups):\n    return round(cups * 250, 1)',
"depth": 'def depth(folder):\n    return 1 + len(folder["folders"])',
"destinations": 'def destinations(services):\n    return sorted(service[2] for service in services)',
"f_to_c": 'def f_to_c(fahrenheit):\n    return round((fahrenheit - 32) * 9 / 5, 1)',
"fastest_name": 'def fastest_name(results):\n    best = results[0]\n    for result in results:\n        if result[1] > best[1]:\n            best = result\n    return best[0]',
"file_count": 'def file_count(folder):\n    return len(folder["files"])',
"find_folder": 'def find_folder(folder, name):\n    if folder["name"] == name:\n        return folder\n    for inner in folder["folders"]:\n        if inner["name"] == name:\n            return inner\n    return None',
"first_three": 'def first_three(titles):\n    return [titles[0], titles[1], titles[2]]',
"folder_names": 'def folder_names(folder):\n    return [folder["name"]] + [f["name"] for f in folder["folders"]]',
"has_song": 'def has_song(titles, title):\n    return title == titles',
"in_both": 'def in_both(left, right):\n    return sorted(set(left) | set(right))',
"insertion_point": 'def insertion_point(times, target):\n    low = 0\n    high = len(times)\n    while low < high:\n        middle = (low + high) // 2\n        if times[middle] <= target:\n            low = middle + 1\n        else:\n            high = middle\n    return low',
"is_warning": 'def is_warning(line):\n    return line.split("|")[0] == "WARN"',
"km_to_miles": 'def km_to_miles(km):\n    return round(km / 0.621371, 2)',
"label": 'def label(minute):\n    return "peak" if 420 <= minute <= 560 or 960 <= minute <= 1140 else "off-peak"',
"largest_file": 'def largest_file(folder):\n    if not folder["files"]:\n        return None\n    return max(folder["files"])',
"leaderboard_lines": 'def ranked(results):\n    return sorted(results, key=lambda result: result[1])\n\ndef leaderboard_lines(results):\n    return [f"{i}. {r[0]} {r[1]}" for i, r in enumerate(results, 1)]',
"level_of": 'def level_of(line):\n    return line.split(" ")[0]',
"longest_title": 'def longest_title(titles):\n    best = titles[0]\n    for title in titles:\n        if title > best:\n            best = title\n    return best',
"message_of": 'def message_of(line):\n    return line.split("|")[1]',
"next_after": 'def by_time(services):\n    return sorted(services, key=lambda service: service[1])\n\ndef next_after(services, minute):\n    for service in by_time(services):\n        if service[1] >= minute:\n            return service\n    return None',
"oven_setting": 'def c_to_f(celsius):\n    return round(celsius * 9 / 5 + 32, 1)\n\n\ndef oven_setting(celsius):\n    return round(c_to_f(celsius) / 10) * 10',
"place_of": 'def ranked(results):\n    return sorted(results, key=lambda result: result[1])\n\ndef place_of(results, name):\n    for place, result in enumerate(ranked(results)):\n        if result[0] == name:\n            return place\n    return None',
"playlist_with": 'def playlist_with(titles, title):\n    return titles',
"podium": 'def ranked(results):\n    return sorted(results, key=lambda result: result[1])\n\ndef podium(results):\n    return [ranked(results)[i][0] for i in range(3)]',
"positions": 'def positions(titles, title):\n    return [titles.index(title)]',
"ranked": 'def ranked(results):\n    return sorted(results)',
"redact": 'def redact(line, word):\n    return line.replace(word, "")',
"register_from": 'def register_from(found):\n    register = {}\n    for item in found:\n        register[item] = 1\n    return register',
"remove_item": 'def remove_item(register, item):\n    new = register.copy()\n    if item in new:\n        del new[item]\n    return new',
"result_for": 'def result_for(results, name):\n    for result in results:\n        if result[0] == name:\n            return result[0]\n    return None',
"route_of": 'def route_of(service):\n    route, departs, destination = service\n    return destination',
"scale_recipe": 'def scale_recipe(amount, factor):\n    return round(amount + factor, 2)',
"size_report": 'def total_size(folder):\n    size = sum(folder["files"])\n    for inner in folder["folders"]:\n        size += total_size(inner)\n    return size\n\ndef size_report(folder):\n    return [f"{folder[\'name\']}: {total_size(folder)}"]',
"sort_times": 'def sort_times(times):\n    out = times.copy()\n    for i in range(1, len(out)):\n        current = out[i]\n        j = i - 1\n        while j >= 0 and out[j] > current:\n            out[j + 1] = out[j]\n            j -= 1\n        out[j] = current\n    return out',
"sorted_items": 'def sorted_items(register):\n    return sorted(register.values())',
"tidy": 'def tidy(line):\n    level, time, message = line.split("|")\n    return "|".join([level.upper(), time, message])',
"time_of": 'def time_of(line):\n    return line.split("|")[0]',
"timetable_lines": 'def clock(minutes):\n    return f"{minutes // 60:02d}:{minutes % 60:02d}"\n\ndef timetable_lines(services):\n    return [f"{s[0]} {clock(s[1])} {s[2]}" for s in services]',
"total_items": 'def total_items(register):\n    return len(register)',
"total_seconds": 'def total_seconds(seconds):\n    return len(seconds)',
"total_size": 'def total_size(folder):\n    return sum(folder["files"])',
"warning_messages": 'def warning_messages(lines):\n    return [line for line in lines\n            if line.split("|")[0].upper() == "WARN"]',
"words_in": 'def words_in(message):\n    return message.split()'})


# Practice steps checked by exact output rather than by calling anything.
OUTPUT_GOOD.update({
"ch02-variables-and-types-practice#1": 'trail = "Kettle Ridge"\ndistance_km = 12.4\nprint(trail, "is", distance_km, "km")',
"ch05-repetition-practice#1": 'for week in range(1, 9):\n    print("Week", week)',
"ch06-functions-practice#6": 'def minutes_to_h_m(total):\n    return total // 60, total % 60\n\nprint(minutes_to_h_m(90))\nprint(minutes_to_h_m(45))\nprint(minutes_to_h_m(125))',
"ch06-functions-practice#8": 'def c_to_f(celsius):\n    return round(celsius * 9 / 5 + 32, 1)\ndef km_to_miles(km):\n    return round(km * 0.621371, 2)\ndef cups_to_ml(cups):\n    return round(cups * 236.588, 1)\n\nprint("180 C is", c_to_f(180), "F")\nprint("5 km is", km_to_miles(5), "miles")\nprint("2 cups is", cups_to_ml(2), "ml")'})


# And their mistakes.
OUTPUT_MUTANT.update({
"ch02-variables-and-types-practice#1": 'trail = "Kettle Ridge"\ndistance_km = 12.4\nprint(trail, "is", distance_km)',
"ch05-repetition-practice#1": 'for week in range(8):\n    print("Week", week)',
"ch06-functions-practice#6": 'def minutes_to_h_m(total):\n    return total % 60, total // 60\n\nprint(minutes_to_h_m(90))\nprint(minutes_to_h_m(45))\nprint(minutes_to_h_m(125))',
"ch06-functions-practice#8": 'def c_to_f(celsius):\n    return round(celsius * 9 / 5 , 1)\ndef km_to_miles(km):\n    return round(km * 0.621371, 2)\ndef cups_to_ml(cups):\n    return round(cups * 236.588, 1)\n\nprint("180 C is", c_to_f(180), "F")\nprint("5 km is", km_to_miles(5), "miles")\nprint("2 cups is", cups_to_ml(2), "ml")'})
