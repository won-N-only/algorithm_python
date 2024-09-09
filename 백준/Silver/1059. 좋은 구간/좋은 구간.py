import sys


def input():
    return sys.stdin.readline()


L = int(input())
v = list(map(int, input().split()))
v.append(0)

n = int(input())

v.sort()

s, e = 0, 0
found = True

for i in range(1, L + 1):
    if n == v[i]:
        found = False
        break
    elif n < v[i]:
        s = v[i - 1] + 1
        e = v[i] - 1
        break

if found:
    result = (n - s) * (e - n + 1) + (e - n)
    print(result)
else:
    print(0)
