ans = []
n, m = map(int, input().split())


def btk2(z):
    if m == len(ans):
        print(' '.join(map(str, ans)))
        return
    for i in range(z, n+1):
        if i not in ans:
            ans.append(i)
            btk2(i+1)
            ans.pop()


btk2(1)
