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


def same_parent(a, b):
    return get(a) == get(b)


v, e = map(int, input().split())
edges = []
for _ in range(e):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])  # C(Cost)가 적은 것부터 정렬
parent = [i for i in range(v+1)]
ans = 0
for a, b, cost in edges:
    if not same_parent(a, b):
        union(a, b)
        ans += cost
print(ans)
