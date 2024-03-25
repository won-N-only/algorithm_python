import heapq
import sys

def input():
    return sys.stdin.readline().strip()

def dijkstra(start, end, buses):
    distances = [10**9] * (n + 1)
    distances[start] = 0  
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in buses[current_node]:
            distance = current_distance + weight 
            if distance < distances[adjacent]:
                distances[adjacent] = distance  
                heapq.heappush(queue, (distance, adjacent))

    return distances[end]  


n = int(input())  # 정점의 개수
m = int(input())  # 간선의 개수

buses = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())  # 시작 정점, 끝 정점, 비용
    buses[s].append((e, c))

go, end = map(int, input().split())  # 출발지, 목적지
cost = dijkstra(go, end, buses)
print(cost)
