import sys


def input():
    return sys.stdin.readline().strip()


def correction(arr):
    for i in range(1, len1+1):
        for j in range(1, len2+1):

            if s1[i-1] == s2[j-1]:
                arr[i][j] += arr[i-1][j-1]+1
    mass = 0
    for i in range(len1+1):
        mass = max(mass, max(arr[i]))
    return print(mass)


s1 = input()
s2 = input()

len1 = len(s1)
len2 = len(s2)

arr = [[0]*(len2+1)for _ in range(len1+1)]
correction(arr)
