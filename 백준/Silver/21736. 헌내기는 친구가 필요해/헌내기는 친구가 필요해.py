import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(start_y, start_x):
    q = deque([(start_y, start_x)])
    visited = set([(start_y, start_x)])  
    cnt = 0  
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        cy, cx = q.popleft()

        if arr[cy][cx] == 'P':
            cnt += 1


        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visited and arr[ny][nx] != 'X':
                visited.add((ny, nx))
                q.append((ny, nx))

    return cnt

n, m = map(int, input().split())
arr = [input() for _ in range(n)]


start = None
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':  
            start = (i, j)
            break
    if start:
        break

result = bfs(*start)

if result > 0:
    print(result)  
else:
    print("TT")  
