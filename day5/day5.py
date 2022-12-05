import re


def parse_input(input):
    crates, moves = input.split("\n\n")
    n_stacks = int(crates.strip()[-1])

    stacks = parse_stacks(crates, n_stacks)
    moves = parse_moves(moves)

    return stacks, moves


def parse_stacks(crates, n_stacks):
    stacks = [[] for _ in range(n_stacks)]

    for level in crates.split("\n")[:-1][::-1]:
        for stack in range(n_stacks):
            crate = level[stack*4+1]
            if crate.strip():
                stacks[stack].append(crate)

    return stacks


def parse_moves(moves):
    move_re = re.compile(r"move (\d+) from (\d+) to (\d+)")
    moves = [tuple(map(int, re.match(move_re, move).groups()))
             for move in moves.split("\n")]

    return moves


def do_moves(stacks, moves):
    for n, fromStack, toStack in moves:
        fromStack, toStack = fromStack - 1, toStack - 1
        for _ in range(n):
            stacks[toStack].append(stacks[fromStack].pop())


def do_moves_9001(stacks, moves):
    for n, fromStack, toStack in moves:
        fromStack, toStack = fromStack - 1, toStack - 1
        for i in range(n):
            stacks[toStack].append(stacks[fromStack].pop(-n+i))


def read_output(stacks):
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    sample = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    stacks, moves = parse_input(sample)
    do_moves(stacks, moves)
    print(stacks)
    print(read_output(stacks))
    print("\n\n")

    with open("input.txt", "r") as f:
        input_text = f.read().strip()
    # Part 1
    stacks, moves = parse_input(input_text)
    do_moves(stacks, moves)
    print(read_output(stacks))

    # Part 2
    stacks, moves = parse_input(sample)
    do_moves_9001(stacks, moves)
    print(stacks)
    print(read_output(stacks))
    print("\n\n")

    stacks, moves = parse_input(input_text)
    do_moves_9001(stacks, moves)
    print(read_output(stacks))
