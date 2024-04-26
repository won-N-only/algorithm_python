import sys


def input():
    return sys.stdin.readline().strip()

def pibo(n):

    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]

    return d[n]


n = int(input())
d = [0]*(n+1)
if n > 2:
    d[1] = d[2] = 1
    ans = pibo(n)
    print(ans)
else:
    print(1)
