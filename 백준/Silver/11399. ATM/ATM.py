import sys


def input():
    return (sys.stdin.readline())


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
summ = 0
for i in range(n+1):
    summ += sum(arr[0:i])
print(summ)
