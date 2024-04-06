v, e = map(int, input().split())

k = int(input())

import sys

input = sys.stdin.readline
INF = int(1e9)


graph = [[] for i in range(v + 1)]
distance = [INF] * (v + 1)

# x->y 의 비용 : z
for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)

for i in range(1, v + 1):
    temp = distance[i]
    if temp == INF:
        print("INF")
    else:
        print(temp)
