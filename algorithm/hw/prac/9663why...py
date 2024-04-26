import sys
input = sys.stdin.readline

def duple_text(col, row):
    global chk, idx
    if temp[col] == temp[row] or abs(col-row) == abs(temp[col]-temp[row]):
        chk = False
        return

def find_Q(col):
    #global은 함수마다 다 해줘야하는건지?? 
    global chk, idx
    if col == n:
        sols.append(list(temp))
        idx += 1
        return
    for i in range(n):
        temp[col] = i
        chk = True
        for j in range(col):
            duple_text(col, j)
        if chk == True:
            find_Q(col+1)

idx = 0
n = int(input())
temp = [-1]*n
sols = []
for i in range(n):
    temp[0] = i
    find_Q(1)
print(idx)
