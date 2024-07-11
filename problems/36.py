def solution(bound):
    return sum(
        number
        for number in range(bound)
        if (str(number) == str(number)[::-1] and f"{number:b}" == f"{number:b}"[::-1])
    )


if __name__ == "__main__":

    bound = 1000000

    print(solution(bound))
