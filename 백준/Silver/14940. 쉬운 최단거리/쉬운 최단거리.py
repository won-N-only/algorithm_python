import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def check_point(nx, ny):
    return 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1


def bfs(start, arr, v: set):
    q = deque([start])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if check_point(nx, ny) and (nx, ny) not in v:
                v.add((nx, ny))
                q.append((nx, ny))
                arr[ny][nx] = arr[y][x] + 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

start = ()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start = (j, i)
            arr[i][j] = 0
            break
    if start:
        break

v = set()
bfs(start, arr, v)

for i in range(n):
    for j in range(m):
        if (j, i) not in v and arr[i][j] == 1:
            arr[i][j] = -1

for row in arr:
    print(*row)
