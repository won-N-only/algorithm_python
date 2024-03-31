import sys


def input():
    return sys.stdin.readline().strip()
def pelind(a, b):
    key = a + b
    if key in discriminator and discriminator[key] <= a:
        return print(1)

    original_a, original_b = a, b
    while a < b:
        if num[a] != num[b]:
            return print(0)
        a += 1
        b -= 1

    discriminator[key] = min(discriminator.get(key, float('inf')), original_a)
    return print(1)

n = int(input())
num = list(map(int, input().split()))
m = int(input())
discriminator = {}

for i in range(m):
    a, b = map(int, input().split())
    pelind(a-1, b-1)
