import sys


def input():
    return sys.stdin.readline().strip()


def power(k):
    for i in range(1, 21):
        if 2**i >= k:
            return 2**i


def choco(k):
    cnt = 0
    last_chocolate = 1
    while k > 0:
        last_chocolate = power(k) // 2
        cnt += 1
        if k - last_chocolate >= 0:
            k -= last_chocolate
    return cnt


def choco(k):
    cnt = 0  
    temp = res  
    if k != res:  
        while k :  
            temp //= 2 
            if k >= temp:  
                k = k - temp  
                cnt += 1  
            else:  
                cnt += 1 
    print(res, cnt)

k = int(input())
res = power(k)

choco(k)