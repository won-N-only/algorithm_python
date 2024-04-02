import heapq
import sys


def input():
    return sys.stdin.readline().strip()

# 컵라면, 데드라인 순


def ramen_heap(arr):
    cnt = 0
    baguni = []

    for dL, cup in arr:
   
        heapq.heappush(baguni, cup)
        cnt += cup

        if len(baguni) > dL:
            cnt -= heapq.heappop(baguni)

    return cnt



n = int(input())

ramen = []
for i in range(n):
    a, b = (map(int, input().split()))
    ramen.append([a, b])
ramen.sort()

ans1 = ramen_heap(ramen)
print(ans1)
