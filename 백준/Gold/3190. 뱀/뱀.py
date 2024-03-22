# snake_x[1,0,0,0,0,0]
# snake_y로 나누고[1,0,0,0,0,0,0]
# 움직일때마다 append0, popleft하고
# 한번 움직일때마다 칸에 apple있나 검증
# is_apple만들어서 x는i, y는j에


import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
for i in range(k):
    app, le = map(int, input().split())
    #사과위치 -1안해줘서 idx error뜸
    board[app-1][le-1] = 1

turn = []
l = int(input())
for i in range(l):
    sec, direction = input().split()
    turn.append([int(sec), direction])

# dxdy이동법 익숙해지기
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 current x,y(head)정해주고 시간이랑 idx해줌
dir, curr_x, curr_y = 0, 0, 0
time, turn_idx = 0, 0
snake = deque()
snake.append([curr_x, curr_y])

while True:
    curr_x  += dx[dir]
    curr_y += dy[dir]
    time += 1
    # 판 나가거나 snake밟으면 컷
    if curr_y < 0 or curr_x < 0 or curr_x >= n or curr_y >= n or [curr_x, curr_y] in snake:
        break

    # 머리부터가고 꼬리나가고 사과먹고 피자먹고
    snake.append([curr_x, curr_y])
    if board[curr_x][curr_y] == 0:
        snake.popleft()
    else:
        board[curr_x][curr_y] = 0

    # 시간되면 dir바꾸고
    if turn_idx < len(turn) and time == turn[turn_idx][0]:
        if turn[turn_idx][1] == 'L':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        # idx+=1해서 idx error나는거방지
        turn_idx += 1

print(time)
