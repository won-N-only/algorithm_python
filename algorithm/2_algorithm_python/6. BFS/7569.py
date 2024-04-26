from collections import deque


m, n, h = map(int, input().split())
tomatoes = [[[int(x) for x in input().split()]
             for _ in range(n)] for _ in range(h)]

q = deque()
for hh in range(h):
    for nn in range(n):
        for mm in range(m):
            if tomatoes[hh][nn][mm] == 1:
                # h,n,m = z,y,x 임. . . .. .
                q.append((hh, nn, mm, 0))

dz, dx, dy = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

max_days = 0
while q:
    z, y, x, days = q.popleft()
    for i in range(6):
        cz, cx, cy = z+dz[i], x+dx[i], y+dy[i]
        if 0 <= cz < h and 0 <= cx < m and 0 <= cy < n and tomatoes[cz][cy][cx] == 0:
            tomatoes[cz][cy][cx] = 1
            max_days = max(max_days, days+1)
            q.append((cz, cy, cx, days+1))

for h2 in tomatoes:
    for n2 in h2:
        if 0 in n2:
            print(-1)
            exit(0)

print(max_days)
