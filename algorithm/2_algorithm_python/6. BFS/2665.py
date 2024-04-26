import heapq
from collections import deque

# 가중치가 있는걸 heap에 넣으니까 최소가중치를 가진것만 나오고
# 따로 갱신안해주고 black일때만 +=1해줘도 답나옴


def chk(x, y):
    return (0 <= x < n) and (0 <= y < n)


# 다익스트라 싫다
def dijkstra(x, y):
    q = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visit = [[-1]*n for i in range(n)]

    heapq.heappush(q, (0, x, y))
    visit[x][y] = 1

    while q:
        w, cx, cy = heapq.heappop(q)
        if cx == n-1 and cy == n-1:
            return w

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if chk(nx, ny) and visit[nx][ny] == -1:
                visit[nx][ny] = 1

                if maze[nx][ny] == 1:
                    heapq.heappush(q, (w, nx, ny))
                else:
                    heapq.heappush(q, (w+1, nx, ny))


# heap안써도 될거같은데? 이러면 모양이 기본하고 같아서 나중에 생각하기 편할듯
def no_heap(w, x, y, arr):
    q = deque([(w, x, y)])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visit = set([(w, x, y)])

    while q:
        w, cx, cy = q.popleft()

        if cx == n-1 and cy == n-1:
            return w
        
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]

            if (nx, ny) not in visit and chk(nx, ny):
                if arr[nx][ny] == 1:
                    visit.add((nx, ny))
                    q.appendleft((w, nx, ny))
                else:
                    visit.add((nx, ny))
                    q.append((w+1, nx, ny))


n = int(input())

maze = [list(map(int, input())) for _ in range(n)]
print(dijkstra(0, 0))
print(no_heap(0, 0, 0, maze))
