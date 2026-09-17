# Reports statistics about a passage of text.


def word_list(text):
    """Return the words of the text, stripped of punctuation and lowercased."""
    words = []
    for raw in text.split():
        cleaned = ""
        for character in raw.lower():
            if character.isalpha() or character == "'":
                cleaned += character
        if cleaned:
            words.append(cleaned)
    return words


def count_vowels(text):
    """Return the number of vowels in the text."""
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def longest_word(words):
    """Return the longest word in a list, or an empty string if there are none."""
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def average_word_length(words):
    """Return the mean length of the words, or 0.0 for an empty list."""
    if not words:
        return 0.0
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)


def analyze(text):
    """Print a report of statistics about the text."""
    words = word_list(text)
    sentences = 0
    for character in text:
        if character in ".!?":
            sentences += 1

    print("=" * 34)
    print(f"{'Characters:':<22}{len(text):>11}")
    print(f"{'Characters (no spaces):':<22}{len(text.replace(' ', '')):>11}")
    print(f"{'Words:':<22}{len(words):>11}")
    print(f"{'Sentences:':<22}{sentences:>11}")
    print(f"{'Vowels:':<22}{count_vowels(text):>11}")
    print(f"{'Longest word:':<22}{longest_word(words):>11}")
    print(f"{'Average word length:':<22}{average_word_length(words):>11.1f}")
    print("=" * 34)


sample = (
    "The quick brown fox jumps over the lazy dog. "
    "Programming is the art of telling another human what one wants "
    "the computer to do. Is that not remarkable?"
)

analyze(sample)
