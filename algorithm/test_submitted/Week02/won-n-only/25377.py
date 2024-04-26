import heapq
import sys

def input():
    return sys.stdin.readline().strip()

def bread(arr):
    if len(arr) > 0:
        curr = heapq.heappop(arr)
        print(curr)
    else:
        print(-1)


n = int(input())
graph = []
for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        heapq.heappush(graph, b)

bread(graph)
import heapq
import sys

def input():
    return sys.stdin.readline().strip()

def bread(arr):
    if len(arr) > 0:
        curr = heapq.heappop(arr)
        print(curr)
    else:
        print(-1)


n = int(input())
graph = []
for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        heapq.heappush(graph, b)

bread(graph)
import heapq
import sys

def input():
    return sys.stdin.readline().strip()

def bread(arr):
    if len(arr) > 0:
        curr = heapq.heappop(arr)
        print(curr)
    else:
        print(-1)


n = int(input())
graph = []
for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        heapq.heappush(graph, b)

bread(graph)
