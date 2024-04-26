import sys


def input():
    return sys.stdin.readline().strip()


def pibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if dp[n] < 0:
            dp[n] = pibo(n-1)+pibo(n-2)
        return dp[n]


n = int(input())
if n == 1:
    print(1)
else:
    dp = [-1 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    print(pibo(n))
