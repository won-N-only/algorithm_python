import heapq
import sys


def input():
    return sys.stdin.readline().strip()


def meetingroom():
    task = [heapq.heappop(q)]

    while q:
        a = heapq.heappop(q)

        if a[0] < task[-1][1] and a[1] >= task[-1][1]:
            continue
        if a[1] < task[-1][1] and a[0] >= task[-1][0]:
            task.pop()

        task.append(a)

    return len(task)


n = int(input())
q = []

for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(q, [a, b])

find = meetingroom()

print(find)
