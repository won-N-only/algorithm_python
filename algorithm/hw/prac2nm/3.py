def perm(arr, m):
    res = []
    if m == 0:
        return [[]]
    for i in range(len(arr)):
        first = arr[i]
        for rest in perm(arr[i+1:], m-1):
            res.append([first]+rest)
    return res


n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

c = perm(arr, m)
for i in range(len(c)):
    print(*c[i])
