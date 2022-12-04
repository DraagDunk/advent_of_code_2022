def load(path: str):
    file = open(path).read()
    return file.split()


def intervals_fully_contained(intervals: str):
    interval1, interval2 = [interval.split(
        "-") for interval in intervals.split(",")]

    if (int(interval1[0]) <= int(interval2[0])
        and int(interval1[1]) >= int(interval2[1])) \
        or (int(interval2[0]) <= int(interval1[0])
            and int(interval2[1]) >= int(interval1[1])):
        return True
    else:
        return False


def intervals_overlap(intervals: str):
    interval1, interval2 = [interval.split(
        "-") for interval in intervals.split(",")]

    if (int(interval1[0]) <= int(interval2[1])
            and int(interval1[1]) >= int(interval2[0])):
        return True
    else:
        return False


# Assignment 1
pairs = load("data/04/input1.txt")

fully_contained_count = 0
for pair in pairs:
    contained = intervals_fully_contained(pair)
    if contained:
        fully_contained_count += 1

print("Assignment 1:")
print("Amount fully contained: ", fully_contained_count)

# Assignment 2
overlap_count = 0
for pair in pairs:
    overlap = intervals_overlap(pair)
    if overlap:
        overlap_count += 1

print("Assignment 2:")
print("Amount overlapping: ", overlap_count)
