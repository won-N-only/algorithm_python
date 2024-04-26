import sys


def input():
    return sys.stdin.readline().strip()



def count_ways(coins, amounts, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin_idx, coin in enumerate(coins):
        next_dp = dp[:] 
        for j in range(1, amounts[coin_idx] + 1):
            coin_value = coin * j
            for amount in range(coin_value, target + 1):
                next_dp[amount] += dp[amount - coin_value]
        dp = next_dp  
    return dp[target]  

n = int(input())
k = int(input())
coins = []
amounts = []

for i in range(k):
    a, b = map(int, input().split())
    coins.append(a)
    amounts.append(b)

print(count_ways(coins, amounts, n))
