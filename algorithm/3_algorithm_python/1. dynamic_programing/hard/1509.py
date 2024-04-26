import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().strip()


def pelin2(s, a, b):
    if a > b:
        return 1

    if dp[a][b] != -1:
        return dp[a][b]

    if s[a] == s[b] and pelin2(s, a + 1, b - 1):
        dp[a][b] = 1
    else:
        dp[a][b] = 0

    return dp[a][b]


def cutcutcut(s):
    n = len(s)
    dp = [1e9] * n

    for i in range(n):
        min_cut = i
    # 이거 거꾸로해도 똑같네
        for j in range(i, -1, -1):
            if pelin2(s, j, i):
                if j == 0:
                    min_cut = 0
                else:
                    min_cut = min(min_cut, dp[j - 1] + 1)

        dp[i] = min_cut
    return dp[-1]


s = input()
dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]

print(cutcutcut(s)+1)
