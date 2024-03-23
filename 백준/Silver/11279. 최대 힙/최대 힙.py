import heapq
import sys


def input():
    return sys.stdin.readline().strip()


arr = []

n = int(input())
for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(arr, -x)
    elif len(arr)>0:
        print(-1*heapq.heappop(arr))
    else:print(0)