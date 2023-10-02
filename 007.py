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


def solution(nth: int = 10001) -> int:
    try:
        nth = int(nth)
    except (TypeError, ValueError):
        raise TypeError("Parameter nth must be int or castable to int.") from None
    if nth <= 0:
        raise ValueError("Parameter nth must be greater than or equal to one.")
    primes: list[int] = []
    num = 2
    while len(primes) < nth:
        if is_prime(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes[len(primes) - 1]

print(f"{solution() = }")
