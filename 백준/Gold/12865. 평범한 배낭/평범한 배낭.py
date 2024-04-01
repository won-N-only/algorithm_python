import sys


def input():
    return sys.stdin.readline().strip()



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
# 이거 dp = [[0]*(k+1)]*(n+1)이렇게만들면 [0]이 다 같은 곳을 참조해서 안됨

not_in_bag = []
for _ in range(n):
    a, b = map(int, input().split())
    not_in_bag.append([a, b])
not_in_bag.sort()


ans2 = my_wallet(k, not_in_bag)

print(ans2)
