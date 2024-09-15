import sys


def input():
    return sys.stdin.readline()


n = int(input())
size_arr = list(map(int, input().split()))
size_bulk, pen_bulk = (map(int, input().split()))
size_res = 0

for size in size_arr:
    if (size % size_bulk > 0):
        size_res += (size//size_bulk+1)
    else:
        size_res += size//size_bulk
print(size_res)
print(n//pen_bulk, n % pen_bulk)
