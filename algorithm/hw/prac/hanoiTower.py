def hanoi(a, start, end):
    # a>1을넣어서 원반1개면 바로 113 나오게
    # 이유는 1이면 바로 옮겨도되니까. ...
    # 6-st-en해서 무조건 st,en이 아닌 블럭으로 이동하게함
    # st,en아닌데로 옮겼다가 원위치로 옮기는식 
    if a > 1:
        hanoi(a-1, start, 1+2+3-start-end)
    # 이때 a원반이 end로감
    print(a, start, end)
    # 이건 위 함수 다하고나서(a원반을 end로 옮기고나서 나머지를 end로)
    if a > 1:
        hanoi(a-1, 1+2+3-start-end, end)

# 2^n-1번 움직임 4 + 2 + (1번=마지막원반이동)


a = int(input())
hanoi(a, 1, 3)

# 원반-1 시작 중간
# 원반 시작 끝
# 원반-1 중간 끝 순으로 움직임
