import heapq
import sys

input = sys.stdin.readline


heap = []
n = int(input())

for _ in range(n):
    temp = list(map(int, input().split()))
    for i in temp:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
print(heap[0])
