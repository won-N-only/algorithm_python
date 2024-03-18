import sys


def input():
    return sys.stdin.readline().strip()


def m_sort(arr, start=0, end=False):
    if end == False:
        end = len(arr)
    if end > start+1:
        mid = (start+end)//2
        m_sort(arr, start, mid)
        m_sort(arr, mid, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    lf = arr[start:mid]
    rt = arr[mid:end]
    now = start
    li, ri = 0, 0
    while li < len(lf) and ri < len(rt):
        if lf[li] < rt[ri]:
            arr[now] = lf[li]
            li += 1
        else:
            arr[now] = rt[ri]
            ri += 1
        now += 1
    while li < len(lf):
        arr[now] = lf[li]
        li += 1
        now += 1
    while ri < len(rt):
        arr[now] = rt[ri]
        ri += 1
        now += 1
    return


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
m_sort(arr)
for i in range(len(arr)):
    print(arr[i])
