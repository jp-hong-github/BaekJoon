t = int(input())

import heapq

result = []

for i in range(t):
    max_heap, min_heap = [], []
    visit = [0] * 1000000

    k = int(input())

    for key in range(k):
        operation, number = map(str, input().split())
        if operation == "I":
            heapq.heappush(min_heap, (int(number), key))
            heapq.heappush(max_heap, (int(number) * -1, key))
            visit[key] = 1

        elif operation == "D":
            if number == "-1":
                while min_heap and visit[min_heap[0][1]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
            elif number == "1":
                while max_heap and visit[max_heap[0][1]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

    while min_heap and visit[min_heap[0][1]] == 0:
        heapq.heappop(min_heap)
    while max_heap and visit[max_heap[0][1]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        result.append([-max_heap[0][0], min_heap[0][0]])
    else:
        result.append("EMPTY")

for i in result:
    if i == "EMPTY":
        print("EMPTY")
    else:
        print("%d %d" % (i[0], i[1]))
