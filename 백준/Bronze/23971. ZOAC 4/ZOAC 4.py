import math
import sys
def input(): return sys.stdin.readline()


H, W, N, M = map(int, input().split())

rows = math.ceil(H / (N + 1))
cols = math.ceil(W / (M + 1))

max_people = rows * cols

print(max_people)
