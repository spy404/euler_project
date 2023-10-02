def solution() -> int:
    for a in range(300):
        for b in range(a + 1, 400):
            for c in range(b + 1, 500):
                if (a + b + c) == 1000 and (a**2) + (b**2) == (c**2):
                    return a * b * c

    return -1


def solution_fast() -> int:
    for a in range(300):
        for b in range(400):
            c = 1000 - a - b
            if a < b < c and (a**2) + (b**2) == (c**2):
                return a * b * c

    return -1


def benchmark() -> None:
    import timeit

    print(
        timeit.timeit("solution()", setup="from __main__ import solution", number=1000)
    )
    print(
        timeit.timeit(
            "solution_fast()", setup="from __main__ import solution_fast", number=1000
        )
    )

print(f"{solution() = }")
