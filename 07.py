class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.directories = set()
        self.files = set()
        self.parent = parent
        if self.parent:
            self.parent.add_directory(self)

    def add_directory(self, child):
        self.directories.add(child)

    def add_file(self, child):
        self.files.add(child)

    def navigate_to_child(self, name: str):
        for directory in self.directories:
            if directory.name == name:
                return directory
        print(f"Directory '{name}' not found.")
        return self

    def navigate_to_parent(self):
        return self.parent

    def navigate_to_root(self):
        if self.parent:
            return self.parent.navigate_to_root()
        else:
            return self

    def navigate_to(self, arg):
        if arg == "/":
            return self.navigate_to_root()
        elif arg == "..":
            return self.navigate_to_parent()
        else:
            return self.navigate_to_child(arg)

    def get_size(self):
        """Calculate the total file size of all children."""
        size = 0
        for child in self.directories:
            size += child.get_size()
        for file in self.files:
            size += file.size

        return size

    def __str__(self):
        return f"{self.parent}/{self.name}" if self.parent else self.name

    def __repr__(self):
        return f"Directory(name={self.name}, parent={self.parent})"


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size})"

    def __repr__(self):
        return f"File(name={self.name}, size={self.size})"


def load(path: str):
    lines = open(path).read().split("\n")
    return lines


def read_line(line: str, prev_command: str = None, current_dir=None):
    parts = line.split()
    if parts[0] == "$":
        command = parts[1]
        args = parts[2:]
        if command == "cd":
            current_dir = current_dir.navigate_to(args[0])
    else:
        command = prev_command
        if prev_command == "ls":
            if parts[0] == "dir":
                new_dir = Directory(parts[1], current_dir)
            else:
                new_file = File(parts[1], int(parts[0]))
                current_dir.add_file(new_file)
    return command, current_dir


def get_dir_sizes(dirs: list, sizes: dict = {}):
    for direc in dirs:
        sizes[str(direc)] = direc.get_size()
        sizes = get_dir_sizes(direc.directories, sizes=sizes)
    return sizes


def get_dirs_below_size(dirs: dict, max_size=100000):
    direc_dict = {}
    for direc, size in dirs.items():
        if size <= max_size:
            direc_dict[direc] = size
    return direc_dict


def get_smallest_above_size(dirs: dict, min_size: int = 0):
    smallest = (None, None)
    for key, item in dirs.items():
        if smallest[1] == None or item >= min_size and item < smallest[1]:
            smallest = (key, item)
    return smallest


lines = load("data/07/input1.txt")

# Assignment 1

root = Directory("/", None)

# Create directories
current_dir = root
command = None

for line in lines:
    command, current_dir = read_line(line, command, current_dir)

sizes = get_dir_sizes([root])
sorted_sizes = get_dirs_below_size(sizes, max_size=100000)

print("Assignment 1:")
print("Sum of smallest dirs: ", sum(sorted_sizes.values()))

# Assignment 2
total_disk_space = 70000000
update_disk_space = 30000000
free_disk_space = total_disk_space - root.get_size()
needed_disk_space = update_disk_space - free_disk_space

smallest_dir = get_smallest_above_size(sizes, min_size=needed_disk_space)

print("Assignment 2:")
print("Smallest directory: ", smallest_dir, ">", needed_disk_space)
