def pibo(n):
    if n == 1:
        return dp[1]

    elif n == 2:
        return dp[2]

    elif dp[n] == -1:
        dp[n] = pibo(n-2)+pibo(n-1)
        return dp[n]

    else:
        return dp[n]


def seat_set():
    ans = 1
    for i in range(1, m+2):
        ans = pibo(vip_seat[i]-vip_seat[i-1])*ans

    return ans


n = int(input())
m = int(input())

vip_seat = [0]
for i in range(m):
    vip_seat.append(int(input()))
vip_seat.append(int(n)+1)

if n == 1:
    print(1)
else:
    dp = [-1]*(n+4)
    dp[1] = 1
    dp[2] = 1
    if m == 0:
        #쓰레기문제 piboㅁ리만들어야함
        
        print(pibo(n+1))
        exit()
    print(seat_set())
