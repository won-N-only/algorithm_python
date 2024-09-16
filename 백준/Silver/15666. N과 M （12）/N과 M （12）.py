import sys


def input():
    return sys.stdin.readline()


def bt(arr, start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    last = -1
    for i in range(start, n):
        if last != numbers[i]:
            arr.append(numbers[i])
            bt(arr, i)
            arr.pop()
            last = numbers[i]


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
bt([], 0)
