import sys

n = int(sys.stdin.readline())
T = []
P = []
dp = [0]*(n+1)
for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(n):
    if i+T[i] <= n:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[-1])
