import math
from decimal import Decimal, getcontext

def solution(n: int = 4000000) -> int:
    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or castable to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater than or equal to one.")
    getcontext().prec = 100
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2)

    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2)
    total = num // 2
    return int(total)

print(f"{solution() = }")
