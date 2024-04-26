def GCD(w, h):
    if w == 0 or h == 0:
        # w=h인 정사각형이니까
        return w
    return GCD(h, w % h)


a, b = map(int, input().split())
print(GCD(a, b))
