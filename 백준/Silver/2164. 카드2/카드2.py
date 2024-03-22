import sys
from collections import deque


n = int(input())
arr = deque()

for i in range(n):
    arr.append(i+1)

while len(arr) != 1:

    arr.popleft()
    arr.append(arr.popleft())

for i in arr:
    print(i)
