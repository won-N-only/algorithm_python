import sys


def input():
    return sys.stdin.readline()


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

visited = [0]*n
sum_cost = 0
ans = sys.maxsize


def letsgo(depth, row):
    global sum_cost, ans
    if depth == n-1:
        if costs[row][0]:
            # 돌아오는거
            sum_cost += costs[row][0]
            if sum_cost < ans:
                ans = sum_cost
            sum_cost -= costs[row][0]
        return

    for i in range(1, n):
        # 방문x, 여행가능일때
        if visited[i] == 0 and costs[row][i]:
            visited[i] = 1
            sum_cost += costs[row][i]
            letsgo(depth+1, i)
            visited[i] = 0

            sum_cost -= costs[row][i]


letsgo(0, 0)
print(ans)
