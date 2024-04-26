from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def bfs(start, arr, visit):
    q = deque([start])
    visit.add(start)

    # 아래 대신 dis = [-1] * (n+1)쓰면 더빠를듯 -1이라 디버깅도 편함
    # [0]+[-1]*n 하면되겠네  dis[start]만 0이면되니까 
    dis = [[] for i in range(n+1)]
    dis[start] = 0

    while q:
        curr = q.popleft()
        for next in arr[curr]:
            if next not in visit:
                visit.add(next)
                q.append(next)

                dis[next] = dis[curr]+1

    return dis


n, m, k, x = map(int, input().split())
cities = [[] for i in range(n+1)]
visit = set([])

for i in range(m):
    a, b = map(int, input().split())
    cities[a].append(b)

plz_use_taxi = bfs(x, cities, visit)
ans = []

for i in range(1, n+1):
    if plz_use_taxi[i] == k:
        ans.append(i)

if ans:
    [print(answer) for answer in ans]
else:
    print(-1)

"""
결과 출력할때 ans = [i for i in range(1, n+1) if plz_use_taxi[i] == k]로 한줄가능

if ans:
    print("\n".join(map(str, ans)))
else:
    print(-1)
    """
