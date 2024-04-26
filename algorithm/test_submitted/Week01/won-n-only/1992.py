import sys


def input():
    return sys.stdin.readline().strip()


# 총계로 1 or 0 구분
def identify_matrix(x, y, n):
    total = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            total += matrix[i][j]
    return total


def quadtree(x, y, n):
    total = identify_matrix(x, y, n)
    if total == n**2:
        res.append(1)
        return
    elif total == 0:
        res.append(0)
        return
    else:
        res.append("(")
        quadtree(x, y, n//2)
        quadtree(x, y + n//2,  n//2)
        quadtree(x + n//2, y,  n//2)
        quadtree(x + n//2, y + n//2,  n//2)
        res.append(")")


n = int(input())
matrix = [list(map(int, (map(str, input())))) for _ in range(n)]
res = []
quadtree(0, 0, n)
print(*res, sep="")
