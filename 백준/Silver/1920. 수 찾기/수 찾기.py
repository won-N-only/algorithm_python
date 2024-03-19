import sys


def input():
    return sys.stdin.readline()


def bin_search(arr, obj, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if arr[mid] == obj:
        return 1
    elif arr[mid] > obj:
        return bin_search(arr, obj, start, mid-1)
    elif arr[mid] < obj:
        return bin_search(arr, obj, mid+1, end)
    


n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
arr_n.sort()
for i in range(m):
    print(bin_search(arr_n, arr_m[i], 0, n-1))
