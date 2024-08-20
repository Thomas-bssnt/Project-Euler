"""
Problem 28: Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""


def solution(square_size):
    return 1 + sum(4 * n ** 2 - 6 * (n - 1) for n in range(3, square_size + 1, 2))


# The sum of the four corner of a square of size n is:
# n^2 + (n^2 - (n-1)) + (n^2 - 2(n-1)) + (n^2 - 3(n-1))
# = 4n^2 - 6(n-1)

if __name__ == "__main__":
    square_size = 1001

    print(solution(square_size))
