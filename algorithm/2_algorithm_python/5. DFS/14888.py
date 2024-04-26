from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def dfs(start, arr):
    q = deque([start])
    visit = set([start])
    while q:
        curr = q.pop()
        for next in arr[curr]:
            if next not in visit:
                visit.add(next)
                q.append(next)
    return -1


n = int(input())
a_list = list(map(int, (input().split())))
opr_list = [i for i in map(int, input().split())]
