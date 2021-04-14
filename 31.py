def solution(price, coins):
    combinations = [1] + [0] * price
    for coin in coins:
        for i in range(coin, price + 1):
            combinations[i] += combinations[i - coin]
    return combinations[-1]


if __name__ == "__main__":

    price = 200
    coins = {1, 2, 5, 10, 20, 50, 100, 200}

    print(solution(price, coins))
