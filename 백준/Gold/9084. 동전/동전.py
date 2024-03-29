def moneycoin(arr, o):
    dp = [0]*(o+1)
    dp[0] = 1

    wallet = arr[:]
    for coin in wallet:
        temp = dp[:]

        for j in range(coin, o+1):
            temp[j] += temp[j-coin]
        dp = temp
    return print(dp[o])


t = int(input())

for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    obj = int(input())
    moneycoin(coins, obj)
