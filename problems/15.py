"""
Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right
corner.

How many such routes are there through a 20×20 grid?
"""

from math import comb


def solution(grid_size):
    return comb(grid_size[0] + grid_size[1], grid_size[0])


if __name__ == "__main__":
    grid_size = (20, 20)

    print(solution(grid_size))
