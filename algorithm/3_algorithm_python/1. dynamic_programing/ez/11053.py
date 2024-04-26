import sys
from bisect import bisect_left


def input():
    return sys.stdin.readline().strip()


def find(n):
    # 브루트포스말고 다른방법없나
    # bfs로.. 는 같겠는데
    arr = list(map(int, input().split()))
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)+1


def binary():

    arr = list(map(int, input().split()))
    dp = []

    for i in arr:
        if not dp or i > dp[-1]:
            dp.append(i)
        # bisect는 의미없는것같기도해
        else:
            idx = bisect_left(dp, i)
            dp[idx] = i

    return (len(dp))


n = int(input())
print(find(n))
print(binary())
