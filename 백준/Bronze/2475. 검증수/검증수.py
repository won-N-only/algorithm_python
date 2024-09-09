import sys


def input():
    return sys.stdin.readline()


arr = list(map(int, input().split()))
summ = 0
for i in range(len(arr)):
    summ += arr[i]**2
print(summ % 10)
