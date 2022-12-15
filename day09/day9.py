import numpy as np

dirs = dict(U=np.array((1, 0)), D=np.array((-1, 0)),
            L=np.array((0, -1)), R=np.array((0, 1)))


def parse_moves(text):
    moves = []
    for move in text.split("\n"):
        moves.append((move[0], int(move.split()[-1])))
    return moves


def move_rope(H, T):
    vector, dist = H - T, np.abs(H-T).sum()
    if dist <= 1: return T #Adjacent
    if dist == 2:
        if 0 not in vector: return T #Diagonal touching
        T = T + vector//2
    if dist >= 3:
        T = T + np.clip(vector, -1, 1)

    return T


def perform_moves(head_moves):
    tail_positions = set()
    tail_positions.add((0,0))
    H = np.array((0, 0))
    T = np.array((0, 0))

    for hmove, count in head_moves:
        for _ in range(count):
            H += dirs[hmove]
            T = move_rope(H, T)
            tail_positions.add(tuple(T.tolist()))

    return len(tail_positions)


def perform_long_moves(head_moves):
    positions = set()
    positions.add((0,0))
    segments = [np.array((0, 0)) for _ in range(10)]

    for hmove, count in head_moves:
        for _ in range(count):
            segments[0] += dirs[hmove]
            for n, H, T in zip(range(1, 10), segments, segments[1:]):
                segments[n] = move_rope(H, T)
            positions.add(tuple(segments[-1].tolist()))

    return len(positions)




if __name__ == "__main__":
    sample = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    # Sample
    print(perform_moves(parse_moves(sample)))

    # # Part 1
    with open("input.txt", "r") as f:
        input_text = f.read().strip()

    print("Part 1:")
    print(perform_moves(parse_moves(input_text)))

    # Part 2
    print("Part 2:")
    sample2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    print(perform_long_moves(parse_moves(sample2)))
    print(perform_long_moves(parse_moves(input_text)))
