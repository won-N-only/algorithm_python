def PPAP(s):
    cnt = 0
    i = 0
    while i < n:
        if s[i:i+4] == 'pPAp':
            cnt += 1
            i += 4
        else:i+=1
    return cnt


n = int(input())
s = input()
ans = PPAP(s)
print(ans)
