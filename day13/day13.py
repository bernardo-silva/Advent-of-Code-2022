from functools import cmp_to_key


class Val():
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __lt__(self, other):
        return compare(self.val, other.val)
    def __eq__(self, other):
        if isinstance(other, Val):
            return self.val == other.val
        return self.val == other


def parse_input(text):
    comparisons = []
    for pair in text.split("\n\n"):
        first, second = pair.strip().split("\n")
        comparisons.append((Val(eval(first)), Val(eval(second))))

    return comparisons


def compare(first, second):
    # print(f"Comparing {first} with {second}")
    if isinstance(first, int):
        if isinstance(second, int):
            if first == second:
                return None
            return first < second
        elif isinstance(second, list):
            return compare([first], second)

    elif isinstance(first, list):
        if isinstance(second, int):
            return compare(first, [second])
        elif isinstance(second, list):
            for f, s in zip(first, second):
                c = compare(f, s)
                if c is None:
                    continue
                return c
                # if c is None:
                #     continue
            # if len(first) <= len(second):
            #     return True
            if len(first) == len(second):
                return None
            return len(first) < len(second)


def compare_inputs(inputs):
    indexes = []
    for n, (first, second) in enumerate(inputs, start=1):
        if compare(first.val, second.val):
            indexes.append(n)
    return indexes


if __name__ == "__main__":
    print("Sample:")
    with open("sample.txt", "r") as f:
        sample = f.read().strip()
    sample = parse_input(sample)
    indexes = compare_inputs(sample)
    print(indexes, sum(indexes))

    print("\nPart 1: ")
    with open("input.txt", "r") as f:
        inputs = f.read().strip()

    inputs = parse_input(inputs)
    indexes = compare_inputs(inputs)
    print(indexes, sum(indexes))

    print("\nPart 2 sample: ")
    new_sample = []
    for s in sample:
        new_sample += list(s)

    new_sample += [Val([[2]]), Val([[6]])]
    new_sample.sort()
    pos2, pos6 = new_sample.index([[2]]) + 1, new_sample.index([[6]]) + 1
    print(pos2 * pos6)

    print("\nPart 2: ")
    new_inputs = []
    for s in inputs:
        new_inputs += list(s)

    new_inputs += [Val([[2]]), Val([[6]])]
    new_inputs.sort()
    pos2, pos6 = new_inputs.index([[2]]) + 1, new_inputs.index([[6]]) + 1
    print(pos2 * pos6)
