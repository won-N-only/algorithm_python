import sys


def input():
    return sys.stdin.readline()


def sq_arr(a, b):
    # [[0]*n]*n하면 안의 [0]*n이 다 같은참조개체임
    # 왜 ?? 왜? 숫자 0인데 ? ? ?쓰레기언어
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k]*b[k][j]%1000

    return result


def pro_arr(arr, b):
    if b == 1:
        # b=1이면 반환
        return arr
    if b == 2:
        return sq_arr(arr, arr)
    if b % 2 == 0:
        temp = pro_arr(arr, b // 2)
        return sq_arr(temp, temp)
    else:
        return sq_arr(pro_arr(arr, b - 1), arr)


n, b = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

res = pro_arr(array, b)
for i in range(n):
    for j in range(n):
        res[i][j] = res[i][j] % 1000

[print(*rest) for rest in res]
