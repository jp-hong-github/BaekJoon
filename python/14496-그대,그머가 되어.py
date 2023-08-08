import sys
import heapq

INF = int(1e9)

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append((y, 1))
    graph[y].append((x, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for go in graph[now]:  # now에서 갈 수 있는 정점
            cost = go[1] + dist  # now를 거쳐서 갈 때의 비용
            if cost < distance[go[0]]:  # 현재 비용보다 now를 거쳐갈 때 비용이 더 적게 나올 경우
                distance[go[0]] = cost
                heapq.heappush(q, (cost, go[0]))


dijkstra(a)
if distance[b] != INF:
    print(distance[b])
else:
    print(-1)
# print(distance)
# print(graph)
