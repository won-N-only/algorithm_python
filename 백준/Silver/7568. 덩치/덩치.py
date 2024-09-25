import sys


def input():
    return sys.stdin.readline()


n = int(input())
people = []

for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

ranks = [1] * n

for i in range(n):
    for j in range(n):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                ranks[i] += 1

print(' '.join(map(str, ranks)))
