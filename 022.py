import os


def solution():
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        names = str(file.readlines()[0])
        names = names.replace('"', "").split(",")

    names.sort()

    name_score = 0
    total_score = 0

    for i, name in enumerate(names):
        for letter in name:
            name_score += ord(letter) - 64

        total_score += (i + 1) * name_score
        name_score = 0
    return total_score

print(solution())
