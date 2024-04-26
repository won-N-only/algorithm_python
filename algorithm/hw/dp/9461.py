t = int(input())
triangle = [0 for i in range(101)]
triangle[1] = 1
triangle[2] = 1
triangle[3] = 1
triangle[4] = 2
for i in range(5, 101):
    triangle[i] = triangle[i-5]+triangle[i-1]


for i in range(t):
    print(triangle[int(input())])
