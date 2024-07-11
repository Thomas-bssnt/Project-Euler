def fibonacci_generator(F1, F2):
    a = F1
    yield a
    b = F2
    yield b
    while True:
        a, b = b, a + b
        yield b


def solution(number_of_digits, F1, F2):
    fibonacci = fibonacci_generator(F1, F2)
    i = 1
    while len(str(next(fibonacci))) < number_of_digits:
        i += 1
    return i


if __name__ == "__main__":

    number_of_digits = 1000
    F1, F2 = 1, 1

    print(solution(number_of_digits, F1, F2))
