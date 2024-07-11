from itertools import count


def generator():

    T = (int(n * (n + 1) / 2) for n in count())
    P = (int(n * (3 * n - 1) / 2) for n in count())
    H = (int(n * (2 * n - 1)) for n in count())

    t = next(T)
    p = next(P)
    h = next(H)

    while True:

        max_ = max(t, p, h)
        if t < max_:
            t = next(T)
        if p < max_:
            p = next(P)
        if h < max_:
            h = next(H)

        if t == p == h:
            yield t
            t = next(T)
            p = next(P)
            h = next(H)


def solution(bound):
    gene = generator()
    while (number := next(gene)) <= bound:
        continue
    return number


if __name__ == "__main__":

    bound = 40755

    print(solution(bound))
