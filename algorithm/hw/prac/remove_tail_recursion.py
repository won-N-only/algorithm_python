# # 원래는
def recurt(n: int) -> int:
    if n > 0:
        recurt(n-2)
        print(n)
        recurt(n-1)


print(recurt(4))

n = int(input())


def recur(n):
    while n > 0:
        recur(n-1)
        print(n)
    # while있으니까 알아서돌아감 ex) n=4면 recur(2)로
        n = n-2


print(recur(n))
