def set(col):
    global sols
    if col == 8:
        sols.append(list(temp))
        return

    for i in range(8):
        check = True
        for j in range(col):
            temp[col] = i
            if temp[col] == temp[j] or abs(col-j) == abs(temp[col]-temp[j]):
                check = False
                break
        if check:
            set(col+1)


sols = []
temp = [-1]*8

for i in range(8):
    temp[0] = i
    set(1)

for sol in sols:
    print(' '.join(map(str, sol)))
