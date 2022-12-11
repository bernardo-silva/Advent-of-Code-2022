from dataclasses import dataclass
from tqdm import tqdm
from functools import reduce


@dataclass
class Monkey():
    items: list
    operation: str
    test: int
    throw_to: tuple
    inspected: int = 0


def parse_input(f):
    monkeys = []
    monkeys_input = [m.split("\n") for m in f.read().strip().split("\n\n")]
    for mi in monkeys_input:
        items = list(map(int, mi[1].split(":")[-1].split(",")))
        operation = mi[2].split(":")[-1].split("=")[-1].strip()
        test = int(mi[3].split()[-1])
        t1 = int(mi[4].split()[-1])
        t2 = int(mi[5].split()[-1])
        monkeys.append(Monkey(items, operation, test, (t1, t2)))

    return monkeys


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def analyze_monkeys(monkeys, rounds=20, worry=3, limit_worry=False):
    if limit_worry:
        factor = reduce(lambda a, b: a*b, [M.test for M in monkeys])
    for i in tqdm(range(rounds)):
        for M in monkeys:
            for _ in range(len(M.items)):
                item = M.items[0]
                M.inspected += 1
                M.items.pop(0)
                item = eval(M.operation.replace("old", str(item)))
                item //= worry
                throw_to = M.throw_to[item % M.test != 0]

                if limit_worry:
                    item -= max(0, (item // factor)-1) * factor
                monkeys[throw_to].items.append(item)


if __name__ == "__main__":
    print("Sample:")
    with open("sample.txt", "r") as f:
        sample = parse_input(f)

    analyze_monkeys(sample, 20)
    inspected = [M.inspected for M in sample]
    inspected.sort(reverse=True)
    print(inspected[0]*inspected[1])

    print("Part 1:")
    with open("input.txt", "r") as f:
        monkeys = parse_input(f)

    analyze_monkeys(monkeys)
    inspected = [M.inspected for M in monkeys]
    print(inspected)
    inspected.sort(reverse=True)
    print(inspected[0]*inspected[1])

    #############################################################
    print("\nSample:")
    with open("sample.txt", "r") as f:
        sample = parse_input(f)
    analyze_monkeys(sample, 10_000, 1, True)
    inspected = [M.inspected for M in sample]
    print(inspected)
    inspected.sort(reverse=True)
    print(inspected[0]*inspected[1])

    print("\nPart 2:")
    with open("input.txt", "r") as f:
        monkeys = parse_input(f)

    analyze_monkeys(monkeys, 10_000, 1, True)
    inspected = [M.inspected for M in monkeys]
    print(inspected)
    inspected.sort(reverse=True)
    print(inspected[0]*inspected[1])
    # sample =
    pass
