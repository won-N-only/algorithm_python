import sys


def input():
    return sys.stdin.readline().strip()


# def calc_s(s):
#     stack = []
#     for char in s:
#         if char == '(':
#             stack.append('(')
#         elif char == '[':
#             stack.append('[')
#         elif char == ')':
#             temp = 0
#             while stack and stack[-1] != '(':
#                 temp += stack.pop()
#             if not stack:
#                 return 0
#             stack.pop()
#             stack.append(max(2 * temp, 2))
#         elif char == ']':
#             temp = 0
#             while stack and stack[-1] != '[':
#                 temp += stack.pop()
#             if not stack:
#                 return 0
#             stack.pop()
#             stack.append(max(3 * temp, 3))
#     return sum(stack)


# def initial_check(s):
#     if len(s) % 2 == 1 or (s[0] == "[" and s[-1] == ")") or (s[-1] == "]" and s[0] == "("):
#         return 0
#     return 1


# s = input().strip()
# if initial_check(s) != 0:

#     print(calc_s(s))

# else:
#     print(0)
bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
