"""Chapter 7 - Lists

Every worked example from the chapter.
"""

# --- Creating lists --------------------------------------------------------

scores = [88, 92, 79, 95]
names = ["Ada", "Grace", "Alan"]
mixed = [1, "two", 3.0, True]
empty = []

print(scores)
print(len(scores))

# --- Indexing --------------------------------------------------------------

names = ["Ada", "Grace", "Alan", "Katherine"]

print(names[0])
print(names[2])
print(names[-1])
print(names[-2])

# names[5] would raise IndexError. Uncomment to see it.
# print(names[5])

# --- Lists are mutable -----------------------------------------------------

scores = [88, 92, 79, 95]
scores[2] = 85
print(scores)

# --- Slicing ---------------------------------------------------------------

letters = ["a", "b", "c", "d", "e", "f"]

print(letters[1:4])
print(letters[:3])
print(letters[3:])
print(letters[-2:])
print(letters[::2])

# --- List methods ----------------------------------------------------------

scores = [88, 92, 79]

scores.append(95)
print(scores)

scores.sort()
print(scores)

highest = scores.pop()
print(highest, scores)

# .sort() returns None; sorted() returns a new list
scores = [88, 92, 79]

result = scores.sort()
print(result)

scores = [88, 92, 79]
ordered = sorted(scores)
print(ordered, scores)

# --- Useful built-ins ------------------------------------------------------

scores = [88, 92, 79, 95]

print(len(scores))
print(sum(scores))
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))
print(92 in scores)
print(100 in scores)

# --- Looping over lists ----------------------------------------------------

scores = [88, 92, 79, 95]

for score in scores:
    print(f"Score: {score}")

names = ["Ada", "Grace", "Alan"]

for position, name in enumerate(names):
    print(f"{position + 1}. {name}")

# Building a new list
temperatures_c = [0, 25, 100, 37]
temperatures_f = []

for c in temperatures_c:
    temperatures_f.append(c * 9 / 5 + 32)

print(temperatures_f)

# Filtering
scores = [88, 92, 45, 95, 58, 71]
passing = []

for score in scores:
    if score >= 60:
        passing.append(score)

print(f"{len(passing)} of {len(scores)} passed: {passing}")

# --- Nested lists ----------------------------------------------------------

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0])
print(grid[1][2])

for row in grid:
    for value in row:
        print(value, end=" ")
    print()

# --- A name is not a copy --------------------------------------------------

a = [1, 2, 3]
b = a
b.append(4)
print(a)

c = [1, 2, 3]
d = c.copy()
d.append(4)
print(c)
