def solution(a_bounds, b_bounds):
    return len({a ** b for a in range(a_bounds[0], a_bounds[1] + 1) for b in range(b_bounds[0], b_bounds[1] + 1)})


if __name__ == "__main__":
    a_bounds = (2, 100)
    b_bounds = (2, 100)

    print(solution(a_bounds, b_bounds))
