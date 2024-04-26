# # min 골라서 lsit 중간에 삽입

# def insert_sort(text):
#     # 1부터하는건 두번째 원소부터 조지기위해
#     for i in range(1, n):
#         # j=i해서 앞으로 안가게
#         j = i
#         temp = text[i]
#         # 리스트 끝 아니게
#         while j > 0 and text[j-1] > temp:
#             text[j-1], text[j] = text[j], text[j-1]
#             j -= 1
#         text[j] = temp
#     return text


# def binary_sort(text):
#     for i in range(1, n):
#         pl = 0
#         pr = i-1
#         key = text[i]
#         while True:
#             pc = (pl + pr) // 2
#             if text[pc] == key:
#                 break
#             elif text[pc] > key:
#                 pr = pc-1
#             else:
#                 pl = pc+1
#             if pl > pr:
#                 break
#         pidx = pc + 1 if pl <= pr else pr+1

#         for j in range(i, pidx, -1):
#             text[j] = text[j-1]
#         text[pidx] = key
#     return text

# 반으로 잘라서 pc찾고 또 잘라서 pc 찾고 찾고 pc=key면 ok
# 못찾아서 pl>pr되면 idx= pr+1, 찾았으면 idx=pc+1

def twojin(text):
    for i in range(1, n):
        key = text[i]
        pl = 0
        pr = i - 1
#         while pr > pl:라고쓰면 i=1일때 아무행동도안함
        while True:
            if pr < pl:
                break
            pc = (pl + pr) // 2
            if text[pc] == key:
                pl = pc + 1
                break
            elif text[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

        for j in range(i, pl, -1):
            text[j] = text[j - 1]
        text[pl] = key
    return text


text = list(map(int, input().split()))
n = len(text)

# print(insert_sort(text))
# print(binary_sort(text))
print(twojin(text))
