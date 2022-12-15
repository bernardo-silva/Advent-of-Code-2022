import re
from coordinates import Coord
from tqdm import tqdm


def parse_input(sensor_msgs, part, line=0):
    sensor_map = dict()
    match_re = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    for msg in sensor_msgs.split("\n"):
        sx, sy, bx, by = map(int, match_re.match(msg).groups())
        sc = Coord(sx, sy)
        bc = Coord(bx, by)

        distance = abs(sc - bc)
        if part == 1:
            sensor_map[sc] = "S"
            sensor_map[bc] = "B"
            distance_to_y = abs(sc.y - line)
            if distance_to_y > distance:
                continue
            for x in range(-(distance-distance_to_y), (distance-distance_to_y)+1):
                empty_c = sc + Coord(x, line - sc.y)
                if empty_c in sensor_map:
                    continue

                sensor_map[empty_c] = "#"
        else:
            sensor_map[sc] = distance
            sensor_map[bc] = 0

    return sensor_map


def find_empty(sensors, max_val):
    for sc, dist in tqdm(sensors.items()):
        for x in tqdm(range(min(-(dist+1), sc.x), min(dist+1+1,
                                                      max_val-sc.x+1))):
            y = min(dist+1-abs(x), sc.y)
            for signal in [-1, 1]:
                C = sc + Coord(x, signal * y)
                if not 0 <= C.x <= max_val or not 0 <= C.y <= max_val:
                    continue
                if C in sensors:
                    continue
                empty = True
                for sc2, dist2 in sensors.items():
                    if abs(C-sc2) <= dist2:
                        empty = False
                        break
                if empty:
                    return C.x, C.y


if __name__ == "__main__":
    print("Sample:")
    with open("sample.txt", "r") as f:
        sample = f.read().strip()

    print(sum([c.y == 10 and v == "#" for c,
          v in parse_input(sample, 1, 10).items()]))

    print("\nPart 1: ")
    with open("input.txt", "r") as f:
        inputs = f.read().strip()

    print("\nPart 2 sample: ")
    sensors = (parse_input(sample, 2))
    x, y = find_empty(sensors, 20)
    print(x, y, x*4_000_000+y)

    print("\nPart 2: ")
    sensors = (parse_input(inputs, 2))
    x, y = find_empty(sensors, 4_000_000)
    print(x, y, x*4_000_000+y)
