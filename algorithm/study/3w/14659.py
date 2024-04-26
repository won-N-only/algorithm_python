import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))

height = arr[0]
ans = 0
cnt = 0

for i in range(1, n):
    if arr[i] < height:
        cnt += 1
    else:
        height = arr[i]
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print((ans))
