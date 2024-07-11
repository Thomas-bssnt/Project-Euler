from math import factorial


def solution():

    factorials = {str(number): factorial(number) for number in range(10)}

    # A number with at least n digits will be always greater than the sum of the factorial of its digits.
    n = 0
    while sum(factorials["9"] for _ in range(n)) >= 10 ** n - 1:
        n += 1
    n += 1

    return sum(
        number
        for number in range(3, 10 ** n)
        if sum(factorials[digit] for digit in str(number)) == number
    )


if __name__ == "__main__":

    print(solution())
