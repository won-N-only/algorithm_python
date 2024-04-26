import sys


def input():
    return sys.stdin.readline().strip()


def bubun(arr, n):
    dp = [None]*n
    dp[0] = arr[0]
    # max_val = 0
    # for i in range(n):
    #     bubun = 1
    #     for j in range(i, n):
    #         bubun *= arr[j]
    #         max_val = max(max_val, bubun)
    # return max_val
    for i in range(1, n):
        dp[i] = max(arr[i], arr[i]*dp[i-1])
    return max(dp)


n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))
res = bubun(arr, n)
# 이거 round면 0이 짤림
print('%.3f' % (res))
