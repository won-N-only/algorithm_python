from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
array = [] #input 배열
for _ in range(n):
    array.append(list(map(int, input().split())))
    
result = [[0] * m for _ in range(n)] 

row = min(n, m) // 2
start = deque([(i, i) for i in range(row)])

indices = [] 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while start:
    temp = []
    x, y = start.popleft()

    for i in range(4):
        if i % 2 == 0:
            for j in range(n-1):
                temp.append((x, y))
                x += dx[i]
                y += dy[i]
        else:
            for j in range(m-1):
                temp.append((x, y))
                x += dx[i]
                y += dy[i]

    indices.append(temp)
    n -= 2
    m -= 2

for i in range(len(indices)):
    length = len(indices[i])
    for j in range(length):
        x, y = indices[i][j]
        nx, ny = indices[i][(j+r) % length]
        result[nx][ny] = array[x][y]

for r in result:
    print(*r)
