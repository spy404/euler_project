def solution(n: int = 100) -> int:
    collect_powers = set()

    current_pow = 0

    n = n + 1

    for a in range(2, n):
        for b in range(2, n):
            current_pow = a**b
            collect_powers.add(current_pow)
    return len(collect_powers)

print("Number of terms ", solution(int(str(input()).strip())))
