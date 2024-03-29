import re

input_str = input()

pattern = re.compile(r'[-+]?\d+')
numbers = pattern.findall(input_str)
numbers_int = [int(num) for num in numbers]

idx = next((i for i, num in enumerate(
    numbers_int) if num < 0), len(numbers_int))

numbers_plus_sum = sum(numbers_int[0:idx])
numbers_minus_sum = sum([-abs(i) for i in numbers_int[idx:]])

print(numbers_plus_sum + numbers_minus_sum)
