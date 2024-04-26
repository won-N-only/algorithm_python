import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def dfs(x, y, arr):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    q = deque([(x, y)])
    arr[x][y] = 0
    
    dis = [[0]*m for i in range(n)]
    dis[x][y] = 1
    while q:
        x, y = q.popleft()

        if (x, y) == (n-1, m-1):
            return dis[x][y]

        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            if (0 <= px < n) and (0 <= py < m) and arr[px][py] == 1:
                q.append((px, py))
                arr[px][py] = 0

                # 도수분포표 활용함
                dis[px][py] = dis[x][y] + 1

    return dis[x][y]


n, m = map(int, input().split())

maze = [[]for i in range(n)]
for i in range(n):
    maze[i] = [int(i) for i in input()]

cnt = dfs(0, 0, maze)
print(cnt)
