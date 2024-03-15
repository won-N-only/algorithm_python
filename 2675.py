t = int(input())
result = []
for _ in range(t):
    loop, case = input().split()
    result = ''.join([case[i] * int(loop) for i in range(len(case))])
    print(result)
