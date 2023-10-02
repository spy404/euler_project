import os


def solution():
    file_path = os.path.join(os.path.dirname(__file__), "num.txt")
    with open(file_path) as file_hand:
        return str(sum(int(line) for line in file_hand))[:10]

print(solution())
