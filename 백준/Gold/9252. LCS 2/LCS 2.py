def ans(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # LCS 길이 계산
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # LCS 추적
    i, j = len(a), len(b)
    lcs = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()

    print(len(lcs))
    if lcs:
        print(''.join(lcs))


# 입력 받기
a = input()
b = input()

ans(a, b)
