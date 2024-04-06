# 소트마스터 배지훈의 후계자
# https://www.acmicpc.net/problem/20551
#inssg과같이품 
import sys


def input():
    return sys.stdin.readline().strip()

def ans():
    n, m = map(int, input().strip().split())
    data = [int(input().strip()) for _ in range(n)]
    data.sort()
    for a in range(m):
        q = int(input())
        left = 0
        right = len(data)-1
        while True:
            mid = (left + right) // 2
            if data[mid] == q:
                if mid == right:
                    print(mid)
                    break
                else:
                    right = mid
            elif data[mid] < q:
                left = mid + 1
            elif data[mid] > q:
                right = mid - 1
            if left > right:
                print(-1)
                break

ans()