import sys


def input():
    return sys.stdin.readline().strip()


def fsort(arr, max_arr=-1):
    if max_arr == -1:
        max_arr = max(arr)
    f = [0]*(max_arr+1)
    brr = [0]*n

    for i in range(n):
        f[arr[i]] += 1
    for i in range(1, max_arr+1):
        f[i] += f[i-1]
    # stable하게만들기위해 뒷자리부터, f[arr[i]]때매 역순될수도있음
    for i in range(n):
        f[arr[i]] -= 1
        brr[f[arr[i]]] = arr[i]

    return brr


n = int(input())
arr = [int(input()) for _ in range(n)]
n = len(arr)
sorted_arr = fsort(arr)
for i in sorted_arr:
    print(i)
