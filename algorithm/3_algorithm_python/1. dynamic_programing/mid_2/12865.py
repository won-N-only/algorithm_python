import sys


def input():
    return sys.stdin.readline().strip()


def mybag(n, k, arr):
    # 이거 dp = [[0]*(k+1)]*(n+1)이렇게만들면 [0]이 다 같은 곳을 참조해서 안됨
    dp = [[0]*(k+1)for _ in range(n+1)]

    for i in range(1, n+1):
        c_weight = arr[i-1][0]
        c_value = arr[i-1][1]

        for weight in range(1, k+1):
            if c_weight <= weight:
                dp[i][weight] = max(
                    dp[i-1][weight], c_value + dp[i-1][weight-c_weight])

            else:
                dp[i][weight] = dp[i-1][weight]

    return dp[n][k]


def my_wallet(k, arr):
    dp2 = [0] * (k+1)

    for wei, v in arr:
        
        # for w in range(k, wei-1, -1):
        #     dp2[w] = max(dp2[w], dp2[w-wei] + v)

        temp = dp2[:]
        for w in range(wei, k+1):
            temp[w] = max(dp2[w], dp2[w-wei] + v)
        dp2 = temp
    return max(dp2)


n, k = map(int, input().split())

not_in_bag = []
for _ in range(n):
    a, b = map(int, input().split())
    not_in_bag.append([a, b])
not_in_bag.sort()


ans = mybag(n, k, not_in_bag)
ans2 = my_wallet(k, not_in_bag)

print(ans)
print(ans2)
