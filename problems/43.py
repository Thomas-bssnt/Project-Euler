from itertools import permutations


def solution():
    return sum(
        int("".join(number))
        for number in permutations("0123456789")
        if (
                int("".join(number[1:4])) % 2 == 0 and
                int("".join(number[2:5])) % 3 == 0 and
                int("".join(number[3:6])) % 5 == 0 and
                int("".join(number[4:7])) % 7 == 0 and
                int("".join(number[5:8])) % 11 == 0 and
                int("".join(number[6:9])) % 13 == 0 and
                int("".join(number[7:10])) % 17 == 0
        )
    )


if __name__ == "__main__":
    print(solution())
