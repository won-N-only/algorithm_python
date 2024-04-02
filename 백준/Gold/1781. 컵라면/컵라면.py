import heapq
import sys


def input():
    return sys.stdin.readline().strip()

# 컵라면, 데드라인 순


def ramen_heap(arr):
    cnt = 0
    r_cnt = 0
    baguni = []
    heapq.heapify(baguni)
    for i in range(n):
        if len(baguni) < arr[i][0]:
            heapq.heappush(baguni, [arr[i][1], arr[i][0]])
            r_cnt += arr[i][1]
        else:
            if baguni[0][0] < arr[i][1]:
                trash = heapq.heappop(baguni)
                heapq.heappush(baguni, [arr[i][1], arr[i][0]])
                r_cnt += (arr[i][1]-trash[0])
    return r_cnt


n = int(input())

ramen = []
for i in range(n):
    a, b = (map(int, input().split()))
    ramen.append([a,b])
ramen.sort()
ans1 = ramen_heap(ramen)
print(ans1)
