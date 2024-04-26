import sys
sys.setrecursionlimit(10**9)


def input():
    return sys.stdin.readline().strip()


nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

# 전위 기준 입력으로 후위 만들기


# 이분탐색이랑 똑같은원리
def postorder(s, e):
    if s > e:
        return
    mid = e + 1                         # 오른쪽 노드가 없을 경우라고 가정

    for i in range(s+1, e+1):           # s+1부터 e까지
        if nums[s] < nums[i]:
            mid = i                     # 오른쪽 트리 시작점 idx
            break

    postorder(s+1, mid-1)               # 왼쪽 확인
    postorder(mid, e)                   # 오른쪽 확인

    # 왼쪽- 오른쪽 순서로 print하고 루트나와서 다시 왼쪽오른쪽print
    print(nums[s])


"""
post(nodedict[root][0])
post(nodedict[root][1])
print(root, end='')
이거생각하면됨"""

postorder(0, len(nums)-1)
