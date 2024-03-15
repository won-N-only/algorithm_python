a = int(input())
b = int(input())
c = int(input())
result = [int(x) for x in str(a*b*c)]
result.sort
for j in range(10):
    ress = result.count(j)
    print(ress)
