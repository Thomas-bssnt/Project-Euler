"""
Problem 39: Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def count_pythagoras_triples_for_perimeter(p):
    """
    Let's choose a, b, c such that a ≤ b < c.

    Moreover, we know that:
    a + b + c = p (by definition)
    a + b > c (triangle inequality)

    For a we have:
    1 ≤ a ≤ p/3
    (as a is the smallest side of the triangle)

    For b we have:
    a ≤ b < (p-a)/2  (from a ≤ b < c)
    (p/2 - a) < b    (from triangle inequality a + b > c)

    Therefore, combining the bounds for b:
    max(a, p/2 - a) < b < (p-a)/2

    Finally:
    c = p - a - b
    """
    n = 0
    for a in range(1, p // 3 + 1):
        for b in range(max(a, p // 2 - a), (p - a) // 2 + 1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                n += 1
    return n


def solution():
    return max(range(3, 1001), key=count_pythagoras_triples_for_perimeter)


if __name__ == "__main__":
    print(solution())
