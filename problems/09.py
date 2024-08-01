def solution(triplet_sum):
    for a in range(1, triplet_sum):
        for b in range(a + 1, triplet_sum):
            c = triplet_sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return None


if __name__ == "__main__":

    triplet_sum = 1000

    print(solution(triplet_sum))
