import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
if n % 2 == 0:
    print("CY")
else:
    print("SK")
