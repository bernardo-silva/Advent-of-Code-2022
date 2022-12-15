def load_input(f):
    return [(line[0:len(line)//2], line[len(line)//2:]) for line in f]


def load_input2(f):
    return [line.strip() for line in f]


def compute_priority(char):
    if(char.islower()):
        return ord(char) - 96
    return ord(char) - 38


def repeated_priority(sacks):
    priority = 0
    for compartment1, compartment2 in sacks:
        repeated = set(compartment1) & set(compartment2)
        priority += sum(map(compute_priority, repeated))

    return priority


def find_groups(sacks):
    priority = 0
    for s1, s2, s3 in zip(sacks[::3], sacks[1::3], sacks[2::3]):
        group = set(s1) & set(s2) & set(s3)
        print(group)
        priority += compute_priority(list(group)[0])
    return priority


if __name__ == "__main__":
    # Part 1
    with open("input.txt", "r") as f:
        sacks = load_input(f)

    part1 = repeated_priority(sacks)
    print(part1)

    # Part 2
    with open("input.txt", "r") as f:
        sacks = load_input2(f)

    part2 = find_groups(sacks)
    print(part2)
