import sys


def input():
    return sys.stdin.readline().strip()


def interview(applicants):
    applicants.sort()
    idx = 1
    best = applicants[0][1]

    for _, score in applicants[1:]:
        if score < best:
            idx += 1
            best = score

    return idx


T = int(input())
for _ in range(T):
    N = int(input())
    applicants = [list(map(int, input().split())) for _ in range(N)]
    print(interview(applicants))
