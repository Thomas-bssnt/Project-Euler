def get_proper_divisors_sum(bound):
    proper_divisors_sum = [0] * bound
    for number in range(1, bound):
        for multiple in range(2 * number, bound, number):
            proper_divisors_sum[multiple] += number
    return proper_divisors_sum


def solution(bound):

    proper_divisors_sum = get_proper_divisors_sum(bound)

    result = 0
    for number in range(bound):
        d_number = proper_divisors_sum[number]
        if (
                d_number < bound and
                d_number != number and
                number == proper_divisors_sum[d_number]
        ):
            result += number
    return result


if __name__ == "__main__":

    bound = 10000

    print(solution(bound))
