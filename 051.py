from __future__ import annotations

from collections import Counter


def prime_sieve(n: int) -> list[int]:
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(n**0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i

    primes = [2]

    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)

    return primes


def digit_replacements(number: int) -> list[list[int]]:
    number_str = str(number)
    replacements = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for duplicate in Counter(number_str) - Counter(set(number_str)):
        family = [int(number_str.replace(duplicate, digit)) for digit in digits]
        replacements.append(family)

    return replacements


def solution(family_length: int = 8) -> int:
    numbers_checked = set()

    primes = {
        x for x in set(prime_sieve(1_000_000)) if len(str(x)) - len(set(str(x))) >= 3
    }

    for prime in primes:
        if prime in numbers_checked:
            continue

        replacements = digit_replacements(prime)

        for family in replacements:
            numbers_checked.update(family)
            primes_in_family = primes.intersection(family)

            if len(primes_in_family) != family_length:
                continue

            return min(primes_in_family)

    return -1

print(solution())
