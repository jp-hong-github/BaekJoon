import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

s, t = map(int, input().split())


def dijkstra():
    pass
    weight_list = [float("inf") for _ in range(n + 1)]
    weight_list[s] = 0
    heap = [(0, s)]

    while heap:
        cur_weight, cur_pos = heapq.heappop(heap)

        if weight_list[cur_pos] < cur_weight:
            continue

        for neighbor, weight_to_neighbor in edges[cur_pos]:
            candidate_next_weight = weight_to_neighbor + cur_weight
            if weight_list[neighbor] > candidate_next_weight:
                weight_list[neighbor] = candidate_next_weight
                heapq.heappush(heap, (candidate_next_weight, neighbor))

    return weight_list[t]


print(dijkstra())
