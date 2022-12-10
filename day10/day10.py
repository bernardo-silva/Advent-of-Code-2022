def read_instructions(instructions):
    instruction_list = []
    for inst in instructions.split("\n"):
        split = inst.split()
        if len(split) == 1:
            instruction_list.append((1, 0))
        else:
            instruction_list.append((2, int(split[1])))

    return instruction_list


def execute_instructions(instructions):
    X = [1, 1]
    for inst in instructions:
        for _ in range(inst[0]-1):
            X.append(X[-1])

        X.append(X[-1] + int(inst[1]))

    return X


def compute_strength(register):
    return sum([r*n for r, n in zip(register[20::40], range(20, len(register), 40))])


def CRT():
    return [["." for _ in range(40)] for _ in range(6)]


def draw_on_crt(register, crt):
    for cycle, sprite in enumerate(register[1:]):
        if abs((cycle % 40) - sprite) <= 1:
            line = (cycle//40) % 6
            col = cycle % 40
            crt[line][col] = "#"


def print_CRT(crt):
    print("\n".join(["".join([px for px in line]) for line in crt]))


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample = f.read().strip()

    register = execute_instructions(read_instructions(sample))
    print(compute_strength(register))
    # Sample

    # # Part 1
    with open("input.txt", "r") as f:
        input_text = f.read().strip()

    print("Part 1:")
    register = execute_instructions(read_instructions(input_text))
    print(compute_strength(register))

    # Part 2
    print("Part 2:")
    crt = CRT()
    draw_on_crt(register, crt)
    print_CRT(crt)
