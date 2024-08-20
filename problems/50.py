"""
Problem 50: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one
hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from helpers import prime_numbers


def solution(bound):
    primes_below_bound = list(prime_numbers(bound))

    longest_sum = 0
    prime_sum = 0

    for start in range(len(primes_below_bound)):
        sum_of_consecutive_primes = primes_below_bound[start]
        for end in range(start + 1, len(primes_below_bound)):
            sum_of_consecutive_primes += primes_below_bound[end]
            if sum_of_consecutive_primes > bound:
                break
            if (
                    sum_of_consecutive_primes in primes_below_bound
                    and (length := end - start + 1) > longest_sum
            ):
                longest_sum = length
                prime_sum = sum_of_consecutive_primes

    return prime_sum


if __name__ == "__main__":
    bound = 1000000

    print(solution(bound))

    # TODO: Very slow
