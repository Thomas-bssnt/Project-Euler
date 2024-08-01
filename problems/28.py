def solution(square_size):
    return 1 + sum(4 * n ** 2 - 6 * (n - 1) for n in range(3, square_size + 1, 2))


# The sum of the four corner of a square of size n is:
# n^2 + (n^2 - (n-1)) + (n^2 - 2(n-1)) + (n^2 - 3(n-1))
# = 4n^2 - 6(n-1)

if __name__ == "__main__":
    square_size = 1001

    print(solution(square_size))
