class Coord():
    def __init__(self, a, b):
        self.x = int(a)
        self.y = int(b)

    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        raise IndexError

    def __add__(self, other):
        return Coord(self.x+other.x, self.y+other.y)

    def __repr__(self):
        return "C"+str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x, self.y).__hash__()


def parse_input(path_input):
    wall = dict()
    for path in path_input.split("\n"):
        points = [Coord(*p.split(",")) for p in path.split("->")]
        for p1, p2 in zip(points, points[1:]):
            xrange = range(min(p1[0], p2[0]), max(p1[0], p2[0])+1)
            yrange = range(min(p1[1], p2[1]), max(p1[1], p2[1])+1)
            for x in xrange:
                for y in yrange:
                    wall[Coord(x, y)] = 1

    return wall


def produce_sand(wall, start=Coord(500, 0)):
    limit_x = (min(wall.keys(), key=lambda x: x[0])[0],
               max(wall.keys(), key=lambda x: x[0])[0])
    limit_y = (0, max(wall.keys(), key=lambda x: x[1])[1])
    print(limit_x, limit_y)

    produced = 0
    while True:
        sand = start
        moved = True
        while moved:
            if not limit_x[0] <= sand[0] <= limit_x[1] or sand[1] > limit_y[1]:
                return produced
            # Move down
            if not wall.get(sand + Coord(0, 1), 0):
                sand += Coord(0, 1)
                continue
            # Move left down
            if not wall.get(sand + Coord(-1, 1), 0):
                sand += Coord(-1, 1)
                continue
            # Move right down
            if not wall.get(sand + Coord(1, 1), 0):
                sand += Coord(1, 1)
                continue
            # Sand can´t move
            moved = False
            produced += 1
            wall[sand] = 2


def produce_sand2(wall, start=Coord(500, 0)):
    limit_y =  max(wall.keys(), key=lambda x: x[1])[1] + 2
    produced = 0
    while True:
        sand = start
        moved = True
        while moved:
            if sand.y == limit_y - 1:
                pass
            # Move down
            elif not wall.get(sand + Coord(0, 1), 0):
                sand += Coord(0, 1)
                continue
            # Move left down
            elif not wall.get(sand + Coord(-1, 1), 0):
                sand += Coord(-1, 1)
                continue
            # Move right down
            elif not wall.get(sand + Coord(1, 1), 0):
                sand += Coord(1, 1)
                continue
            # Sand can´t move
            moved = False
            produced += 1
            wall[sand] = 2
            if sand == start: 
                return produced


if __name__ == "__main__":
    print("Sample:")
    with open("sample.txt", "r") as f:
        sample = f.read().strip()

    print(produce_sand(parse_input(sample)))

    print("\nPart 1: ")
    with open("input.txt", "r") as f:
        inputs = f.read().strip()

    print(produce_sand(parse_input(inputs)))

    print("\nPart 2 sample: ")
    print(produce_sand2(parse_input(sample)))

    print("\nPart 2: ")
    print(produce_sand2(parse_input(inputs)))
