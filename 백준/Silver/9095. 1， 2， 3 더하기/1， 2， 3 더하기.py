def dp(n):
    for i in range(4, n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]

    return print(d[n])


t = int(input())

for i in range(t):
    n = int(input())
    if n>=3:
        d = [1, 2, 4]+[0]*(n-2)
        d[1] = 1
        d[2] = 2
        d[3] = 4
        dp(n)
    else:print(n)
        
