def moneycoin(arr, o):
    dp = [0]*(o+1)
    dp[0] = 1

    for coin in arr:
        for j in range(coin, o+1):
            dp[j] += dp[j-coin]
            
    return print(dp[o])


t = int(input())

for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    obj = int(input())
    moneycoin(coins, obj)
