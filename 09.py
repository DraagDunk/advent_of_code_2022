def load(path):
    lst = open(path).read().split("\n")
    out = []
    for command in lst:
        direction, moves = command.split()
        out.append((direction, int(moves)))
    return out


class Head:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.last_x = 0
        self.lasy_y = 0

    @property
    def position(self):
        return (self.x, self.y)

    def move(self, direction: str):
        self.last_x = self.x
        self.last_y = self.y
        if direction == "U":
            self.y += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "D":
            self.y -= 1
        elif direction == "R":
            self.x += 1

    def __str__(self):
        return f"Head at {self.position}."


class Tail:
    def __init__(self, head):
        self.head = head
        self.x = 0
        self.y = 0

        self.last_x = 0
        self.last_y = 0

        self.history = set((self.x, self.y))

    @property
    def head_is_adjacent(self):
        return abs(self.x - self.head.x) <= 1 and abs(self.y - self.head.y) <= 1

    @property
    def position(self):
        return(self.x, self.y)

    def move_with_head(self):
        if not self.head_is_adjacent:
            self.last_x = self.x
            self.last_y = self.y

            self.x = self.head.last_x
            self.y = self.head.last_y

            self.history.add(self.position)

    def __str__(self):
        return f"Tail at {self.position}."


commands = load("data/09/input1.txt")

# Assignment 1

head = Head()
tail = Tail(head=head)

for command in commands:
    direction, moves = command
    for i in range(moves):
        head.move(direction)
        tail.move_with_head()

print("Assignment 1:")
print("Visited spots: ", len(tail.history))

# Assignment 2

head = Head()
tails = [Tail(head=head)]
for i in range(8):
    tails.append(Tail(head=tails[i]))

for command in commands:
    direction, moves = command
    for i in range(moves):
        head.move(direction)
        for tail in tails:
            tail.move_with_head()

print(head)
for tail in tails:
    print(tail)

print("Assignment 2:")
print("Visited spots (last tail): ", len(tails[-1].history))
