import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def dfs(start, arr, visit):
    stk = deque([start])
    visit.add(start)
    trail = 0
    while stk:
        curr = stk.pop()
        for next in arr[curr]:
            if next not in visit and a[next] == 0:
                stk.append(next)
            elif next not in visit and a[next] == 1:
                visit.add(next)
                trail += 1
                continue
    return trail


n = int(input())
a = [0]+[int(char) for char in input()]
route66 = [[] for i in range(n+1)]
trail = 0

for i in range(n-1):
    u, v = map(int, (input().split()))
    route66[v].append(u)
    route66[u].append(v)

for i in range(1, n+1):
    if a[i] == 1:
        visit = set([])
        trail += dfs(i, route66, visit)
print(trail)
