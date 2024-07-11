def fibonacci_generator(F1, F2):
    a = F1
    yield a
    b = F2
    yield b
    while True:
        a, b = b, a + b
        yield b


def solution(bound, F1, F2):
    fibonacci = fibonacci_generator(F1, F2)
    result = 0
    while (number := next(fibonacci)) < bound:
        if number % 2 == 0:
            result += number
    return result


if __name__ == "__main__":

    bound = 4000000
    F1, F2 = 1, 1

    print(solution(bound, F1, F2))
