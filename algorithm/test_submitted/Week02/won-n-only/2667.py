from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def bfs(x, y, arr, visit):
    visit.add((x, y))
    q = deque([(x, y)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if (nx, ny) not in visit and (0 <= nx < n) and (0 <= ny < n) and arr[nx][ny] != 0:
                visit.add((nx, ny))
                q.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())

binary_map = [[] for _ in range(n)]
for i in range(n):
    binary_map[i] = list(map(int, input()))

ans = []
visit = set([()])
for i in range(n):
    for j in range(n):
        if (i, j)not in visit and binary_map[i][j] != 0:
            ans.append(bfs(i, j, binary_map, visit))
ans.sort()
print(len(ans))
[print(i)for i in ans]
from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def bfs(x, y, arr, visit):
    visit.add((x, y))
    q = deque([(x, y)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if (nx, ny) not in visit and (0 <= nx < n) and (0 <= ny < n) and arr[nx][ny] != 0:
                visit.add((nx, ny))
                q.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())

binary_map = [[] for _ in range(n)]
for i in range(n):
    binary_map[i] = list(map(int, input()))

ans = []
visit = set([()])
for i in range(n):
    for j in range(n):
        if (i, j)not in visit and binary_map[i][j] != 0:
            ans.append(bfs(i, j, binary_map, visit))
ans.sort()
print(len(ans))
[print(i)for i in ans]
from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def bfs(x, y, arr, visit):
    visit.add((x, y))
    q = deque([(x, y)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if (nx, ny) not in visit and (0 <= nx < n) and (0 <= ny < n) and arr[nx][ny] != 0:
                visit.add((nx, ny))
                q.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())

binary_map = [[] for _ in range(n)]
for i in range(n):
    binary_map[i] = list(map(int, input()))

ans = []
visit = set([()])
for i in range(n):
    for j in range(n):
        if (i, j)not in visit and binary_map[i][j] != 0:
            ans.append(bfs(i, j, binary_map, visit))
ans.sort()
print(len(ans))
[print(i)for i in ans]
