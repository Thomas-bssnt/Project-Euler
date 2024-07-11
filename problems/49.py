def primes_below(bound):
    primes = []
    L = [False, False] + [True] * (bound - 1)
    for number, is_prime in enumerate(L):
        if is_prime:
            primes.append(number)
            for k in range(2, bound // number + 1):
                L[number * k] = False
    return primes


def solution(number_of_digits):

    primes_with_4_digits = [
        prime
        for prime in primes_below(10 ** number_of_digits)
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

    number_of_digits = 4

    print(solution(number_of_digits))
