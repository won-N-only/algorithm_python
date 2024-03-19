import sys


def input():
    return sys.stdin.readline()


def happy(dpth, total, pl, mi, pr, di):
    global minn, maxx, opr
    if dpth == n:
        minn = min(minn, total)
        maxx = max(maxx, total)
        return

    num = arr[dpth]
    if pl > 0:
        happy(dpth+1, total+num, pl-1, mi, pr, di)
    if mi > 0:
        happy(dpth+1, total-num, pl, mi-1, pr, di)
    if pr > 0:
        happy(dpth+1, total*num, pl, mi, pr-1, di)
    if di > 0:
        if total >= 0:
            happy(dpth+1, total//num, pl, mi, pr, di-1)
        if total < 0:
            happy(dpth+1, -(-total//num), pl, mi, pr, di-1)


n = int(input())
arr = list(map(int, input().split()))
opr = list(map(int, input().split()))
minn, maxx = 10**9, -10**9
happy(1, arr[0], opr[0], opr[1], opr[2], opr[3])
print(maxx)
print(minn)
