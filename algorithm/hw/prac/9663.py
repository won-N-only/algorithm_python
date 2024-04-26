# 시간초과뜸
def find_queen(col):
    global idx
    if col == n:
        sols.append(list(temp))
        idx += 1
        return
    for i in range(n):
        temp[col] = i
        chk = True
        for j in range(col):
            if temp[col] == temp[j] or abs(temp[col]-temp[j]) == abs(col-j):
                chk = False
                # 여긴 왜 break 없어도되는지
        if chk == True:
            find_queen(col+1)

idx = 0
n = int(input())
sols = []
# temp [ ] *n이랑 [ -1] *n이랑 차이점
temp = [-1]*n
for i in range(n):
    temp[0] = i
    find_queen(1)
# for sol in sols:
#     print(' '.join(map(str, sol)))
print(idx)
# 뒤에서 숫자매기는것도 물어보기
# 앞에서만대겠는디 음
# 왜 시간초과지 ?
