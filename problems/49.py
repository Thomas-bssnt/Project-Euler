"""
Problem 49: Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from collections import defaultdict
from itertools import combinations

from helpers import prime_numbers

NUMBER_OF_DIGITS = 4
KNOWN_SEQUENCE = (1487, 4817, 8147)


def solution():
    primes_with_4_digits = [
        prime
        for prime in prime_numbers(10 ** NUMBER_OF_DIGITS)
        if len(str(prime)) == 4
    ]

    prime_groups = defaultdict(list)
    for prime in primes_with_4_digits:
        prime_groups[tuple(sorted(str(prime)))].append(prime)

    for prime_group in prime_groups.values():
        if len(prime_group) >= 3:
            for prime1, prime2, prime3 in combinations(prime_group, 3):
                # itertools.combinations preserves the order
                if (
                        prime2 - prime1 == prime3 - prime2 and
                        prime1 not in KNOWN_SEQUENCE
                ):
                    return str(prime1) + str(prime2) + str(prime3)


if __name__ == "__main__":
    print(solution())
