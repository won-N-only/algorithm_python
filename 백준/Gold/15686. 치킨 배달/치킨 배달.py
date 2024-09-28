from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chicken_shops = []

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken_shops.append((r, c))


def get_city_chicken_distance(selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance


min_chicken_distance = float('inf')

for chicken_comb in combinations(chicken_shops, m):
    city_chicken_distance = get_city_chicken_distance(chicken_comb)
    min_chicken_distance = min(min_chicken_distance, city_chicken_distance)
    
print(min_chicken_distance)
