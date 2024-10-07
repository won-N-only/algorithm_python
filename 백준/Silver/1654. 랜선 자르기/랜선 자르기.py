def max_lan_cable_length(K, N, cables):
    start, end = 1, max(cables)

    result = 0

    while start <= end:
        mid = (start + end) // 2
        count = sum(cable // mid for cable in cables)

        if count >= N:  
            result = mid
            start = mid + 1
        else:
            end = mid - 1 

    return result

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

print(max_lan_cable_length(K, N, cables))
