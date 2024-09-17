n, m = map(int, input().split())
a = set(input() for _ in range(n))
b = set(input() for _ in range(m))

result = sorted(a.intersection(b))

print(len(result))
for name in result:
    print(name)
