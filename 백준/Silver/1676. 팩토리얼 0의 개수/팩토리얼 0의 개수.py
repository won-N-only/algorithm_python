import sys


def input():
    return sys.stdin.readline()


def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n-1) * n


n = int(input())
res = str(fact(n))[::-1]
cnt = 0
for r in res:
    if r == "0":
        cnt += 1
    else:
        print(cnt)
        break
