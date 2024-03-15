def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_list = []
# t=int(input())
for i in range(2, 992):
    if (isprime(i) == True):
        prime_list.append(i)
print(prime_list)

num = int(int(input())/2)
for i in range(4,num):
    if num-prime_list[i] in prime_list:
        print(i, num*2-i)
        break
