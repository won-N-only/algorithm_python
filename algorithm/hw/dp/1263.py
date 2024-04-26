import heapq


def time_manage(q):
    dL, t = heapq.heappop(q)
    ava = -dL-t

    while q:
        # -a가 덷라인 b가 시간
        a, b = heapq.heappop(q)
        ava = min(ava, -a)
        ava -= b

    return ava if ava >= 0 else -1


n = int(input())
q = []

for i in range(n):
    t, dL = map(int, input().split())
    heapq.heappush(q, (-dL, t))

ans = time_manage(q)
print(ans)
