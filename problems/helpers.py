from typing import Generator
from math import isqrt, sqrt


def fibonacci(f1: int, f2: int) -> Generator[int, None, None]:
    """
    Generates the fibonacci sequence starting with f1 and f2.
    """
    yield f1
    yield f2

    a = f1
    b = f2
    while True:
        a, b = b, a + b
        yield b


def prime_numbers(limit: int) -> Generator[int, None, None]:
    """
    Generates the prime numbers below the given limit.
    """
    primes = [True] * (limit + 1)

    primes[0] = primes[1] = False

    for number in range(isqrt(limit) + 1):
        if primes[number]:
            for multiple in range(number * number, limit + 1, number):
                primes[multiple] = False
            yield number

    for number in range(isqrt(limit) + 1, limit + 1):
        if primes[number]:
            yield number


def prime_factorization(number: int) -> list[int]:
    """
    Returns a list of prime factors of the given number.
    The factors are sorted in ascending order.
    """
    prime_factors = []

    factor = 2
    while factor <= int(sqrt(number)):
        while number % factor == 0:
            number /= factor
            prime_factors.append(factor)
        factor += 1

    # If remaining, number_to_factorize is a prime factor
    if number > 1:
        prime_factors.append(int(number))

    return prime_factors


def maximum_path_sum(triangle: list[list[int]]) -> int:
    """
    Returns the maximum path sum of the given triangle.
    """
    cumulated_row = triangle[-1]
    for row in reversed(triangle[:-1]):
        cumulated_row = [
            row[i] + max(cumulated_row[i], cumulated_row[i + 1])
            for i in range(len(row))
        ]
    return cumulated_row[0]


def is_palindrome(number: int | str) -> bool:
    """
    Returns whether the given number is a palindrome number.
    """
    num_str = str(number)
    return num_str == num_str[::-1]


def is_prime(number: int) -> bool:
    """
    Returns whether the given number is a prime number.
    """
    if number < 2:
        return False

    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return False

    return True
