"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def get_prime_factors(number_to_factorize):
    prime_factors = []

    number = 2
    while number <= number_to_factorize:
        if number_to_factorize % number == 0:
            number_to_factorize /= number
            prime_factors.append(number)
        else:
            number += 1

    return prime_factors


def solution(number_to_factorize):
    return max(get_prime_factors(number_to_factorize))


if __name__ == "__main__":
    number_to_factorize = 600851475143

    print(solution(number_to_factorize))
