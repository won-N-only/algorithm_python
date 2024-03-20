import sys


def input():
    return sys.stdin.readline()


def HerosOfTheStorm(arr, lf, rt, obj):
    if lf > rt:
        return rt
    mid = (lf+rt)//2
    cnt = k

    cnt += sum(arr[:mid])

    if cnt >= arr[mid]*(mid):
        return HerosOfTheStorm(arr, mid+1, rt, obj)
    elif cnt < arr[mid]*(mid):
        return HerosOfTheStorm(arr, lf, mid-1, obj)


n, k = map(int, (input().split()))
Lv = [int(input()) for _ in range(n)]
Lv.sort()
Lvsum = 0
for i in range(n-1):
    if Lv[i] == Lv[i+1]:
        Lvsum += 1
    else:
        break


if Lvsum == n-1:
    ans = Lv[0]+k//n
else:
    levup = HerosOfTheStorm(Lv, 0, n-1, k)
    total_level = k

    for i in range(levup+1):
        total_level += Lv[i]
    ans = total_level//(levup+1)

print(ans)
