class Elf:
    def __init__(self, inventory_list):
        self.inventory = [int(item) for item in inventory_list if item]

    def __str__(self):
        return ",".join([str(item) for item in self.inventory])

    @property
    def total_calories(self):
        return sum(self.inventory)


def find_top_three(lst: list):
    top = []
    for i in range(3):
        val = max(lst)
        top.append(val)
        ind = lst.index(val)
        lst.pop(ind)
    return top


def read_inventory_string(string: str):
    all_list = string.split("\n\n")
    elves = []
    for substring in all_list:
        elves.append(Elf(substring.split("\n")))
    return elves


# Assignment 1
input_string = open("data/01/input1.txt").read()
elves = read_inventory_string(input_string)

total_calories = [elf.total_calories for elf in elves]
max_calories = max(total_calories)

print("Assignment 1:")
print("Elf with most calories: ", max_calories)

# Assignment 2
top_three = find_top_three(total_calories)

print("Assignment 2:")
print("Top three elves calories: ", sum(top_three))
