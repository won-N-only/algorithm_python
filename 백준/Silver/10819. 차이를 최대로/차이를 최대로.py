from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

max_val = 0
for perm in permutations(a, n):
    curr_val = sum(abs(perm[i] - perm[i+1]) for i in range(n-1)) 
    max_val = max(max_val, curr_val)

print(max_val)