import sys


def input():
    return sys.stdin.readline().strip()


def mybag(n, k, arr):
    for i in range(1, n+1):
        for w in range(1, k+1):
            if arr[i-1][0] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-arr[i-1][0]]+arr[i-1][1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][k]



n, k = map(int, input().split())
# 이거 dp = [[0]*(k+1)]*(n+1)이렇게만들면 [0]이 다 같은 곳을 참조해서 안됨
dp = [[0]*(k+1)for _ in range(n+1)]

not_in_bag = []
for _ in range(n):
    a, b = map(int, input().split())
    not_in_bag.append([a, b])

not_in_bag.sort()

ans = mybag(n, k, not_in_bag)

print(ans)
