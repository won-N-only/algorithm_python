import sys


def input():
    return sys.stdin.readline()


n = int(input())
towers = list(map(int, input().split()))
# 인덱스랑 타워높이 같이입력함
temp = [[1, towers[0]]]
res = [[0]]
for i in range(1, n):
    # 앞에 타워없을떄까지 / 높은타워 만날떄까지 pop
    # 타워없어지면 res=0
    while len(temp) > 0 and towers[i] >= temp[-1][1]:
        temp.pop()
        # 타워 다 pop되면 break
        if len(temp) == 0:
            res.append([0])
            temp.append([i+1, towers[i]])
            break
    # 앞에 나보다 높은 타워있는상태로 진행
    # len-1!=i는 윗조건 for-while에서 break 하는법 몰라서
    if len(temp) > 0 and len(res)-1 != i:
        if towers[i] < temp[-1][1]:
            res.append([temp[-1][0]])
        else:
            res.append(0)
        temp.append([i+1, towers[i]])


result = []
for i in range(len(res)):
    result.append(*res[i])

print(*result)
