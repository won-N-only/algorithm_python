def dfs(start, graph, visited, indoor):
    if visited[start]:  # 이미 방문한 노드는 탐색하지 않음
        return 0
    visited[start] = True
    count = 0
    for next in graph[start]:
        if not visited[next]:
            if indoor[next]:  # 다음 노드가 실내인 경우
                count += 1  # 실내 장소에 도달한 경로를 카운트
            else:
                count += dfs(next, graph, visited, indoor)
    visited[start] = False  # 다른 경로 탐색을 위해 방문 상태를 초기화
    return count

n = int(input())
a = [0] + [int(x) for x in input()]  # 실내/실외 정보
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

total_count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if a[i] == 1:  # 실내에서 시작하는 모든 경로 탐색
        total_count += dfs(i, graph, visited, a)

print(total_count)
