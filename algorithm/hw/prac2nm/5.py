# def btk(m):
#     if len(ans) == m:
#         print(' '.join(map(str, ans)))
#         return

#     for i in range(1, n+1):
#         if i not in ans:
#             ans.append(i)
#             btk(m)
#             ans.pop()


# n, m = map(int, input().split())
# ans = []
# btk(m)
""" --------------------------------"""
# ans = []
# n, m = map(int, input().split())


# def btk2(z):
#     if m == len(ans):
#         print(' '.join(map(str, ans)))
#         return
#     for i in range(z, n+1):
#         if i not in ans:
#             ans.append(i)
#             btk2(i+1)
#             ans.pop()


# btk2(1)
""" --------------------------------"""
n, m = map(int, input().split())
ans = []


def stay():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n+1):

        ans.append(i)
        stay()
        ans.pop()
    return ans


stay()
