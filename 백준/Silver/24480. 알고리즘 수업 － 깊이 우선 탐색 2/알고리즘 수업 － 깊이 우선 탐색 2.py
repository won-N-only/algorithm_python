import sys

sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().strip()


def dfs(v):
    global cnt

    visit[v] = 1
    ans[v] = cnt

    arr[v].sort(reverse=True)

    for i in arr[v]:
        if (visit[i] == -1):
            cnt += 1
            dfs(i)


n, m, r = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n + 1)]
visit = [-1] * (n + 1)
ans = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

dfs(r)

for val in ans[1:]:
    print(val)
