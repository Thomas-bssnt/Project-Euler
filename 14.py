from functools import cache


@cache
def collatz_sequence_length(number):
    if number == 1:
        return 1
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    return collatz_sequence_length(number) + 1


def solution(bound):
    return max(range(1, bound), key=collatz_sequence_length)


if __name__ == "__main__":

    bound = 1000000

    print(solution(bound))
