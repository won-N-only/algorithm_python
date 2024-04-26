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
            # 이부분 못고치나? 1,2대신 1,-1쓰면 curr, -curr로 쓸수도있을거같네
            # 하노이처럼 3-curr해도 될듯?
            colour[next] = (colour[curr]) % 2+1
            if next not in visit:
                visit.add(next)
                q.append(next)
    return 0


k = int(input())

for i in range(k):
    v, e = map(int, input().split())
    res = 0
    # 정점수만큼 있어야하니까 정점기준
    graph = [[] for _ in range(v+1)]
    colour = [0] * (v+1)  # 원래 [0 for _ in range(v+1)] 였음
    visit = set([])

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 연결안된 정점까지 방문
    # 간소화 못하나? i부터 다 확인하니까 가성비안좋은데
    # visit을 (unvisit)으로쓰면 될거같기도
    # 0~v중에 방문한놈만빼고 not in 대신 in으로쓰면
    # 안간곳 확인 빠를듯
    # 방문때마다 list에서 remove해야하는데 O(n)은어케되지?
    for i in range(1, v+1):
        if i not in visit and res == 0:
            res += bfs(i, graph, visit)
    if res > 0:
        print("NO")
    else:
        print("YES")
