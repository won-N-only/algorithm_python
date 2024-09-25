import sys


def input():
    return sys.stdin.readline()


n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))
points.sort(key=lambda x: (x[1], x[0]))
print('\n'.join(' '.join(map(str, point)) for point in points))
