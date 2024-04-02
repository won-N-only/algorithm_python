import sys

def input():
    return sys.stdin.readline().strip()


def find_next(arr, posi, next):
    for i in range(posi + 1, len(arr)):
        if arr[i] == next:
            return i
    return float('inf')


def plug_out(n, k, arr):
    plug_in = set()
    cnt = 0

    for i in range(k):
        curr = arr[i]

        if curr in plug_in:
            continue

        if len(plug_in) < n:
            plug_in.add(curr)
            continue

        next_use = {next: find_next(arr, i, next) for next in plug_in}
        unplug = max(next_use, key=next_use.get)
        plug_in.remove(unplug)

        plug_in.add(curr)
        cnt += 1

    return cnt


n, k = map(int, input().split())
elec = list(map(int, input().split()))
ans = plug_out(n, k, elec)
print(ans)
