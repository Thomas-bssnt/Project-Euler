def is_prime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    result = 1
    for number in numbers:
        if is_prime(number):
            power = 1
            while number ** power <= max(numbers):
                result *= number
                power += 1
    return result


if __name__ == "__main__":

    numbers = range(1, 20)

    print(solution(numbers))
