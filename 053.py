from math import factorial


def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def solution():
    total = 0

    for i in range(1, 101):
        for j in range(1, i + 1):
            if combinations(i, j) > 1e6:
                total += 1
    return total

print(solution())
