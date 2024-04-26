from collections import deque

import sys
import time


def input2():
    return sys.stdin.readline().strip()


def bfs(start, arr, visit):
    q = deque([start])
    visit.add(start)
    while q:
        curr = q.popleft()
        for next in arr[curr]:
            if next not in visit:
                visit.add(next)
                q.append(next)
    return visit


def dfs(start, arr, visit):
    visit.add(start)
    for next in arr[start]:
        if next not in visit:
            dfs(next, arr, visit)
    return visit


computer_death = int(input())
computer_couple = int(input())
computer_list = [[] for i in range(computer_death+1)]

for i in range(computer_couple):
    a, b = map(int, input().split())
    computer_list[a].append(b)
    computer_list[b].append(a)

# 이런식으로 링크를 찾는문제는 bfs가 더빠르네 왜지
# 아마 토리가 균등하게 이어져있어서 그런것같네
# 만약 leaf가 긴 트리였으면 dfs가 더나았을듯?

# visit_list = set([])
# a = time.time()
# bfs(1, computer_list, visit_list)
# b = time.time()
# dfs(1, computer_list, visit_list)
# c = time.time()
# print(len(visit_list)-1)
# print((a-b)*1000, (b-c)*1000)
visit_list_bfs = set([])
start_time_bfs = time.time()
bfs(1, computer_list, visit_list_bfs)
end_time_bfs = time.time()

visit_list_dfs = set([])
start_time_dfs = time.time()
dfs(1, computer_list, visit_list_dfs)
end_time_dfs = time.time()

print(len(visit_list_bfs)-1)
print("BFS time:", (end_time_bfs - start_time_bfs) * 100000, "ms")
print("DFS time:", (end_time_dfs - start_time_dfs) * 100000, "ms")
