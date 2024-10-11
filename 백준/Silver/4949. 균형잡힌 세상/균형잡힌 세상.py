import sys


def check_balance(s):
    stack = []

    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()

    if not stack:
        return "yes"
    else:
        return "no"


while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break
    print(check_balance(line))
