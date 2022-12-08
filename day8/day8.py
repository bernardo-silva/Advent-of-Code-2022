import numpy as np


def is_visible(arr, i, j):
    return (np.all(arr[i, j] > arr[:i, j]) or
            np.all(arr[i, j] > arr[i+1:, j]) or
            np.all(arr[i, j] > arr[i, :j]) or
            np.all(arr[i, j] > arr[i, j+1:]))


def count_visible(trees):
    m, n = trees.shape
    edges = 2*m + 2*n - 4

    middle = sum((is_visible(trees, i, j)
                 for i in range(1, m-1) for j in range(1, n-1)))

    return edges + middle


def scenic_score(arr, i, j):
    height = arr[i, j]

    directions = [0, 0, 0, 0]
    for n, direction in enumerate([arr[i, :j][::-1],
                                   arr[i, j+1:],
                                   arr[:i, j][::-1],
                                   arr[i+1:, j]]):
        for t in direction:
            directions[n] += 1
            if t >= height:
                break

    return directions[0]*directions[1]*directions[2]*directions[3]


def highest_score(trees):
    m, n = trees.shape
    return max([scenic_score(trees, i, j) for i in range(m) for j in range(n)])


if __name__ == "__main__":
    sample = """30373
25512
65332
33549
35390"""

    # Sample
    trees = np.array([list(line) for line in sample.split("\n")], dtype=int)
    print("Sample:")
    print(count_visible(trees))
    print(highest_score(trees))

    # # Part 1
    with open("input.txt", "r") as f:
        input_text = [list(line.strip()) for line in f]

    trees = np.array(input_text, dtype=int)
    print("Part 1:")
    print(count_visible(trees))

    # Part 2
    print("Part 2:")
    print(highest_score(trees))
