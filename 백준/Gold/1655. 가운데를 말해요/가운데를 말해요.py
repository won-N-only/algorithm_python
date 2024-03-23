import heapq
import sys


def input():
    return sys.stdin.readline().strip()


def calc_mid(num, mid, maxx, minn):
    if num > -mid:
        heapq.heappush(minn, num)
    else:
        heapq.heappush(maxx, -num)

    if len(minn) > len(maxx):
        heapq.heappush(maxx, -heapq.heappop(minn))
    if len(minn) <= len(maxx)-2:
        heapq.heappush(minn, -heapq.heappop(maxx))

    print(-maxx[0])


maxx = []
minn = []

n = int(input())

for i in range(n):
    number = int(input())
    if i == 0:
        heapq.heappush(maxx, -number)
        print(-maxx[0])
        continue
    calc_mid(number, maxx[0], maxx, minn)
