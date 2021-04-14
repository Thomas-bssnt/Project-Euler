def solution(bound):
    return sum(
        n
        for n in range(bound)
        if n % 3 == 0 or n % 5 == 0
    )


if __name__ == "__main__":

    bound = 1000

    print(solution(bound))
