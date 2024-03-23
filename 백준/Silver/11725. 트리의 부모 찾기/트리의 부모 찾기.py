from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


ans = [0]*(N+1)

q = deque([(1)])


def dfs(arr):
    while q:
        curr = q.popleft()
        for next in arr[curr]:
            if ans[next] == 0:
                ans[next] = curr
                q.append(next)
    return ans


ans = dfs(graph)

ans = ans[2:]
for i in range(len(ans)):
    print(ans[i])
