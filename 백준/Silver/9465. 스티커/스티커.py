import sys


def input():
    return sys.stdin.readline()


T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))

    dp_prev = [0, sticker[0][0], sticker[1][0]]

    for i in range(1, n):
        dp = [0, 0, 0]
        dp[0] = max(dp_prev[0], dp_prev[1], dp_prev[2])
        dp[1] = max(dp_prev[0], dp_prev[2]) + sticker[0][i]
        dp[2] = max(dp_prev[0], dp_prev[1]) + sticker[1][i]
        dp_prev = dp

    print(max(dp_prev))
