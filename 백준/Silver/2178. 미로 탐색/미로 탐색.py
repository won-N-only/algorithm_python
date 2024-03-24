import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def dfs(x, y, arr, visit):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    q = deque([(x, y)])
    arr[x][y] = 0
    visit.add((x, y))
    dis = [[0]*m for i in range(n)]
    dis[x][y] = 1
    while q:
        x, y = q.popleft()
        if (x, y) == (n-1, m-1):
            return dis[x][y]
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            if (0 <= px < n) and (0 <= py < m) and arr[px][py] == 1 and (px, py)not in visit:
                visit.add((px, py))
                q.append((px, py))
                dis[px][py] = dis[x][y] + 1
                # if (px, py) == (n, m):
                #     return dis[px][py]
    return dis[x][y]


n, m = map(int, input().split())

visit = set([])
maze = [[]for i in range(n)]
for i in range(n):
    maze[i] = [int(i) for i in input()]
end = (n, m)
cnt = dfs(0, 0, maze, visit)
print(cnt)
