import sys
import heapq


input = sys.stdin.readline

inf = float("inf")


T, C, Ts, Te = map(int, input().split())

graph = [[] for _ in range(T + 1)]


for i in range(C):
    x, y, cost = map(int, input().split())

    graph[x].append((y, cost))
    graph[y].append((x, cost))


def dijkstra(graph, start_vertex):
    dist_list = [inf] * (T + 1)
    dist_list[start_vertex] = 0

    heap = [(0, start_vertex)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        if current_dist > dist_list[current_vertex]:
            continue

        for neighbor, neighbor_dist in graph[current_vertex]:
            sum_dist = current_dist + neighbor_dist

            if sum_dist < dist_list[neighbor]:
                dist_list[neighbor] = sum_dist
                heapq.heappush(heap, (sum_dist, neighbor))

    return dist_list


print(dijkstra(graph, Ts)[Te])
