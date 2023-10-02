import os


def solution():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    triangle = os.path.join(script_dir, "triangle.txt")

    with open(triangle) as f:
        triangle = f.readlines()

    a = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle]

    for i in range(1, len(a)):
        for j in range(len(a[i])):
            number1 = a[i - 1][j] if j != len(a[i - 1]) else 0
            number2 = a[i - 1][j - 1] if j > 0 else 0
            a[i][j] += max(number1, number2)
    return max(a[-1])

print(solution())
