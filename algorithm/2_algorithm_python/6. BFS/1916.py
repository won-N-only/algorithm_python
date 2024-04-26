import heapq
import sys


def input():
    return sys.stdin.readline().strip()


def dijkstra(s, e, arr):
    # 거리기준만들고
    dis = [10**9] * (n+1)
    dis[s] = 0
    q = []
    heapq.heappush(q, (s, 0))

    while q:
        curr_posi, curr_dis = heapq.heappop(q)
        # 어차피 가까우면 pass
        if dis[curr_posi] < curr_dis:
            continue
        # 멀면 갱신
        for next, w in arr[curr_posi]:
            di = curr_dis+w
            if di < dis[next]:
                dis[next] = di
                heapq.heappush(q, (next, di))
    # 조건 몇개뺴곤 bfs랑 같음
    return dis[e]


n = int(input())
m = int(input())

buses = [[]for _ in range(n+1)]
for i in range(m):
    s, e, c = map(int, input().split())
    buses[s].append((e, c))

go, end = map(int, input().split())
cost = dijkstra(go, end, buses)
print(cost)
