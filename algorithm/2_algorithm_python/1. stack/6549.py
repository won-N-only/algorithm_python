import sys


def input():
    return sys.stdin.readline().strip()


def sizing_histogram(height):

    stk = []
    max_area = 0

    # 이러면 height는 [[idx,h],[idx,h]]

    for idx, h in enumerate(height):
        # stk가 정상이고 prev가 curr보다 크면
        while len(stk) > 0 and height[stk[-1]] > h:
            top = stk.pop()
            # 오름차순이니까 width곱해주면 넓이나옴
            if len(stk) <= 0:
                width = idx
            else:
                width = idx-stk[-1]-1
            max_area = max(max_area, height[top]*width)
        stk.append(idx)

    # 다햇는데도 stk 남으면 남은걸로 다시돌림
    # 11191111같은상황 방지위함
    while len(stk) > 0:
        top = stk.pop()
        if len(stk) <= 0:
            width = len(height)
        else:
            width = len(height) - stk[-1]-1
        max_area = max(max_area, height[top]*width)

    return max_area

# 기존 출력부분: while은 구문마다 조건 검사하는게 아니라서 이러면 n[0]=0이라도 break 안됨
# n = [1]
# while n[0] != 0:
#     n = list(map(int, input().split()))
#     testcase = n[1:]
#     ans = sizing_histogram(testcase)
#     print(ans)

# --------------출력부분 변경-------------#


# 1:
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    testcase = n[1:]
    result = sizing_histogram(testcase)
    print(result)

# 2: while문 조건 없애고 입력단 아랫부분에 조건달아줌
n = [1]
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    testcase = n[1:]
    ans = sizing_histogram(testcase)
    print(ans)
