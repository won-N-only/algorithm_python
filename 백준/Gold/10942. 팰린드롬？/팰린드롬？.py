import sys

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().strip()
def is_palindrome(a, b):
    if a >= b:
        return True
    if dp[a][b] != -1:
        return dp[a][b]
    if num[a] == num[b] and is_palindrome(a + 1, b - 1):
        dp[a][b] = 1
    else:
        dp[a][b] = 0
    return dp[a][b]

n = int(input())
num = list(map(int, input().split()))
m = int(input())
dp = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    print(1 if is_palindrome(a-1, b-1) else 0)