from math import comb


def solution(grid_size):
    return comb(grid_size[0] + grid_size[1], grid_size[0])


if __name__ == "__main__":
    grid_size = (20, 20)

    print(solution(grid_size))
