from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def bfs(start, arr):
    q = deque([(start)])
    visit = set([(start)])
    while q:
        curr = q.popleft()
        bfs_ans.append(curr)
        for next in arr[curr]:
            if next not in visit:
                visit.add(next)
                q.append(next)
    return -1


def dfs(start, arr, visite):
    visite.append(start)
    for next in arr[start]:
        if next not in visite:
            dfs(next, arr, visite)
    return visite


n, m, v = map(int, input().split())

edges = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for edge in edges:
    edge.sort()
bfs_ans = []
dfs_ans = []

dfs(v, edges, dfs_ans)
bfs(v, edges)

print(*dfs_ans)
print(*bfs_ans)
