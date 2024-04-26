import re
import sys


def input():
    return sys.stdin.readline().strip()


def sum1():
    pattern = re.compile(r'[-+]?\d+')
    numbers = pattern.findall(expression)

    numbers_list = [int(num) for num in numbers]

    idx = len(numbers_list)
    for i, num in enumerate(numbers_list):
        if num < 0:
            idx = i
            break

    numbers_plus_sum = sum(numbers_list[0:idx])
    numbers_minus_sum = sum([-abs(i) for i in numbers_list[idx:]])

    print(numbers_plus_sum + numbers_minus_sum)


def sum2():

    plus_minus_list = expression.split("-")

    plus_sum = sum(map(int, plus_minus_list[0].split("+")))

    for i in range(1, len(plus_minus_list)):
        minus_sum = plus_minus_list[i].split("+")
    minus_sum = sum(map(int, minus_sum))

    print(plus_sum-minus_sum)


expression = input()

sum1()

sum2()
