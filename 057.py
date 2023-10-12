def solution(n: int = 1000) -> int:
    prev_numerator, prev_denominator = 1, 1
    result = []
    for i in range(1, n + 1):
        numerator = prev_numerator + 2 * prev_denominator
        denominator = prev_numerator + prev_denominator
        if len(str(numerator)) > len(str(denominator)):
            result.append(i)
        prev_numerator = numerator
        prev_denominator = denominator

    return len(result)

print(f"{solution() = }")
