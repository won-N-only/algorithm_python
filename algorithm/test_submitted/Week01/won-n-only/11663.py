def bin_section(arr, lf, rt):
    if lf > rt:
        return

    mid = (lf+rt)//2

    if mid==:
        return mid
    if mid<:
        bin_section(arr,lf,mid-1)
    if mid>:
        bin_section(arr,mid+1,rt)


n, m = map(int, (input()).split())
dots = list(map(int, input().split()))
for i in range(m):
    lines = int(input())
res = 0
for i in range(m):
    bin_section(lines[i], 0, m-1)
