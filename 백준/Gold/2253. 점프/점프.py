import sys


def input():
    return sys.stdin.readline().strip()


def jump(n, trash):
    dp = [[88577] * (int((2*n)**(1/2))+2) for _ in range(n+1)]
    dp[1][0] = 0
    # c_s=현재돌 p_s=이전돌 p_j=이전점프
    for c_s in range(2, n+1):
        if c_s in trash:
            continue
        for p_j in range(1, int((2*c_s)**(1/2))+1):
            p_s = c_s-p_j
            dp[c_s][p_j] = min(dp[p_s][p_j-1], dp[p_s]
                               [p_j], dp[p_s][p_j+1]) + 1
    return dp[n]


n, k = map(int, input().split())

trash = set()
for _ in range(k):
    trash.add(int(input()))

ans = min(jump(n, trash))
if ans == 88577:
    print(-1)
else:
    print(ans)
