import heapq

n = int(input())

min_h = []
max_h = []
result = []


for i in range(n):
    item = int(input())
    if i % 2 == 0:  # 홀수번째
        heapq.heappush(max_h, -item)
    else:  # 짝수번째
        heapq.heappush(min_h, item)

    if len(min_h) > 0 and len(max_h) > 0:
        if min_h[0] < -(max_h[0]):
            big = heapq.heappop(min_h)
            small = -(heapq.heappop(max_h))
            heapq.heappush(max_h, -big)
            heapq.heappush(min_h, small)
    if len(max_h) != 0:
        result.append(-max_h[0])
    else:
        result.append(min_h[0])
"""
max_h : 1 
min_h : 5
"""
for i in result:
    print(i)
