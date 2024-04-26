import sys


# def input():
#     return sys.stdin.readline().strip()


# def correction(arr):
#     for i in range(1, len1+1):
#         for j in range(1, len2+1):

#             if s1[i-1] == s2[j-1]:
#                 arr[i][j] += arr[i-1][j-1]+1
#             else:
#                 arr[i][j] = max(arr[i-1][j], arr[i][j-1])

#     return print(arr[-1][-1])


# def find_corr(arr):
#     i, j = len1, len2
#     ans = [[]for _ in range(arr[-1][-1])]

#     while i > 0 and j > 0:
#         if s1[i-1] == s2[j-1]:
#             # 1. ans.append(s1[i-1])
#             # 2. ans[arr[i][j]-1] = s1[i-1]

#             # 1안이 2안보다 빠름
#             # cause 매번 arr[i][j]-1을 계산하는시간이
#             # reverse( O(n) )보다 더 들기때문 + ans를 []로 init하는데도 시간듦

#             i -= 1
#             j -= 1
#         elif arr[i-1][j] == arr[i][j]:
#             i -= 1
#         elif arr[i][j] == arr[i][j-1]:
#             j -= 1
#     ans.reverse()
#     return print(''.join(ans))


# s1 = input()
# s2 = input()

# len1 = len(s1)
# len2 = len(s2)

# arr = [[0]*(len2+1)for _ in range(len1+1)]
# res = []

# correction(arr)
# find_corr(arr)


def input():
    return sys.stdin.readline().strip()


def lcs_length(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [0] * (len2 + 1)

    for i in range(1, len1 + 1):
        prev = 0
        for j in range(1, len2 + 1):
            temp = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp
    return dp


s1 = input()
s2 = input()
dp = lcs_length(s1, s2)
res = []

for i in range(len(dp)-1, 0, -1):
    if dp[i] == dp[i-1]+1:
        res.append(s1[i-1])

res.reverse()
print(len(res))
print(*res, sep="")
