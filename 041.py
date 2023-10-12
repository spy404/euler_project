from __future__ import annotations

import math
from itertools import permutations


def is_prime(number: int) -> bool:

    if 1 < number < 4:
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def solution(n: int = 7) -> int:
    pandigital_str = "".join(str(i) for i in range(1, n + 1))
    perm_list = [int("".join(i)) for i in permutations(pandigital_str, n)]
    pandigitals = [num for num in perm_list if is_prime(num)]
    return max(pandigitals) if pandigitals else 0

print(f"{solution() = }")
