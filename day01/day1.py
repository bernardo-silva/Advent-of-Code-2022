def count_calories(file) -> list:
    calories = [int(f.readline())]

    for line in f:
        if line.strip():
            calories[-1] += int(line)
        else:
            calories.append(0)

    return calories


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        calories = count_calories(f)

    # Part 1
    print(max(calories))

    # Part 2
    print(sum(sorted(calories, reverse=True)[:3]))
