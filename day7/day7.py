from dataclasses import dataclass


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = {}
        self.parent = parent

    def add_file(self, filename, filesize):
        self.files[filename] = File(filename, filesize, self)

    def add_dir(self, dirname):
        self.files[dirname] = Directory(dirname, parent=self)

    @property
    def size(self):
        return sum([f.size for f in self.files.values()])

    def cd(self, dir):
        if dir == "..":
            return self.parent
        if dir in self.files.keys():
            return self.files[dir]
        if dir == self.name:
            return self

    def __repr__(self):
        files = "\n" + "\n".join(["|   " + "\n|   ".join(file.__repr__().split("\n"))
                                 for file in self.files.values()])
        return f"""{self.name}:  {self.size}{files}"""


@dataclass
class File:
    name: str
    size: int
    parent: Directory

    def __repr__(self):
        return self.name + " " + str(self.size)


def parse_input(commands):
    root = Directory("/")
    current_dir = root
    for command in commands.split("\n"):
        if command.startswith("$"):
            if "$ cd" in command:
                current_dir = current_dir.cd(command.split()[-1])
        else:
            if command.startswith("dir "):
                _, name = command.split()
                current_dir.add_dir(name)
            else:
                size, name = command.split()
                current_dir.add_file(name, int(size))
    return root


def find_dirs_by_size(root, size, comparison):
    dirs = []
    for file in root.files.values():
        if not isinstance(file, Directory):
            continue
        if comparison(file.size, size):
            dirs += [file]
        dirs += find_dirs_by_size(file, size, comparison)

    return dirs


if __name__ == "__main__":
    sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    # Part 1
    fs = parse_input(sample)
    print(fs)

    print(sum([d.size for d in find_dirs_by_size(
        fs, 100_000, lambda a, b: a <= b)]))
    print()

    with open("input.txt", "r") as f:
        input_text = f.read().strip()

    fs = parse_input(input_text)
    print(fs)
    print("\nPart 1: ")
    print(sum([d.size for d in find_dirs_by_size(
        fs, 100_000, lambda a, b: a <= b)]))

    # Part 2
    unused_space = 70_000_000 - fs.size
    needed_space = 30_000_000 - unused_space
    print("\nPart 2: ")
    print("Need to free ", needed_space)
    print(min([d.size for d in find_dirs_by_size(
        fs, needed_space, lambda a, b: a >= b)]))
