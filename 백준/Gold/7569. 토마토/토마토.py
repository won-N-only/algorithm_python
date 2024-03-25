from collections import deque

# 입력 받기
M, N, H = map(int, input().split())
tomatoes = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(H)]

# BFS 준비
queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                queue.append((h, n, m, 0))  # (z, y, x, days)

# 방향 벡터
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

# BFS 실행
max_days = 0
while queue:
    z, y, x, days = queue.popleft()
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomatoes[nz][ny][nx] == 0:
            tomatoes[nz][ny][nx] = 1
            max_days = max(max_days, days + 1)
            queue.append((nz, ny, nx, days + 1))

# 모든 토마토가 익었는지 확인
for h in tomatoes:
    for n in h:
        if 0 in n:
            print(-1)
            exit(0)

print(max_days)
