def correction(arr):
    for i in range(1, ls1+1):
        for j in range(1, ls2+1):

            if s1[i-1] == s2[j-1]:
                arr[i][j] += arr[i-1][j-1]+1
    return arr


s1 = input()
s2 = input()
ls1 = len(s1)
ls2 = len(s2)
dp = [[0]*(ls2+1) for i in range(ls1+1)]
ans = []
res = correction(dp)
for i in range(ls1+1):
    ans.append(max(dp[i]))

print(max(ans))
