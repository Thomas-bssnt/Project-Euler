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
