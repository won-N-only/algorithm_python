pos = [0]*8
flag = [False]*8


def put():
    for i in range(8):
        print(f'{pos[i]:2}', end="")
    print()


def set(i):
    for j in range(8):
        if not flag[j]:
            pos[i] = j
            if i == 7:
                put()
            else:
                flag[j] = True
                set(i+1)
                # i+1에서 set(6)일때 밖으로나오는데
                # flag[6]=false로만들고 falg[7]=false무조건
                # 그럼 i부터시작함
                flag[j] = False


set(0)
