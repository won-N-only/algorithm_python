import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
s = [int(i) for i in (input())]
res = [s[0]]
i = 1

while k != 0 and i < n:
    while len(res) != 0 and k > 0 and res[-1] < s[i]:
        res.pop()
        k -= 1
    res.append(s[i])
    i += 1

while k > 0:
    res.pop()
    k -= 1

res += s[i:]

print(''.join(map(str, res)))
