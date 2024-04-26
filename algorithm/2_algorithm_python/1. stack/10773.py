import sys


def input():
    return sys.stdin.readline().strip()


k = int(input())
paper = []
for i in range(k):
    w = int(input())
    if w != 0:
        paper.append(w)
    else:
        paper.pop()

print(sum(paper))
