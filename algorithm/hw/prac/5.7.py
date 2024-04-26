pos = [0]*8


def put():
    for i in range(8):
        print(f'{pos[i]:2}', end="")
    print()


def set(i):
    for j in range(8):
        pos[i] = j
        if i == 7:
            put()
        else:
            # i=6일때 set에서넘어간거임
            # ㅌ모양의 옆으로가는 tree생각하면
            set(i+1)
            print(pos)


set(0)
