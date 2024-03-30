import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def dfs(start, graph, a):
    stk = deque([start])
    visited = set([start])
    count = 0

    while stk:
        curr = stk.pop()
        for next in graph[curr]:
            if next not in visited:
                visited.add(next)  # 방문한 정점을 추가
                if a[next] == 1:  # 다음 정점이 실내인 경우
                    count += 1  # 경로를 카운트
                else:
                    stk.append(next)  # 실외 정점인 경우, 스택에 추가하여 탐색 계속
    return count


n = int(input())
a = [0] + [int(x) for x in input()]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

total_count = 0
for i in range(1, n+1):
    if a[i] == 1:  # 실내에서 시작하는 모든 경로 탐색
        total_count += dfs(i, graph, a)

print(total_count)
