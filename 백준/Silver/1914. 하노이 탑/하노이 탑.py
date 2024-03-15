def hanoi(disk, start, end):
    if disk > 1:
        hanoi(disk-1, start, 1+2+3-end-start)

    print( start, end)

    if disk > 1:
        hanoi(disk-1, 1+2+3-end-start, end)


n = int(input())

if n < 21:
    print(2**n-1)
    hanoi(n, 1, 3)
else:
    print(2**n-1)
