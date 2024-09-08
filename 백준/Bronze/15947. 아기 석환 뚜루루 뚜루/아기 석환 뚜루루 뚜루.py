import sys


def input():
    return sys.stdin.readline().strip()


ly = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu",
      "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]

n = int(input()) - 1

k = n // 14
index = n % 14

if index in [3, 7, 11]:
    if k >= 4:
        print(f"tu+ru*{k+1}")
    else:
        print("turu" + "ru" * k)

elif index in [2, 6, 10]:
    if k >= 3:
        print(f"tu+ru*{k+2}")
    else:
        print("tururu" + "ru" * k)

else:
    print(ly[index])
