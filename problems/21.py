"""
Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are amicable.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

BOUND = 10000


def get_proper_divisors_sum(bound):
    proper_divisors_sum = [0] * bound
    for number in range(1, bound):
        for multiple in range(2 * number, bound, number):
            proper_divisors_sum[multiple] += number
    return proper_divisors_sum


def solution():
    proper_divisors_sum = get_proper_divisors_sum(BOUND)

    result = 0
    for number in range(BOUND):
        d_number = proper_divisors_sum[number]
        if (
                d_number < BOUND and
                d_number != number and
                number == proper_divisors_sum[d_number]
        ):
            result += number
    return result


if __name__ == "__main__":
    print(solution())
