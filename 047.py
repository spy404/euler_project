from functools import lru_cache


def unique_prime_factors(n: int) -> set:
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


@lru_cache
def upf_len(num: int) -> int:
    return len(unique_prime_factors(num))


def equality(iterable: list) -> bool:
    return len(set(iterable)) in (0, 1)


def run(n: int) -> list:
    base = 2

    while True:
        group = [base + i for i in range(n)]

        checker = [upf_len(x) for x in group]
        checker.append(n)

        if equality(checker):
            return group

        base += 1


def solution(n: int = 4) -> int:
    results = run(n)
    return results[0] if len(results) else None

print(solution())
