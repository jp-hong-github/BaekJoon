import sys
import heapq

input = sys.stdin.readline
INF = int(10e9)

n, m, k, x = map(int, input().split())

visited = [False] * (n + 1)
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


dijkstra(x)

is_zero = True
for i in range(1, n + 1):
    if k == distance[i]:
        print(i)
        is_zero = False

if is_zero:
    print(-1)
