import heapq
import sys


def input():
    return sys.stdin.readline().strip()

# 컵라면, 데드라인 순


def ramen_heap(arr):
    cnt = 0
    baguni = []
    heapq.heapify(baguni)


    for i in range(n):
        dL=arr[i][0]
        cup=arr[i][1]
        if len(baguni) < dL:
            heapq.heappush(baguni, [cup, dL])
            cnt += cup

        elif baguni[0][0] < cup:
                trash = heapq.heappop(baguni)
                heapq.heappush(baguni, [cup, dL])
                cnt += (cup-trash[0])
    return cnt


n = int(input())

ramen = []
for i in range(n):
    a, b = (map(int, input().split()))
    ramen.append([a, b])
ramen.sort()

ans1 = ramen_heap(ramen)
print(ans1)
