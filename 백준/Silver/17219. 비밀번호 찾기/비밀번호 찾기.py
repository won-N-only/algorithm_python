import sys


def input():
    return sys.stdin.readline().strip()


n, m = map(int, input().split())
arr = {}
for i in range(n):
    site, pw = input().split()
    arr[site] = pw
for i in range(m):
    print(arr[input()])
