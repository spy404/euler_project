def solution(power: int = 1000) -> int:
    num = 2**power
    string_num = str(num)
    list_num = list(string_num)
    sum_of_num = 0

    for i in list_num:
        sum_of_num += int(i)

    return sum_of_num


if __name__ == "__main__":
    power = int(input("Enter the power of 2: ").strip())
    print("2 ^ ", power, " = ", 2**power)
    result = solution(power)
    print("Sum of the digits is: ", result)
