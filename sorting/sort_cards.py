# Problem No. 1715

import sys
import heapq

input = sys.stdin.readline

num_cards = int(input().rstrip())
cards = [int(input().rstrip()) for _ in range(num_cards)]
heapq.heapify(cards)
answer = 0
while cards:
    min_1 = heapq.heappop(cards)
    if cards:
        min_2 = heapq.heappop(cards)
    else:
        break
    new_bunch = min_1 + min_2
    answer += new_bunch
    heapq.heappush(cards, new_bunch)
print(answer)