import sys

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for i in range(n + 1)]

INF = int(1e9)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

import heapq


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for point in graph[now]:
            if dist + point[1] < distance[point[0]]:
                distance[point[0]] = dist + point[1]
                heapq.heappush(q, (dist + point[1], point[0]))

    return distance[end]


result = min(
    dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n),
    dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n),
)

if result >= INF:
    print(-1)
else:
    print(result)
