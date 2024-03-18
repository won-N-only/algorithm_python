import sys


def input():
    return sys.stdin.readline().strip()
mlist = []
n = int(input())
for _ in range(n):
    mlist.append(int(input()))
mlist.sort()
for i in range(n):
    print(mlist[i])
