import math
import sys


def input():
    return sys.stdin.readline().strip()


def combi(n, r):
    return math.factorial(n)//math.factorial(r)//math.factorial(n-r)


def fact(n):
    if n > 1:
        return n*fact(n-1)
    else:
        return 1


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    ans = combi(b, a)
    # a! / b!(a-b)!
    print(ans)
    n = fact(b)
    r = fact(a)
    n_r = fact(b-a)
    print(n//r//n_r)
