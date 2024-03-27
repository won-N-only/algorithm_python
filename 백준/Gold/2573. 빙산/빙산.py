from collections import deque
import sys
def input():
    return sys.stdin.readline().strip()

def melt_iceberg(arr, n, m):
    new_arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                water_count = 0
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                        water_count += 1
                new_arr[i][j] = max(arr[i][j] - water_count, 0)
    return new_arr


def count_components(arr):
    visited = set()
    components = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and arr[i][j] != 0:
                bfs(i, j, arr, visited)
                components += 1
    return components


def bfs(x, y, arr, visited):
    q = deque([(x, y)])
    visited.add((x, y))
    while q:
        cx, cy = q.pop()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and arr[nx][ny] != 0:
                visited.add((nx, ny))
                q.append((nx, ny))


n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

year = 0
while True:
    comp = count_components(iceberg)
    if comp >= 2:
        print(year)
        break
    elif comp == 0:
        print(0)
        break
    iceberg = melt_iceberg(iceberg, n, m)
    year += 1
