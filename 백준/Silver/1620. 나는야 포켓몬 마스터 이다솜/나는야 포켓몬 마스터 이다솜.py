import sys


def input():
    return sys.stdin.readline().strip()


n, m = map(int, input().split())

name_map = {}
index_map = {}
for i in range(1, n+1):
    name = input()
    name_map[i] = name
    index_map[name] = i

for _ in range(m):
    x = input()
    if x.isdigit():
        print(name_map[int(x)])
    else:
        print(index_map[x])
