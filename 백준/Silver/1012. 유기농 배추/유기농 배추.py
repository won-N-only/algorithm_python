import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(start, arr, v, w, h):
    q = deque([start])
    v.add(start)

    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and arr[ny][nx] == 1 and (nx, ny) not in v:
                v.add((nx, ny))
                q.append((nx, ny))


T = int(input())
for _ in range(T):
    w, h, k = map(int, input().split())

    arr = [[0]*w for _ in range(h)]
    v = set()

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    count = 0

    for i in range(w):
        for j in range(h):
            if arr[j][i] == 1 and (i, j) not in v:
                bfs((i, j), arr, v, w, h)
                count += 1

    print(count)
