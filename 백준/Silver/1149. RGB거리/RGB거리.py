import sys

def input():
    return sys.stdin.readline().strip()

def colour(n):

    for i in range(2, n+1):
        dp[i][1] = min(dp[i-1][2], dp[i-1][3])+red[i]
        dp[i][2] = min(dp[i-1][1], dp[i-1][3])+blue[i]
        dp[i][3] = min(dp[i-1][1], dp[i-1][2])+green[i]
    return min(dp[n])


n = int(input())
red = [[0]]
blue = [[0]]
green = [[0]]
dp = [[2e9]*(4) for i in range(n+1)]
for i in range(n):
    r, g, b = map(int, input().split())
    red.append(r)
    blue.append(b)
    green.append(g)
dp[1][1] = red[1]
dp[1][2] = blue[1]
dp[1][3] = green[1]

res = colour(n)
print(res)
