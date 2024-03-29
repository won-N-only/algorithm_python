def count_ways(coins, amounts, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin_idx, coin in enumerate(coins):
        # 현재 동전을 1개부터 최대 amounts[coin_idx]개까지 사용하는 경우 고려
        next_dp = dp[:]  # 현재까지의 dp 상태를 복사
        for j in range(1, amounts[coin_idx] + 1):
            coin_value = coin * j
            for amount in range(coin_value, target + 1):
                # 현재 동전을 사용해 amount 금액을 만드는 방법의 수 업데이트
                next_dp[amount] += dp[amount - coin_value]
        dp = next_dp  # dp 배열 업데이트

    return dp[target]  # 목표 금액을 만들 수 있는 방법의 수 반환


n = int(input())
k = int(input())
coins = []
amounts = []
for i in range(k):
    a, b = map(int, input().split())
    coins.append(a)
    amounts.append(b)

# 결과 출력
print(count_ways(coins, amounts, n))
