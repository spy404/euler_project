def solution(numerator: int = 1, digit: int = 1000) -> int:
    the_digit = 1
    longest_list_length = 0

    for divide_by_number in range(numerator, digit + 1):
        has_been_divided: list[int] = []
        now_divide = numerator
        for _ in range(1, digit + 1):
            if now_divide in has_been_divided:
                if longest_list_length < len(has_been_divided):
                    longest_list_length = len(has_been_divided)
                    the_digit = divide_by_number
            else:
                has_been_divided.append(now_divide)
                now_divide = now_divide * 10 % divide_by_number

    return the_digit
#Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
