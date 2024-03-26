# 고슴도치 움직임은 bfs로하고 물의움직임만 for문돌려서 상하좌우로 퍼지게하면 되지않나?
# if 고슴도치 next == "*" 면 exit(0)하고 print kaktus하고
# next=d면 ㅇㅋㅇㅋ하고 ?
# 돌있으면 못가는건 어떻게하지 if == 돌이면 안가게
# 물먼저생기게하고 물 돌 있으면 안가게하면될듯?
# 비버 위치 찾아서 start에 넣고 일단 돌리면 ㄱㄱ

from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def chk_curr(a, b, arr):
    if 0 <= b < c and 0 <= a < r:
        if arr[a][b] != "*" and arr[a][b] != "X":
            return True

    return False


def chk_map():
    global echidna_x, echidna_y, beaver_x, beaver_y, water
    for i, row in enumerate(twforest):
        for j, x in enumerate(row):
            if x == "S":
                echidna_x = j
                echidna_y = i
                break

    for i, row in enumerate(twforest):
        for j, x in enumerate(row):
            if x == "D":
                beaver_x = j
                beaver_y = i
                break

    water = []
    for i, row in enumerate(twforest):
        for j, x in enumerate(row):
            if x == "*":
                water.append((j, i))
                continue


def bfs(day, x, y, arr):

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visit = set([(x, y)])
    q = deque([(day, x, y)])

    wq = deque([])
    for i in range(len(water)):
        wq.append((water[i][0], water[i][1]))

    while q:

        for i in range(len(wq)):
            cwx, cwy = wq.popleft()

            for i in range(4):
                nwx = cwx+dx[i]
                nwy = cwy+dy[i]
                if chk_curr(nwy, nwx, arr):
                    if arr[nwy][nwx] != "D":
                        arr[nwy][nwx] = "*"
                        wq.append((nwx, nwy))
        for _ in range(len(q)):

            cday, cx, cy = q.popleft()

            if (cx, cy) == (beaver_x, beaver_y):
                return cday

            for i in range(4):
                nx = cx+dx[i]
                ny = cy+dy[i]
                if (nx, ny) not in visit:
                    if chk_curr(ny, nx, arr):
                        q.append((cday+1, nx, ny))
                        visit.add((nx, ny))


r, c = map(int, input().split())
twforest = [list(input()) for _ in range(r)]

chk_map()
res = bfs(0, echidna_x, echidna_y, twforest)
if res:
    print(res)
else:
    print("KAKTUS")
