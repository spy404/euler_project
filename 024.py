from itertools import permutations


def solution():
    result = list(map("".join, permutations("0123456789")))
    return result[999999]

print(solution())
