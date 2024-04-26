def sum1(n):
    summ1 = 0
    for i in range(n):
        summ1 += i
    return summ1


def sum2(n):
    summ2 = 0
    for i in range(n):
        summ2 += i
    return summ2**2


def sum3(n):
    summ3 = 0
    for i in range(n):
        summ3 += i**3
    return summ3


inn = int(input())
n = inn+1

print(sum1(n))
print(sum2(n))
print(sum3(n))
