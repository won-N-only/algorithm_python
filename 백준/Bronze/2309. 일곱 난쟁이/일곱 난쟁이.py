import sys


def input():
    return int(sys.stdin.readline())


dwarves = [int(input()) for _ in range(9)]
total = sum(dwarves)
diff = total-100

for i in range(8):
    temp = dwarves.pop(i)
    if diff - temp in dwarves:
        dwarves.remove(diff - temp)
        break
    else:
        dwarves.insert(i,temp)

[print(dwarf) for dwarf in sorted(dwarves)]
