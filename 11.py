from tqdm import tqdm
import re


def load(path):
    return open(path).read().split("\n\n")


class Monkey:
    def __init__(self, monkey_string: str):
        p = re.compile(
            r'Monkey ([\d*]).*\n.*: (.*)\n.*: new = (.*)\n.*by (.*)\n.*monkey (.*)\n.*monkey (.*)')
        regex_groups = p.findall(
            monkey_string)[0]
        self.num = int(regex_groups[0])
        self.starting_items = [int(value)
                               for value in regex_groups[1].split(", ")]
        self.new_algo = regex_groups[2].split()
        self.test_val = int(regex_groups[3])
        self.true_throw = int(regex_groups[4])
        self.false_throw = int(regex_groups[5])

        self.reset()

    def reset(self):
        self.inventory = self.starting_items
        self.inspections = 0

    def take_turn(self, monkeys: list, manage_relief=True):
        for item in self.inventory:
            self.inspections += 1
            new_val = self.inspect(item)
            if manage_relief:
                new_val = int(new_val/3)
            else:
                new_val = new_val % self.test_val
            self.throw(new_val, monkeys)
        self.inventory = []

    def inspect(self, old):
        var = old if self.new_algo[2] == "old" else int(self.new_algo[2])
        if self.new_algo[1] == "+":
            new = old + var
        elif self.new_algo[1] == "-":
            new = old - var
        elif self.new_algo[1] == "*":
            new = old * var
        else:
            print("WARNING! Unknown operator ", self.new_algo[1])
        return new

    def throw(self, val, monkeys: list):
        if self.test(val):
            monkeys[self.true_throw].inventory.append(val)
        else:
            monkeys[self.false_throw].inventory.append(val)

    def test(self, val):
        return val % self.test_val == 0

    def __str__(self):
        return ", ".join([str(item) for item in self.inventory])

    def __repr__(self):
        return str(self)


monkey_strings = load("data/11/input1.txt")

# Assignment 1

monkeys = [Monkey(monkey_string) for monkey_string in monkey_strings]

for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn(monkeys)

inspections = [monkey.inspections for monkey in monkeys]
sorted_inspections = sorted(inspections)
monkey_business = sorted_inspections[-2] * sorted_inspections[-1]

print("Assignment 1:")
print("Monkey business level: ", monkey_business)

# Assignment 2

for monkey in monkeys:
    monkey.reset()


for _ in tqdm(range(10000)):
    for monkey in monkeys:
        monkey.take_turn(monkeys, manage_relief=False)

inspections = [monkey.inspections for monkey in monkeys]
sorted_inspections = sorted(inspections)
monkey_business = sorted_inspections[-2] * sorted_inspections[-1]

print("Assignment 2:")
print("Monkey business level: ", monkey_business)
