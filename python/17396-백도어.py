import sys
import heapq

input = sys.stdin.readline

n, m = list(map(int, input().split()))
look = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(m):
    a, b, t = list(map(int, input().split()))
    graph[a].append((b, t))
    graph[b].append((a, t))


def dijkstra(graph, start):
    # 거리,시야
    dist = [float("inf") for _ in range(n)]

    dist[start] = 0

    heap = [(0, start)]  # 거리, 현재 위치

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        if current_dist > dist[current_vertex]:
            continue

        for neighbor, neighbor_dist in graph[current_vertex]:
            next_dist = current_dist + neighbor_dist

            if next_dist < dist[neighbor] and look[neighbor] == 0:
                dist[neighbor] = next_dist
                heapq.heappush(heap, (next_dist, neighbor))
            if next_dist < dist[neighbor] and neighbor == n - 1:
                dist[neighbor] = next_dist
                heapq.heappush(heap, (next_dist, neighbor))
    return dist


dist = dijkstra(graph, 0)

if dist[-1] == float("inf"):
    print(-1)
else:
    print(dist[-1])
