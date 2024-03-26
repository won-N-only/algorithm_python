from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def topology():
    q = deque()
    for i in range(1, n+1):
        if ind[i] == 0:
            q.append(i)
            ans[i][i] = 1
    while q:
        curr = q.popleft()
        for next, quantity in parts[curr]:
            for i in range(1, n+1):
                ans[next][i] += ans[curr][i]*quantity
            ind[next] -= 1
            if ind[next] == 0:
                q.append(next)


n = int(input())
m = int(input())
parts = [[]for i in range(n+1)]
ind = [0]*(n+1)
ans = [[0]*(n+1) for _ in range(n+1)]


for i in range(m):
    x, y, k = map(int, input().split())
    parts[y].append([x, k])
    ind[x] += 1


topology()
for i in range(1, n):
    if ans[n][i] > 0:
        print(i, ans[n][i])
