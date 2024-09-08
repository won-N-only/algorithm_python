import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append([x, y])
points.sort(key=lambda p: (p[0], p[1]))
for i in range(n):
    print(*points[i])
