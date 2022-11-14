import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = {}

for i in range(m):
    a, b, cost = map(int, input().split())
    if a in graph:
        graph[a].append([b, cost])
    else:
        graph[a] = []
        graph[a].append([b, cost])


result = [0] * (n + 1)
import heapq

for i in range(1, n + 1):
    if i == x:
        continue

    distance = [int(10e9)] * (n + 1)
    q = []
    heapq.heappush(q, (i, 0))
    distance[i] = 0
    while q:
        current, dist = heapq.heappop(q)
        if dist > distance[current]:
            continue
        else:
            for road in graph[current]:
                cost = dist + road[1]
                if cost < distance[road[0]]:
                    distance[road[0]] = cost
                    heapq.heappush(q, (road[0], cost))

    result[i] = distance[x]

distance = [int(10e9)] * (n + 1)
q = []
heapq.heappush(q, (x, 0))
distance[x] = 0
while q:
    current, dist = heapq.heappop(q)
    if dist > distance[current]:
        continue
    else:
        for road in graph[current]:
            cost = dist + road[1]
            if cost < distance[road[0]]:
                distance[road[0]] = cost
                heapq.heappush(q, (road[0], cost))

max_value = 0
for i in range(1, n + 1):
    temp = result[i] + distance[i]
    if max_value < temp:
        max_value = temp
print(max_value)
