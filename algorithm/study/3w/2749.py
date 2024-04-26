import sys


def input(): return sys.stdin.readline().strip()


mod = 1000000
p = mod // 10 * 15
fibo = [0] * p
fibo[1] = 1

for i in range(2, p):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % mod

n = int(input())

print(fibo[n % p])

