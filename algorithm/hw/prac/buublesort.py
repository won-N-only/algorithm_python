

"""버블 정렬 기본"""


# def bubble(text):
#     for j in range(len(text)-1):
#         for i in range(len(text)-1, j, -1):
#             if text[i-1] >= text[i]:
#                 text[i-1], text[i] = text[i], text[i-1]
#     return text


# text = list(map(int, input().split()))
# print(bubble(text))

"""버블 정렬 pass=0이면 정렬종료하게"""

# def bubble(text):
#     global idx, ex
#     for j in range(len(text)-1):
#         ex = 0
#         for i in range(len(text)-1, j, -1):
#             if text[i-1] >= text[i]:
#                 text[i-1], text[i] = text[i], text[i-1]
#                 ex += 1
#                 idx += 1
#         if ex == 0:
#             return text
#     return text


# idx = 0
# text = list(map(int, input().split()))
# print(bubble(text))
# print( idx)

"""버블 정렬 안바꾼위치 저장"""


def bubble(text):
    global k, n, l
    last = n-1
    l = 0
    k = 0
    while k < n-1:
        for i in range(n):
            for j in range(last, i, -1):
                if text[j-1] > text[j]:
                    text[j-1], text[j] = text[j], text[j-1]
                """여기서 l+=1하고 k=l해도되고 그냥j써도되고 """
            k = j
    return text

"""left right이용해서 좌우왔다갔다하ㅔㄱ"""
def shake(text):
    left = 0
    right = n-1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if text[j-1] > text[j]:
                text[j-1], text[j] = text[j], text[j-1]
                last = j
            left = last
        for j in range(left, right):
            if text[j-1] < text[j]:
                text[j-1], text[j] = text[j], text[j-1]
                last = j
            right = last
    return text


text = list(map(int, input().split()))
n = len(text)
print(bubble(text))
print(shake(text))
