def load(path):
    program_list = open(path).read().split("\n")
    program = []
    for line in program_list:
        command, *args = line.split()
        program.append((command, int(*args)))
    return program


class Cpu:
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.strengths = []

        self.display = ""

    def run_program(self, program: list):
        for line in program:
            self.execute(line)

    def execute(self, line: tuple):
        command, num = line
        if command == "addx":
            self.addx(num)
        elif command == "noop":
            self.noop()

    def addx(self, num):
        self.run_cycle()
        self.run_cycle()
        self.X += num

    def noop(self):
        self.run_cycle()

    def run_cycle(self):
        if abs(self.cycle % 40 - self.X) <= 1:
            self.display += "#"
        else:
            self.display += "."

        self.cycle += 1

        if self.cycle % 40 == 0:
            print(self.display)
            self.display = ""
        if (self.cycle - 20) % 40 == 0 and self.cycle <= 220:
            self.strengths.append(self.cycle*self.X)


program = load("data/10/input1.txt")

# Assignment 1

cpu = Cpu()

cpu.run_program(program)

print("Assignment 1:")
print("Sum of signal strengths: ", sum(cpu.strengths))
