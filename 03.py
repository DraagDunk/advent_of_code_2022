char_score = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Rucksack:
    def __init__(self, content: str):
        self.first_compartment = content[:int(len(content)/2)]
        self.second_compartment = content[int(len(content)/2):]
        self.common_item = self.find_common_item()
        self.common_score = self.score_common()

    def find_common_item(self):
        for item in self.first_compartment:
            if item in self.second_compartment:
                return item
        return None

    def score_common(self):
        return char_score.index(self.common_item) + 1

    @property
    def all_content(self):
        return self.first_compartment + self.second_compartment


class Group:
    def __init__(self, rucksacks: list):
        self.rucksacks = rucksacks
        self.common_item = self.find_common_item()
        self.common_score = self.score_common()

    def find_common_item(self):
        for item in self.rucksacks[0].all_content:
            if item in self.rucksacks[1].all_content and item in self.rucksacks[2].all_content:
                return item
        return None

    def score_common(self):
        return char_score.index(self.common_item) + 1


def load(path: str):
    file = open(path).read()
    return file.split()


# Assignment 1
rucksacks = [Rucksack(content)
             for content in load("data/03/input1.txt") if content]

total_priority = sum([rucksack.common_score for rucksack in rucksacks])

print("Assignment 1:")
print("Total priority: ", total_priority)

# Assignment 2
groups = [Group(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)]

total_group_priority = sum([group.common_score for group in groups])

print("Assignment 2:")
print("Total priority: ", total_group_priority)
