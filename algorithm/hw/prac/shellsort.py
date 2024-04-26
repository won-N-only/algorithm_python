def shell_sort(arr):
    N = len(arr)
    h = N // 2
    if h % 2 == 0:
        h += 1

    while h > 0:
        for i in range(h, N):

            temp = arr[i]
            j = i - h

            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp

        h //= 2
        if h % 2 == 0 and h != 0:
            h += 1
    print(arr)


arr = [8, 1, 4, 2, 7, 6, 3, 5]
shell_sort(arr)
n = len(arr)
h = n//2
while h > 0:
    for i in range(h, n):
        j = i-h
        temp = arr[i]
        while j > 0 and arr[j] > temp:
            arr[j+h] = arr[j]
            j -= h
        arr[j+h] = temp
    h //= 2
    print(arr)
