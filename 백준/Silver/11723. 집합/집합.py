import sys


def input():
    return sys.stdin.readline().strip()


def add(x: int):
    arr[x] = 1


def remove(x: int):
    arr[x] = 0


def check(x: int):
    print(arr[x])


def toggle(x: int):
    arr[x] = 1 - arr[x]


def all():
    global arr
    arr = [1] * 21


def empty():
    global arr
    arr = [0] * 21


arr = [0] * 21
m = int(input())

for _ in range(m):
    cmd = input().split()
    if cmd[0] == "all":
        all()
    elif cmd[0] == "empty":
        empty()
    else:
        func, x = cmd[0], int(cmd[1])
        if func == "add":
            add(x)
        elif func == "remove":
            remove(x)
        elif func == "check":
            check(x)
        elif func == "toggle":
            toggle(x)
