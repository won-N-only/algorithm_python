def dupl_test(col, j):
    if temp[col] == temp[j] or abs(col-j) == abs(temp[col]-temp[j]):
        return False
    return True


def findQ(col):
    global idx, sols, chk
    if col == n:
        sols.append(' '.join(map(str, temp)))
        idx += 1
        return
    for i in range(n):
        if chk[i] == 1:
            continue
        temp[col] = i
        chk_pre = True
        for j in range(col):
            # false가뭐지
            if dupl_test(col, j) == False:
                chk_pre = False
                break
        if chk_pre:
            chk[i] = 1
            findQ(col+1)
            chk[i] = 0


idx = 0
n = int(input())
temp = [-1]*n
chk = [-1]*n
sols = []
findQ(0)
print(idx)
