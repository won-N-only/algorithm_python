def set(col):
    global sols
    if col == 8:
        sols.append((list(temp)))

        return

    for i in range(8):
        chk = True
        for j in range(col):
            temp[col] = i
            if temp[col] == temp[j] or abs(col - j) == abs(temp[col]-temp[j]):
                chk = False
        if chk == True:
            set(1+col)


sols = []
temp = [-1]*8
for i in range(8):
    temp[0] = i
    set(1)
for sol in sols:
    print(' '.join(map(str, sol)))
