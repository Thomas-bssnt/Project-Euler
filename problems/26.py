def periodic_decimals_len(divisor):
    dividend = 1
    seen_dividends = {}
    position = 0
    while dividend:
        if dividend in seen_dividends:
            return position - seen_dividends[dividend]
        seen_dividends[dividend] = position
        dividend = (dividend * 10) % divisor
        position += 1
    return 0


def solution():
    return max(range(1, 1000), key=periodic_decimals_len)


if __name__ == "__main__":
    print(solution())
