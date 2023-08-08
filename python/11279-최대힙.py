n = int(input())

import heapq

heap = []

result = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        if len(heap) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-temp, temp))


for i in result:
    print(i)
