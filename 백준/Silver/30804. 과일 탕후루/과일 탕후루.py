from collections import defaultdict

def max_fruit_count(n, fruits):
    left = 0
    max_length = 0
    fruit_count = defaultdict(int)

    for right in range(n):
        fruit_count[fruits[right]] += 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

n = int(input())
fruits = list(map(int, input().split()))

print(max_fruit_count(n, fruits))
