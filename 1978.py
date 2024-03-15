def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))

prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

print(prime_count)

# 이건?
# n = int(input())
# lst = []
# sup = []
# idx = 0
# p = list(map(int, input().split()))
# for i in range(n):
#     ind = []
#     for j in range(1, p[i]+1):
#         if p[i] % j == 0:
#             ind.append(j)
#     if len(ind) == 2:
#         idx += 1

# print(idx)
