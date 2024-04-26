import sys
import heapq


def input():
    return sys.stdin.readline().strip()


def interview(applicants):
    applicants.sort()
    idx = 1
    best = applicants[0][1]

    for _, score in applicants[1:]:
        if score < best:
            idx += 1
            best = score

    return print(idx)

# 힙쓰면 힙으로 바꿔주는시간때문에 오히려 더 오래걸림


def interview(arr):
    heapq.heapify(arr)
    best = heapq.heappop(arr)
    idx = 1

    while arr:
        next = heapq.heappop(arr)
        if next[1] < best[1]:
            idx += 1
            best = next

    return print(idx)


T = int(input())
for _ in range(T):
    N = int(input())
    applicants = [list(map(int, input().split())) for _ in range(N)]
    interview(applicants)
