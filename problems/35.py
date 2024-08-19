from math import isqrt


def prime_numbers_generator(max_number):
    numbers = [True] * (max_number + 1)

    numbers[0] = numbers[1] = False

    for i in range(isqrt(max_number) + 1):
        if numbers[i]:
            for j in range(i * i, max_number + 1, i):
                numbers[j] = False
            yield i

    for i in range(isqrt(max_number) + 1, max_number + 1):
        if numbers[i]:
            yield i


def cyclic_permutations(number):
    number = str(number)
    for i in range(len(number)):
        yield int(number[i:] + number[:i])


def solution():
    bound = 1000000

    prime_numbers = set(prime_numbers_generator(bound))

    return sum(
        1
        for prime in prime_numbers
        if set(cyclic_permutations(prime)).issubset(prime_numbers)
    )


if __name__ == "__main__":
    print(solution())
