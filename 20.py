from math import factorial


def solution(number):
    return sum(int(digit) for digit in str(factorial(number)))


if __name__ == "__main__":

    number = 100

    print(solution(number))
