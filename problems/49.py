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

from helpers import prime_numbers

NUMBER_OF_DIGITS = 4


def solution():
    primes_with_4_digits = [
        prime
        for prime in prime_numbers(10 ** NUMBER_OF_DIGITS)
        if len(str(prime)) == 4
    ]

    for i in range(len(primes_with_4_digits)):
        for j in range(i + 1, len(primes_with_4_digits)):
            for k in range(j + 1, len(primes_with_4_digits)):

                if (
                        primes_with_4_digits[j] - primes_with_4_digits[i]
                        == primes_with_4_digits[k] - primes_with_4_digits[j]
                ):
                    if (
                            sorted(str(primes_with_4_digits[i]))
                            == sorted(str(primes_with_4_digits[j]))
                            == sorted(str(primes_with_4_digits[k]))
                    ):

                        if primes_with_4_digits[i] not in [1487, 4817, 8147]:
                            return (
                                    str(primes_with_4_digits[i])
                                    + str(primes_with_4_digits[j])
                                    + str(primes_with_4_digits[k])
                            )

    return None


if __name__ == "__main__":
    print(solution())
