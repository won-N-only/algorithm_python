import sys
import math


def input():
    return sys.stdin.readline().strip()


n = int(input())

res = math.comb(n+9, 9) % 10007
print(res)
