def bin_make(n):

    for i in range(3, n+1):
        d[i] = (d[i-1]+d[i-2]) % 15746

    return d[n]


n = int(input())+1
d = [0]*(n+1)

if n > 2:
    d[1] = d[2] = 1
    ans = bin_make(n)
    print(ans)

else:
    print(1)
