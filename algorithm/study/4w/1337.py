import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
cnt = 0
max_cnt = 0
for i in range(1, n):
    if arr[i]-arr[i-1] == 1:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0

print(cnt)