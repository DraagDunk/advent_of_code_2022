def load(path):
    rows = open(path).read().split("\n")
    trees = []
    for row in rows:
        trees.append([int(char) for char in list(row)])
    return trees


class Tree:
    def __init__(self, height: int):
        self.height = height

        self.visible = None

    def set_neighbours(self, neighbours: list):
        self.up = neighbours[0]
        self.left = neighbours[1]
        self.down = neighbours[2]
        self.right = neighbours[3]

    def get_neighbours(self):
        return [self.up, self.left, self.down, self.right]

    def find_visible(self):
        neighbours = self.get_neighbours()
        if None in neighbours:
            self.visible = True
        else:

    def check_up(self):
        if self.height > self.up.height

    def __str__(self):
        return f"Tree of height {self.height}"

    def __repr__(self):
        return f"Tree(height={self.height})"


tree_heights = load("data/08/test.txt")

trees = []

for row in range(len(tree_heights)):
    tree_row = []
    for column in range(len(tree_heights[row])):
        new_tree = Tree(tree_heights[row][column])
        tree_row.append(new_tree)
    trees.append(tree_row)

for row, tree_row in enumerate(trees):
    for column, tree in enumerate(tree_row):
        up = trees[row-1][column] if row != 0 else None
        left = trees[row][column-1] if column != 0 else None
        down = trees[row+1][column] if row != len(trees) - 1 else None
        right = trees[row][column+1] if column != len(tree_row) - 1 else None
        tree.set_neighbours([up, left, down, right])

print(trees[0][2].get_neighbours())
