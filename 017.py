def solution(n: int = 1000) -> int:
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

    count = 0

    for i in range(1, n + 1):
        if i < 1000:
            if i >= 100:
                count += ones_counts[i // 100] + 7

                if i % 100 != 0:
                    count += 3

            if 0 < i % 100 < 20:
                count += ones_counts[i % 100]
            else:
                count += ones_counts[i % 10]
                count += tens_counts[(i % 100 - i % 10) // 10]
        else:
            count += ones_counts[i // 1000] + 8
    return count

print(solution(int(input().strip())))
