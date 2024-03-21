import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
sticks = [int(input()) for i in range(n)]
first = sticks[-1]
idx = 1
for i in range(n-1, -1, -1):
    if sticks[i]-first > 0:
        idx += 1
        first = sticks[i]
print(idx)
