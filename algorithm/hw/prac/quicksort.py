def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return 

        mid = part(low, high)
        sort(low, mid - 1)
        sort(mid, high)
    # 사실 여기서 찾음

    def part(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


arr = [1, 2, 3, 124, 134, 31, 53, 251, 246, 4316, 526, 345, 6435, 734, 3]
quick_sort(arr)
print(arr)
