from collections import deque

import sys


def input():
    return sys.stdin.readline().strip()


def topology():
    q = deque()
    for i in range(1, n+1):
        if ind[i] == 0:
            q.append(i)
    while q:
        curr = q.popleft()
        res.append(curr)
        for next in graph[curr]:
            ind[next] -= 1
            if ind[next] == 0:
                q.append(next)


n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
ind = [0]*(n+1)
res = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1
topology()
[print(r, end=" ") for r in res]
