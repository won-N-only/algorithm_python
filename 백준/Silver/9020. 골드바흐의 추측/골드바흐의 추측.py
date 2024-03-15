import sys


def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_list = []
for i in range(2, 10000):
    if (isprime(i) == True):
        prime_list.append(i)


t = int(sys.stdin.readline().rstrip())
for x in range(t):
    num = int(int((sys.stdin.readline().rstrip()))/2)
    for j in range(num, 0, -1):
        if j in prime_list and (num*2-j) in prime_list:
            print(j, num*2-j)
            break