from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().strip()


t = int(input())
for _ in range(t):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        name, kind = input().split()
        clothes[kind] += 1

    result = 1
    for count in clothes.values():
        result *= (count + 1)

    print(result - 1)
