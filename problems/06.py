"""
Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

NUMBER = 100


def solution():
    sum_of_the_square = sum(i ** 2 for i in range(1, NUMBER + 1))
    square_of_the_sum = sum(i for i in range(1, NUMBER + 1)) ** 2
    return square_of_the_sum - sum_of_the_square


if __name__ == "__main__":
    print(solution())
