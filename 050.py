from __future__ import annotations


def prime_sieve(limit: int) -> list[int]:
    is_prime = [True] * limit
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(limit**0.5 + 1), 2):
        index = i * 2
        while index < limit:
            is_prime[index] = False
            index = index + i

    primes = [2]

    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)

    return primes


def solution(ceiling: int = 1_000_000) -> int:
    primes = prime_sieve(ceiling)
    length = 0
    largest = 0

    for i in range(len(primes)):
        for j in range(i + length, len(primes)):
            sol = sum(primes[i:j])
            if sol >= ceiling:
                break

            if sol in primes:
                length = j - i
                largest = sol

    return largest

print(f"{solution() = }")
