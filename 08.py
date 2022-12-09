def load(path):
    rows = open(path).read().split("\n")
    trees = []
    for row in rows:
        trees.append([int(char) for char in list(row)])
    return trees


class Tree:
    def __init__(self, height: int):
        self.height = height
        self.visible = False

        self.up_count = 0
        self.left_count = 0
        self.down_count = 0
        self.right_count = 0

    @property
    def scenic_score(self):
        return self.up_count * self.left_count * self.down_count * self.right_count

    def __str__(self):
        return f"Tree of height {self.height}"

    def __repr__(self):
        return f"Tree(height={self.height})"


def count_trees(trees):
    return sum([sum([tree.visible for tree in tree_row]) for tree_row in trees])


tree_heights = load("data/08/input1.txt")

# Assignment 1

trees = []

for row in range(len(tree_heights)):
    tree_row = []
    for column in range(len(tree_heights[row])):
        new_tree = Tree(tree_heights[row][column])
        tree_row.append(new_tree)
    trees.append(tree_row)

# Check rows
for row, tree_row in enumerate(trees):
    # Check left to right
    row_max = 0
    for column, tree in enumerate(tree_row):
        if column == 0 or tree.height > row_max:
            tree.visible = True
            row_max = tree.height

    # Check right to left
    row_max = 0
    for column, tree in enumerate(reversed(tree_row)):
        if column == 0 or tree.height > row_max:
            tree.visible = True
            row_max = tree.height

# Check columns
for col in range(len(trees[0])):
    # Check top to bottom
    col_max = 0
    for row, tree_row in enumerate(trees):
        tree = tree_row[col]
        if row == 0 or tree.height > col_max:
            tree.visible = True
            col_max = tree.height

    # Check bottom to top
    col_max = 0
    for row, tree_row in enumerate(reversed(trees)):
        tree = tree_row[col]
        if row == 0 or tree.height > col_max:
            tree.visible = True
            col_max = tree.height

print("Assignment 1:")
print("Visible trees: ", count_trees(trees))

# Assignment 2

max_scenic = 0

for row, tree_row in enumerate(trees):
    for col, tree in enumerate(tree_row):
        # Check up
        for y in range(row - 1, -1, -1):
            tree.up_count += 1
            if trees[y][col].height >= tree.height:
                break

        # Check left
        for x in range(col - 1, -1, -1):
            tree.left_count += 1
            if trees[row][x].height >= tree.height:
                break

        # Check down
        for y in range(row + 1, len(trees)):
            tree.down_count += 1
            if trees[y][col].height >= tree.height:
                break

        # Check right
        for x in range(col + 1, len(tree_row)):
            tree.right_count += 1
            if trees[row][x].height >= tree.height:
                break

        if tree.scenic_score > max_scenic:
            max_scenic = tree.scenic_score

print("Assignment 2:")
print("Max scenic score: ", max_scenic)
