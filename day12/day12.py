import networkx as nx
import matplotlib.pyplot as plt

directions = dict(U=(0, 1), D=(0, -1), L=(-1, 0), R=(1, 0))


class Heightmap():
    def __init__(self, map, start, end):
        self.map = map
        self.start = start
        self.end = end
        self.p = start
        self.rows = len(map)
        self.cols = len(map[0])

    def possible_moves(self, p):
        moves = []
        for move_name, coord in directions.items():
            i, j = p[0] + coord[0], p[1] + coord[1]
            if i >= self.rows or j >= self.cols or i < 0 or j < 0:
                continue
            if self.map[i][j] - self.map[p[0]][p[1]] <= 1:
                # print(f"Possible to move from {p} to {(i,j)}")
                moves.append(coord)
        return moves

    def get_graph(self):
        G = nx.DiGraph()
        for i in range(self.rows):
            for j in range(self.cols):
                for d in self.possible_moves((i, j)):
                    G.add_edge((i, j), (i+d[0], j+d[1]))

        return G

    def shortest_path(self):
        G = self.get_graph()
        return len(nx.shortest_path(G, self.start, self.end)) - 1

    def shortest_part2(self):
        lens = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map[i][j] == 0:
                    self.start = (i, j)
                    try: 
                        lens.append(self.shortest_path())
                    except Exception as e:
                        continue

        return min(lens)
        

    def __repr__(self):
        return str(self.map)


def parse_input(map):
    heightmap = []
    start = ()
    end = ()
    for i, line in enumerate(map.split("\n")):
        if "S" in line:
            start = (i, line.index("S"))
            line = line.replace("S", "a")
        if "E" in line:
            end = (i, line.index("E"))
            line = line.replace("E", "z")
        heightmap.append([ord(c)-97 for c in line])

    return Heightmap(heightmap, start, end)


if __name__ == "__main__":
    print("Sample part 1: ")
    with open("sample.txt", "r") as f:
        sample = f.read().strip()

    sample_map = parse_input(sample)
    print(sample_map.shortest_path())

    print()
    print("Part 1: ")
    with open("input.txt", "r") as f:
        input_map = f.read().strip()

    hmap = parse_input(input_map)
    print(hmap.shortest_path())

    print()
    print("Sample part 2: ")
    print(sample_map.shortest_part2())

    print()
    print("Part 2: ")
    print(hmap.shortest_part2())

