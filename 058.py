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


def solution(ratio: float = 0.1) -> int:

    j = 3
    primes = 3

    while primes / (2 * j - 1) >= ratio:
        for i in range(j * j + j + 1, (j + 2) * (j + 2), j + 1):
            primes += is_prime(i)
        j += 2
    return j


if __name__ == "__main__":
    import doctest

    doctest.testmod()
