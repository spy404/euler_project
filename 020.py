def factorial(num: int) -> int:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def split_and_add(number: int) -> int:
    sum_of_digits = 0
    while number > 0:
        last_digit = number % 10
        sum_of_digits += last_digit
        number = number // 10
    return sum_of_digits


def solution(num: int = 100) -> int:
    nfact = factorial(num)
    result = split_and_add(nfact)
    return result

print(solution(int(input("Enter the Number: ").strip())))
