import sys
import math

input = sys.stdin.readline

T = int(input())


def lcm(a, b):
    return a * b // math.gcd(a, b)


for _ in range(T):
    M, N, x, y = map(int, input().split())

    if y == N:
        y = 0

    found = False
    for k in range(x, M * N + 1, M):
        if k % N == y:
            print(k)
            found = True
            break

    if not found:
        print(-1)
