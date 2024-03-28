def square(n):
    dp = [[]for i in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 10007
    return print(dp[n])


n = int(input())
if n>1:
    square(n)
else: print(1)