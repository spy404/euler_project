from __future__ import annotations

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


def list_truncated_nums(n: int) -> list[int]:
    str_num = str(n)
    list_nums = [n]
    for i in range(1, len(str_num)):
        list_nums.append(int(str_num[i:]))
        list_nums.append(int(str_num[:-i]))
    return list_nums


def validate(n: int) -> bool:
    if len(str(n)) > 3:
        if not is_prime(int(str(n)[-3:])) or not is_prime(int(str(n)[:3])):
            return False
    return True


def compute_truncated_primes(count: int = 11) -> list[int]:
    list_truncated_primes: list[int] = []
    num = 13
    while len(list_truncated_primes) != count:
        if validate(num):
            list_nums = list_truncated_nums(num)
            if all(is_prime(i) for i in list_nums):
                list_truncated_primes.append(num)
        num += 2
    return list_truncated_primes


def solution() -> int:
    return sum(compute_truncated_primes(11))

print(f"{sum(compute_truncated_primes(11)) = }")
