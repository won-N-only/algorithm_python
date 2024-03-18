
import sys


def sort():
    chklst = [0]*10001
    n = int(sys.stdin.readline())

    for i in range(n):
        num = int(sys.stdin.readline())
        chklst[num] += 1

    for i in range(1, 10001):
        if chklst[i] != 0:
            for _ in range(chklst[i]):
                print(i)


sort()
