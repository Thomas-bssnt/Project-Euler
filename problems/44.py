"""
Problem 44: Pentagon numbers

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 −
22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of
D?
"""
from math import inf

from helpers import pentagonal_number


def solution():
    """
    The algorithm generates pentagonal numbers on the fly, storing their sums
    and differences in a dictionary if the difference is also pentagonal. It
    then checks each new pentagonal number against this dictionary to find pairs
    that satisfy the condition. The algorithm continues to generate numbers
    until the difference between consecutive pentagonal numbers exceeds the
    current minimum difference, at which point it returns the minimum difference
    found.
    """
    pentagonals = []
    pentagonals_lookup = set()
    sum_to_diff = {}
    min_diff = inf

    for new_pentagonal in pentagonal_number():

        if (
                new_pentagonal in sum_to_diff and
                sum_to_diff[new_pentagonal] < min_diff
        ):
            min_diff = sum_to_diff[new_pentagonal]

        if pentagonals and new_pentagonal - pentagonals[-1] > min_diff:
            return min_diff

        for old_pentagonal in reversed(pentagonals):
            diff = new_pentagonal - old_pentagonal

            if diff in pentagonals_lookup:
                sum_to_diff[new_pentagonal + old_pentagonal] = diff

            if diff > min_diff:
                break

        pentagonals.append(new_pentagonal)
        pentagonals_lookup.add(new_pentagonal)


if __name__ == "__main__":
    print(solution())