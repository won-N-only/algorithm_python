
def get(x):
    if parent[x] == x:
        return x
    parent[x] = get(parent[x])
    return parent[x]


def union(a, b):
    a = get(a)
    b = get(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def same(a, b):
    return get(a) == get(b)


v, e = map(int, (input().split()))

edges = []
for i in range(e):
    a, b, cnt = map(int, (input().split()))
    edges.append((a, b, cnt))
#가중치 작은순 정렬
edges.sort(key=lambda x: x[2])

parent = [i for i in range(v+1)]

ans = 0

for edge in edges:
    a, b, cnt = edge
    if not same(a, b):
        union(a, b)
        ans += cnt
print(ans)
