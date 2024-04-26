from collections import deque

import sys


def input():
    return sys.stdin.readline().strip()


def dfs(start, arr, visited):
    visited.add(start)
    for next in arr[start]:
        if next not in visited:
            dfs(next, arr, visited)
    return visited


def bfs(start, arr, vis):
    q = deque([(start)])
    vis.add(start)
    while q:
        curr = q.popleft()
        for next in arr[curr]:
            if next not in vis:
                vis.add(next)
                q.append(next)
    return vis
# 이거좀 신기하네? dfs bfs차이가 pop, popleft 에서나오네
def dfs(start, graph):
    visited = set([start])  
    stack = deque([start]) 
    while stack:  
        current = stack.pop()  
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)   
                visited.add(neighbor)



n, m = map(int, (input().split()))

nodelist = [[] for i in range(n+1)]
for i in range(m):
    ch, ng = map(int, (input().split()))
    # 서로 위치바꿔넣어서 서로의 idx에 서로가 존재하게함
    nodelist[ch].append(ng)
    nodelist[ng].append(ch)

cnt = 0
visit = set([])

# dfs풀이
# for i in range(1, n+1):
#     if i not in visit:
#         dfs(i, nodelist, visit)
#         cnt += 1

# bfs풀이
# for i in range(1, n+1):
#     if i not in visit:
#         bfs(i, nodelist, visit)
#         cnt += 1

print(cnt)

