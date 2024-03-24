from collections import deque

import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10**6)


def dfs(start, arr, visited):
    visited.add(start)
    for next in arr[start]:
        if next not in visited:
            res.append(next)
            dfs(next, arr, visited)
    return visited


n, m = map(int, (input().split()))

nodelist = [[] for i in range(n+1)]
for i in range(m):
    ch, ng = map(int, (input().split()))
    nodelist[ch].append(ng)
    nodelist[ng].append(ch)

visit = set([])
res = []
cnt = 0

for i in range(1, n+1):
    if i not in visit:
        dfs(i, nodelist, visit)
        cnt += 1
print(cnt)
