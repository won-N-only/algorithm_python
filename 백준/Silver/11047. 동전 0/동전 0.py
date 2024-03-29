import sys


def input():
    return sys.stdin.readline().strip()


def coin():

    n, k = map(int, input().split())

    coins = []
    for i in range(n):
        coins.append(int(input()))
    coins.reverse()
    idx = 0
    for coin_value in coins:
        if k == 0:
            break
        idx += k // coin_value
        k %= coin_value
    print(idx)


coin()
