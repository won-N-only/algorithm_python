import sys


def input():
    return (sys.stdin.readline())


T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        # 원의 범위안에 시작점 끝점 있으면 안됨
        start_in = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
        end_in = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2

        if start_in != end_in:
            cnt += 1

    print(cnt)
