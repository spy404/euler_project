def fibonacci(n: int) -> int:
    if n == 1 or not isinstance(n, int):
        return 0
    elif n == 2:
        return 1
    else:
        sequence = [0, 1]
        for i in range(2, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2])

        return sequence[n]


def fibonacci_digits_index(n: int) -> int:
    digits = 0
    index = 2

    while digits < n:
        index += 1
        digits = len(str(fibonacci(index)))

    return index


def solution(n: int = 1000) -> int:
    return fibonacci_digits_index(n)


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
