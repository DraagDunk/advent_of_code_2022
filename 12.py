height_string = "abcdefghijklmnopqrstuvwxyz"


def load(path):
    string_list = open(path).read().split("\n")
    array = [list(string) for string in string_list]
    return array


class Node:
    def __init__(self, value: str):
        self.value = "a" if value == "S" else "z" if value == "E" else value
        self.end = value == "E"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"Node({self.value})"

    def set_neighbours(self, neighbours: tuple):
        self.up, self.left, self.down, self.right = neighbours

    @property
    def neighbours(self):
        return (self.up, self.left, self.down, self.right)

    @property
    def hval(self):
        return height_string.index(self.value)

    def get_legal_moves(self):
        legal_moves = []
        for neighbour in self.neighbours:
            if neighbour and neighbour.hval - self.hval in [0, 1]:
                legal_moves.append(neighbour)
        return legal_moves


class Path:
    def __init__(self, history: list):
        self.history = history
        self.current = self.history[-1]

    def get_moves(self):
        legal_moves = [
            move for move in self.current.get_legal_moves() if move not in self.history]
        return legal_moves

    def move(self, node):
        self.current = node
        self.history.append(node)

    def check_done(self):
        return self.current.end

    @property
    def length(self):
        return len(self.history)

    def __str__(self):
        return "»".join([node.value for node in self.history])

    def __repr__(self):
        return f"Path({'»'.join([move.value for move in self.history])})"


hmap = load("data/12/test.txt")

nodes = []
for row, height_row in enumerate(hmap):
    node_row = []
    for col, height in enumerate(height_row):
        node = Node(height)
        node_row.append(node)
        if height == "S":
            starting_node = node
    nodes.append(node_row)

for row, node_row in enumerate(nodes):
    for col, node in enumerate(node_row):
        neighbours = (
            nodes[row-1][col] if row != 0 else None,
            nodes[row][col-1] if col != 0 else None,
            nodes[row+1][col] if row != len(nodes)-1 else None,
            nodes[row][col+1] if col != len(node_row)-1 else None
        )
        node.set_neighbours(neighbours)

paths = [Path([starting_node])]

full_paths = []

traversed = 0

while traversed < len(paths):
    print("Traversed: ", traversed, " - Path: ", paths[traversed])
    moves = paths[traversed].get_moves()
    if len(moves) > 1:
        history = paths[traversed].history
        print(history)
        for i, move in enumerate(moves):
            if i > 0:
                new_path = Path(history)
                paths.append(Path(history))
                paths[-1].move(move)
                print(paths)

    paths[traversed].move(moves[0])

    if paths[traversed].check_done():
        print("DONE!")
        full_paths.append(paths[traversed])
        traversed += 1
    elif len(moves) == 0:
        traversed += 1
