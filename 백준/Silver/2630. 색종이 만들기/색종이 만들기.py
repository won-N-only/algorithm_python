import sys


def input():
    return sys.stdin.readline()


def divied(x, y, n):
    global bidx, widx
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                divied(x, y, n//2)
                divied(x+n//2, y, n//2)
                divied(x, y+n//2, n//2)
                divied(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        widx += 1
    else:
        bidx += 1


bidx, widx = 0, 0
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
divied(0, 0, n)
print(widx)
print(bidx)
