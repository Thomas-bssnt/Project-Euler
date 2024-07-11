# def triangular_number():
#     triangular_num = number = 1
#     while True:
#         yield triangular_num
#         number += 1
#         triangular_num += number


# def get_factors(number):
#     return [n for n in range(1, number + 1) if number % n == 0]


# triangular_number = triangular_number()

# while True:
#     triangular_num = next(triangular_number)
#     factors = get_factors(triangular_num)
#     if len(factors) > 500:
#         result = triangular_num
#         break

#     print(triangular_num, len(factors))

# print(result)

from math import sqrt
from itertools import count


# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
    end = int(sqrt(n))
    result = sum(2 for i in range(1, end + 1) if n % i == 0)
    if end ** 2 == n:
        result -= 1
    return result


def solution():
    triangle = 0
    for i in count(1):
        triangle += i
        if num_divisors(triangle) > 500:
            return triangle


if __name__ == "__main__":

    print(solution())
