def gosurum(n):
    dp = [8888577]*(n+1)
    dp[0] = 0
    for c in coin:
        temp = dp[:]
        for i in range(c, n+1):
            temp[i] = min(temp[i], temp[i-c]+1)
        dp = temp
    return dp[-1] if dp[-1] != 8888577 else -1


coin = [2, 5]
n = int(input())

ans = gosurum(n)
print(ans)
