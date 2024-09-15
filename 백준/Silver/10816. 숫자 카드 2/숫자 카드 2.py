import sys
from collections import deque


def input():
    return sys.stdin.readline()


n = int(input())
card = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

count = {}
for c in card:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

for target in targets:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
