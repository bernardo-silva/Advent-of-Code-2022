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
    __radd__ = __add__

    def __sub__(self, other):
        return Coord(self.x-other.x, self.y-other.y)

    def __repr__(self):
        return "C"+str((self.x, self.y))
    __str__ = __repr__

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x, self.y).__hash__()

    def __abs__(self):
        return abs(self.x) + abs(self.y)
