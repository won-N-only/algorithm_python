import sys


def input():
    return sys.stdin.readline().strip()

t = int(input())
brackets = []
for i in range(t):
    brackets.append(input())
chk = [-1]*len(brackets)
for j in range(t):
    idx = 0
    for i in range(len(brackets[j])):
        if brackets[j][i] == "(":
            idx += 1
        elif brackets[j][i] == ")":
            idx -= 1
            if idx < 0:
                chk[j] = 0

                break
    if idx == 0:
        chk[j] = 1
    else:
        chk[j] = 0

for i in chk:
    if i == 1:
        print("YES")
    else:
        print("NO")
