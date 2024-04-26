import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def dfs(start, arr):
    stk = deque([start])
    visit = set([start])
    trail = 0

    while stk:
        curr = stk.pop()
        for next in arr[curr]:
            if next not in visit:
                # 0이어도 visit에 add해줘야 시간빨라지네
                #어차피 curr='0인요소'기때문에 add해도 ㄱㅊ
                visit.add(next)
                if a[next] == 0:
                    stk.append(next)
                elif a[next] == 1:
                    trail += 1
    return trail


n = int(input())
a = [0]+[int(char) for char in input()]
route66 = [[] for i in range(n+1)]
trail = 0

for i in range(n-1):
    u, v = map(int, (input().split()))
    route66[u].append(v)
    route66[v].append(u)

# 모든경로말고 중복경로없애서 하나만갈수있을거같은데
# visited_site를 set으로 놓는다거나? 
# 123 124 234 45 이거만 나오게해서 *2하면 되잖아
for i in range(1, n+1):
    if a[i] == 1:
        trail += dfs(i, route66)

print(trail)
