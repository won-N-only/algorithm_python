from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def bfs(x, y, arr):
    idx = 1
    q = deque([(x, y)])
    paint[x][y] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if paint[nx][ny] == 1:
                    q.append((nx, ny))
                    idx += paint[nx][ny]
                    paint[nx][ny] = 0

    return idx


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())

paint = [[[] for _ in range(m)] for _ in range(n)]

for i in range(n):
    paint[i] = (list(map(int, input().split())))
cnt = []
for i in range(n):
    for j in range(m):
        if paint[i][j] != 0:
            idx = bfs(i, j, paint)
            cnt.append(idx)

print(len(cnt))
print(max(cnt))if cnt else print(0)
