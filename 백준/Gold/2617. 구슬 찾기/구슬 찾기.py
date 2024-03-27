from collections import deque

def dfs(start, graph):
    visit = set([start])
    q = deque([start])
    count = 0
    while q:
        curr = q.pop()
        for next in graph[curr]:
            if next not in visit:
                visit.add(next)
                q.append(next)
                count += 1
    return count

n, m = map(int, input().split())
heavy_list = [[] for _ in range(n+1)]
light_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    heavy_list[a].append(b)
    light_list[b].append(a)

ans = 0
for i in range(1, n+1):
    if dfs(i, light_list) > n//2 or dfs(i, heavy_list) > n//2:
        ans += 1

print(ans)
