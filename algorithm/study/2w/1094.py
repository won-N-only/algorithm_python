import sys


def input():
    return sys.stdin.readline().strip()


def stick(x):
    stick_list = [64, 32, 16, 8, 4, 2, 1]
    cnt = 0
    i = 0
    while x > 0:
        if stick_list[i] <= x:
            x -= stick_list[i]
            cnt += 1
        i += 1
    return cnt


x = int(input())
print(stick(x))
