import sys
from collections import deque

MAX_NUMBER = 100001


def input():
    return sys.stdin.readline().strip()


def bfs():
    q = deque([n])
    visited[n] = 0
    while q:
        x = q.popleft()

        if 0 <= x*2 < MAX_NUMBER and visited[x*2] == -1:
            visited[x*2] = visited[x]
            q.append(x*2)
            if x*2 == k:
                return visited[x*2]
        for nxt in (x-1, x+1, x*2):
            if 0 <= nxt < MAX_NUMBER and visited[nxt] == -1:
                visited[nxt] = visited[x] + 1
                q.append(nxt)
                if nxt == k:
                    return visited[nxt]
    return visited[k]


n, k = map(int, input().split())
visited = [-1] * MAX_NUMBER

if n == k:
    print(0)
else:
    print(bfs())
