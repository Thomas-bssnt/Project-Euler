from typing import Generator
from math import isqrt, sqrt
from itertools import count


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


def triangular_number(start: int = 0) -> Generator[int, None, None]:
    """
    Generates the triangular numbers
    """
    for i in count(start):
        yield i * (i + 1) // 2


def pentagonal_number(start: int = 0) -> Generator[int, None, None]:
    """
    Generates the pentagonal numbers
    """
    for i in count(start):
        yield i * (3 * i - 1) // 2


def prime_numbers(limit: int) -> Generator[int, None, None]:
    """
    Generates the prime numbers below the given limit.
    Uses the sieve of Eratosthenes algorithm.
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
    Returns a sorted list of the prime factors of the given number.
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


def proper_divisors(number: int) -> list[int]:
    """
    Returns a sorted list of the proper divisors of the given number.
    """

    if number == 1:
        return []

    divisors = [1]

    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)

    return sorted(divisors)


def sum_proper_divisors(number: int) -> int:
    """
    Returns the sum of the proper divisors of the given number.
    """
    return sum(proper_divisors(number))


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
