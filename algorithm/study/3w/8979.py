import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
arr = []
cnt = [0] * 5

for _ in range(6):
    direction, length = map(int, input().split())
    arr.append((direction, length))
    cnt[direction] += 1

s = 1
b = 1

for i in range(6):
    if cnt[arr[i][0]] == 1:
        b *= arr[i][1]
    else:
        n = (i + 1) % 6
        nn = (i + 2) % 6
        if arr[i][0] == arr[nn][0]:
            s *= arr[n][1]

print((b - s) * N)
