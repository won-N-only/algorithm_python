import sys
from collections import deque

input = sys.stdin.readline

def topology():
    q = deque()
    for i in range(1, n+1):
        if ind[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        res.append(curr)
        for node in graph[curr]:
            ind[node] -= 1
            if ind[node] == 0:
                q.append(node)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ind = [0]*(n+1)
res = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1
topology()
print(' '.join([str(i) for i in res]))
