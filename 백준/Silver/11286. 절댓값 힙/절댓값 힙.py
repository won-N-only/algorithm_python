import heapq
import sys
def input():
    return sys.stdin.readline().strip()
arr = []
heapq.heapify(arr)
n = int(input())
for i in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(arr, (abs(a), a//abs(a)))
    else:
        if len(arr) != 0:
            z = heapq.heappop(arr)
            print(z[0]*z[1])
        else:
            print(0)
