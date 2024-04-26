import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().strip()
# 문제가좀 .. .


def matrix_chain_multiplication(mat):
    n = len(mat)
    dp = [[0] * n for _ in range(n)]
    for cnt in range(1, n):
        for i in range(n - cnt):
            j = i + cnt
            dp[i][j] = 1e9
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + \
                    mat[i][0] * mat[k][1] * mat[j][1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]


n = int(input())
mat = [tuple(map(int, input().split())) for i in range(n)]
ans = matrix_chain_multiplication(mat)
print(ans)
