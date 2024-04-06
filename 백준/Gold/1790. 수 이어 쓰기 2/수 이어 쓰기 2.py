n, m = map(int, input().split())

def get_count(d):
    return 9 * (10 ** (d - 1)) * d

d = 1
while m > get_count(d):
    m -= get_count(d)
    d += 1

if d == 1:
    num = m
else:
    num = (m + d - 1) // d + 10 ** (d - 1) - 1

if num > n:
    print(-1)
else:
    print(str(num)[(m - 1) % d])
