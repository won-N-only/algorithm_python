import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    #command = input().split()

    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'front':
        print(dq[0] if len(dq) > 0 else -1)
    elif command[0] == 'back':
        print(dq[-1] if len(dq) > 0 else -1)
    elif command[0] == 'empty':
        print(0 if len(dq) > 0 else 1)
    elif command[0] == 'pop':
        if len(dq) > 0:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
