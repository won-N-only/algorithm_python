import heapq
import sys


def input():
    return sys.stdin.readline().strip()


def select_room():

    while pre_list:
        curr = heapq.heappop(pre_list)

        if not post_list or post_list[0][0] > curr[0]:
            heapq.heappush(post_list, (curr[1], curr[0]))
            continue

        heapq.heappop(post_list)
        heapq.heappush(post_list, (curr[1], curr[0]))


n = int(input())

pre_list = []
post_list = []

for _ in range(n):
    s, t = map(int, input().split())
    heapq.heappush(pre_list, (s, t))

select_room()
print(len(post_list))
