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

    primes_below_bound = primes_below(bound)

    longest_sum = 0
    prime_sum = 0

    for start in range(len(primes_below_bound)):
        sum_of_consecutive_primes = primes_below_bound[start]
        for end in range(start + 1, len(primes_below_bound)):
            sum_of_consecutive_primes += primes_below_bound[end]
            if sum_of_consecutive_primes > bound:
                break
            if sum_of_consecutive_primes in primes_below_bound and (length := end - start + 1) > longest_sum:
                longest_sum = length
                prime_sum = sum_of_consecutive_primes

    return prime_sum


if __name__ == "__main__":

    bound = 1000000

    print(solution(bound))
