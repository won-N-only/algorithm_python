import sys
from collections import deque


def input():
    return sys.stdin.readline().split()


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


m, n = map(int, input())
arr = [list(map(int, input())) for _ in range(n)]

q = deque([(i, j) for i in range(n) for j in range(m) if arr[i][j] == 1])

bfs()

res = 0
for row in arr:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
    res = max(res, max(row))

print(res - 1)
