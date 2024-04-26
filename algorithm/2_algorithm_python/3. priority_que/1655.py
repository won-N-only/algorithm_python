import heapq
import sys


def input():
    return sys.stdin.readline().strip()


def calc_mid(num, mid, maxx, minn):
    # 모든 수 다 비교하는식
    if num > -mid:
        heapq.heappush(minn, num)
    else:
        heapq.heappush(maxx, -num)

    if len(minn) > len(maxx):
        heapq.heappush(maxx, -heapq.heappop(minn))

    # 이거없으면 내림차순일때 안됨
    elif len(minn) <= len(maxx)-2:
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

############################################################


def add_number(number, max_heap, min_heap):
    # 저글링 굴려서 mid-value찾아냄
    # maxx,minn왔다 갔다 하면서 mid만 뽑는식
    heapq.heappush(max_heap, -number)
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])


N = int(input())
max_heap, min_heap = [], []

for _ in range(N):
    number = int(input())
    add_number(number, max_heap, min_heap)
