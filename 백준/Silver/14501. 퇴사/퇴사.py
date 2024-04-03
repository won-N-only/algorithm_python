import sys


def input():
    return sys.stdin.readline().strip()


def quit():
    for i in range(n):
        if i+T[i] <= n:
            dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
        dp[i+1] = max(dp[i+1], dp[i])
    return dp


n = int(input())
T = []
P = []
dp = [0]*(n+1)
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
ans = quit()
print(ans[-1])
