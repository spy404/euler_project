def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def sum_reverse(n: int) -> int:
    return int(n) + int(str(n)[::-1])


def solution(limit: int = 10000) -> int:
    lychrel_nums = []
    for num in range(1, limit):
        iterations = 0
        a = num
        while iterations < 50:
            num = sum_reverse(num)
            iterations += 1
            if is_palindrome(num):
                break
        else:
            lychrel_nums.append(a)
    return len(lychrel_nums)

print(f"{solution() = }")
