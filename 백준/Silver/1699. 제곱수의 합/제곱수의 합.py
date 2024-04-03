import sys





def square(n):
    for i in range(1, n+1):
        dp[i] = i
        j = 1
        while j*j <= i:
            if dp[i] > dp[i-j*j]+1:
                dp[i] = dp[i-j*j]+1
            j += 1
    return dp[n]


n = int(sys.stdin.readline().strip())
dp = [0]*(n+1)
ans=square(n)
print(ans)