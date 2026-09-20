"""Chapter 9 - Dictionaries and Sets

Every worked example from the chapter.
"""

# --- Creating and reading --------------------------------------------------

scores = {"Ada": 88, "Grace": 92, "Alan": 45}

print(scores["Grace"])
print(len(scores))

# --- Adding, changing, removing --------------------------------------------

scores = {"Ada": 88, "Grace": 92}

scores["Alan"] = 45
scores["Ada"] = 91
print(scores)

del scores["Alan"]
print(scores)

# --- Missing keys ----------------------------------------------------------

scores = {"Ada": 88}

# scores["Grace"] would raise KeyError. Uncomment to see it.
# print(scores["Grace"])

if "Grace" in scores:
    print(scores["Grace"])
else:
    print("No score recorded.")

print(scores.get("Grace"))
print(scores.get("Grace", 0))

# --- Looping ---------------------------------------------------------------

scores = {"Ada": 88, "Grace": 92, "Alan": 45}

for name in scores:
    print(name)

print()

for score in scores.values():
    print(score)

print()

for name, score in scores.items():
    print(f"{name}: {score}")

# --- Built-ins on values ---------------------------------------------------

scores = {"Ada": 88, "Grace": 92, "Alan": 45}

print(sum(scores.values()))
print(max(scores.values()))
print(sum(scores.values()) / len(scores))

top = max(scores, key=scores.get)
print(f"{top} has the highest score: {scores[top]}")

# --- Counting: the killer application --------------------------------------

text = "the quick brown fox jumps over the lazy dog the end"
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1

print(counts["the"])
print(counts)

ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

for word, count in ranked[:3]:
    print(f"{word:<8}{count}")

# --- Nested dictionaries ---------------------------------------------------

students = {
    "Ada": {"score": 88, "grade": "B", "absences": 2},
    "Grace": {"score": 92, "grade": "A", "absences": 0},
}

print(students["Ada"]["score"])
print(students["Grace"]["absences"])

for name, record in students.items():
    print(f"{name}: {record['score']} ({record['grade']})")

# --- Sets ------------------------------------------------------------------

vowels = {"a", "e", "i", "o", "u"}

print("e" in vowels)
print(len(vowels))

numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)
print(len(unique))

band = {"Ada", "Grace", "Alan"}
chorus = {"Grace", "Alan", "Katherine"}

print(band | chorus)
print(band & chorus)
print(band - chorus)
