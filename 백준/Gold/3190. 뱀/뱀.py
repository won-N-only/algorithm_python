import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
for i in range(k):
    app, le = map(int, input().split())
    board[app-1][le-1] = 1

turn = []
l = int(input())
for i in range(l):
    sec, direction = input().split()
    turn.append([int(sec), direction])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir, curr_x, curr_y = 0, 0, 0
time, turn_idx = 0, 0
snake = deque()
snake.append([curr_x, curr_y])

while True:
    curr_x += dx[dir]
    curr_y += dy[dir]
    time += 1
    if curr_y < 0 or curr_x < 0 or curr_x >= n or curr_y >= n or [curr_x, curr_y] in snake:
        break

    snake.append([curr_x, curr_y])
    if board[curr_x][curr_y] == 0:
        snake.popleft()
    else:
        board[curr_x][curr_y] = 0

    if turn_idx < len(turn) and time == turn[turn_idx][0]:
        if turn[turn_idx][1] == 'L':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        turn_idx += 1

print(time)
