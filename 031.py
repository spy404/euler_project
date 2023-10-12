def one_pence() -> int:
    return 1


def two_pence(x: int) -> int:
    return 0 if x < 0 else two_pence(x - 2) + one_pence()


def five_pence(x: int) -> int:
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x)


def ten_pence(x: int) -> int:
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x)


def twenty_pence(x: int) -> int:
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x)


def fifty_pence(x: int) -> int:
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x)


def one_pound(x: int) -> int:
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x)


def two_pound(x: int) -> int:
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x)


def solution(n: int = 200) -> int:
    return two_pound(n)

print(solution(int(input().strip())))
