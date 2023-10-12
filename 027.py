import math


def is_prime(number: int) -> bool:
    if 1 < number < 4:
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def solution(a_limit: int = 1000, b_limit: int = 1000) -> int:
    longest = [0, 0, 0]
    for a in range((a_limit * -1) + 1, a_limit):
        for b in range(2, b_limit):
            if is_prime(b):
                count = 0
                n = 0
                while is_prime((n**2) + (a * n) + b):
                    count += 1
                    n += 1
                if count > longest[0]:
                    longest = [count, a, b]
    ans = longest[1] * longest[2]
    return ans

print(solution(1000, 1000))
