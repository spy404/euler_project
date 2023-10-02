def solution(n: int = 100) -> int:
    sum_of_squares = 0
    sum_of_ints = 0
    for i in range(1, n + 1):
        sum_of_squares += i**2
        sum_of_ints += i
    return sum_of_ints**2 - sum_of_squares

print(f"{solution() = }")
