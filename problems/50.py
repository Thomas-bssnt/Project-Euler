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

LIMIT = 1000000


def solution():
    primes_up_to_limit = list(prime_numbers(LIMIT))
    prime_lookup = set(primes_up_to_limit)

    max_chain_length = 0
    max_chain_sum = 0

    for start in range(len(primes_up_to_limit)):
        chain_sum = primes_up_to_limit[start]
        for end in range(start + 1, len(primes_up_to_limit)):
            chain_sum += primes_up_to_limit[end]
            if chain_sum > LIMIT:
                break
            if (
                    chain_sum in prime_lookup
                    and (chain_length := end - start + 1) > max_chain_length
            ):
                max_chain_length = chain_length
                max_chain_sum = chain_sum

    return max_chain_sum


if __name__ == "__main__":
    print(solution())
