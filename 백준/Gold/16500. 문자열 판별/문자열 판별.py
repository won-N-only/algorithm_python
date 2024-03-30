def can_form(s, words):
    dp = [0] * (len(s) + 1)
    dp[0] = 1   

    for i in range(1, len(s) + 1):
        for word in words:
            if dp[i-len(word)] and s[i-len(word):i] == word:
                dp[i] = 1
                break

    return dp[-1]

s = input()
n = int(input())
words = [input() for _ in range(n)]

print(1 if can_form(s, words) else 0)
