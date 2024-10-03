R, C, K = map(int, input().split())
grid = [input().strip() for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
target = (0, C - 1)
start = (R - 1, 0)
visited = [[False] * C for _ in range(R)]

count = 0

def dfs(x, y, dist):
    global count
    if (x, y) == target:
        if dist == K:
            count += 1
        return
    
    visited[x][y] = True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == '.':
            dfs(nx, ny, dist + 1)
    
    visited[x][y] = False

dfs(start[0], start[1], 1)

print(count)
