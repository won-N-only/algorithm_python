import sys


def input():
    return sys.stdin.readline().strip()


def power(k):
    for i in range(1, 21):
        if 2**i >= k:
            return 2**i


def choco(k, res):
    cnt = 0
    if k != res:

        while k > 0:
            res //= 2

            if k >= res:
                k = k - res
                cnt += 1
            else:
                cnt += 1

    print(cnt)


k = int(input())
res = power(k)
print(res, end=" ")
choco(k, res)
