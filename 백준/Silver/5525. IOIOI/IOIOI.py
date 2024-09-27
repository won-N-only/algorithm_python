def count_pn(N, M, S):
    count = 0
    i = 0
    pattern_count = 0

    while i < M - 1:
        if S[i:i+3] == "IOI":
            pattern_count += 1
            i += 2
            if pattern_count == N:
                count += 1
                pattern_count -= 1
        else:
            pattern_count = 0
            i += 1

    return count


N = int(input())
M = int(input())
S = input().strip()

print(count_pn(N, M, S))
