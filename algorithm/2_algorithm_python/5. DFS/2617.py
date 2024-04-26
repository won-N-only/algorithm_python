from collections import deque


def dfs(start, arr, find):
    visit = set([(start)])
    q = deque([(start)])
    while q:
        curr = q.pop()
        for next in arr[curr]:
            if next not in visit:
                visit.add(next)
                q.append(next)
                find[start] += 1
    return find[start]


n, m = map(int, input().split())

heavy_list = [[]for i in range(n+1)]
find_heavy = [0]*(n+1)
light_list = [[]for i in range(n+1)]
find_light = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    heavy_list[a].append(b)
    light_list[b].append(a)

for i in range(1, n+1):
    dfs(i, light_list, find_light)
    dfs(i, heavy_list, find_heavy)

print(find_heavy, find_light)
ans = 0
for i in range(1, n+1):
    if find_light[i] > n//2:
        ans += 1
    if find_heavy[i] > n//2:
        ans += 1

print(ans)
