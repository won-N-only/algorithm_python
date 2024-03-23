import sys
import heapq


n = int(sys.stdin.readline().strip())
locations = []  # ([(시작 좌표, 끝 좌표) ...]
for _ in range(n):
    h, o = map(int, sys.stdin.readline().strip().split())
    # 집과 사무실 중 좌표값이 낮은 것을 앞에, 좌표값이 높은 것을 뒤에 넣어줌
    locations.append((min(h, o), max(h, o)))
d = int(sys.stdin.readline().strip())

# 선분의 끝점을 기준으로 오름차순 정렬한 다음, 앞점을 기준으로 오름차순 정렬
locations.sort(key=lambda x: (x[1], x[0]))

heap = []
max_cnt = 0
# 사람마다 다 도는건 맞는데 철로를 끝좌표랑 일치시켜서 안에들어가는지
# 한번 push한거 계속 들고가면서 시작점이랑 비교하기
# heap을 1회용이아니고 계속 쓰는거라고생각함
for location in locations:  # 각 사람의 좌표를 기준으로 반복문 돌기
    start, end = location
    heapq.heappush(heap, start)  # 최소 힙. pop했을 때 start가 작은 것부터 나올 수 있도록
    # 여기서 저장된 heap은 pop전까지(line의 시작점 벗어나기전까지) 안사라짐
    line_start = end - d  # 현재 사람의 끝 좌표를 기준으로 철로의 시작 지점 계산
    while heap and heap[0] < line_start:  # heap[0] = 힙에 저장된 시작 지점 중 최소값
        heapq.heappop(heap)  # 철로의 시작 지점보다 시작 좌표가 작은 경우 철로를 벗어나므로 pop
    max_cnt = max(max_cnt, len(heap))  # 현재 철로에 포함되는 사람 수가 최대값인 경우 갱신

print(max_cnt)
