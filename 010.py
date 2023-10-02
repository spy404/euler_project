import math


def is_prime(number: int) -> bool:
    if 1 < number < 4:
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def solution(n: int = 2000000) -> int:
    return sum(num for num in range(3, n, 2) if is_prime(num)) + 2 if n > 2 else 0

print(f"{solution() = }")
