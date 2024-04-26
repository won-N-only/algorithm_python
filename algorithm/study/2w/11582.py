import sys


def input():
    return sys.stdin.readline().strip()


def chicken_N_beer(arr, n, beer):
    idx = n // beer
    arr = []
    res = []
    for i in range(0, n, idx):
        arr = chicken[i:i+idx]
        arr.sort()
        res.append(arr)
        print(*arr, end=" ")


n = int(input())
chicken = list(map(int, input().split()))
beer = int(input())


chicken_N_beer(chicken_N_beer, n, beer)
