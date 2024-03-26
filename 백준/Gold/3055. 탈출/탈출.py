from collections import deque


def bfs(twforest, r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    water, visit, q = deque(), set(), deque()
    for i in range(r):
        for j in range(c):
            if twforest[i][j] == 'S':
                start = (i, j)
                twforest[i][j] = '.'  # 시작 위치를 빈 칸으로 변경
            elif twforest[i][j] == 'D':
                end = (i, j)
            elif twforest[i][j] == '*':
                water.append((i, j))
                visit.add((i, j))

    q.append((start, 0))  # 시작 위치와 시간 초기화

    while q:
        # 먼저 물 확장
        for _ in range(len(water)):
            wx, wy = water.popleft()
            for dx, dy in directions:
                nx, ny = wx + dx, wy + dy
                if 0 <= nx < r and 0 <= ny < c and twforest[nx][ny] == '.':
                    twforest[nx][ny] = '*'
                    water.append((nx, ny))

        # 고슴도치 이동
        for _ in range(len(q)):
            (x, y), time = q.popleft()
            if (x, y) == end:
                return time
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visit:
                    if twforest[nx][ny] == '.' or twforest[nx][ny] == 'D':
                        q.append(((nx, ny), time + 1))
                        visit.add((nx, ny))

    return "KAKTUS"


r, c = map(int, input().split())
twforest = [list(input()) for _ in range(r)]

res = bfs(twforest, r, c)
print(res)
