def min_coins(n):
    if n == 1 or n == 3:
        return -1
    if n % 5 == 0:
        return n // 5
    else:
        f_c = n // 5
        for i in range(f_c, -1, -1):
            gosurum = n - (i * 5)
            if gosurum % 2 == 0:
                t_c = gosurum // 2
                return i + t_c
    return -1
n=int(input())

print(min_coins(n))
