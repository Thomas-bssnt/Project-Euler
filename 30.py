def solution(power):

    # A number with at least n digits will be always greater than the sum of the powers
    n = 0
    while sum(9 ** power for _ in range(n)) >= 10 ** n - 1:
        n += 1
    n += 1

    return sum(
        number
        for number in range(3, 10 ** n)
        if number == sum(int(digit) ** power for digit in str(number))
    )


if __name__ == "__main__":

    power = 5

    print(solution(power))
