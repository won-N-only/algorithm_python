import sys


def input():
    return sys.stdin.read()


data = input().splitlines()

N, M = map(int, data[0].split())
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for i in range(1, M + 1):
    a, b = map(int, data[i].split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_bacon = float('inf')
min_user = -1

for i in range(1, N + 1):
    bacon_sum = sum(graph[i][1:])
    if bacon_sum < min_bacon:
        min_bacon = bacon_sum
        min_user = i
    elif bacon_sum == min_bacon and i < min_user:
        min_user = i

print(min_user)
