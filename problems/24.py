from itertools import permutations


def solution(numbers, index):
    return int("".join(list(permutations(numbers))[index - 1]))


if __name__ == "__main__":
    numbers = "0123456789"
    index = 1000000

    print(solution(numbers, index))

    # No need to sort as permutations return in the right order already
