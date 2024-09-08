import sys


def input():
    return sys.stdin.readline().strip()


n, r, c = map(int, input().split())

num = (r + c) % 2

for i in range(n):
    row = ""
    for j in range(n):
        if (i + j) % 2 == num:
            row += 'v'
        else:
            row += '.'
    print(row)
