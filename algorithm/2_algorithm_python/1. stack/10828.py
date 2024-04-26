import sys


def input():
    return sys.stdin.readline().strip()


class stack:
    def __init__(self, size):
        self.stk = [None]*size
        self.ptr = 0
        self.size = size

    def push(self, value: int):
        if self.ptr < self.size:
            self.stk[self.ptr] = value
            self.ptr += 1

    def pop(self):
        if self.ptr <= 0:
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def amount(self):
        return self.ptr

    def empty(self):
        if self.ptr > 0:
            return 0
        else:
            return 1

    def top(self):
        if self.ptr <= 0:
            return -1
        return self.stk[self.ptr-1]

    def is_empty(self):
        return self.ptr <= 0

    def clear(self):
        self.ptr = 0


s = stack(1000)

s.push(3)
s.push(3)
s.push(3)
s.push(3)
s.push(3)
s.clear()
print(s.stk[3])


# n = int(input())
# # stack size잘못설정함 ㅎㅎ
# s = stack(1000)
# for i in range(n):
#     m = list(map(str, input().split()))
#     if m[0] == "push":
#         s.push(int(m[1]))
#     elif m[0] == "pop":
#         print(s.pop())
#     elif m[0] == "size":
#         print(s.amount())
#     elif m[0] == "empty":
#         print(s.empty())
#     elif m[0] == "top":
#         print(s.top())
