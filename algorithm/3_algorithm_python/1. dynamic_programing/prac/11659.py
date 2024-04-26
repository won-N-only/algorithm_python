import sys


def input():
    return sys.stdin.readline().strip()


n, m = map(int, input().split())
num_list = []
num_list = list(map(int, input().split()))

sum_list = [[]for i in range(n+1)]
sum_list[0] = 0

for i in range(1, n+1):

    sum_list[i] = num_list[i-1]+sum_list[i-1]

for i in range(m):

    x, y = map(int, input().split())
    if x == y:
        print(num_list[x-1])
    else:
        print(sum_list[y]-sum_list[x-1])
