import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)

for i in range(m):
    min_1 = heapq.heappop(cards)
    min_2 = heapq.heappop(cards)
    temp = min_1 + min_2
    heapq.heappush(cards, temp)
    heapq.heappush(cards, temp)

print(sum(cards))
