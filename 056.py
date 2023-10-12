def solution(a: int = 100, b: int = 100) -> int:
    return max(
        sum(int(x) for x in str(base**power))
        for base in range(a)
        for power in range(b)
    )


# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
