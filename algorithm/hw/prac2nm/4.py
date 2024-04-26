def hungry(arr, m):
    if m == 0:
        return [[]]
    res = []
    for i in range(len(arr)):
        st = arr[i]
        for am in hungry(arr[:i]+arr[i:], m-1):
            res.append([st]+am)
    return res


n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
tl = hungry(arr, m)

for i in range(len(tl)):
    print(*tl[i])
