def find_middle(arr, left, mid, right):
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[mid] > arr[right]:
        arr[right], arr[mid] = arr[mid], arr[right]
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    return mid


def quicksort(arr, left, right):
    if left < right:
        pl = left
        pr = right
        pv = find_middle(arr, pl, (pl+pr)//2, pr)
        chk = arr[pv]
        arr[pv], arr[pr-1] = arr[pr-1], arr[pv]
        pl += 1
        pr -= 2
        while pl <= pr:

            while arr[pl] < chk:
                pl += 1
            while arr[pr] > chk:
                pr -= 1
            if pl <= pr:
                arr[pl], arr[pr] = arr[pr], arr[pl]
                pl += 1
                pr -= 1
        if left < pl:
            quicksort(arr, left, pv)
        if right > pl:
            quicksort(arr, pv, right)


text = []
n = int(input())
for i in range(n):
    text.append(int(input()))


quicksort(text, 0, len(text)-1)

print(text)
