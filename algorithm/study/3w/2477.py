import sys
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())
medals = []

for i in range(n):
    medals.append(list(map(int, input().split())))

medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for j in range(n):
    if medals[j][0] == m:
        idx = j
        
for i in range(n):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break
