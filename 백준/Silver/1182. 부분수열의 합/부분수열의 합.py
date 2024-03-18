def comb(arr, m):
    res = []

    if m == 0:
        return [[]]

    for i in range(len(arr)):
        first = arr[i]
        for rest in comb(arr[i+1:], m-1):
            res.append([first]+rest)
    return res


n, s = map(int, input().split())
arr = list(map(int, input().split()))
idx = 0
for i in range(1, n+1):
    for combi in comb(arr, i):
        if sum(combi) == s:
            idx += 1

print(idx)
