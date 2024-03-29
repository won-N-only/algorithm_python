import re
import sys


def input():
    return sys.stdin.readline().strip()


input_str = input()
pattern = re.compile(r'[-+]?\d+')
numbers = pattern.findall(input_str)

numbers_list = [int(num) for num in numbers]


idx = len(numbers_list)
for i, num in enumerate(numbers_list):
    if num < 0:
        idx = i
        break

numbers_plus_sum = sum(numbers_list[0:idx])
numbers_minus_sum = sum([-abs(i) for i in numbers_list[idx:]])

print(numbers_plus_sum + numbers_minus_sum)
