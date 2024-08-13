from itertools import combinations
from fractions import Fraction
from math import prod


def get_non_trivial_fractions():
    numbers = set(range(10, 100)) - set(range(10, 100, 10))
    fractions = []
    for numerator, denominator in combinations(numbers, 2):
        for i in str(numerator):
            if i in str(denominator):
                reduced_numerator = int(str(numerator).replace(i, '', 1))
                reduced_denominator = int(str(denominator).replace(i, '', 1))
                if numerator / denominator == reduced_numerator / reduced_denominator:
                    fractions.append((numerator, denominator))
    return fractions


def solution():
    return prod(
        Fraction(*fraction)
        for fraction in get_non_trivial_fractions()
    ).denominator


if __name__ == "__main__":
    print(solution())
