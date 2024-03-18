def power_mod(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        y = power_mod(a, b // 2, c)
        return (y * y) % c
    else:
        return ((a % c) * power_mod(a, b-1, c)) % c
a, b, c = map(int, input().split())
print(power_mod(a, b, c))