import heapq
import sys


def input():
    return sys.stdin.readline().strip()


def card_suffle(cardlist, n):
    temp = 0
    while len(cardlist) >= 2:
        sum_cards = 0
        sum_cards += heapq.heappop(cardlist)
        sum_cards += heapq.heappop(cardlist)

    #    temp += sum_cards
        heapq.heappush(cardlist, sum_cards)

    return (temp)


# def card_suffle(cardlist, n):
#     i = 1
#     while len(cardlist) > 2:
#         sum_cards = 0

#         for j in range((n+1)//(2**i)):
#             sum_cards += heapq.heappop(cardlist) + heapq.heappop(cardlist)
#             heapq.heappush(cardlist, sum_cards)

#         i += 1

#     return sum(cardlist)

n = int(input())
cardlist = [int(input()) for _ in range(n)]
heapq.heapify(cardlist)
cnt = card_suffle(cardlist, n)
print(cnt)
