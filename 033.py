from __future__ import annotations

from fractions import Fraction


def is_digit_cancelling(num: int, den: int) -> bool:
    return (
        num != den and num % 10 == den // 10 and (num // 10) / (den % 10) == num / den
    )


def fraction_list(digit_len: int) -> list[str]:
    solutions = []
    den = 11
    last_digit = int("1" + "0" * digit_len)
    for num in range(den, last_digit):
        while den <= 99:
            if (num != den) and (num % 10 == den // 10) and (den % 10 != 0):
                if is_digit_cancelling(num, den):
                    solutions.append(f"{num}/{den}")
            den += 1
        num += 1
        den = 10
    return solutions


def solution(n: int = 2) -> int:
    result = 1.0
    for fraction in fraction_list(n):
        frac = Fraction(fraction)
        result *= frac.denominator / frac.numerator
    return int(result)

print(solution())
