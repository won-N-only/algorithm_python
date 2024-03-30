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
    return dp[len2]

s1 = input()
s2 = input()
print( lcs_length(s1, s2))
