def get(path: str):
    file = open(path).read()
    rounds = file.split("\n")
    return rounds


wins_against = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draws_against = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}


loses_against = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

state_scores = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def get_score(rnd: str):
    if rnd:
        opponent, me = rnd.split()
    else:
        return 0

    score = scores[me]

    if wins_against[opponent] == me:
        score += 6
    elif loses_against[opponent] == me:
        pass
    else:
        score += 3

    return score


def get_score2(rnd: str):
    if rnd:
        opponent, state = rnd.split()
    else:
        return 0

    score = state_scores[state]

    if state == "X":  # Lose
        move = loses_against[opponent]
    elif state == "Y":  # Draw
        move = draws_against[opponent]
    elif state == "Z":  # Win
        move = wins_against[opponent]
    score += scores[move]

    return score


# Assignment 1
rounds = get("data/02/input1.txt")

result = sum([get_score(rnd) for rnd in rounds])

print("Assignment 1:")
print("Total score: ", result)

# Assignment 2
result2 = sum([get_score2(rnd) for rnd in rounds])

print("Assignment 2:")
print("Total score: ", result2)
