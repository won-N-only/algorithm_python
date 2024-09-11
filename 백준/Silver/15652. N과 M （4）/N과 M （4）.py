import sys


def input():
    return sys.stdin.readline()


def dfs(start, visited: list):
    if len(visited) == m:
        print(' '.join(map(str, visited)))
        return

    for i in range(start, n+1):
        dfs(i, visited+[i])


n, m = map(int, input().split())
dfs(1, [])
