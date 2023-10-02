def solution(n: int = 998001) -> int:
    for number in range(n - 1, 9999, -1):
        str_number = str(number)

        if str_number == str_number[::-1]:
            divisor = 999
            while divisor != 99:
                if (number % divisor == 0) and (len(str(number // divisor)) == 3.0):
                    return number
                divisor -= 1
    raise ValueError("That number is larger than our acceptable range.")

print(f"{solution() = }")
