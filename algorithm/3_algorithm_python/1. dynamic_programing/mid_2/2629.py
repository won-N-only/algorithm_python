# def pendulum(weights, beads):
#     for weight in weights:
#         추 무게 다 더한 표 만들고
#         목록에서 구슬무게뺀거가 in arr면 yes임
import sys


def input():
    return sys.stdin.readline().strip()


def find_weights(arr):
    max_weight = sum(arr)
    dp = [0] * (max_weight + 1)
    dp[0] = 1

    for weight in arr:
        for w in range(max_weight - weight, -1, -1):
            if dp[w]:
                dp[w + weight] = 1

    ans = [i for i, w in enumerate(dp) if w]

    return ans


def lingard(arr):
    for i in range(len(beads)):
        found = 0
        for j in range(len(arr)):
            if -beads[i] + arr[j] in arr:
                print("Y")
                found = 1
                break

        if not found:
            print("N")
    return


n = int(input())
weights = list(map(int, input().split()))

n = int(input())
beads = list(map(int, input().split()))

res = (find_weights(weights))
lingard(res)
