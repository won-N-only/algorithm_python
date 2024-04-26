from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def bfs(start):
    q = deque([(start, 1)])
    visit.add(start)
    while q:
        ccost, cidx = q.popleft()
        for next in coins:
            total = ccost+next
            if total not in visit:
                if total < k:
                    q.append((total, cidx+1))
                    visit.add(total)
                elif total == k:
                    return cidx+1
    return float('inf')


n, k = map(int, input().split())

visit = set([])

coins = set()
for i in range(n):
    a = int(input())
    if a < k:
        coins.add(a)
    elif a == k:
        print(1)
        exit()

coins = sorted(list(coins), reverse=True)

res = float('inf')

for i in range(len(coins)):
    kind = bfs(coins[i])
    res = min(kind, res)

if res != float('inf'):
    print(res)
    
else:
    print(-1)
