import sys

def input():
    return sys.stdin.readline().strip()

def era(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:  
            for j in range(i * i, limit + 1, i): 
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]] 

limit = 10**6
primes = era(limit)  
n, m = map(int, input().split())

for prime in primes:
    if prime > m: 
        break
    if prime >= n:  
        print(prime)
