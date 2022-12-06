def find_marker(signal, lenght):
    for i, _ in enumerate(signal[lenght-1:], start=lenght-1):
        if len(set(signal[i-lenght+1:i+1])) == lenght:
            return i + 1


if __name__ == "__main__":
    samples = ["bvwbjplbgvbhsrlpgdmjqwftvncz",
               "nppdvjthqldpwncqszvftbrmjlhg",
               "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
               "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

    # Part 1
    print(list(map(lambda x: find_marker(x, 4), samples)))

    with open("input.txt", "r") as f:
        input_text = f.read().strip()

    print(find_marker(input_text, 4))

    # Part 2
    new_samples = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",  # 19
                   "bvwbjplbgvbhsrlpgdmjqwftvncz",  # 23
                   "nppdvjthqldpwncqszvftbrmjlhg",  # 23
                   "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",  # 29
                   "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]  # 26

    print(list(map(lambda x: find_marker(x, 14), new_samples)))
    print(find_marker(input_text, 14))
