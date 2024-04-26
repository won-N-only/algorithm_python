from collections import deque


def topology(arr):
    ans = []
    q = deque()
    for i in range(1, n+1):
        if ind[i] == 0:
            q.append(i)
    while q:
        curr = q.popleft()
        ans.append(curr)
        for next in arr[curr]:
            ind[next] -= 1
            if ind[next] == 0:
                q.append(next)
    return ans


n, m = map(int, input().split())
ind = [0]*(n+1)
members = [[]for i in range(n+1)]

for _ in range(m):
    case = list(map(int, input().split()))
    for i in range(1, len(case) - 1):
        members[case[i]].append(case[i + 1])
        ind[case[i + 1]] += 1

ans = topology(members)
if len(ans) == n:
    [print(i) for i in ans]

else:
    print(0)
