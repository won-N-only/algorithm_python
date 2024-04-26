import sys
import heapq


def input():
    return sys.stdin.readline().strip()


def navigating():

    n = len(cities)
    # [0]에 2e222 append한거랑 같은느김
    dis = [0]+[2e222]*(n-1)

    # 여러 대상에 대한 다익스트라도 ㅇㅋ
    for ter in interview:
        dis[ter] = 0
    q = [(0, nd) for nd in interview]
    heapq.heapify(q)

    while q:
        dist, curr = heapq.heappop(q)

        if dis[curr] < dist:
            continue

        for ndist, next in cities[curr]:
            if dis[next] > dist+ndist:
                dis[next] = dist+ndist
                heapq.heappush(q, (dis[next], next))
    return dis


n, m, k = map(int, input().split())
cities = [[] for _ in range(n+1)]

# 목적지에서 out하게
for i in range(m):
    x, y, w = map(int, input().split())
    cities[y].append((w, x))

interview = list(map(int, input().split()))

distances = navigating()

max_distance = max(distances)
max_city = distances.index(max_distance)
print(max_city, max_distance)
