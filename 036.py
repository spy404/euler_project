from __future__ import annotations


def is_palindrome(n: int | str) -> bool:
    n = str(n)
    return n == n[::-1]


def solution(n: int = 1000000):
    total = 0

    for i in range(1, n):
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]):
            total += i
    return total

print(solution(int(str(input().strip()))))
