import sys
sys.setrecursionlimit(10**9)
nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break


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
    print(nums[s])                      # 정점 나올때마다 chk해서 print


"""        post(nodedict[root][0])
        post(nodedict[root][1])
        print(root, end='')
이거생가갛면됨"""

postorder(0, len(nums)-1)
