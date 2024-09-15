import sys


def input():
    return sys.stdin.readline()


while (1):
    arr = list(map(int, input().split()))
    if (arr[0] == 0):
        exit()
    arr.sort()
    if (arr[0]**2 + arr[1]**2 == arr[2]**2):
        print("right")
    else:
        print('wrong')
