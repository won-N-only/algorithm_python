import sys

from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(start, arr, visit):
    q = deque([start])
    visit.add(start)
    colour[start] = 1
    while q:
        curr = q.popleft()
        for next in arr[curr]:
            if colour[curr] == colour[next]:
                return 1
            if colour[curr] == 1:
                colour[next] = 2
            elif colour[curr] == 2:
                colour[next] = 1
            if next not in visit:
                visit.add(next)
                q.append(next)
    return 0


k = int(input())

for i in range(k):
    v, e = map(int, input().split())
    res=0
    # 정점수만큼 있어야하니까 정점기준
    graph = [[] for _ in range(v+1)]
    colour = [[0] for _ in range(v+1)]
    visit = set([])

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 연결안된 정점까지 방문
    for i in range(1, v+1):
        if i not in visit:
            res += bfs(i, graph, visit)
    if res  >0:
        print("NO")
    else:
        print("YES")
