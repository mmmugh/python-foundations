# Tallies votes and displays the results as a text bar chart.


def tally(votes):
    """Return a dictionary mapping each option to its number of votes."""
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts


def winners(counts):
    """Return a list of every option tied for the most votes."""
    if not counts:
        return []
    best = max(counts.values())
    return [option for option, count in counts.items() if count == best]


def report(counts, total):
    """Print each option with its count, percentage, and a bar."""
    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

    print(f"{'Option':<12}{'Votes':>6}{'Share':>8}  Chart")
    print("-" * 46)
    for option, count in ranked:
        share = count / total * 100
        bar = "#" * round(share / 4)
        print(f"{option:<12}{count:>6}{share:>7.1f}%  {bar}")
    print("-" * 46)


votes = [
    "pizza", "tacos", "pizza", "sushi", "pizza",
    "tacos", "salad", "sushi", "pizza", "tacos",
    "sushi", "pizza", "tacos", "pizza", "sushi",
]

counts = tally(votes)
report(counts, len(votes))

print(f"Total votes:  {len(votes)}")
print(f"Options used: {len(set(votes))}")

leaders = winners(counts)
if len(leaders) == 1:
    print(f"Winner:       {leaders[0]}")
else:
    print(f"Tied:         {', '.join(sorted(leaders))}")
