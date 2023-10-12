DIGITS_FIFTH_POWER={str(digit): digit**5 for digit in range(10)}


def digits_fifth_powers_sum(number: int) -> int:
    return sum(DIGITS_FIFTH_POWER[digit] for digit in str(number))


def solution() -> int:
    return sum(
        number
        for number in range(1000, 1000000)
        if number == digits_fifth_powers_sum(number)
    )

print(solution())
