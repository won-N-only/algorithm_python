import sys


def input():
    return sys.stdin.readline()


n = int(input())
arr = list(map(int, input().split()))
ans = 0
min_lists = []

if n == 1:
    arr.sort()
    for i in range(5):
        ans += arr[i]

else:
    min_lists.append(min(arr[0], arr[5]))
    min_lists.append(min(arr[1], arr[4]))
    min_lists.append(min(arr[2], arr[3]))
    min_lists.sort()

    min3 = sum(min_lists)
    min2 = min_lists[0] + min_lists[1]
    min1 = min_lists[0]

    n3 = 4
    n2 = 4 * (n - 1) + 4 * (n - 2)
    n1 = 4 * (n - 2) * (n - 1) + (n - 2) ** 2

    ans += min1 * n1
    ans += min2 * n2
    ans += min3 * n3
print(ans)
