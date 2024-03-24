from collections import deque

import sys


def input():
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
visit_list = set([])
dfs(1, computer_list, visit_list)
print(len(visit_list)-1)