import re


def load(path: str):
    string = open(path).read()
    split_string = string.split("\n\n")
    return split_string[0], split_string[1].split("\n")


def load_stacks(stacks_str: str):
    stacks_lst = stacks_str.split("\n")
    only_stacks = stacks_lst[:-1]
    only_numbers = stacks_lst[-1].split()

    number_of_stacks = int(only_numbers[-1])

    stacks = {num: [] for num in only_numbers}

    only_stacks.reverse()

    for layer in only_stacks:
        for stack, i in enumerate(range(1, len(layer), 4)):
            if layer[i] != " ":
                stacks[str(stack+1)].append(layer[i])

    return stacks


def load_move(move: str):
    p = re.compile(r'\d+')
    num_list = p.findall(move)
    return [int(obj) for obj in num_list]


def perform_move(stacks: dict, move: str, reverse=True):
    amount, move_from, move_to = load_move(move)

    boxes = stacks[str(move_from)][-amount:]
    if reverse:
        boxes.reverse()
    stacks[str(move_to)].extend(boxes)
    del(stacks[str(move_from)][-amount:])


stacks, moves = load("data/05/input1.txt")

# Assignment 1

loaded_stacks = load_stacks(stacks)

for move in moves:
    perform_move(loaded_stacks, move)

top_string = ""
for num in range(len(loaded_stacks)):
    top_string += loaded_stacks[str(num+1)][-1]

print("Assignment 1:")
print("Top boxes: ", top_string)

# Assignment 2

loaded_stacks = load_stacks(stacks)

for move in moves:
    perform_move(loaded_stacks, move, reverse=False)

top_string = ""
for num in range(len(loaded_stacks)):
    top_string += loaded_stacks[str(num+1)][-1]

print("Assignment 2:")
print("Top boxes: ", top_string)
