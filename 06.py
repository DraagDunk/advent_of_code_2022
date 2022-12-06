def load(path: str):
    data = open(path).read().split("\n")
    return data


def find_marker(signal: str, set_size: int = 4):
    for i in range(set_size, len(signal)+1):
        set_size_chars = signal[i-set_size:i]
        if len(set(set_size_chars)) == len(set_size_chars):
            return i


signals = load("data/06/input1.txt")

# Assignment 1

print("Assignment 1:")
for signal in signals:
    marker_char_num = find_marker(signal)
    print(signal[:15], "...", marker_char_num)

# Assignment 2

print("Assignment 2:")
for signal in signals:
    message_marker = find_marker(signal, set_size=14)
    print(signal[:15], "...", message_marker)
