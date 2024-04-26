import sys


def input():
    return sys.stdin.readline().strip()


# n, k = map(int, input().split())
# s = [int(i) for i in (input())]
# res = [s[0]]
# i = 1
# while k != 0:
#     if i == n:
#         break
#     while len(res) != 0 and k > 0 and len(res)+(n-i) > k:
#         if res[-1] < s[i]:
#             res.pop()
#             k -= 1
#         else:
#             break
#     res.append(s[i])

#     i += 1

# while k>0:
#     res.pop()
#     k-=1

# if sum(s) == s[0]*n:
#     for j in range(n):
#         print(s[0], end="", sep="")
# else:
#     print(*res+s[i:], sep="")


n, k = map(int, input().split())
s = [int(i) for i in (input())]
res = [s[0]]
i = 1

# k 0까지 빼줌 이거 for로는 더복잡해질라나 i가 애매하네
# 한바퀴돌고
while k != 0 and i < n:
    while len(res) != 0 and k > 0:
        if res[-1] < s[i]:
            res.pop()
            k -= 1
    res.append(s[i])
    i += 1

# 남은 k 처리함
while k > 0:
    res.pop()
    k -= 1
# k다썼는데 s 남아있을수도있으니까  (ex 10 5 4177252841) s더해줌
res += s[i:]

print(''.join(map(str, res)))
# 왜 for써서 출력하면 에러나는지
print(*res,sep="")
