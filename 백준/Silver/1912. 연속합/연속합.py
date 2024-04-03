def maxSum(a, size):
    max_far = a[0]
    curr = a[0]

    for i in range(1, size):
        curr = max(a[i], curr + a[i])
        max_far = max(max_far, curr)

    return max_far


n = int(input())
arr = list(map(int, input().split()))
print(maxSum(arr, n))
