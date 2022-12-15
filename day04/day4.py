def contained_in(p1, p2):
    return p2[0] <= p1[0] <= p1[1] <= p2[1] or p1[0] <= p2[0] <= p2[1] <= p1[1]


def overlaps(p1, p2):
    return len(set(range(p1[0], p1[1]+1)) & set(range(p2[0], p2[1]+1))) != 0


def count_overlaps(assignments, comparision_func):
    overlaps = 0
    for pair in assignments.split("\n"):
        p1, p2 = map(lambda s: list(map(int, s.split("-"))), pair.split(","))
        overlaps += comparision_func(p1, p2)

    return overlaps


if __name__ == "__main__":
    sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    print(count_overlaps(sample, contained_in))

    with open("input.txt", "r") as f:
        assignments = f.read().strip()
    # Part 1
    print(count_overlaps(assignments, contained_in))

    # Part 2
    print(count_overlaps(sample, overlaps))
    print(count_overlaps(assignments, overlaps))
