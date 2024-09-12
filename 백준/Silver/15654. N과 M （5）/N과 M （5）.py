import sys


def input():
    return sys.stdin.readline()


def dfs(path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(path + [nums[i]])
            visited[i] = False


n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

visited = [False] * n

dfs([])
