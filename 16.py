def solution(power):
    return sum(int(digit) for digit in str(2 ** power))


if __name__ == "__main__":

    power = 1000

    print(solution(power))
