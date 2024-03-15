# 1~99까지는 다 한수임
# 3자리면 각 자리수 차이 같은지 확인
# 한수 리스트먼저 만들기
arithmetic = []
for i in range(1, 100):
    arithmetic.append(i)
for i in range(100, 1000):
    i = str(i)
    if int(i[1])-int(i[0]) == +int(i[2])-int(i[1]):
        arithmetic.append(int(i))
idx = 0
n = int(input())
for num in arithmetic:
    if num <= n:
        idx += 1
    else:
        break
print(idx)
