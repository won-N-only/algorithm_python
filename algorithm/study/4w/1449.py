import sys
def input(): return sys.stdin.readline().strip()


n, l = map(int, input().split())
posi = list(map(int, input().split()))
posi.sort()

tapes = 0
start = posi[0]
# 테이프 다 써야 새 테이프 꺼냄
for i in range(1, n):
    if posi[i] - start >= l:
        tapes += 1
        start = posi[i]

tapes += 1

print(tapes)
