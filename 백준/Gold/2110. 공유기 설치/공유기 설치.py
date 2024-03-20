
n, m = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start, end, res= 0, house[n-1], 0
while start <= end:
    now=house[0]
    mid = (start+end)//2
    cnt = 1
    for i in range(1, n):
        if now+mid <= house[i]:
            now = house[i]
            cnt += 1
    if cnt >= m:
        res = mid
        start = mid+1
    else:
        end = mid-1
print(res)