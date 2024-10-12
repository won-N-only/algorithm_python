import sys
import math

def custom_round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

input = sys.stdin.readline

n = int(input().strip())

if n == 0:
    print(0)
    sys.exit(0)

opinions = [int(input().strip()) for _ in range(n)]

opinions.sort()

cut = custom_round(n * 0.15)

sum_values = sum(opinions[cut:n - cut])

res = custom_round(sum_values / (n - 2 * cut))
print(res)
