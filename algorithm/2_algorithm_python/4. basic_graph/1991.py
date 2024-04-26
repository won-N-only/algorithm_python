import sys


def input():
    return sys.stdin.readline().strip()


def pre(root):
    if root != '.':
        print(root, end='')
        pre(nodedict[root][0])
        pre(nodedict[root][1])


def mid(root):
    if root != '.':
        mid(nodedict[root][0])
        print(root, end='')
        mid(nodedict[root][1])


def post(root):
    if root != '.':
        post(nodedict[root][0])
        post(nodedict[root][1])
        print(root, end='')


n = int(input())
nodedict = {}

for _ in range(n):
    p, l, r = input().split()
    nodedict[p] = [l, r]
pre("A")
print()
mid("A")
print()
post("A")
