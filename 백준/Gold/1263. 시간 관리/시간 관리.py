import heapq


def time_manage(q):
    dL, t = heapq.heappop(q)
    ava = -dL-t

    while q:
        #-a가 덷라 b가 시간
        a, b = heapq.heappop(q)
        ava = min(ava, -a)
        ava-=b

    return ava if ava>=0 else -1


n = int(input())
T = []
S = []
q = []

for i in range(n):
    t, dL = map(int, input().split())
    T.append(t)
    S.append(dL)
    heapq.heappush(q, (-dL, t))

if sum(T) > max(S):
    print(-1)

else:
    ans = time_manage(q)
    print(ans)
