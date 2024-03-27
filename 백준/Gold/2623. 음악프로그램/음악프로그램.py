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

for i in range(m):
    case = list(map(int, input().split()))
    hh = case[0]
    for i in range(len(case)-2):
        members[case[i+1]].append(case[i+2])
        ind[case[i+2]] += 1

ans = topology(members)
if len(ans) == n:
    [print(i) for i in ans]

else:
    print(0)
