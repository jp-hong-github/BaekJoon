import sys

input = sys.stdin.readline
INF = int(10e9)

a, b = map(int, input().split())
n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

import heapq

distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 순서 중요
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for next in arr[now]:
            cost = dist + 1

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))


dijkstra(a)

if distance[b] == INF:
    print(-1)
else:
    print(distance[b])
