import sys


def input():
    return sys.stdin.readline().strip()


def pelind(a, b):
    key = a + b
    if key in discriminator:
        if any(saved_start <= a for saved_start in discriminator[key]):
            return print(1)

    origin_a = a
    while a < b:
        if num[a] != num[b]:
            return print(0)
        a += 1
        b -= 1

    if key not in discriminator:
        discriminator[key] = set()
    discriminator[key].add(origin_a)
    
    return print(1)


def pelin2(a, b):
    # pypy로 제출하거나 재귀제한 바꾸거나
    # sys.setrecursionlimit(10**6)
    if a > b:
        return True

    if dp[a][b] != -1:
        return dp[a][b]

    if num[a] == num[b] and pelin2(a + 1, b - 1):
        dp[a][b] = 1
    else:
        dp[a][b] = 0

    return dp[a][b]


n = int(input())
num = list(map(int, input().split()))

m = int(input())
discriminator = {}

dp = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    pelind(a-1, b-1)
    print(pelin2(a-1, b-1))
