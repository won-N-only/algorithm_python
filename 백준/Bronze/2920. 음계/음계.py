import sys


def input():
    return sys.stdin.readline()


a = list(map(int, input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')