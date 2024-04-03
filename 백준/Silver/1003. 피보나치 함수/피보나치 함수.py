import sys


def input():
    return sys.stdin.readline().strip()


def pibo(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)

    zeros = [0] * (n + 1)
    ones = [0] * (n + 1)
    zeros[0], ones[1] = 1, 1

    for i in range(2, n + 1):
        zeros[i] = zeros[i - 1] + zeros[i - 2]
        ones[i] = ones[i - 1] + ones[i - 2]

    return zeros[n], ones[n]


t = int(input())
for i in range(t):
    n = int(input())
    z, o = pibo(n)
    print(z, o)
