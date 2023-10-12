def solution(limit=28123):
    sum_divs = [1] * (limit + 1)

    for i in range(2, int(limit**0.5) + 1):
        sum_divs[i * i] += i
        for k in range(i + 1, limit // i + 1):
            sum_divs[k * i] += k + i

    abundants = set()
    res = 0

    for n in range(1, limit + 1):
        if sum_divs[n] > n:
            abundants.add(n)

        if not any((n - a in abundants) for a in abundants):
            res += n

    return res

print(solution())
