def is_prime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_truncatable_prime(number):
    if not is_prime(number):
        return False

    number = str(number)
    for i in range(1, len(number)):
        if not is_prime(int(number[i:])) or not is_prime(int(number[:-i])):
            return False

    return True


def solution():
    I = []
    i = 10
    count = 0
    while count < 11:
        if is_truncatable_prime(i):
            I.append(i)
            count += 1
        i += 1
    return sum(I)


if __name__ == "__main__":
    # TODO This is very slow
    
    print(solution())
