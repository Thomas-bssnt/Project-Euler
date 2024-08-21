"""
Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import comb

GRID_SIZE = (20, 20)


def solution():
    return comb(GRID_SIZE[0] + GRID_SIZE[1], GRID_SIZE[0])


if __name__ == "__main__":
    print(solution())
