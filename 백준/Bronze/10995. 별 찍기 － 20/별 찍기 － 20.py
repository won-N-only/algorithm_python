import sys


def input():
    return (sys.stdin.readline())


n = int(input())

for i in range(n):
    if i % 2 == 0:
        print("* " * n)
    else:
        print(" *" * n)
