import sys


def input():
    return sys.stdin.readline()


n = int(input())
towers = list(map(int, input().split()))
temp = [[1, towers[0]]]
res = [[0]]
for i in range(1, n):

    while len(temp) > 0 and towers[i] >= temp[-1][1]:
        temp.pop()
        if len(temp) == 0:
            res.append([0])
            temp.append([i+1, towers[i]])
            break
    if len(temp) > 0 and len(res)-1 != i:
        if towers[i] < temp[-1][1]:
            res.append([temp[-1][0]])
        else: res.append(0)
        temp.append([i+1, towers[i]])


result = []
for i in range(len(res)):
    result.append(*res[i])

print(*result)
