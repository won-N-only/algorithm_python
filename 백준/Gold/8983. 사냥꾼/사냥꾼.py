import sys


def input():
    return sys.stdin.readline().strip()


def endangered(arr, lf, rt, obj):
    mid = (lf+rt)//2
    if rt < lf:
        return mid
    if arr[mid] == obj:
        return mid
    elif arr[mid] > obj:
        return endangered(arr, lf, mid-1, obj)
    elif arr[mid] < obj:
        return endangered(arr, mid+1, rt, obj)


m, n, l = map(int, input().split())
posi = [i for i in list(map(int, input().split()))]
posi.sort()

animal = []
big_game = 0

for i in range(n):
    animal.append(list(map(int, input().split())))

animal.sort(key=lambda x: x[1])
for i in range(n):
    if animal[i][1] > l:
        del animal[i:]
        break

n = len(animal)

for i in range(n):
    ex = endangered(posi, 0, m-1, animal[i][0])
    if abs(posi[ex]-animal[i][0])+animal[i][1] <= l:
        big_game += 1
    else:
        if ex+1 < m and abs(posi[ex+1]-animal[i][0])+animal[i][1] <= l:
            big_game += 1

print(big_game)
