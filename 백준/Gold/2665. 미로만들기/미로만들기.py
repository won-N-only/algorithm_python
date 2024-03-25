import heapq


def dijkstra(maze):
    n = len(maze)
    change = [[float('inf')] * n for _ in range(n)]
    change[0][0] = 0
    q = [(0, 0, 0)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        cnt, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_cnt = cnt + 1 if maze[nx][ny] == 0 else cnt
                if next_cnt < change[nx][ny]:
                    change[nx][ny] = next_cnt
                    heapq.heappush(q, (next_cnt, nx, ny))
    return change[n-1][n-1]


n = int(input())
maze = [list(map(int, input())) for _ in range(n)]
print(dijkstra(maze))
