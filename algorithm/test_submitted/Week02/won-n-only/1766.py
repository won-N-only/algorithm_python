import sys
import heapq


def input():
    return sys.stdin.readline().strip()


def solve(start, arr):
    q = []
    heapq.heapify(q)
    for i in range(1, n+1):
        if ind[i] == 0:
            heapq.heappush(q, i)

    while q:
        curr = heapq.heappop(q)
        ans.append(curr)

        for next in arr[curr]:
            ind[next] -= 1

            if ind[next] == 0:
                heapq.heappush(q, next)

    return ans


n, m = map(int, input().split())

prob_list = [[]for i in range(n+1)]
ind = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    prob_list[a].append(b)
    ind[b] += 1

ans = []
solve(0, prob_list)
print(*ans)
