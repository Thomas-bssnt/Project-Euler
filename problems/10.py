"""
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def primes_below(bound):
    primes = []
    L = [False, False] + [True] * (bound - 1)
    for number, is_prime in enumerate(L):
        if is_prime:
            primes.append(number)
            for k in range(2, bound // number + 1):
                L[number * k] = False
    return primes


def solution(bound):
    return sum(primes_below(bound))


if __name__ == "__main__":
    bound = 2000000

    print(solution(bound))
