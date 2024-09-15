import sys


def input():
    return sys.stdin.readline()


def gcd(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(int(a*b/g))
