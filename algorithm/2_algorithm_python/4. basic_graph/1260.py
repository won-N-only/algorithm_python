from collections import deque
import sys


# 테스트케이스
"""
5 5 3
5 4
5 2
1 2
3 4
3 1
"""


def input():
    return sys.stdin.readline().strip()


def dfs(start, arr, visite):
    # visit 하고시작(올라올때 방문하는거 방지용)
    visite.append(start)
    for next in arr[start]:
        if next not in visite:
            dfs(next, arr, visite)
    return visite


def bfs(start, arr):
    q = deque([(start)])
    visit = set([(start)])
    while q:
        curr = q.popleft()
        bfs_ans.append(curr)
        for next in arr[curr]:
            if next not in visit:
                visit.add(next)
                q.append(next)
    return -1


n, m, v = map(int, input().split())

# 간선간 연결할때 이거 중요
# 1~n까지 a,b idx에 서로넣어줘서 트리표현함
edges = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for edge in edges:
    edge.sort()

bfs_ans = []
dfs_ans = []

dfs(v, edges, dfs_ans)
bfs(v, edges)

print(*dfs_ans)
print(*bfs_ans)
