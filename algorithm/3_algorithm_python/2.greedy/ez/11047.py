import sys


def input():
    return sys.stdin.readline().strip()


def coin(k, idx):
    for coin_value in coins:
        if k == 0:
            break

        idx += k // coin_value
        k %= coin_value
    print(idx)


def coin2():
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    print(dp[k])


n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
coins.reverse()

idx = 0

coin(k, idx)
coin2()
