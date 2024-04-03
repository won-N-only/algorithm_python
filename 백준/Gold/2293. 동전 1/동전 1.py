import sys


def input():
    return sys.stdin.readline().strip()


def coin_segi(wallet):
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for coin in wallet:
        for i in range(coin, k+1):
            dp[i] += dp[i-coin]
    return dp


n, k = map(int, input().split())
wallet = set()
for i in range(n):
    wallet.add(int(input()))
ans = coin_segi(wallet)
print(ans[-1])
