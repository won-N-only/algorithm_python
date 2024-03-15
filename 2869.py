# 시간초과함
# import sys
# a, b, v = map(int, sys.stdin.readline().split())
# day = int(v//(a-b))-a
# elavion = day*(a-b)
# while True:
#     elavion += a
#     day += 1
#     if v-elavion <= 0:
#         break
#     elavion -= b
# sys.stdout.write(str(day))

# 이거 ㄱㅊ음
a, b, v = map(int, input().split())

days = (v - a) // (a - b)

if (v - a) % (a - b) != 0:
    days += 1

days += 1

print(days)
