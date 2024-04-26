import sys


def input():
    return sys.stdin.readline().strip()


def change(wallet):
    temp = [1e9]*(k+1)
    temp[0] = 0
    for coin in wallet:
        for i in range(coin, k+1):
            # 1로 만들기랑 같은느낌이네 이거
            temp[i] = min(temp[i], temp[i-coin]+1)
    return print(temp[-1]) if temp[-1] < 1e9-1 else print(-1)


n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
change(coins)
