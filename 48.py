def solution(number_of_digits, bound):
    sum_ = sum(i ** i for i in range(1, bound + 1))
    return str(sum_)[-number_of_digits:]


if __name__ == "__main__":

    number_of_digits = 10
    bound = 1000

    print(solution(number_of_digits, bound))
