import sys


def input():
    return sys.stdin.readline().strip()

    # 브루트포스말고 다른방법없나
    # bfs로.. 는 같겠는데


def find(n):
    arr = list(map(int, input().split()))
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)+1


n = int(input())
print(find(n))
