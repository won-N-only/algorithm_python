

t = int(input())

dong = [[0]*15 for _ in range(15)]
for j in range(0, 15):
    dong[0][j] = j
    dong[j][1] = 1
for k in range(1, 15):
    for l in range(1, 15):
        dong[k][l] = dong[k-1][l]+dong[k][l-1]

for i in range(t):
    a = int(input())
    b = int(input())
    print(dong[a][b])
