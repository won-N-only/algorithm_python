import sys


def input():
    return sys.stdin.readline().strip()


def pathfinder(dp):
    for f in range(1, m):
        dp[0][f] += dp[0][f-1]

    for i in range(1, n):
        temp_l = dp[i][:]
        temp_r = dp[i][:]

        for j in range(m):
            if j == 0:
                temp_l[j] += dp[i-1][j]
            else:
                temp_l[j] += max(temp_l[j-1], dp[i-1][j])

        for j in range(m-1, -1, -1):
            if j == m-1:
                temp_r[j] += dp[i-1][j]
            else:
                temp_r[j] += max(temp_r[j+1], dp[i-1][j])

        for k in range(m):
            dp[i][k] = max(temp_l[k], temp_r[k])
    return dp[-1][-1]


n, m = map(int, input().split())
robot_route = []
for i in range(n):
    robot_route.append(list(map(int, input().split())))

ans = pathfinder(robot_route)
print(ans)
