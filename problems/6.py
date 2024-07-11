def solution(number):
    sum_of_the_square = sum(i ** 2 for i in range(1, number + 1))
    square_of_the_sum = sum(i for i in range(1, number + 1)) ** 2
    return square_of_the_sum - sum_of_the_square


if __name__ == "__main__":

    number = 100

    print(solution(number))
