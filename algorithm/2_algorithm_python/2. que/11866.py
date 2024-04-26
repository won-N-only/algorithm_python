from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


people = deque()

n, k = map(int, input().split())
# # (n+k % n)으로 기본 사람순서
# idx = n+k
# for i in range(k, n+k):
#     people.append((k*i) % n + 1)
# print(people)
# for i in range(n):
#     print(people.popleft())
# 돌리는거말고 다른방법없나

people = deque([i for i in range(1, 1+n)])
res = []
for i in range(n):
    for j in range(k-1):
        people.append(people.popleft())
    res.append(people.popleft())
print("<", end="")
print(*res, end="", sep=", ")
print(">", end="")
